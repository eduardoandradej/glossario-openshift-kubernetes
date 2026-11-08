# DaemonSet

## Definição em uma frase

O DaemonSet garante que **todos os nós, ou um subconjunto deles, rodem uma cópia de um [Pod](pod.md)**: quando um nó entra no cluster, o Pod é criado nele; quando o nó sai, o Pod é removido.

## Explicação didática

Algumas tarefas precisam rodar **em cada máquina**: coletar logs, monitorar o nó, fornecer a rede ou o armazenamento local. Em vez de contar réplicas, o DaemonSet pensa em **nós**: "um Pod por nó elegível". O número de Pods acompanha o número de nós.

## Para que existe e qual problema resolve

Fornece serviços locais de nó, fundamentais para a operação do cluster ou de *add-ons*. A documentação cita como usos típicos daemons de armazenamento, coleta de logs e monitoramento em cada nó.

## Funcionamento técnico e ciclo de vida

- O controller de DaemonSet cria um Pod por nó que satisfaz o seletor de nós e a afinidade do template.
- Apagar o DaemonSet remove os Pods que ele criou.
- **Tolerations automáticas:** o controller acrescenta tolerations a taints como `memory-pressure`, `disk-pressure` e de nó não agendável, para que os daemons não sejam interrompidos por essas condições. Ver [Toleration](../../02-compute-e-nodes/verbetes/toleration.md).
- **Atualização:** suporta rolling update (padrão) e `OnDelete` (o Pod só é trocado quando apagado manualmente).
- No [Drain](../../02-compute-e-nodes/verbetes/drain.md), os Pods de DaemonSet são tratados à parte (`--ignore-daemonsets`).

## Relações e dependências

- Gerencia [Pods](pod.md), um por [Node](../../02-compute-e-nodes/verbetes/node.md) elegível.
- Usa [Node Selector](../../02-compute-e-nodes/verbetes/node-selector.md) ou [Node Affinity](../../02-compute-e-nodes/verbetes/node-affinity.md) para limitar os nós.
- Muitos componentes de plataforma do OpenShift são DaemonSets (CoreDNS, OVN-Kubernetes, MCD...).

## Exemplo de situação real

Um novo worker entra no cluster e, em poucos segundos, recebe os Pods do agente de logs, do DNS e da rede, sem que ninguém tenha escalado nada. São todos DaemonSets.

## Como visualizar e inspecionar (somente leitura)

```bash
# DaemonSets: desejado, atual, pronto, por nó
oc get daemonsets -A

# Em quais nós os Pods de um DaemonSet estão
oc get pods -n <namespace> -l <label> -o wide

# Seletor de nós e estratégia de atualização
oc describe daemonset <nome> -n <namespace>
```

## Como interpretar a saída

- `DESIRED` é o número de nós elegíveis; `READY` menor indica Pods com problema em algum nó. Veja qual com `-o wide`.
- A coluna `NODE SELECTOR` mostra se o DaemonSet roda só em parte dos nós (por exemplo, só em Linux ou só em workers).

## Diferenças e confusões frequentes

- **DaemonSet × Deployment:** um por nó × N réplicas em quaisquer nós.
- **DaemonSet × Static Pod:** objeto da API gerenciado por controller × arquivo local gerenciado pelo kubelet. A documentação recomenda DaemonSet para rodar algo em todos os nós.

## No OpenShift 4.22 versus Kubernetes

Mesmo objeto (`apps/v1`). Vários componentes da plataforma são DaemonSets gerenciados por Operators: não os edite.

## No HomeLab SNO

Cada DaemonSet tem `DESIRED 1`, porque há um único nó. `oc get daemonsets -A` é uma boa forma de ver quais serviços de nó a plataforma roda.

## Termos relacionados

[Pod](pod.md) · [Node](../../02-compute-e-nodes/verbetes/node.md) · [Toleration](../../02-compute-e-nodes/verbetes/toleration.md) · [Static Pod](../../01-arquitetura-e-control-plane/verbetes/static-pod.md) · [CoreDNS](../../01-arquitetura-e-control-plane/verbetes/coredns.md) · [Device Plugin](../../02-compute-e-nodes/verbetes/device-plugin.md)

## Fontes oficiais

- Kubernetes — DaemonSet: <https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/> (fonte: `kubernetes/website` `release-1.35`, `concepts/workloads/controllers/daemonset.md`)
- Kubernetes — Taints and Tolerations (tolerations automáticas de DaemonSets): <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/daemonset
- **Termo original:** DaemonSet
- **Tradução:** não se traduz
- **Classe ontológica:** objeto da API
- **API:** `apiVersion: apps/v1`, `kind: DaemonSet`
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** namespaced
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido (antes era uma versão inicial). Fontes conferidas em 2026-11-08.
- **Pendências:** as estratégias de atualização (`RollingUpdate` e `OnDelete`) são conhecidas da página de atualização de DaemonSets, que **não foi lida**; confirmar com `oc explain daemonset.spec.updateStrategy`.

</details>
