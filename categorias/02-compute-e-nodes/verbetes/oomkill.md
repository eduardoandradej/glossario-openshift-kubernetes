# OOMKill

## Definição em uma frase

OOMKill é o **encerramento de um processo pelo OOM killer do kernel Linux** quando falta memória. No Kubernetes, aparece como `OOMKilled` no status do contêiner, quando ele passa do seu limite de memória ou quando o nó fica sem memória.

## Explicação didática

"OOM" é *out of memory*. Quando um processo tenta usar mais memória do que o seu cgroup permite, ou o nó inteiro fica sem memória, o kernel escolhe um processo e o encerra para se proteger. Se o processo encerrado for o principal do contêiner, o contêiner termina com o motivo `OOMKilled`, e o kubelet o reinicia conforme a `restartPolicy`.

## Para que existe e qual problema resolve

É a última linha de defesa da memória: impede que um processo derrube a máquina inteira.

## Funcionamento técnico e ciclo de vida

Duas situações diferentes:

1. **Limite do contêiner:** o contêiner passa do seu `limits.memory`, e o OOM killer age **dentro do cgroup do contêiner**. É o caso mais comum.
2. **Falta de memória no nó:** antes que o kubelet consiga liberar memória por despejo, o nó fica sem memória, e o OOM killer escolhe a vítima pelo `oom_score`. Esse valor é a porcentagem de memória do nó usada pelo processo, somada ao `oom_score_adj`, que o kubelet define pela [QoS Class](qos-class.md): Guaranteed `-997`, BestEffort `1000`, Burstable intermediário. Resultado: contêineres de QoS baixa que usam muita memória em relação ao seu request são encerrados primeiro.

O limite de memória é aplicado de forma reativa: o contêiner pode passar dele por um momento antes de ser encerrado.

## Relações e dependências

- Consequência de [Resource Limit](resource-limit.md) de memória e de falta de [Memory](memory.md) no nó.
- Ordem de vítimas influenciada pela [QoS Class](qos-class.md); aplicado pelos [cgroups](cgroups.md).
- Diferente do despejo (*eviction*) decidido pelo kubelet ([Node Condition](node-condition.md)).

## Exemplo de situação real

Um Pod aparece em `CrashLoopBackOff`. Em `oc describe pod`, o contêiner mostra `Last State: Terminated`, `Reason: OOMKilled`, e `Restart Count` crescente. O processo estoura o limite a cada execução; é preciso ajustar o limite ou corrigir o consumo de memória.

## Como visualizar e inspecionar (somente leitura)

```bash
# Motivo do último encerramento e reinícios de cada contêiner
oc get pod <nome> -n <namespace> \
  -o jsonpath='{range .status.containerStatuses[*]}{.name}: last={.lastState.terminated.reason} exit={.lastState.terminated.exitCode} restarts={.restartCount}{"\n"}{end}'

# Visão humana (seções Last State e Events)
oc describe pod <nome> -n <namespace>

# Limite configurado e uso atual
oc get pod <nome> -n <namespace> -o jsonpath='{.spec.containers[*].resources.limits.memory}{"\n"}'
oc adm top pod <nome> -n <namespace>
```

## Como interpretar a saída

- `last=OOMKilled`, normalmente com `exitCode` `137` (processo encerrado por `SIGKILL`), confirma o OOMKill.
- Uso de memória sempre perto do limite antes de cada reinício indica limite curto ou vazamento de memória.

## Diferenças e confusões frequentes

- **OOMKill × eviction:** o kernel encerra um processo × o kubelet encerra e marca um Pod como `Failed` (`Evicted`).
- **OOMKill × CrashLoopBackOff:** `CrashLoopBackOff` é o estado de espera entre reinícios; o OOMKill pode ser a causa.
- **Excesso de CPU não causa OOMKill;** causa throttling.

## No OpenShift 4.22 versus Kubernetes

Mesmo mecanismo. O uso de cgroup v2 no OpenShift exige runtimes compatíveis (por exemplo, versões de Java listadas na documentação), para que a aplicação "enxergue" o limite do contêiner e não seja encerrada por calcular a memória errada.

## No HomeLab SNO

OOMKills frequentes num SNO pequeno também podem indicar falta de memória do **nó**. Verifique a condição `MemoryPressure` antes de culpar a aplicação.

## Termos relacionados

[Resource Limit](resource-limit.md) · [Memory](memory.md) · [QoS Class](qos-class.md) · [cgroups](cgroups.md) · [Node Condition](node-condition.md)

## Fontes oficiais

- Kubernetes — Resource Management for Pods and Containers, "How Kubernetes applies resource requests and limits" e "My container is terminated": <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> (fonte: `kubernetes/website` `release-1.35`)
- Kubernetes — Node-pressure Eviction, "Node out of memory behavior": <https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/>
- OCP 4.22 — About Linux cgroup version 2 (fonte: `modules/architecture-about-cgroup-v2.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/oomkill
- **Termo original:** OOMKill, OOMKilled, OOM killer
- **Tradução:** encerramento por falta de memória (só como apoio)
- **Classe ontológica:** estado / evento (motivo de encerramento de contêiner)
- **Plataforma:** Kubernetes / OpenShift (mecanismo do kernel Linux)
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-05

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-05.
- **Pendências:** o `exitCode` 137 é a convenção de sinal `SIGKILL` (128 + 9), mas **não foi citado** nas páginas lidas; confirmar num caso real no SNO.

</details>
