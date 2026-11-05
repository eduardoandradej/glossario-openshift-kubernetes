# Resource Limit

## Definição em uma frase

Um Resource Limit (`resources.limits`) é o **teto de consumo** de um recurso por um contêiner, aplicado pelo kubelet e, em última instância, pelo **kernel** do nó.

## Explicação didática

Se o [request](resource-request.md) é a reserva mínima, o limit é o "não pode passar daqui". A consequência de atingi-lo depende do recurso:

| Recurso | Ao atingir o limit |
|---|---|
| **CPU** | *Throttling*: o kernel pausa o contêiner até o próximo intervalo. Ele fica mais lento, mas **não é encerrado** |
| **Memória** | O OOM killer do kernel pode encerrar um processo do contêiner ([OOMKill](oomkill.md)); se for o processo principal, o contêiner reinicia |
| **Ephemeral storage** | O kubelet pode **despejar** o Pod |

```yaml
# Trecho didático
resources:
  requests:
    cpu: 250m
    memory: 256Mi
  limits:
    cpu: "1"
    memory: 512Mi
```

## Para que existe e qual problema resolve

Impede que um contêiner com defeito (vazamento de memória, laço infinito) consuma o nó inteiro e prejudique os vizinhos.

## Funcionamento técnico e ciclo de vida

- O kubelet passa os requests e limits ao runtime, que configura os [cgroups](cgroups.md) do contêiner.
- O limit de CPU é um teto rígido por intervalo de tempo.
- O limit de memória é aplicado de forma **reativa**: o encerramento acontece quando o kernel detecta a pressão.
- Se só o limit for definido, o request recebe o mesmo valor, salvo padrão de admissão.
- **Overcommit:** a soma dos limits num nó **pode** passar do Allocatable; a dos requests, não. Por isso, sob carga real, os limits podem não ser todos atendidos ao mesmo tempo.

## Relações e dependências

- Par do [Resource Request](resource-request.md); a relação entre os dois define a [QoS Class](qos-class.md).
- Aplicado por meio de [cgroups](cgroups.md); excesso de memória leva a [OOMKill](oomkill.md).

## Exemplo de situação real

Um serviço tem `limits.memory: 256Mi` e reinicia toda vez que processa um arquivo grande. O status mostra `OOMKilled`. O limite está abaixo do pico real de uso; é preciso medir o uso e ajustá-lo.

## Como visualizar e inspecionar (somente leitura)

```bash
# Limits declarados
oc get pod <nome> -n <namespace> \
  -o jsonpath='{range .spec.containers[*]}{.name}: {.resources.limits}{"\n"}{end}'

# Soma dos limits no nó (pode passar de 100%)
oc describe node <nó> | sed -n '/Allocated resources/,/Events/p'

# Contêineres encerrados por limite de memória
oc get pod <nome> -n <namespace> \
  -o jsonpath='{range .status.containerStatuses[*]}{.name}: restarts={.restartCount} last={.lastState.terminated.reason}{"\n"}{end}'
```

## Como interpretar a saída

- Em `Allocated resources`, a coluna `Limits` acima de 100% é **overcommit**: permitido, mas arriscado sob carga.
- `restarts` crescente com `last=OOMKilled`: limite de memória insuficiente ou vazamento de memória.

## Diferenças e confusões frequentes

- **Limit × request:** teto × reserva.
- **CPU limit × memory limit:** lentidão × encerramento.
- **Sem limit ≠ uso ilimitado seguro:** o contêiner pode usar até a capacidade do nó, e é candidato a ser despejado sob pressão.

## No OpenShift 4.22 versus Kubernetes

Mesmo mecanismo. Projetos do OpenShift costumam ter LimitRange com limits padrão (lote 2 desta categoria).

## No HomeLab SNO

Defina limits de memória nas aplicações de estudo, para que um erro não pressione o nó único inteiro.

## Termos relacionados

[Resource Request](resource-request.md) · [OOMKill](oomkill.md) · [QoS Class](qos-class.md) · [cgroups](cgroups.md) · [CPU](cpu.md) · [Memory](memory.md)

## Fontes oficiais

- Kubernetes — Resource Management for Pods and Containers, "Requests and limits", "How Kubernetes applies resource requests and limits", "My container is terminated": <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> (fonte: `kubernetes/website` `release-1.35`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/resource-limit
- **Termo original:** resource limit (`resources.limits`)
- **Remissões:** overcommit
- **Tradução:** limite de recursos (só como apoio)
- **Classe ontológica:** conceito (campo do contêiner)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-05

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-05.
- **Pendências:** o despejo por limite de `ephemeral-storage` vem da documentação de armazenamento efêmero, citada e **não lida** nesta rodada.

</details>
