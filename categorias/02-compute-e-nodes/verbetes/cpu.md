# CPU (recurso `cpu`)

## Definição em uma frase

No Kubernetes, `cpu` é o tipo de recurso que mede **capacidade de processamento**, em unidades em que **1 CPU equivale a 1 núcleo físico ou virtual**, com frações expressas em milicores (`m`).

## Explicação didática

Pedir `500m` é pedir **meio núcleo**: metade do tempo de processamento de um núcleo. A unidade é **absoluta**: `500m` representa aproximadamente a mesma capacidade de processamento num nó de 2 ou de 48 núcleos.

| Expressão | Significado |
|---|---|
| `1` ou `1000m` | 1 núcleo |
| `0.5` ou `500m` | meio núcleo |
| `0.1` ou `100m` | um décimo de núcleo |
| `1m` | a menor fração permitida |

A documentação recomenda usar a forma em milicores abaixo de 1 CPU, porque fica mais fácil perceber um valor inválido: `0.5m` é visivelmente errado, e `0.0005` não.

## Para que existe e qual problema resolve

Dá uma medida comum para reservar e limitar processamento entre contêineres que dividem a mesma máquina.

## Funcionamento técnico e ciclo de vida

- **Request** (`resources.requests.cpu`): usado pelo scheduler para escolher o nó e, no nó, funciona como um **peso**. Sob disputa, quem pediu mais recebe mais tempo de CPU.
- **Limit** (`resources.limits.cpu`): **teto rígido** aplicado pelo kernel. Ao atingi-lo, o contêiner sofre **throttling** (é pausado até o próximo intervalo); ele **não é encerrado** por excesso de CPU.
- A aplicação dessas regras é feita pelo runtime de contêineres por meio dos [cgroups](cgroups.md) do Linux.

## Relações e dependências

- Tipo de recurso usado em [Resource Request](resource-request.md) e [Resource Limit](resource-limit.md).
- Faz parte da [Capacity](capacity.md) e do [Allocatable](allocatable.md) do nó.
- Influencia a [QoS Class](qos-class.md) do Pod.

## Exemplo de situação real

Uma API fica lenta em horários de pico, sem reiniciar. O contêiner tem `limits.cpu: 500m` e está sendo limitado pelo kernel (throttling). A solução é revisar o limite e o dimensionamento; o contêiner não está "travando".

## Como visualizar e inspecionar (somente leitura)

```bash
# Requests e limits de CPU dos contêineres de um Pod
oc get pod <nome> -n <namespace> \
  -o jsonpath='{range .spec.containers[*]}{.name}: req={.resources.requests.cpu} lim={.resources.limits.cpu}{"\n"}{end}'

# Uso real de CPU dos Pods (depende do monitoramento)
oc adm top pods -n <namespace>

# CPU total e alocável do nó
oc get node <nó> -o jsonpath='{.status.capacity.cpu} / {.status.allocatable.cpu}{"\n"}'
```

## Como interpretar a saída

- Em `oc adm top pods`, a coluna `CPU(cores)` vem em milicores (ex.: `250m`). Uso **perto do limit** de forma constante sugere throttling.
- `Allocatable` de CPU pode aparecer em milicores (ex.: `3500m`) quando há reserva fracionária.

## Diferenças e confusões frequentes

- **CPU limit × memory limit:** excesso de CPU causa throttling; excesso de memória pode causar [OOMKill](oomkill.md).
- **`m` em CPU × `m` em memória:** em CPU, `m` é milicore; em memória, `m` é *milibyte*, quase sempre um erro.
- **CPU request não é uso garantido em todo instante:** é a garantia de fatia sob disputa e a base do agendamento.

## No OpenShift 4.22 versus Kubernetes

Mesmo modelo. O OpenShift reserva parte da CPU de cada nó para o sistema (mínimo de 0,5 CPU; ver [Allocatable](allocatable.md)) e oferece recursos avançados, como CPUs reservadas e isoladas, para cargas sensíveis à latência.

## No HomeLab SNO

Com poucos núcleos, *requests* de CPU altos esgotam o Allocatable rapidamente. Prefira *requests* modestos nas aplicações de estudo.

## Termos relacionados

[Resource Request](resource-request.md) · [Resource Limit](resource-limit.md) · [Memory](memory.md) · [cgroups](cgroups.md) · [QoS Class](qos-class.md) · [Allocatable](allocatable.md)

## Fontes oficiais

- Kubernetes — Resource Management for Pods and Containers, "CPU resource units" e "How Kubernetes applies resource requests and limits": <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> (fonte: `kubernetes/website` `release-1.35`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/cpu
- **Termo original:** CPU (`cpu` resource)
- **Remissões:** millicore, milliCPU, CPU throttling
- **Tradução:** processador (só como apoio)
- **Classe ontológica:** conceito (tipo de recurso computacional)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-05

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-05.
- **Pendências:** `oc adm top` depende do monitoramento; confirmar no SNO. Detalhar CPUs reservadas e isoladas (Performance Profile) na categoria 11.

</details>
