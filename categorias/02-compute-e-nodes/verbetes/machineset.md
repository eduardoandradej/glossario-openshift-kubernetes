# MachineSet

## Definição em uma frase

Um MachineSet mantém **um número desejado de [Machines](machine.md)** iguais, a partir de um modelo, e está para as Machines **assim como o ReplicaSet está para os Pods**.

## Explicação didática

A própria documentação do OpenShift faz a comparação: para ter mais nós de compute, ou menos, muda-se o campo `replicas` do MachineSet, e a Machine API cria ou remove Machines até chegar ao número pedido. É a [Reconciliation](../../00-fundamentos-e-linguagem/verbetes/reconciliation.md) aplicada à infraestrutura.

## Para que existe e qual problema resolve

Permite escalar o cluster em nós de forma declarativa e repor máquinas perdidas automaticamente, junto com o [MachineHealthCheck](machinehealthcheck.md).

## Funcionamento técnico e ciclo de vida

- **Compute machine sets** gerenciam máquinas com papel `worker` (ou papéis personalizados, como `infra`).
- **Máquinas de Control Plane não** são gerenciadas por compute machine sets; para isso existem os *control plane machine sets*, em plataformas suportadas.
- Cada compute machine set fica **numa única zona**; por isso o instalador cria um por zona disponível.
- Pode ser escalado automaticamente por um `MachineAutoscaler`, que só tem efeito quando existe um `ClusterAutoscaler` (categoria 11).
- Infra machine sets são um uso específico, para [Infrastructure Nodes](../../01-arquitetura-e-control-plane/verbetes/infrastructure-node.md).

## Relações e dependências

- Cria e mantém [Machines](machine.md); cada Machine vira um [Node](node.md).
- Escalado por `MachineAutoscaler` e `ClusterAutoscaler`; remediado por [MachineHealthCheck](machinehealthcheck.md).
- Não confundir com [MachineConfigPool](../../01-arquitetura-e-control-plane/verbetes/machineconfigpool.md), que agrupa nós para **configuração**.

## Exemplo de situação real

Uma loja virtual se prepara para a Black Friday aumentando `replicas` de um MachineSet de 3 para 6. Novas VMs são criadas na nuvem, entram como nós, e o scheduler passa a usá-las.

## Como visualizar e inspecionar (somente leitura)

```bash
# MachineSets: desejado, atual, prontos, disponíveis
oc get machinesets -n openshift-machine-api

# Detalhe: zona, tipo de instância, labels aplicadas aos nós
oc describe machineset <nome> -n openshift-machine-api

# Autoscalers ligados a MachineSets (se houver)
oc get machineautoscalers -n openshift-machine-api
```

**Alteração (NÃO EXECUTAR AUTOMATICAMENTE):**

```bash
oc scale machineset <nome> -n openshift-machine-api --replicas=<n>
```

## Como interpretar a saída

- Colunas `DESIRED`, `CURRENT`, `READY`, `AVAILABLE`: iguais significa MachineSet estável. `READY` menor por muito tempo indica máquinas presas no provisionamento.
- `No resources found` é comum em instalações sem integração de plataforma.

## Diferenças e confusões frequentes

- **MachineSet × MachineConfigPool:** criar e escalar máquinas × configurar o SO delas.
- **MachineSet × ReplicaSet:** a mesma ideia aplicada a máquinas e a Pods.
- **Compute machine set × control plane machine set:** workers × Control Plane.

## No OpenShift 4.22 versus Kubernetes

Recurso da Machine API do OpenShift, sem equivalente nativo no Kubernetes upstream.

## No HomeLab SNO

Num SNO com `platform: none`, não se espera MachineSet. O nó único foi instalado diretamente, e escalar por MachineSet não se aplica.

## Termos relacionados

[Machine](machine.md) · [MachineHealthCheck](machinehealthcheck.md) · [Node](node.md) · [Infrastructure Node](../../01-arquitetura-e-control-plane/verbetes/infrastructure-node.md) · [MachineConfigPool](../../01-arquitetura-e-control-plane/verbetes/machineconfigpool.md) · [ReplicaSet](../../03-workloads/verbetes/replicaset.md)

## Fontes oficiais

- OCP 4.22 — Machine management, "Machine API overview" (MachineSet, comparação com ReplicaSet, control plane machine sets, autoscalers, uma zona por machine set; fonte: `modules/machine-api-overview.adoc`): <https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/index>
- OCP 4.22 — Creating infrastructure machine sets (fonte: `machine_management/creating-infrastructure-machinesets.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/machineset
- **Termo original:** MachineSet (compute machine set)
- **Remissões:** control plane machine set, MachineAutoscaler, ClusterAutoscaler
- **Tradução:** conjunto de máquinas (só como apoio)
- **Classe ontológica:** objeto da API (OpenShift)
- **API:** `machine.openshift.io/v1beta1`, `kind: MachineSet`
- **Plataforma:** OpenShift
- **Escopo:** namespaced (`openshift-machine-api`)
- **Disponibilidade:** nativo em instalações integradas a uma plataforma
- **Versões validadas:** OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** as colunas de `oc get machinesets` e a versão do grupo devem ser conferidas num cluster com Machine API, porque o SNO provavelmente não tem. Autoscaling fica para a categoria 11.

</details>
