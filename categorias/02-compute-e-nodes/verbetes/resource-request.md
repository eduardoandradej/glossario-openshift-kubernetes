# Resource Request

## Definição em uma frase

Um Resource Request (`resources.requests`) é a **quantidade de um recurso (CPU, memória, armazenamento efêmero) que um contêiner declara precisar**. O scheduler usa esse valor para escolher um nó que tenha esse espaço disponível.

## Explicação didática

É uma **reserva**: "este contêiner precisa de pelo menos 250m de CPU e 256Mi de memória". O scheduler só coloca o Pod num nó em que a soma dos *requests* já agendados mais o novo caiba no [Allocatable](allocatable.md). O consumo real pode ser maior ou menor; o request é o que conta para o agendamento.

```yaml
# Trecho didático de um contêiner
resources:
  requests:
    cpu: 250m
    memory: 256Mi
```

## Para que existe e qual problema resolve

Evita superlotar nós. Mesmo que o uso real esteja baixo no momento, o scheduler **recusa** colocar um Pod onde os requests não cabem, para proteger o nó de picos futuros.

## Funcionamento técnico e ciclo de vida

- **Agendamento:** para cada tipo de recurso, a soma dos requests dos contêineres agendados num nó precisa ser menor que a capacidade alocável desse nó.
- **No nó:** o request de CPU vira um **peso** (mais request, mais tempo de CPU sob disputa); o request de memória pode ser usado como referência no cgroup v2.
- **Sem request, mas com limit:** se só o limit for definido e nenhum mecanismo de admissão (como um LimitRange) aplicar um padrão, o Kubernetes **copia o limit para o request**.
- **Pod-level resources:** versões recentes permitem declarar recursos no nível do Pod, além do contêiner. Confira a disponibilidade no seu cluster antes de usar.
- O request também influencia a [QoS Class](qos-class.md) e a ordem de despejo sob pressão.

## Relações e dependências

- Comparado ao [Allocatable](allocatable.md) do nó pelo [kube-scheduler](../../01-arquitetura-e-control-plane/verbetes/kube-scheduler.md).
- Par do [Resource Limit](resource-limit.md); define a [QoS Class](qos-class.md).
- Pode receber padrões e restrições de LimitRange e ResourceQuota (lote 2 desta categoria).

## Exemplo de situação real

Um Deployment escala para 5 réplicas, mas só 3 sobem; as outras ficam `Pending` com `Insufficient cpu`. O uso real de CPU do nó está em 20%, mas os **requests** já somam quase todo o Allocatable. Para caber, é preciso reduzir os requests (se estiverem superdimensionados) ou ter mais capacidade.

## Como visualizar e inspecionar (somente leitura)

```bash
# Requests declarados no Pod
oc get pod <nome> -n <namespace> \
  -o jsonpath='{range .spec.containers[*]}{.name}: {.resources.requests}{"\n"}{end}'

# Soma dos requests no nó, comparada ao Allocatable
oc describe node <nó> | sed -n '/Allocated resources/,/Events/p'

# Por que um Pod não foi agendado
oc get events -n <namespace> --field-selector reason=FailedScheduling
```

## Como interpretar a saída

- Em `Allocated resources`, a coluna `Requests` com percentuais altos significa nó "cheio" para o scheduler, independentemente do uso real.
- Mensagens `Insufficient cpu` ou `Insufficient memory` em `FailedScheduling` indicam que o request não cabe em nenhum nó.

## Diferenças e confusões frequentes

- **Request × uso real:** o scheduler olha o request; o monitoramento mostra o uso.
- **Request × limit:** mínimo reservado × teto.
- **Request alto demais desperdiça capacidade; baixo demais aumenta o risco de despejo.**

## No OpenShift 4.22 versus Kubernetes

Mesmo mecanismo. No OpenShift, projetos costumam ter LimitRange e ResourceQuota, criados pelo *project template*, que impõem requests padrão e máximos.

## No HomeLab SNO

Os componentes da plataforma já consomem parte do Allocatable com seus requests. Use requests pequenos nas aplicações de estudo e confira o espaço em `Allocated resources`.

## Termos relacionados

[Resource Limit](resource-limit.md) · [Allocatable](allocatable.md) · [QoS Class](qos-class.md) · [CPU](cpu.md) · [Memory](memory.md) · [kube-scheduler](../../01-arquitetura-e-control-plane/verbetes/kube-scheduler.md)

## Fontes oficiais

- Kubernetes — Resource Management for Pods and Containers, "Requests and limits", "How Pods with resource requests are scheduled", "Pod-level resource specification": <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> (fonte: `kubernetes/website` `release-1.35`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/resource-request
- **Termo original:** resource request (`resources.requests`)
- **Tradução:** requisição de recursos (só como apoio)
- **Classe ontológica:** conceito (campo do contêiner)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-05

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-05.
- **Pendências:** o estado de maturidade de *pod-level resources* no Kubernetes 1.35 e no OCP 4.22 **não foi verificado**; conferir com `oc explain pod.spec.resources`.

</details>
