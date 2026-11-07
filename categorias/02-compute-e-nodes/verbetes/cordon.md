# Cordon (e Uncordon)

## Definição em uma frase

*Cordon* é marcar um [Node](node.md) como **não agendável** (`spec.unschedulable: true`): nenhum Pod novo vai para ele, e os que já estão lá **continuam rodando**. *Uncordon* desfaz a marcação.

## Explicação didática

É como pendurar a placa "fechado para novos clientes" sem expulsar quem já está dentro. É o primeiro passo de uma manutenção: primeiro isola-se o nó com *cordon* e, se for preciso esvaziá-lo, [drena-se](drain.md) depois.

| Ação | Efeito |
|---|---|
| `cordon` | Bloqueia agendamentos novos; Pods existentes ficam |
| `uncordon` | Volta a aceitar Pods novos |

## Para que existe e qual problema resolve

Permite preparar um nó para manutenção, ou investigá-lo, sem que o scheduler continue colocando cargas nele.

## Funcionamento técnico e ciclo de vida

- O cordon define `spec.unschedulable: true` no Node, e o Control Plane aplica o taint `node.kubernetes.io/unschedulable:NoSchedule`.
- Em `oc get nodes`, o status passa a `Ready,SchedulingDisabled`. A documentação esclarece que `SchedulingDisabled` **não é uma condição** da API, e sim o reflexo do campo `unschedulable`.
- DaemonSets toleram esse taint, então seus Pods ainda podem ir para o nó. A documentação recomenda **não** tolerar esse taint em outras cargas.
- Pods com `spec.nodeName` definido manualmente ignoram o scheduler e podem ir para um nó em cordon.

## Relações e dependências

- Pré-requisito do [Drain](drain.md).
- Gera um [Taint](taint.md) automático.

## Exemplo de situação real

Um nó começa a apresentar erros de disco. O administrador faz `cordon` para que nenhum Pod novo vá para ele e investiga com calma. Os Pods em execução seguem atendendo enquanto isso.

## Como visualizar e inspecionar (somente leitura)

```bash
# Nós em cordon aparecem com SchedulingDisabled
oc get nodes

# Campo e taint correspondentes
oc get node <nó> -o jsonpath='unschedulable={.spec.unschedulable}{"\n"}taints={.spec.taints}{"\n"}'
```

**Alteração (NÃO EXECUTAR AUTOMATICAMENTE):**

```bash
oc adm cordon <nó>
oc adm uncordon <nó>
# vários nós de uma vez, por label
oc adm cordon --selector=<label>=<valor>
```

## Como interpretar a saída

- `Ready,SchedulingDisabled`: nó saudável, mas em cordon.
- `unschedulable=true` com o taint `node.kubernetes.io/unschedulable`: confirma o cordon.

## Diferenças e confusões frequentes

- **Cordon × drain:** bloquear novos × esvaziar.
- **Cordon × NotReady:** decisão administrativa × problema de saúde.

## No OpenShift 4.22 versus Kubernetes

No OpenShift, os comandos ficam em `oc adm` (`oc adm cordon` e `oc adm uncordon`). O mecanismo é o do Kubernetes. O MCO também faz cordon e drain dos nós ao aplicar configurações, um de cada vez por pool.

## No HomeLab SNO

Cordon no nó único impede **qualquer** Pod novo no cluster, inclusive os da plataforma que precisem ser recriados. Não faça isso fora de um procedimento oficial.

## Termos relacionados

[Drain](drain.md) · [Taint](taint.md) · [Node](node.md) · [Node Condition](node-condition.md) · [Machine Config Operator](../../01-arquitetura-e-control-plane/verbetes/machine-config-operator.md)

## Fontes oficiais

- Kubernetes — Node Status (`SchedulingDisabled` não é condição): <https://kubernetes.io/docs/reference/node/node-status/> (fonte: `kubernetes/website` `release-1.35`)
- Kubernetes — Safely Drain a Node (taint `node.kubernetes.io/unschedulable`): <https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/>
- OCP 4.22 — Working with nodes, "Understanding how to mark nodes as unschedulable or schedulable" (fonte: `modules/nodes-nodes-working-marking.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/cordon
- **Termo original:** cordon, uncordon
- **Remissões:** Uncordon, SchedulingDisabled, `spec.unschedulable`
- **Tradução:** isolar / reabilitar (só como apoio)
- **Classe ontológica:** ferramenta / estado (ação sobre o campo `spec.unschedulable` do Node)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** a aplicação automática do taint `unschedulable` pelo Control Plane é a descrita na documentação upstream; confirmar num cluster de estudo. **Uncordon** é tratado aqui, sem página própria.

</details>
