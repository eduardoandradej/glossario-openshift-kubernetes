# Capacity

## Definição em uma frase

Capacity é a **quantidade total de recursos** que um [Node](node.md) tem (CPU, memória, armazenamento efêmero, número máximo de Pods...), relatada pelo kubelet no `status.capacity` do nó.

## Explicação didática

É o "tamanho da máquina" do ponto de vista do Kubernetes: quantos núcleos, quanta memória, quantos Pods cabem. Mas nem tudo isso fica disponível para as aplicações, porque parte é reservada para o sistema operacional e os componentes do nó. O que sobra é o [Allocatable](allocatable.md).

## Para que existe e qual problema resolve

Dá ao Control Plane a referência do tamanho de cada nó, base para calcular o Allocatable e para planejar a capacidade do cluster.

## Funcionamento técnico e ciclo de vida

- Reportada pelo kubelet a partir do hardware ou da VM. Em VMs, 1 CPU equivale a 1 núcleo virtual.
- Campos típicos: `cpu`, `memory`, `ephemeral-storage`, `pods` e, quando existirem, `hugepages-<tamanho>` e recursos estendidos (como GPUs expostas por device plugins).
- Muda quando a máquina muda (por exemplo, uma VM redimensionada), depois que o kubelet reinicia e relata os novos valores.

## Relações e dependências

- Ponto de partida do [Allocatable](allocatable.md).
- Os [Resource Requests](resource-request.md) dos Pods são comparados ao Allocatable, e não à Capacity.

## Exemplo de situação real

Um nó tem 16 GiB de memória na Capacity, mas os Pods não conseguem reservar mais que cerca de 13 GiB. A diferença é a reserva do sistema e o limiar de despejo, descontados no Allocatable. É comportamento esperado.

## Como visualizar e inspecionar (somente leitura)

```bash
# Capacity e Allocatable lado a lado
oc get node <nó> -o jsonpath='capacity={.status.capacity}{"\n"}allocatable={.status.allocatable}{"\n"}'

# Em forma de tabela, para todos os nós
oc get nodes -o custom-columns=NOME:.metadata.name,CPU:.status.capacity.cpu,MEM:.status.capacity.memory,PODS:.status.capacity.pods
```

## Como interpretar a saída

- `memory` vem em `Ki` (ex.: `16367304Ki`, cerca de 15,6 GiB). Divida por 1024² para obter GiB.
- `pods` é o número máximo de Pods no nó (configuração do kubelet), e não o número atual.
- A diferença entre Capacity e Allocatable é a reserva do nó. Ver [Allocatable](allocatable.md).

## Diferenças e confusões frequentes

- **Capacity × Allocatable:** total × disponível para Pods.
- **Capacity × uso:** capacity é o tamanho; uso real é medido pelo monitoramento (`oc adm top nodes`).

## No OpenShift 4.22 versus Kubernetes

Igual ao Kubernetes. O que muda no OpenShift é o cálculo da reserva, e portanto do Allocatable.

## No HomeLab SNO

A Capacity do nó único é toda a capacidade do cluster. Compare-a com os recursos mínimos do SNO (4 vCPUs, 16 GB de RAM) para entender a folga do laboratório.

## Termos relacionados

[Allocatable](allocatable.md) · [Node](node.md) · [CPU](cpu.md) · [Memory](memory.md) · [Ephemeral Storage](ephemeral-storage.md) · [Resource Request](resource-request.md)

## Fontes oficiais

- Kubernetes — Node Status, "Capacity and Allocatable": <https://kubernetes.io/docs/reference/node/node-status/#capacity> (fonte: `kubernetes/website` `release-1.35`)
- Kubernetes — Resource Management for Pods and Containers, "Resource types" e "Resource units": <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/capacity
- **Termo original:** capacity (node capacity)
- **Tradução:** capacidade (só como apoio)
- **Classe ontológica:** conceito (campo `status.capacity` do Node)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-05

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-05.
- **Pendências:** o valor de exemplo em `Ki` é ilustrativo. Confirmar no SNO, onde **não foi executado**.

</details>
