# MachineHealthCheck

## Definição em uma frase

Um MachineHealthCheck **detecta Machines não saudáveis e as remedia automaticamente**: apaga a [Machine](machine.md) com problema para que o [MachineSet](machineset.md) crie outra no lugar.

## Explicação didática

É o "sistema imunológico" dos nós. Você define o que é "doente" (por exemplo, o nó em `NotReady` por 5 minutos) e quais máquinas vigiar (por labels). Quando uma máquina se encaixa na regra, o controller a substitui.

## Para que existe e qual problema resolve

Reduz o tempo e o trabalho manual de recuperação de nós com falha, mantendo a capacidade do cluster.

## Funcionamento técnico e ciclo de vida

- **Só vale para máquinas gerenciadas** por compute machine sets ou control plane machine sets.
- **Condições:** você define as condições do nó a vigiar (como `Ready` em `False` ou `Unknown` por um tempo) e um seletor de máquinas.
- **Remediação:** a máquina que falha a verificação é apagada (o evento `machine deleted` aparece), e outra é criada.
- **Limites de impacto:**
  - o controller drena e apaga **um nó por vez**;
  - se houver mais máquinas doentes do que o limite `maxUnhealthy` permite, a remediação **para**, para permitir intervenção manual.
- **Remediação imediata:** se o objeto Node da máquina for removido do cluster; se o nó não entrar no cluster dentro do `nodeStartupTimeout`; ou se a Machine estiver na fase `Failed`.
- **Tempos:** tempos longos prolongam a indisponibilidade; tempos curtos demais podem causar um laço de remediação (máquinas apagadas antes de terminar de iniciar).
- Para desligar a verificação, remove-se o recurso.

## Relações e dependências

- Age sobre [Machines](machine.md) de um [MachineSet](machineset.md); observa as [condições](node-condition.md) do [Node](node.md).

## Exemplo de situação real

Um worker na nuvem perde a conectividade e fica `NotReady`. Depois do tempo configurado, o MachineHealthCheck apaga a Machine, o MachineSet cria uma VM nova, e em poucos minutos o cluster volta à capacidade normal, sem intervenção.

## Como visualizar e inspecionar (somente leitura)

```bash
# MachineHealthChecks: quantas máquinas esperadas e quantas saudáveis
oc get machinehealthchecks -n openshift-machine-api

# Regras e limites (unhealthyConditions, maxUnhealthy, nodeStartupTimeout)
oc get machinehealthcheck <nome> -n openshift-machine-api -o yaml

# Eventos de remediação
oc get events -n openshift-machine-api --sort-by=.lastTimestamp
```

## Como interpretar a saída

- `EXPECTEDMACHINES` e `CURRENTHEALTHY` (**ilustrativo**): diferença persistente indica máquinas doentes aguardando remediação, ou remediação suspensa por `maxUnhealthy`.
- Eventos `machine deleted` confirmam remediações.

## Diferenças e confusões frequentes

- **MachineHealthCheck × condição do nó:** a condição relata; o MHC age, substituindo a máquina.
- **MachineHealthCheck × despejo de Pods:** o despejo move Pods; o MHC troca a máquina.

## No OpenShift 4.22 versus Kubernetes

Recurso da Machine API do OpenShift, sem equivalente nativo no Kubernetes upstream.

## No HomeLab SNO

**Não aplicável:** não há MachineSet e não há como substituir o único nó automaticamente.

## Termos relacionados

[Machine](machine.md) · [MachineSet](machineset.md) · [Node Condition](node-condition.md) · [Node](node.md)

## Fontes oficiais

- OCP 4.22 — Machine management, "About machine health checks" e "Limitations when deploying machine health checks" (fonte: `modules/machine-health-checks-about.adoc`)
- OCP 4.22 — "Machine API overview" (fonte: `modules/machine-api-overview.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/machinehealthcheck
- **Termo original:** MachineHealthCheck
- **Remissões:** maxUnhealthy, nodeStartupTimeout
- **Tradução:** verificação de saúde da máquina (só como apoio)
- **Classe ontológica:** objeto da API (OpenShift)
- **API:** `machine.openshift.io/v1beta1`, `kind: MachineHealthCheck`
- **Plataforma:** OpenShift
- **Escopo:** namespaced (`openshift-machine-api`)
- **Disponibilidade:** nativo em instalações com Machine API
- **Versões validadas:** OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** as colunas de `oc get machinehealthchecks` são ilustrativas; conferir num cluster com Machine API.

</details>
