# cgroups

## Definição em uma frase

cgroups (*control groups*) são o mecanismo do kernel Linux que **agrupa processos e limita, contabiliza e isola os recursos** (CPU, memória, I/O) que eles podem usar. É sobre eles que o Kubernetes aplica requests e limits.

## Explicação didática

Quando você define `limits.memory: 512Mi`, quem realmente impõe o limite é o kernel, através do cgroup do contêiner. O [kubelet](../../01-arquitetura-e-control-plane/verbetes/kubelet.md) passa os valores ao runtime, e o runtime configura os cgroups. Os cgroups formam uma **hierarquia**: há grupos para o sistema, para os Pods e, dentro de cada Pod, para os contêineres.

Existem duas versões:

| Versão | Características |
|---|---|
| **cgroup v1** | Várias hierarquias separadas por tipo de recurso |
| **cgroup v2** | Hierarquia **única e unificada**, delegação mais segura para contêineres, *Pressure Stall Information* (PSI), melhor isolamento e contabilidade de memória |

## Para que existe e qual problema resolve

Permite que muitos contêineres compartilhem uma máquina sem que um consuma os recursos de todos. É a base técnica de requests, limits, QoS e do isolamento de recursos entre Pods.

## Funcionamento técnico e ciclo de vida

- **CPU:** o request vira peso (mais tempo de CPU sob disputa); o limit vira um teto por intervalo de tempo (throttling).
- **Memória:** o limit é o limite do cgroup, e exceder leva ao [OOMKill](oomkill.md). No cgroup v2, o request pode orientar `memory.min` e `memory.low`.
- **Reserva do sistema:** no OpenShift, os recursos reservados para os componentes do nó ficam no cgroup `system.slice` (ver [Allocatable](allocatable.md)).
- Alguns recursos do Kubernetes funcionam **apenas com cgroup v2**, como o *MemoryQoS*.

## Relações e dependências

- Configurados pelo runtime ([CRI-O](../../01-arquitetura-e-control-plane/verbetes/cri-o.md)) a pedido do [kubelet](../../01-arquitetura-e-control-plane/verbetes/kubelet.md).
- Aplicam [Resource Request](resource-request.md), [Resource Limit](resource-limit.md) e [QoS Class](qos-class.md).

## Exemplo de situação real

Depois de migrar para um cluster com cgroup v2, uma aplicação Java antiga passa a ser encerrada por OOM: a JVM calcula o *heap* pela memória total do nó, e não pelo limite do contêiner, porque a versão não entende cgroup v2. A correção é usar uma versão do Java compatível.

## Como visualizar e inspecionar (somente leitura)

```bash
# Versão de cgroup configurada no cluster (OpenShift)
oc get nodes.config.openshift.io cluster -o jsonpath='{.spec.cgroupMode}{"\n"}'

# A partir de um contêiner em execução: tipo de sistema de arquivos dos cgroups
oc exec <pod> -n <namespace> -- stat -fc %T /sys/fs/cgroup/
```

## Como interpretar a saída

- `cgroupMode` igual a `v2` (ou vazio, que significa o padrão da versão) indica cgroup v2. Confirme o significado do valor vazio com `oc explain nodes.config.openshift.io.spec.cgroupMode`.
- `stat -fc %T /sys/fs/cgroup/` mostrando `cgroup2fs` confirma cgroup v2 dentro do contêiner; `tmpfs` indica cgroup v1.

## Diferenças e confusões frequentes

- **cgroups × namespaces do Linux:** cgroups **limitam recursos**; os namespaces do Linux (pid, net, mnt...) **isolam a visão** do processo. São coisas diferentes de Namespace do Kubernetes.
- **cgroup v1 × v2:** comportamento diferente em CPU, memória e I/O. Agentes e runtimes antigos podem não funcionar no v2.

## No OpenShift 4.22 versus Kubernetes

O OpenShift 4.22 **usa cgroup v2**. A documentação alerta para atualizar agentes de monitoramento e segurança que dependem do sistema de arquivos de cgroups, o cAdvisor avulso (v0.43.0 ou mais recente) e runtimes Java e Node.js para versões compatíveis.

## No HomeLab SNO

O nó do SNO usa cgroup v2. Não altere o modo de cgroup do cluster: isso reconfigura e reinicia o nó.

## Termos relacionados

[Resource Limit](resource-limit.md) · [Resource Request](resource-request.md) · [OOMKill](oomkill.md) · [QoS Class](qos-class.md) · [Allocatable](allocatable.md) · [CRI-O](../../01-arquitetura-e-control-plane/verbetes/cri-o.md)

## Fontes oficiais

- Kubernetes — About cgroup v2: <https://kubernetes.io/docs/concepts/architecture/cgroups/> (fonte: `kubernetes/website` `release-1.35`, `concepts/architecture/cgroups.md`)
- Kubernetes — Resource Management for Pods and Containers, "How Kubernetes applies resource requests and limits": <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>
- OCP 4.22 — About Linux cgroup version 2 (fonte: `modules/architecture-about-cgroup-v2.adoc`)
- OCP 4.22 — Allocating resources for nodes (`system.slice`; fonte: `modules/nodes-nodes-resources-configuring-about.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/cgroups
- **Termo original:** control groups (cgroups), cgroup v1, cgroup v2
- **Tradução:** grupos de controle (só como apoio)
- **Classe ontológica:** tecnologia (mecanismo do kernel Linux)
- **Plataforma:** Linux / Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário → avançado
- **Atualizado em:** 2026-11-05

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-05.
- **Pendências:** o campo `nodes.config.openshift.io/cluster` `spec.cgroupMode` é conhecido da configuração de cgroup do OpenShift, mas **não foi conferido** nos módulos lidos; validar com `oc explain`. O comando `stat` depende de a imagem do contêiner ter essa ferramenta.

</details>
