# Node Condition

## Definição em uma frase

Node Conditions são as **condições de saúde** que o kubelet relata no `status` de cada [Node](node.md), como `Ready` e as condições de pressão (`MemoryPressure`, `DiskPressure`, `PIDPressure`), e que o Control Plane usa para decidir se o nó pode receber ou manter Pods.

## Explicação didática

É o "painel de luzes" do nó. Cada condição tem um tipo e um valor `True`, `False` ou `Unknown`. A principal é `Ready`: diz se o nó está saudável e pronto para aceitar Pods. As outras sinalizam falta de algum recurso. Para elas, o normal é `False`.

| Condição | Normal | Significado quando anormal |
|---|---|---|
| `Ready` | `True` | `False`: nó não saudável; `Unknown`: o Control Plane não tem notícias do nó há mais de 50 s (padrão) |
| `MemoryPressure` | `False` | Memória do nó baixa |
| `DiskPressure` | `False` | Disco do nó com pouco espaço |
| `PIDPressure` | `False` | Processos demais no nó |
| `NetworkUnavailable` | `False` | Rede do nó mal configurada |

Remissões: **Node Ready** é a condição `Ready`; **Node Pressure** são as três condições de pressão.

## Para que existe e qual problema resolve

Permite ao Control Plane reagir automaticamente a problemas: parar de agendar em nós doentes e despejar Pods de nós que ficaram inalcançáveis ou sem recursos.

## Funcionamento técnico e ciclo de vida

- O kubelet avalia periodicamente o nó e atualiza as condições, com `reason`, `message`, `lastHeartbeatTime` e `lastTransitionTime`.
- **Taints automáticos:** quando há problemas, o Control Plane cria taints que correspondem às condições. Por exemplo, `Ready` em `Unknown` ou `False` por mais que o `NodeMonitorGracePeriod` (50 s por padrão) gera `node.kubernetes.io/unreachable` ou `node.kubernetes.io/not-ready`. Taints `NoExecute` podem despejar os Pods existentes.
- **Pressão e despejo:** com `MemoryPressure` ou `DiskPressure`, o kubelet pode despejar Pods para recuperar recursos (*node-pressure eviction*), começando pelos de [QoS](qos-class.md) mais baixa.
- `SchedulingDisabled`, que aparece em `oc get nodes`, **não é uma condição** da API: indica que o nó foi *cordoned* (`spec.unschedulable`).

## Relações e dependências

- Faz parte do `status` do [Node](node.md); é um caso de [Conditions](../../00-fundamentos-e-linguagem/verbetes/conditions.md).
- Ligada a taints (lote 2), ao despejo por pressão e à [QoS Class](qos-class.md).

## Exemplo de situação real

Um nó aparece com `MemoryPressure=True`. Pouco depois, Pods `BestEffort` são despejados com o motivo `Evicted`. Não é falha das aplicações: o kubelet está liberando memória para proteger o nó.

## Como visualizar e inspecionar (somente leitura)

```bash
# Condições do nó, uma por linha
oc get node <nó> -o jsonpath='{range .status.conditions[*]}{.type}={.status} ({.reason}){"\n"}{end}'

# Taints aplicados (inclusive os automáticos)
oc get node <nó> -o jsonpath='{.spec.taints}{"\n"}'

# Pods despejados no namespace
oc get pods -n <namespace> --field-selector=status.phase=Failed
```

## Como interpretar a saída

- Saudável: `Ready=True (KubeletReady)` e as pressões em `False`.
- `Ready=Unknown`: o kubelet parou de relatar (nó desligado, rede, kubelet parado).
- Pods despejados aparecem como `Failed`, com `reason: Evicted` e uma mensagem citando o recurso (por exemplo, "The node was low on resource: memory").

## Diferenças e confusões frequentes

- **Condição × taint:** a condição relata; o taint age sobre o agendamento.
- **`NotReady` × `SchedulingDisabled`:** problema de saúde × decisão administrativa (cordon).
- **Despejo por pressão × OOMKill:** o despejo é feito pelo kubelet; o OOMKill, pelo kernel. Ver [OOMKill](oomkill.md).

## No OpenShift 4.22 versus Kubernetes

Mesmo mecanismo. No OpenShift, condições ruins de nós aparecem também em alertas do monitoramento da plataforma (categoria 12).

## No HomeLab SNO

Num nó único com pouca memória, `MemoryPressure` é um risco real: o despejo pode atingir Pods de aplicações e, em casos extremos, deixar a plataforma instável. Observe as condições antes de colocar cargas novas.

## Termos relacionados

[Node](node.md) · [Conditions](../../00-fundamentos-e-linguagem/verbetes/conditions.md) · [QoS Class](qos-class.md) · [OOMKill](oomkill.md) · [Allocatable](allocatable.md) · [kubelet](../../01-arquitetura-e-control-plane/verbetes/kubelet.md)

## Fontes oficiais

- Kubernetes — Node Status, "Conditions" (tabela, taints automáticos, `SchedulingDisabled`): <https://kubernetes.io/docs/reference/node/node-status/#condition> (fonte: `kubernetes/website` `release-1.35`, `reference/node/node-status.md`)
- Kubernetes — Node-pressure Eviction: <https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/node-condition
- **Termo original:** node condition
- **Remissões:** Node Ready, Node Pressure, MemoryPressure, DiskPressure, PIDPressure
- **Tradução:** condição do nó (só como apoio)
- **Classe ontológica:** estado (campo `status.conditions` do Node)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico → intermediário
- **Atualizado em:** 2026-11-05

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-05.
- **Pendências:** o texto da mensagem de despejo é ilustrativo; confirmar no SNO. O valor do `NodeMonitorGracePeriod` no OCP 4.22 pode ser diferente do padrão upstream; **não foi verificado**.

</details>
