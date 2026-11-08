# Ephemeral Container

## Definição em uma frase

Um Ephemeral Container é um **contêiner temporário adicionado a um [Pod](pod.md) já em execução para depuração**, por exemplo quando a imagem da aplicação não tem shell nem ferramentas de diagnóstico.

## Explicação didática

Imagens de produção costumam ser mínimas: sem `sh`, sem `curl`. Para investigar um problema sem recriar o Pod, você "encaixa" nele um contêiner com as ferramentas necessárias, que compartilha o contexto do Pod (rede e, opcionalmente, a visão dos processos de um contêiner-alvo).

## Para que existe e qual problema resolve

Permite depurar Pods que não podem ser recriados nem alterados, e imagens que não oferecem ferramentas de inspeção.

## Funcionamento técnico e ciclo de vida

- Ficam em `spec.ephemeralContainers` e são adicionados por uma subresource especial da API (`ephemeralcontainers`), **não** editando o Pod da forma usual.
- **Não têm** garantia de recursos nem portas, probes ou `lifecycle`.
- **Nunca são reiniciados** e não podem ser removidos depois de adicionados; somem com o Pod.
- A forma usual de criá-los é `kubectl debug` com `--image` e, para ver os processos de um contêiner, `--target`.

## Relações e dependências

- Ferramenta de diagnóstico, ao lado do [Node Debug](../../02-compute-e-nodes/verbetes/node-debug.md) (que depura o nó).
- Não confundir com [Sidecar Container](sidecar-container.md), que é permanente.

## Exemplo de situação real

Uma aplicação feita com imagem *distroless* não responde. Um Ephemeral Container com ferramentas de rede, adicionado ao Pod, testa conexões e DNS a partir da mesma rede do Pod, sem reiniciá-lo.

## Como visualizar e inspecionar (somente leitura)

```bash
# Há Ephemeral Containers no Pod?
oc get pod <nome> -n <namespace> -o jsonpath='{range .spec.ephemeralContainers[*]}{.name} {.image}{"\n"}{end}'

# Estado deles
oc get pod <nome> -n <namespace> -o jsonpath='{range .status.ephemeralContainerStatuses[*]}{.name}: {.state}{"\n"}{end}'
```

Altera o Pod em execução:

```bash
# NÃO EXECUTAR AUTOMATICAMENTE — adiciona um contêiner de depuração ao Pod
kubectl debug -it <nome> -n <namespace> --image=<imagem-de-ferramentas> --target=<contêiner>
```

## Como interpretar a saída

- Lista vazia: nenhum contêiner de depuração foi adicionado.
- Estado `Terminated`: a sessão de depuração terminou; o registro permanece no Pod.

## Diferenças e confusões frequentes

- **Ephemeral Container × `oc debug` de um Pod:** no OpenShift, `oc debug pod/<nome>` costuma criar **uma cópia** do Pod para depuração, em vez de alterar o original. Verifique o comportamento antes de usar.
- **Ephemeral × Init Container:** o init roda antes da aplicação; o efêmero é adicionado depois, sob demanda.

## No OpenShift 4.22 versus Kubernetes

O recurso existe conforme o Kubernetes 1.35. Adicioná-lo exige permissão na subresource `pods/ephemeralcontainers` e respeita as SCCs.

## No HomeLab SNO

Prefira depurar Pods de estudo. Não adicione contêineres efêmeros a Pods do sistema sem necessidade.

## Termos relacionados

[Sidecar Container](sidecar-container.md) · [Init Container](init-container.md) · [Node Debug](../../02-compute-e-nodes/verbetes/node-debug.md) · [Pod](pod.md) · [Container](container.md)

## Fontes oficiais

- Kubernetes — Ephemeral Containers: <https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/> (fonte: `kubernetes/website` `release-1.35`, `concepts/workloads/pods/ephemeral-containers.md`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/ephemeral-container
- **Termo original:** ephemeral container (`spec.ephemeralContainers`)
- **Remissões:** kubectl debug, pods/ephemeralcontainers
- **Tradução:** contêiner efêmero (só como apoio)
- **Classe ontológica:** componente do Pod (ferramenta de diagnóstico)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-08.
- **Pendências:** o comportamento de `oc debug pod/<nome>` (cópia do Pod) não foi conferido na documentação do 4.22; confirmar com `oc debug --help`.

</details>
