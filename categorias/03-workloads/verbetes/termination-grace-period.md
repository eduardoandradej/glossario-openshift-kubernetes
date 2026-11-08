# Termination Grace Period

## Definição em uma frase

O Termination Grace Period (`terminationGracePeriodSeconds`) é o **tempo que o Kubernetes dá aos contêineres de um [Pod](pod.md) para encerrarem de forma limpa** depois do pedido de término, antes de matá-los à força; o padrão é **30 segundos**.

## Explicação didática

Encerrar um Pod é como fechar uma loja: primeiro avisa-se que vai fechar (para de entrar gente, termina-se o atendimento) e só depois se baixa a porta. O grace period é o tempo entre o aviso e a porta baixada.

Sequência resumida:

1. O Pod é apagado; a API registra o prazo e o Pod aparece como [Terminating](terminating.md).
2. Se houver hook `preStop`, ele roda primeiro.
3. O kubelet envia o sinal **TERM** (ou o `STOPSIGNAL` da imagem) ao processo principal de cada contêiner.
4. Esgotado o prazo, os processos que restarem recebem **KILL**.
5. O Pod é removido da API.

## Para que existe e qual problema resolve

Evita cortar requisições no meio, corromper dados ou perder mensagens: a aplicação tem tempo para terminar o que está fazendo.

## Funcionamento técnico e ciclo de vida

- O prazo conta a partir do pedido de término e **inclui** o tempo do `preStop`. Se o `preStop` ainda estiver rodando ao fim do prazo, o kubelet concede uma extensão única de 2 segundos.
- Ao mesmo tempo, o Pod sai do balanceamento: os endpoints em encerramento ficam nas EndpointSlices com `ready=false` (e a condição `serving` indica se ainda atendem).
- A aplicação precisa **tratar o TERM**. Se ignorá-lo, ela será morta só no fim do prazo.
- Encerramento forçado (`--grace-period=0 --force`) remove o Pod da API sem esperar a confirmação do nó; é arriscado, sobretudo com StatefulSets.

## Relações e dependências

- Define a duração do estado [Terminating](terminating.md).
- Último passo do [Pod Lifecycle](pod-lifecycle.md) e do [drain](../../02-compute-e-nodes/verbetes/drain.md) de nós.

## Exemplo de situação real

Em cada rollout, alguns usuários recebem erros. A aplicação não tratava o TERM e era morta no meio das requisições. Tratar o sinal (terminar as requisições em curso) e, se necessário, um `preStop` curto resolvem o problema.

## Como visualizar e inspecionar (somente leitura)

```bash
# Prazo configurado no Pod
oc get pod <nome> -n <namespace> -o jsonpath='{.spec.terminationGracePeriodSeconds}{"\n"}'

# Prazo em vigor durante o encerramento
oc get pod <nome> -n <namespace> -o jsonpath='{.metadata.deletionTimestamp} {.metadata.deletionGracePeriodSeconds}{"\n"}'
```

Encerramento forçado:

```bash
# NÃO EXECUTAR AUTOMATICAMENTE — remove o Pod sem esperar o encerramento limpo
oc delete pod <nome> -n <namespace> --grace-period=0 --force
```

## Como interpretar a saída

- `30`: valor padrão.
- `deletionTimestamp` preenchido: o encerramento já começou.

## Diferenças e confusões frequentes

- **Grace period × timeout do `preStop`:** não há prazo separado para o hook; ele consome o mesmo grace period.
- **TERM × KILL:** o TERM pode ser tratado pela aplicação; o KILL não.

## No OpenShift 4.22 versus Kubernetes

Mesmo comportamento do Kubernetes 1.35.

## No HomeLab SNO

Pods que demoram exatamente 30 segundos para sumir costumam estar ignorando o TERM.

## Termos relacionados

[Terminating](terminating.md) · [Pod Lifecycle](pod-lifecycle.md) · [Container Lifecycle](container-lifecycle.md) · [drain](../../02-compute-e-nodes/verbetes/drain.md) · [Pod](pod.md)

## Fontes oficiais

- Kubernetes — Pod Lifecycle, "Termination of Pods" e "Forced Pod termination": <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination> (fonte: `kubernetes/website` `release-1.35`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/termination-grace-period
- **Termo original:** termination grace period (`terminationGracePeriodSeconds`)
- **Remissões:** graceful shutdown, SIGTERM, SIGKILL, force delete
- **Tradução:** período de carência de término (só como apoio)
- **Classe ontológica:** campo de configuração / processo
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-08.
- **Pendências:** nenhuma específica.

</details>
