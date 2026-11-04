# Worker Node

## Definição em uma frase

Um Worker Node é uma máquina, VM ou física, que **executa as cargas de trabalho** (Pods) e é gerenciada pelo [Control Plane](control-plane.md).

## Explicação didática

O Control Plane decide; o Worker Node faz. Cada worker anuncia sua capacidade (CPU, memória...), e o [kube-scheduler](kube-scheduler.md) escolhe em qual worker cada Pod vai rodar. No nó, o [kubelet](kubelet.md) recebe a tarefa e usa o [Container Runtime](container-runtime.md) para subir os contêineres.

"Worker Node" é um **papel**. O objeto da API é o [Node](../../02-compute-e-nodes/verbetes/node.md), detalhado na categoria 02.

## Para que existe e qual problema resolve

Concentra a execução num conjunto de máquinas que pode crescer ou diminuir conforme a demanda, sem mexer no Control Plane.

## Funcionamento técnico e ciclo de vida

Serviços importantes em cada worker do OpenShift, segundo a documentação:

- **CRI-O:** o container engine ([CRI-O](cri-o.md));
- **kubelet:** aceita e executa pedidos para iniciar e parar contêineres ([kubelet](kubelet.md));
- **um service proxy**, que gerencia a comunicação dos Pods entre os workers;
- **crun ou runC:** o runtime de baixo nível que cria e roda os contêineres. O padrão é o **crun**; o runC pode ser habilitado com um `ContainerRuntimeConfig`.

No OpenShift, as máquinas com papel **`worker`** são chamadas de *compute machines*, e os termos *worker machine* e *compute machine* são usados como sinônimos. Elas são controladas por *compute machine sets* (no namespace `machine-api`, quando a plataforma suporta) e agrupadas em *machine config pools* para receber configuração (categoria 01, lote 2).

## Relações e dependências

- Gerenciado pelo [Control Plane](control-plane.md); representado por um objeto [Node](../../02-compute-e-nodes/verbetes/node.md).
- Executa [kubelet](kubelet.md), [CRI-O](cri-o.md) e o runtime de baixo nível.

## Exemplo de situação real

Pods ficam `Pending` com `Insufficient cpu`. Não há worker com CPU livre suficiente para os *requests*. A solução é de capacidade (mais workers, ou *requests* menores), e não do Control Plane.

## Como visualizar e inspecionar (somente leitura)

```bash
# Nós com papel worker
oc get nodes -l node-role.kubernetes.io/worker

# Capacidade e alocação de um nó
oc describe node <nó>

# OpenShift: pools de configuração por papel
oc get machineconfigpools
```

## Como interpretar a saída

- Em `oc describe node`, as seções `Capacity`/`Allocatable` e `Allocated resources` mostram o total e o que já foi reservado. *Allocatable* é menor que *Capacity* porque parte fica reservada para o sistema.
- `Conditions` do nó (`Ready`, `MemoryPressure`, `DiskPressure`, `PIDPressure`) indicam a saúde: o normal é `Ready=True` e as pressões em `False`.
- Em `oc get machineconfigpools`, o pool `worker` mostra se a configuração está aplicada (`UPDATED=True`).

## Diferenças e confusões frequentes

- **Worker Node × Node:** papel × objeto da API.
- **Worker × compute × infra:** no OCP 4.22, *worker* e *compute* são sinônimos; *infrastructure node* é um uso especializado (categoria 01, lote 3).
- **Minion:** nome dos nós nas primeiras versões do Kubernetes; obsoleto.

## No OpenShift 4.22 versus Kubernetes

O OpenShift gerencia workers como *machines* (Machine API) e configura o SO deles por MachineConfig, em vez de configuração manual por nó.

## No HomeLab SNO

Não há worker separado: o único nó tem os papéis `control-plane`, `master` e `worker`. As aplicações dividem CPU e memória com o Control Plane.

## Termos relacionados

[Control Plane](control-plane.md) · [kubelet](kubelet.md) · [CRI-O](cri-o.md) · [Container Runtime](container-runtime.md) · [kube-scheduler](kube-scheduler.md) · [Node](../../02-compute-e-nodes/verbetes/node.md)

## Fontes oficiais

- Kubernetes Glossary — Node: <https://kubernetes.io/docs/reference/glossary/?all=true#term-node> (fonte: `kubernetes/website` `release-1.35`, `reference/glossary/node.md`)
- Kubernetes — Nodes: <https://kubernetes.io/docs/concepts/architecture/nodes/>
- OCP 4.22 — Control plane architecture, "Machine roles" → "Cluster workers": <https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/architecture/control-plane> (fonte: `modules/architecture-machine-roles.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 01-arquitetura-e-control-plane/worker-node
- **Termo original:** worker node, compute node, compute machine
- **Remissões:** minion (termo antigo)
- **Tradução:** nó de trabalho (só como apoio)
- **Classe ontológica:** conceito (papel de um Node)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável (o objeto `Node` é cluster-scoped)
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-04

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** confirmar a label `node-role.kubernetes.io/worker` e as seções do `describe node` no SNO, que **não foram executados**.

</details>
