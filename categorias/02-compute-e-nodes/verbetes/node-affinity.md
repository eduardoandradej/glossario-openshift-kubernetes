# Node Affinity

## Definição em uma frase

Node Affinity é a regra, no Pod, que **atrai o Pod para nós com determinadas [labels](node-label.md)**, como exigência ou como preferência. É uma versão mais expressiva do [nodeSelector](node-selector.md).

## Explicação didática

Há dois tipos:

| Tipo | Comportamento |
|---|---|
| `requiredDuringSchedulingIgnoredDuringExecution` | **Obrigatório:** sem nó que satisfaça a regra, o Pod não é agendado |
| `preferredDuringSchedulingIgnoredDuringExecution` | **Preferência:** o scheduler tenta; se não achar, agenda em outro nó. Cada preferência tem um `weight` de 1 a 100 |

O sufixo `IgnoredDuringExecution` significa que, se as labels do nó mudarem depois, o Pod **continua** rodando onde está.

```yaml
# Trecho didático
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
      - matchExpressions:
        - key: topology.kubernetes.io/zone
          operator: In
          values: ["zona-a", "zona-b"]
    preferredDuringSchedulingIgnoredDuringExecution:
    - weight: 50
      preference:
        matchExpressions:
        - key: disktype
          operator: In
          values: ["ssd"]
```

## Para que existe e qual problema resolve

Resolve o que o `nodeSelector` não consegue: "OU" entre valores, exclusões (`NotIn`, `DoesNotExist`), comparações numéricas e preferências que não bloqueiam o agendamento.

## Funcionamento técnico e ciclo de vida

- **Operadores:** `In`, `NotIn`, `Exists`, `DoesNotExist`, `Gt` e `Lt`. Os dois últimos comparam inteiros e só existem para afinidade de **nó**.
- **Lógica:** vários `nodeSelectorTerms` são combinados com **OU**; várias expressões dentro de um termo, com **E**.
- `NotIn` e `DoesNotExist` permitem **anti-afinidade** de nó. Outra forma de repelir é usar [taints](taint.md).
- Com `nodeSelector` e `nodeAffinity` juntos, **as duas** condições valem.
- Afinidade e anti-afinidade **entre Pods** (*inter-pod affinity*) é outro mecanismo, tratado na categoria 11.

## Relações e dependências

- Lê [Node Labels](node-label.md); complementa o [Node Selector](node-selector.md).
- Combina com [Toleration](toleration.md) para nós dedicados com [taint](taint.md).

## Exemplo de situação real

Uma aplicação precisa rodar em duas zonas e prefere nós com SSD. Com afinidade obrigatória por zona e preferência por SSD, ela continua sendo agendada mesmo quando os nós com SSD estão cheios.

## Como visualizar e inspecionar (somente leitura)

```bash
# Afinidade de nó de um Pod
oc get pod <nome> -n <namespace> -o jsonpath='{.spec.affinity.nodeAffinity}' ; echo

# Esquema do campo
oc explain pod.spec.affinity.nodeAffinity

# Nós candidatos a uma expressão
oc get nodes -l 'topology.kubernetes.io/zone in (zona-a,zona-b)'
```

## Como interpretar a saída

- Um bloco `required...` sem nós correspondentes explica `Pending` com `didn't match Pod's node affinity/selector`.
- Um bloco `preferred...` nunca impede o agendamento; só influencia a pontuação.

## Diferenças e confusões frequentes

- **Node affinity × nodeSelector:** expressiva × simples.
- **Node affinity × taint:** atração (no Pod) × repulsão (no nó).
- **Node affinity × pod affinity:** relativa a labels de nós × relativa a outros Pods.

## No OpenShift 4.22 versus Kubernetes

Mesmo mecanismo do Kubernetes 1.35.

## No HomeLab SNO

Com um nó único, só regras **obrigatórias** fazem diferença, e podem deixar Pods `Pending`. Regras de preferência são inócuas.

## Termos relacionados

[Node Selector](node-selector.md) · [Node Label](node-label.md) · [Taint](taint.md) · [Toleration](toleration.md) · [kube-scheduler](../../01-arquitetura-e-control-plane/verbetes/kube-scheduler.md)

## Fontes oficiais

- Kubernetes — Assigning Pods to Nodes, "Node affinity", "Node affinity weight", "Operators": <https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity> (fonte: `kubernetes/website` `release-1.35`)
- OCP 4.22 — About node selectors (regras ao combinar `nodeSelector` e `nodeAffinity`; fonte: `modules/nodes-scheduler-node-selectors-about.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/node-affinity
- **Termo original:** node affinity
- **Remissões:** requiredDuringSchedulingIgnoredDuringExecution, preferredDuringSchedulingIgnoredDuringExecution, node anti-affinity
- **Tradução:** afinidade de nó (só como apoio)
- **Classe ontológica:** conceito (campo `spec.affinity.nodeAffinity` do Pod)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** exemplos **não executados** no SNO. Pod affinity e anti-affinity ficam para a categoria 11.

</details>
