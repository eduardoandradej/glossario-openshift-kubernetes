# Node Selector

## Definição em uma frase

`nodeSelector` é a forma **mais simples** de restringir em que nós um Pod pode rodar: uma lista de [labels de nó](node-label.md) que o nó precisa ter, todas elas, para receber o Pod.

## Explicação didática

```yaml
# Trecho didático de um Pod
spec:
  nodeSelector:
    disktype: ssd
    kubernetes.io/os: linux
```

O scheduler só considera nós com **todas** essas labels. Se nenhum nó as tiver, o Pod fica `Pending`. É um "E" simples: sem "OU", sem preferência. Para regras mais expressivas, existe a [Node Affinity](node-affinity.md).

## Para que existe e qual problema resolve

Direciona cargas para nós com características específicas, sem citar nomes de máquinas.

## Funcionamento técnico e ciclo de vida

- Avaliado pelo [kube-scheduler](../../01-arquitetura-e-control-plane/verbetes/kube-scheduler.md) **no agendamento**. Mudar as labels do nó depois não move o Pod.
- Com `nodeSelector` **e** `nodeAffinity` no mesmo Pod, **as duas** condições precisam ser satisfeitas.
- Não é possível acrescentar um node selector a um Pod já agendado; muda-se o objeto que o controla (o template do Deployment, por exemplo).
- **No OpenShift**, há três níveis:
  - **no Pod:** o `nodeSelector` do próprio Pod;
  - **padrão do cluster:** o administrador define `defaultNodeSelector` na configuração do scheduler (`schedulers.config.openshift.io/cluster`), e ele é acrescentado a todo Pod novo;
  - **por projeto:** a annotation `openshift.io/node-selector` no namespace acrescenta um seletor aos Pods novos do projeto e **tem precedência** sobre o padrão do cluster.

## Relações e dependências

- Lê [Node Labels](node-label.md); alternativa mais simples à [Node Affinity](node-affinity.md).
- Costuma ser combinado com [Toleration](toleration.md) para nós com [taint](taint.md).

## Exemplo de situação real

Todos os Pods novos de um projeto ficam `Pending`, sem que ninguém tenha mudado os manifestos. O administrador colocou um node selector de projeto (`openshift.io/node-selector`) com uma label que nenhum nó tem. Os Pods recebem o seletor automaticamente.

## Como visualizar e inspecionar (somente leitura)

```bash
# Seletor efetivo de um Pod (inclui o acrescentado pelo projeto ou cluster)
oc get pod <nome> -n <namespace> -o jsonpath='{.spec.nodeSelector}{"\n"}'

# Seletor por projeto
oc get namespace <projeto> -o jsonpath='{.metadata.annotations.openshift\.io/node-selector}{"\n"}'

# Seletor padrão do cluster
oc get scheduler cluster -o jsonpath='{.spec.defaultNodeSelector}{"\n"}'

# Nós que satisfazem um seletor
oc get nodes -l disktype=ssd
```

## Como interpretar a saída

- Um seletor no Pod que você não escreveu veio do projeto ou do cluster.
- `oc get nodes -l ...` sem resultado explica um `Pending` com `didn't match Pod's node affinity/selector` nos Events.

## Diferenças e confusões frequentes

- **nodeSelector × nodeAffinity:** simples (só "E", obrigatório) × expressivo (operadores, preferências, "OU" entre termos).
- **nodeSelector × nodeName:** o `nodeName` ignora o scheduler e fixa o nó; o seletor apenas filtra.
- **nodeSelector × label selector** de Services e Deployments: os dois usam labels, mas um escolhe nós, e o outro, Pods.

## No OpenShift 4.22 versus Kubernetes

O campo `nodeSelector` é do Kubernetes. Os seletores padrão do cluster e por projeto são recursos do OpenShift.

## No HomeLab SNO

Com um único nó, qualquer seletor que o nó não satisfaça deixa o Pod `Pending`. Use-o só para estudar o conceito.

## Termos relacionados

[Node Label](node-label.md) · [Node Affinity](node-affinity.md) · [Taint](taint.md) · [Toleration](toleration.md) · [Project](../../00-fundamentos-e-linguagem/verbetes/project.md) · [kube-scheduler](../../01-arquitetura-e-control-plane/verbetes/kube-scheduler.md)

## Fontes oficiais

- Kubernetes — Assigning Pods to Nodes, "nodeSelector": <https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector> (fonte: `kubernetes/website` `release-1.35`)
- OCP 4.22 — Placing pods on specific nodes using node selectors (seletores por Pod, padrão do cluster e por projeto; fontes: `nodes/scheduling/nodes-scheduler-node-selectors.adoc`, `modules/nodes-scheduler-node-selectors-about.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/node-selector
- **Termo original:** nodeSelector
- **Remissões:** defaultNodeSelector, `openshift.io/node-selector`
- **Tradução:** seletor de nó (só como apoio)
- **Classe ontológica:** conceito (campo `spec.nodeSelector` do Pod)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** confirmar o caminho `schedulers.config.openshift.io/cluster` `.spec.defaultNodeSelector` com `oc explain scheduler.spec`, que **não foi executado**.

</details>
