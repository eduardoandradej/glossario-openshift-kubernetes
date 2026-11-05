# Memory (recurso `memory`)

## Definição em uma frase

No Kubernetes, `memory` é o tipo de recurso que mede **memória RAM em bytes**, expressa com sufixos decimais (`M`, `G`) ou binários (`Mi`, `Gi`).

## Explicação didática

| Sufixo | Base | Exemplo |
|---|---|---|
| `k`, `M`, `G`, `T` | potências de 10 | `128M` = 128 000 000 bytes |
| `Ki`, `Mi`, `Gi`, `Ti` | potências de 2 | `128Mi` = 134 217 728 bytes |

**Cuidado com maiúsculas:** `M` é megabyte, mas `m` é *milibyte*. Pedir `400m` de memória é pedir **0,4 byte**; quem escreve isso quase sempre queria `400Mi`.

Diferente da CPU, a memória **não pode ser "espremida"**: um contêiner que precisa de mais memória do que tem não fica só mais lento; ele pode ser encerrado.

## Para que existe e qual problema resolve

Permite reservar e limitar o uso de RAM, protegendo o nó e as outras cargas de um contêiner que consome memória demais.

## Funcionamento técnico e ciclo de vida

- **Request** (`resources.requests.memory`): usado principalmente no **agendamento**. Em nós com cgroup v2, o runtime pode usá-lo como referência para `memory.min` e `memory.low`.
- **Limit** (`resources.limits.memory`): limite do cgroup do contêiner. Ao tentar passar dele, o subsistema de falta de memória (OOM) do kernel intervém e, em geral, encerra um processo do contêiner. Ver [OOMKill](oomkill.md).
- A aplicação é **reativa**: um contêiner pode passar do limite por um momento, e o encerramento acontece quando o kernel detecta a pressão de memória.
- Volumes `emptyDir` em memória (`tmpfs`) contam como **uso de memória do contêiner**, e não como armazenamento efêmero.
- Com o nó com pouca memória, Pods que usam mais que o seu *request* estão entre os mais prováveis de ser **despejados**.

## Relações e dependências

- Usada em [Resource Request](resource-request.md) e [Resource Limit](resource-limit.md); entra na [Capacity](capacity.md) e no [Allocatable](allocatable.md).
- Ligada a [OOMKill](oomkill.md), à [QoS Class](qos-class.md) e à condição `MemoryPressure` ([Node Condition](node-condition.md)).

## Exemplo de situação real

Um contêiner Java reinicia em ciclo, com `Last State: Terminated, Reason: OOMKilled`. O *heap* configurado na JVM é maior que o `limits.memory` do contêiner. É preciso alinhar a configuração da JVM ao limite, ou aumentar o limite.

## Como visualizar e inspecionar (somente leitura)

```bash
# Requests e limits de memória dos contêineres
oc get pod <nome> -n <namespace> \
  -o jsonpath='{range .spec.containers[*]}{.name}: req={.resources.requests.memory} lim={.resources.limits.memory}{"\n"}{end}'

# Uso real (depende do monitoramento)
oc adm top pods -n <namespace>

# Último encerramento de cada contêiner
oc get pod <nome> -n <namespace> \
  -o jsonpath='{range .status.containerStatuses[*]}{.name}: {.lastState.terminated.reason}{"\n"}{end}'
```

## Como interpretar a saída

- `MEMORY(bytes)` em `oc adm top pods` vem em `Mi`. Uso perto do limite indica risco de OOMKill.
- `lastState.terminated.reason: OOMKilled` confirma o encerramento por limite de memória.

## Diferenças e confusões frequentes

- **Memory limit × CPU limit:** encerramento × throttling.
- **`Mi` × `M`:** binário × decimal; para memória, prefira `Mi`/`Gi`.
- **Despejo × OOMKill:** o despejo é decidido pelo kubelet sob pressão do nó; o OOMKill é do kernel, por limite ou falta de memória.

## No OpenShift 4.22 versus Kubernetes

Mesmo modelo. O OpenShift usa **cgroup v2** e reserva memória para o sistema com uma fórmula ponderada (ver [Allocatable](allocatable.md)). A documentação recomenda versões de Java e outros runtimes compatíveis com cgroup v2, para que respeitem os limites do contêiner.

## No HomeLab SNO

A memória é o recurso mais escasso num SNO pequeno. Defina sempre `requests` e `limits` de memória nas aplicações de estudo, para não pressionar o nó único.

## Termos relacionados

[OOMKill](oomkill.md) · [Resource Request](resource-request.md) · [Resource Limit](resource-limit.md) · [CPU](cpu.md) · [QoS Class](qos-class.md) · [cgroups](cgroups.md)

## Fontes oficiais

- Kubernetes — Resource Management for Pods and Containers, "Memory resource units" e "How Kubernetes applies resource requests and limits": <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> (fonte: `kubernetes/website` `release-1.35`)
- OCP 4.22 — About Linux cgroup version 2 (versões de Java compatíveis; fonte: `modules/architecture-about-cgroup-v2.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/memory
- **Termo original:** memory (`memory` resource)
- **Remissões:** Mi, Gi
- **Tradução:** memória (só como apoio)
- **Classe ontológica:** conceito (tipo de recurso computacional)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-05

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-05.
- **Pendências:** exemplos **não executados** no SNO.

</details>
