# Node Label

## Definição em uma frase

Node Labels são as [labels](../../00-fundamentos-e-linguagem/verbetes/label.md) aplicadas aos objetos [Node](node.md): pares chave/valor que descrevem características do nó (papel, zona, sistema operacional, hardware) e que seletores e regras de agendamento usam para escolher onde cada Pod pode rodar.

## Explicação didática

O mecanismo é o mesmo das labels de qualquer objeto. O que muda é o uso: com labels de nó, você diz "estes Pods só podem rodar em nós com SSD" ou "nesta zona". Há dois tipos:

- **labels padrão:** preenchidas automaticamente pelo Kubernetes e pela plataforma, como `kubernetes.io/hostname`, `kubernetes.io/os`, `topology.kubernetes.io/zone`, `node-role.kubernetes.io/<papel>` e, no OpenShift, `node.openshift.io/os_id`;
- **labels próprias:** acrescentadas pelo administrador, como `disktype=ssd`.

A documentação avisa que os **valores** das labels padrão dependem do ambiente e não são garantidos. Por exemplo, `kubernetes.io/hostname` pode ou não ser igual ao nome do nó.

## Para que existe e qual problema resolve

Permite direcionar cargas para nós específicos (hardware, localização, requisitos de segurança) sem amarrar os Pods a nomes de máquinas.

## Funcionamento técnico e ciclo de vida

- Labels de nó são lidas por [Node Selector](node-selector.md), [Node Affinity](node-affinity.md), pools de configuração ([MachineConfigPool](../../01-arquitetura-e-control-plane/verbetes/machineconfigpool.md)) e regras de distribuição.
- **Isolamento seguro:** para labels usadas em isolamento, escolha chaves que o kubelet **não possa alterar**. O admission plugin `NodeRestriction` impede o kubelet de definir labels com o prefixo `node-restriction.kubernetes.io/`, o que evita que um nó comprometido se rotule para atrair cargas sensíveis.
- Mudar labels de um nó **não move** Pods já em execução; o efeito vale para os próximos agendamentos.

## Relações e dependências

- Caso particular de [Label](../../00-fundamentos-e-linguagem/verbetes/label.md) num [Node](node.md).
- Consumidas por [Node Selector](node-selector.md) e [Node Affinity](node-affinity.md).
- Labels de papel definem o pool de MCO do nó.

## Exemplo de situação real

Uma equipe rotula dois workers com `gpu=true` e usa um node selector nos Pods de treinamento. Os Pods passam a ir apenas para esses nós. Se um terceiro nó receber a label por engano, ele também passa a receber essas cargas.

## Como visualizar e inspecionar (somente leitura)

```bash
# Todas as labels de todos os nós
oc get nodes --show-labels

# Labels específicas como colunas
oc get nodes -L topology.kubernetes.io/zone,node-role.kubernetes.io/worker,kubernetes.io/os

# Nós que têm uma label
oc get nodes -l disktype=ssd
```

**Alteração (NÃO EXECUTAR AUTOMATICAMENTE; em nós de plataforma, nunca):**

```bash
oc label node <nó> disktype=ssd
oc label node <nó> disktype-     # remove a label
```

## Como interpretar a saída

- Labels de papel aparecem como `node-role.kubernetes.io/worker=` (valor vazio): o que importa é a presença da chave.
- Labels `node.openshift.io/os_id=rhcos` e `node.openshift.io/os_version` indicam o SO do nó no OpenShift.

## Diferenças e confusões frequentes

- **Node label × Node annotation:** a label serve para selecionar; a annotation guarda metadados de ferramentas. Ver [Node Annotation](node-annotation.md).
- **Node label × taint:** a label **atrai**, quando usada por seletores; o taint **repele**. Ver [Taint](taint.md).

## No OpenShift 4.22 versus Kubernetes

O OpenShift acrescenta labels próprias (como `node.openshift.io/os_id`), usa labels de papel para os pools do MCO e oferece seletores de nó padrão por cluster e por projeto. Ver [Node Selector](node-selector.md).

## No HomeLab SNO

Ler labels é seguro. **Não** altere labels de papel do nó único: elas determinam o pool de configuração e o agendamento da plataforma.

## Termos relacionados

[Label](../../00-fundamentos-e-linguagem/verbetes/label.md) · [Node Selector](node-selector.md) · [Node Affinity](node-affinity.md) · [Taint](taint.md) · [Node](node.md) · [Node Annotation](node-annotation.md)

## Fontes oficiais

- Kubernetes — Assigning Pods to Nodes, "Node labels" e "Node isolation/restriction": <https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/> (fonte: `kubernetes/website` `release-1.35`)
- Kubernetes — Well-Known Labels, Annotations and Taints: <https://kubernetes.io/docs/reference/labels-annotations-taints/>
- OCP 4.22 — About node selectors (exemplo de Node com labels `node.openshift.io/*`; fonte: `modules/nodes-scheduler-node-selectors-about.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/node-label
- **Termo original:** node label
- **Tradução:** label de nó (só como apoio)
- **Classe ontológica:** conceito (campo `metadata.labels` do Node)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** confirmar no SNO as labels `node.openshift.io/*`, que **não foram executadas**.

</details>
