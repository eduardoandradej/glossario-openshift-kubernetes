# QoS Class

## Definição em uma frase

A QoS Class (*Quality of Service class*) é a **classificação que o Kubernetes dá a cada Pod**, entre `Guaranteed`, `Burstable` e `BestEffort`, conforme os [requests](resource-request.md) e [limits](resource-limit.md) dos seus contêineres. Ela define quem é despejado primeiro quando o nó fica sem recursos.

## Explicação didática

Você não escolhe a QoS diretamente: ela é **calculada** a partir de como os recursos foram declarados.

| Classe | Regra (resumida) | Sob pressão no nó |
|---|---|---|
| **Guaranteed** | Todo contêiner tem request e limit de CPU **e** de memória, maiores que zero e **iguais** entre si | Último a ser despejado |
| **Burstable** | Não é Guaranteed, mas ao menos um contêiner tem algum request ou limit de CPU ou memória | Despejado depois dos BestEffort |
| **BestEffort** | Nenhum contêiner tem request nem limit de CPU ou memória | Primeiro a ser despejado |

Num despejo por pressão de recursos, só os Pods que **passam do seu request** são candidatos.

## Para que existe e qual problema resolve

Dá ao kubelet e ao kernel uma ordem de prioridade objetiva para liberar recursos sem decisões arbitrárias.

## Funcionamento técnico e ciclo de vida

- **Despejo pelo kubelet:** sob pressão, o kubelet despeja primeiro BestEffort, depois Burstable e, por fim, Guaranteed.
- **OOM do kernel:** o kubelet ajusta o `oom_score_adj` de cada contêiner conforme a QoS. Guaranteed recebe `-997` (menos propenso a ser encerrado), BestEffort recebe `1000` (o mais propenso), e Burstable fica no meio, proporcional ao request de memória. Ver [OOMKill](oomkill.md).
- **Guaranteed e CPUs exclusivas:** com a política de CPU `static` do kubelet, Pods Guaranteed podem usar CPUs exclusivas.
- A classe é gravada em `status.qosClass` do Pod.

## Relações e dependências

- Calculada a partir de [Resource Request](resource-request.md) e [Resource Limit](resource-limit.md).
- Determina a ordem de despejo ([Node Condition](node-condition.md)) e o `oom_score_adj` ([OOMKill](oomkill.md)).

## Exemplo de situação real

Num nó com `MemoryPressure`, os Pods de um job de teste, sem requests nem limits, são despejados primeiro. O banco de dados, com requests iguais aos limits, continua rodando. É a QoS funcionando como esperado.

## Como visualizar e inspecionar (somente leitura)

```bash
# Classe de QoS de um Pod
oc get pod <nome> -n <namespace> -o jsonpath='{.status.qosClass}{"\n"}'

# Classe de todos os Pods do namespace
oc get pods -n <namespace> -o custom-columns=POD:.metadata.name,QOS:.status.qosClass
```

## Como interpretar a saída

- `Guaranteed`, `Burstable` ou `BestEffort`, conforme as regras acima.
- Muitos `BestEffort` num nó com pouca memória significam muitos candidatos a despejo.

## Diferenças e confusões frequentes

- **QoS Class × PriorityClass:** a QoS vem dos recursos declarados; a prioridade é definida explicitamente e influencia a preempção (categoria 11).
- **Guaranteed não é imune:** pode ser encerrado se passar do próprio limit, ou em último caso.

## No OpenShift 4.22 versus Kubernetes

Mesmo mecanismo. Componentes críticos da plataforma usam prioridades (como `system-node-critical`) que também protegem do OOM.

## No HomeLab SNO

Para aplicações de estudo que não podem ser despejadas facilmente, use requests e limits iguais (Guaranteed), lembrando que isso reserva recursos do nó único.

## Termos relacionados

[Resource Request](resource-request.md) · [Resource Limit](resource-limit.md) · [OOMKill](oomkill.md) · [Node Condition](node-condition.md) · [Memory](memory.md)

## Fontes oficiais

- Kubernetes — Pod Quality of Service Classes: <https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/> (fonte: `kubernetes/website` `release-1.35`, `concepts/workloads/pods/pod-qos.md`)
- Kubernetes — Node-pressure Eviction, "Node out of memory behavior" (`oom_score_adj` por QoS): <https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/qos-class
- **Termo original:** Quality of Service (QoS) class
- **Remissões:** Guaranteed, Burstable, BestEffort
- **Tradução:** classe de qualidade de serviço (só como apoio)
- **Classe ontológica:** estado (campo `status.qosClass` do Pod)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-05

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-05.
- **Pendências:** a regra para *pod-level resources* também consta na documentação e deve ser incluída quando o recurso for validado no OCP 4.22.

</details>
