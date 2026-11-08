# Pod Condition

## Definição em uma frase

Pod Conditions são as **condições que o kubelet registra no `status` do Pod** para indicar por quais etapas ele já passou: agendado, inicializado, contêineres prontos, pronto para receber tráfego e outras.

## Explicação didática

A [Pod Phase](pod-phase.md) dá o resumo; as condições dão o detalhe. Cada uma tem `type`, `status` (`True`, `False` ou `Unknown`), horários e, quando falha, `reason` e `message`.

| Condição | Significa que... |
|---|---|
| `PodScheduled` | O Pod foi agendado num nó |
| `PodReadyToStartContainers` | O sandbox do Pod foi criado e a rede configurada (beta, ativa por padrão) |
| `Initialized` | Todos os [init containers](init-container.md) concluíram com sucesso |
| `ContainersReady` | Todos os contêineres estão prontos |
| `Ready` | O Pod pode atender e deve entrar nos balanceamentos dos Services correspondentes |
| `DisruptionTarget` | O Pod está prestes a ser encerrado por uma interrupção (preempção, despejo ou coleta de lixo) |
| `PodResizePending` / `PodResizeInProgress` | Redimensionamento de recursos pedido ou em andamento |

## Para que existe e qual problema resolve

Permite saber exatamente em que ponto o Pod parou e, sobretudo, se ele deve receber tráfego (`Ready`).

## Funcionamento técnico e ciclo de vida

- O kubelet atualiza as condições conforme o Pod avança.
- **`Ready` e tráfego:** só Pods `Ready` entram nos endpoints dos Services. A readiness é determinada pelas *readiness probes* (lote 3 desta categoria) e, opcionalmente, por *readiness gates* personalizados.
- Campos: `type`, `status`, `lastProbeTime`, `lastTransitionTime`, `reason` e `message`.

## Relações e dependências

- Caso de [Conditions](../../00-fundamentos-e-linguagem/verbetes/conditions.md) aplicado ao [Pod](pod.md).
- `Ready` liga o Pod ao [Service](../../04-networking/verbetes/service.md).

## Exemplo de situação real

Uma aplicação aparece `Running`, mas o Service não entrega tráfego a ela. A condição `Ready` está `False`, porque a *readiness probe* falha. O Pod roda, mas não foi considerado pronto.

## Como visualizar e inspecionar (somente leitura)

```bash
# Condições do Pod
oc get pod <nome> -n <namespace> -o jsonpath='{range .status.conditions[*]}{.type}={.status} {.reason} {.message}{"\n"}{end}'

# Visão humana (seção Conditions)
oc describe pod <nome> -n <namespace>
```

## Como interpretar a saída

- `PodScheduled=False` com `reason: Unschedulable`: problema de agendamento (recursos, taints, seletores).
- `Initialized=False`: um init container não terminou.
- `ContainersReady=False` e `Ready=False` com o Pod `Running`: contêiner não pronto (probe ou inicialização).

## Diferenças e confusões frequentes

- **Condition × phase:** detalhe × resumo.
- **`ContainersReady` × `Ready`:** `Ready` também considera os *readiness gates*.

## No OpenShift 4.22 versus Kubernetes

Mesmas condições do Kubernetes 1.35.

## No HomeLab SNO

Leia as condições antes de mexer em qualquer coisa: elas apontam a etapa exata do problema.

## Termos relacionados

[Pod Phase](pod-phase.md) · [Pod Lifecycle](pod-lifecycle.md) · [Conditions](../../00-fundamentos-e-linguagem/verbetes/conditions.md) · [Init Container](init-container.md) · [Service](../../04-networking/verbetes/service.md)

## Fontes oficiais

- Kubernetes — Pod Lifecycle, "Pod conditions" e "Pod readiness": <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions> (fonte: `kubernetes/website` `release-1.35`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/pod-condition
- **Termo original:** Pod condition
- **Remissões:** PodScheduled, Initialized, ContainersReady, Ready, readiness gate
- **Tradução:** condição do Pod (só como apoio)
- **Classe ontológica:** estado (campo `status.conditions` do Pod)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-08. Esta lista atualiza a citada como pendência no verbete Conditions (categoria 00).
- **Pendências:** confirmar no SNO a presença de `PodReadyToStartContainers`.

</details>
