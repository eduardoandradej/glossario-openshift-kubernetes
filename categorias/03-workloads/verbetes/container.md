# Container

## Definição em uma frase

Um contêiner é um **processo isolado**, criado a partir de uma **imagem**, que leva consigo a aplicação e as suas dependências. No Kubernetes, ele sempre roda dentro de um [Pod](pod.md).

## Explicação didática

A imagem é o "pacote pronto": código, runtime, bibliotecas e configurações padrão. O contêiner é esse pacote **em execução**, isolado do resto da máquina pelo kernel (namespaces do Linux e cgroups). Por levar tudo junto, ele se comporta igual em qualquer ambiente.

A documentação do Kubernetes lembra que "contêiner" é uma palavra sobrecarregada: confirme se o seu interlocutor usa o mesmo sentido.

## Para que existe e qual problema resolve

Desacopla a aplicação da infraestrutura: a mesma imagem roda no laptop, no cluster de testes e em produção, com o mesmo comportamento.

## Funcionamento técnico e ciclo de vida

- **Imutável por princípio:** não se altera o código de um contêiner em execução. Para mudar, constrói-se uma **imagem nova** e se recriam os contêineres a partir dela.
- **Sem estado por padrão:** dados gravados na camada do contêiner somem com ele; dados persistentes vão para volumes (categoria 05).
- **No Pod:** o `spec` define, para cada contêiner, nome, imagem, comando, variáveis de ambiente, portas, recursos ([requests](../../02-compute-e-nodes/verbetes/resource-request.md) e [limits](../../02-compute-e-nodes/verbetes/resource-limit.md)), *probes* e contexto de segurança.
- **Execução:** o [kubelet](../../01-arquitetura-e-control-plane/verbetes/kubelet.md) pede ao [Container Runtime](../../01-arquitetura-e-control-plane/verbetes/container-runtime.md) que crie e inicie o contêiner; os estados do contêiner (`Waiting`, `Running`, `Terminated`) são assunto do lote 2 desta categoria.
- **Tipos no Pod:** contêineres de aplicação, *init containers*, *sidecars* e contêineres efêmeros de depuração (lote 2).

## Relações e dependências

- Roda dentro de um [Pod](pod.md); executado pelo [CRI-O](../../01-arquitetura-e-control-plane/verbetes/cri-o.md).
- Criado a partir de uma imagem (categoria 10).
- Limitado por [cgroups](../../02-compute-e-nodes/verbetes/cgroups.md).

## Exemplo de situação real

Um desenvolvedor entra num contêiner com `oc rsh` e corrige um arquivo de configuração "na mão". Quando o Pod é recriado, a correção some. O caminho certo é levar a mudança para a imagem ou para um ConfigMap.

## Como visualizar e inspecionar (somente leitura)

```bash
# Contêineres e imagens de um Pod
oc get pod <nome> -n <namespace> -o jsonpath='{range .spec.containers[*]}{.name}: {.image}{"\n"}{end}'

# Estado de cada contêiner
oc get pod <nome> -n <namespace> -o jsonpath='{range .status.containerStatuses[*]}{.name}: ready={.ready} restarts={.restartCount}{"\n"}{end}'

# Logs do contêiner atual e da execução anterior
oc logs <pod> -n <namespace> -c <contêiner>
oc logs <pod> -n <namespace> -c <contêiner> --previous
```

## Como interpretar a saída

- `ready=false` com `restarts` subindo: o contêiner não consegue ficar de pé. Os logs `--previous` mostram o que aconteceu antes do último reinício.
- `imageID` em `containerStatuses` mostra o *digest* exato da imagem em execução, útil quando a tag é reutilizada.

## Diferenças e confusões frequentes

- **Contêiner × imagem:** processo em execução × pacote estático.
- **Contêiner × Pod:** o Pod agrupa contêineres e dá a eles rede e volumes.
- **Contêiner × VM:** o contêiner compartilha o kernel do nó; a VM tem kernel próprio.

## No OpenShift 4.22 versus Kubernetes

O conceito é o mesmo. No OpenShift, por padrão, os contêineres rodam com um **UID arbitrário** e sem privilégios (SCC `restricted-v2`); imagens que exigem root precisam ser adaptadas (categoria 08).

## No HomeLab SNO

Use `oc logs` e `oc get pod -o jsonpath` para estudar contêineres; `oc rsh` e `oc exec` abrem um shell, o que deve ser feito só em aplicações de estudo.

## Termos relacionados

[Pod](pod.md) · [Pod Template](pod-template.md) · [Container Runtime](../../01-arquitetura-e-control-plane/verbetes/container-runtime.md) · [CRI-O](../../01-arquitetura-e-control-plane/verbetes/cri-o.md) · [Resource Limit](../../02-compute-e-nodes/verbetes/resource-limit.md)

## Fontes oficiais

- Kubernetes — Containers: <https://kubernetes.io/docs/concepts/containers/> (fonte: `kubernetes/website` `release-1.35`, `concepts/containers/_index.md`)
- Kubernetes — Pods: <https://kubernetes.io/docs/concepts/workloads/pods/>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/container
- **Termo original:** container
- **Tradução:** contêiner
- **Classe ontológica:** conceito (unidade de execução dentro do Pod)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável (faz parte do Pod)
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-08.
- **Pendências:** o comportamento de UID arbitrário e da SCC `restricted-v2` deve ser detalhado e conferido na categoria 08.

</details>
