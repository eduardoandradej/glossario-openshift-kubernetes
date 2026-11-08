# Container Lifecycle (estados do contêiner)

## Definição em uma frase

Além da fase do Pod, o Kubernetes acompanha o **estado de cada [contêiner](container.md)**, que pode ser `Waiting`, `Running` ou `Terminated`, com motivos e códigos de saída que explicam o que está acontecendo.

## Explicação didática

| Estado | Significado | O que observar |
|---|---|---|
| **Waiting** | Ainda não está rodando nem terminou: fazendo o necessário para iniciar (baixar a imagem, aplicar dados de Secrets) | O `reason`, como `ContainerCreating`, `ImagePullBackOff` ou `CrashLoopBackOff` |
| **Running** | Executando sem problemas (se houver hook `postStart`, ele já terminou) | Quando entrou em execução (`startedAt`) |
| **Terminated** | Começou e terminou, com sucesso ou falha (se houver hook `preStop`, ele roda antes) | `reason`, `exitCode`, início e fim |

O estado atual fica em `state`; o anterior, em `lastState`, o que é útil para entender reinícios.

## Para que existe e qual problema resolve

A [fase do Pod](pod-phase.md) é resumida demais para diagnosticar. Os estados dos contêineres dizem **qual** contêiner tem problema e **por quê**.

## Funcionamento técnico e ciclo de vida

- Depois do agendamento, o kubelet cria os contêineres pelo runtime; cada um passa por `Waiting` → `Running` → `Terminated`.
- Se a [Restart Policy](restart-policy.md) permitir, um contêiner `Terminated` é reiniciado e volta a `Waiting`/`Running`, e o `restartCount` sobe.
- **Hooks de ciclo de vida** (`postStart` e `preStop`) rodam em pontos definidos desse ciclo (lote 3 desta categoria).

## Relações e dependências

- Detalha o [Pod Lifecycle](pod-lifecycle.md); motivos frequentes: [CrashLoopBackOff](crashloopbackoff.md), [ImagePullBackOff](imagepullbackoff.md) e [OOMKill](../../02-compute-e-nodes/verbetes/oomkill.md).

## Exemplo de situação real

Um contêiner mostra `state: Waiting (CrashLoopBackOff)` e `lastState: Terminated (Error, exitCode 1)`. A última execução saiu com erro da aplicação, e agora o kubelet espera o *backoff* antes de tentar de novo. Os logs `--previous` mostram o erro.

## Como visualizar e inspecionar (somente leitura)

```bash
# Estado atual e anterior de cada contêiner
oc get pod <nome> -n <namespace> -o jsonpath='{range .status.containerStatuses[*]}{.name}: state={.state} last={.lastState}{"\n"}{end}'

# Visão humana (State, Last State, Exit Code, Restart Count)
oc describe pod <nome> -n <namespace>

# Logs da execução anterior
oc logs <nome> -n <namespace> -c <contêiner> --previous
```

## Como interpretar a saída

- `Waiting` com `ContainerCreating`: ainda preparando (imagem, volumes).
- `Terminated` com `exitCode 0` e `reason: Completed`: terminou com sucesso (normal em Jobs).
- `Terminated` com `exitCode` diferente de 0: falha da aplicação. `137` costuma indicar `SIGKILL`, por exemplo um [OOMKill](../../02-compute-e-nodes/verbetes/oomkill.md).

## Diferenças e confusões frequentes

- **Estado do contêiner × fase do Pod:** um por contêiner × um para o Pod.
- **`reason` do estado × coluna `STATUS`:** o `oc get pods` costuma mostrar na coluna `STATUS` o `reason` do contêiner com problema.

## No OpenShift 4.22 versus Kubernetes

Mesmos estados do Kubernetes 1.35.

## No HomeLab SNO

`oc describe pod` com a seção `Last State` é o melhor ponto de partida para entender reinícios.

## Termos relacionados

[Container](container.md) · [Pod Lifecycle](pod-lifecycle.md) · [Restart Policy](restart-policy.md) · [CrashLoopBackOff](crashloopbackoff.md) · [ImagePullBackOff](imagepullbackoff.md) · [OOMKill](../../02-compute-e-nodes/verbetes/oomkill.md)

## Fontes oficiais

- Kubernetes — Pod Lifecycle, "Container states": <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-states> (fonte: `kubernetes/website` `release-1.35`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/container-lifecycle
- **Termo original:** container lifecycle, container states
- **Remissões:** Waiting, Running (contêiner), Terminated, lastState
- **Tradução:** ciclo de vida do contêiner (só como apoio)
- **Classe ontológica:** estado
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-08.
- **Pendências:** os `reason` `ContainerCreating` e `Completed` são os exibidos usualmente pelo cliente; confirmar no SNO.

</details>
