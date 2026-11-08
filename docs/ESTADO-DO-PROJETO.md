# Estado do projeto

## Rodada 2026-11-08 — categoria 03, lote 1

- **11 verbetes:** Pod, Deployment, ReplicaSet, StatefulSet, DaemonSet e Job (reescritos; antes versões iniciais), Container, Pod Template, CronJob, ReplicationController (legado) e DeploymentConfig (deprecated desde o 4.14). Remissões: Replica (→ ReplicaSet) e Batch (→ Job).
- **Fatos verificados (Kubernetes 1.35):** rollout só com mudança no template; `maxUnavailable`/`maxSurge` 25%; seletor do Deployment imutável; StatefulSet com Headless Service, ordinais, `volumeClaimTemplates`, `OrderedReady` e volumes preservados; Job com `backoffLimit` 6 e `restartPolicy` Never/OnFailure; CronJob com `concurrencyPolicy` Allow/Forbid/Replace; ReplicationController substituído por Deployment/ReplicaSet.
- README: categoria 03 como Em construção.

### Próximo lote recomendado (categoria 03, lote 2)

Pod Lifecycle, Pod Phase (com Pending, Running, Completed), Pod Condition, Container Lifecycle, Restart Policy, Init Container, Sidecar Container, Ephemeral Container, Termination Grace Period, Terminating, CrashLoopBackOff e ImagePullBackOff. Lote 3: Rollout, RollingUpdate, Recreate, Rollback, Readiness/Liveness/Startup Probe, Lifecycle Hook, PreStop e HorizontalPodAutoscaler.

## Rodada 2026-11-07 (2) — categoria 02, lote 3 (categoria concluída)

- **9 verbetes:** Machine, MachineSet, MachineHealthCheck, BareMetalHost, RHCOS, HugePages, Extended Resource, Device Plugin e NUMA.
- **Categoria 02 coberta:** 35/35 candidatos (32 verbetes + 3 remissões). README: categoria 02 como Concluída.
- **Fatos do OCP 4.22:** Machine API baseada no Cluster API (MachineSet ≈ ReplicaSet para máquinas; uma zona por machine set); regras do MachineHealthCheck (um nó por vez, `maxUnhealthy`); recursos do Bare Metal Operator; características do RHCOS (`rpm-ostree`, `/usr` somente leitura, `/var/lib/containers`); huge pages via Node Tuning Operator; NUMA Resources Operator com scheduler secundário.
- **Divergência registrada:** HugePages com vários tamanhos por nó (Kubernetes) × um tamanho por nó (OCP 4.22).

### Próximo passo recomendado

Categoria 03 (Workloads), reescrevendo as 6 versões iniciais (Pod, Deployment, ReplicaSet, StatefulSet, DaemonSet, Job), ou a revisão das categorias 00 a 02.

## Rodada 2026-11-07 — categoria 02, lote 2

- **11 verbetes:** Node Label, Node Annotation, Taint, Toleration, Node Selector, Node Affinity, Cordon, Drain, Node Debug, LimitRange e ResourceQuota. Remissão: Uncordon (→ Cordon).
- **Fatos do OCP 4.22:** drain indisponível em SNO; `oc debug node` + `chroot /host` como acesso recomendado (SSH desaconselhado); node selector padrão do cluster e por projeto (`openshift.io/node-selector`, com precedência do projeto); ClusterResourceQuota para vários projetos; tolerations padrão por namespace via annotation.

### Próximo lote recomendado (categoria 02, lote 3, que fecha a categoria)

Machine, MachineSet, MachineHealthCheck, BareMetalHost, RHCOS, HugePages, Extended Resource, Device Plugin e NUMA.

## Rodada 2026-11-05 (2) — categoria 02, lote 1

- **12 verbetes:** Node (reescrito, antes versão inicial), Node Condition, Capacity, Allocatable, CPU, Memory, Ephemeral Storage, Resource Request, Resource Limit, QoS Class, OOMKill e cgroups. Remissões: Node Ready e Node Pressure (→ Node Condition).
- **Fatos do OCP 4.22:** reserva automática de CPU e memória para o sistema (fórmulas documentadas); `Allocatable = Capacity − system-reserved − hard eviction thresholds`; `kubeReserved` não suportado; reserva automática desabilitada em clusters atualizados de antes da 4.21; cgroup v2 como padrão.
- README: categoria 02 como Em construção.

### Próximo lote recomendado (categoria 02, lote 2)

Node Label, Node Annotation, Taint, Toleration, Node Selector, Node Affinity, Cordon, Drain, Uncordon, Node Debug, LimitRange e ResourceQuota. Lote 3: Machine, MachineSet, MachineHealthCheck, BareMetalHost, RHCOS, HugePages, Extended Resource, Device Plugin e NUMA.

## Rodada 2026-11-05 — categoria 01, lote 3 (categoria concluída)

- **7 verbetes:** Bootstrap, Quorum, High Availability, SNO, HyperShift, Hosted Control Plane e Infrastructure Node.
- **Categoria 01 coberta:** 31/31 candidatos (28 verbetes + 3 remissões). README: categoria 01 como Concluída.
- **Fatos verificados:** passos do bootstrapping; `bootstrap-in-place` no SNO; SNO em hipervisor usa `platform.none` na maioria dos casos; recursos mínimos do SNO (4 vCPU, 16 GB, 120 GB); Two-Node with Arbiter e two-node com fencing GA no 4.22; HCP com HyperShift Operator, MCE e API `hypershift.openshift.io`; regras de infra node (assinatura e pool `infra`).

### Próximo passo recomendado

Revisão das categorias 00 e 01 com o `PROMPT-REVISAO.md`, ou a categoria 02 (Compute, Nodes e capacidade), aprofundando o verbete Node.

## Rodada 2026-11-04 (5) — categoria 01, lote 2, e ajustes de apresentação

- **Lote 2 (9 verbetes):** kube-proxy, OVN-Kubernetes, CoreDNS, DNS Operator, Cluster DNS, Cluster Version Operator, Machine Config Operator, MachineConfig e MachineConfigPool. Remissão: Cluster Operator (→ ClusterOperator, categoria 09).
- **Apresentação (decisões do autor):** README sóbrio, sem controles internos; páginas de categoria só com termos publicados e "Em breve"; índices sem ícones; ficha técnica e notas de revisão dos verbetes num bloco recolhido no fim; seção "Diagrama" (sem "Mermaid"); ícones limitados a ✅/🚧/📝 na tabela do README.
- Fontes: `openshift-docs` `enterprise-4.22` (OVN-Kubernetes, DNS Operator, Cluster Network Operator, CVO, OSUS, release images, MCO, MachineConfig, MCP) e Kubernetes 1.35 (kube-proxy opcional, DNS).

### Próximo lote recomendado (categoria 01, lote 3, que fecha a categoria)

Bootstrap, Quorum, High Availability, SNO, HyperShift, Hosted Control Plane e Infrastructure Node.

## Rodada 2026-11-04 (4) — padronização de termos e categoria 01, lote 1

- **Padronização (decisão do autor):** termos técnicos no original em inglês (Control Plane, Desired State, Current State, Reconciliation, Garbage Collection, Object, Resource...), com o conceito explicado em português. Toda a categoria 00 foi ajustada, e a regra está no `CLAUDE.md` e no modelo de verbete.
- **Categoria 01, lote 1 (12 verbetes):** Control Plane, Worker Node, Master Node (legado), etcd, kube-scheduler, kube-controller-manager, cloud-controller-manager, kubelet, Container Runtime, CRI, CRI-O e Static Pod. Remissões: kube-apiserver (→ API Server, categoria 00) e Node Agent (→ kubelet).
- Fontes: `kubernetes/website` `release-1.35` (glossário, kube-scheduler, cloud-controller, CRI, static pods) e `openshift-docs` `enterprise-4.22` (machine roles, etcd overview, Cloud Controller Manager Operator).
- Todos desenvolvidos: **sem validação no cluster**.

### Próximo lote recomendado (categoria 01, lote 2)

Kube Proxy, OVN-Kubernetes, CoreDNS, DNS Operator, Cluster DNS, Cluster Version Operator, Cluster Operator (remissão para a categoria 09), Machine Config Operator, MachineConfig e MachineConfigPool. Lote 3: Bootstrap, Quorum, High Availability, SNO, HyperShift, Hosted Control Plane e Infrastructure Node.

## Rodada 2026-11-04 (3) — categoria 00, lote 3 (categoria coberta)

- **12 verbetes novos:** Project, Label, Annotation, Selector, OwnerReference, Finalizer, Garbage Collection, ResourceVersion, Generation, ObservedGeneration, Conditions e Events.
- **Categoria 00 coberta:** os 37 candidatos viraram 34 verbetes e 3 remissões (K8s, Control Loop e o próprio API/Kubernetes API). Todos desenvolvidos: **sem validação no cluster**.
- **Correção transversal:** no Kubernetes 1.35, `resourceVersion` passou a ser ordenável dentro do mesmo tipo de recurso (requisito de conformidade). O verbete Metadata foi ajustado.
- Remissões "verbete futuro" dos lotes anteriores agora apontam para páginas existentes.

### Próximo passo recomendado

1. **Revisão da categoria 00** com o [prompt de revisão](../PROMPT-REVISAO.md), gerando `docs/revisoes/00-fundamentos-e-linguagem.md`.
2. **Validação no SNO**, com autorização do autor, dos itens de [TERMOS-A-VALIDAR](TERMOS-A-VALIDAR.md).
3. Depois disso, a categoria **01 — Arquitetura e control plane**.

## Rodada 2026-11-04 (2) — categoria 00, lote 2

- **10 verbetes novos:** API Server, API Group, API Version, Manifest, YAML, JSON, Metadata, Controller, Resource Name e UID. **Namespace** reescrito (de semente para desenvolvido). **Control Loop** virou remissão para Controller e Reconciliation.
- Fontes: `kubernetes/website` `release-1.35` (names, namespaces, using-api, api-concepts, components, controller, glossário), API Conventions e `openshift-docs` `enterprise-4.22` (control plane / machine roles, working with projects, glossary).
- Todos desenvolvidos: **sem validação no cluster**; pendências em [TERMOS-A-VALIDAR](TERMOS-A-VALIDAR.md).
- **README:** abertura com apresentação do autor, LinkedIn e Credly. Os repositórios de curso privados não são mais citados.

### Próximo lote recomendado na época (categoria 00, lote 3) — concluído

Project, Label, Annotation, Selector, OwnerReference, Finalizer, Garbage Collection, ResourceVersion, Generation, ObservedGeneration, Conditions e Events.

## Rodada 2026-11-04 — categoria 00, lote 1

- **Kit inicial importado** para a `main` sem alterações (commit próprio).
- **12 verbetes desenvolvidos** na categoria 00, mais 1 remissão (K8s): Kubernetes, OpenShift Container Platform, Cluster, API, Objeto, Recurso, Kind, Spec, Status, Desired state, Current state, Reconciliation.
- Estado de todos: **desenvolvido**. Fontes oficiais conferidas, mas **sem validação no cluster** e com as URLs publicadas não abertas (detalhes em [TERMOS-A-VALIDAR](TERMOS-A-VALIDAR.md)). Nenhum deles é considerado "concluído".
- **Versão de referência confirmada:** o OCP 4.22 usa **Kubernetes 1.35** com CRI-O (release notes 4.22). Os fontes do Kubernetes foram lidos na branch `release-1.35`.
- **Novos índices:** [por categoria](INDICE-POR-CATEGORIA.md), [mapa de relações](MAPA-DE-RELACOES.md), [termos a validar](TERMOS-A-VALIDAR.md); [índice alfabético](INDICE-ALFABETICO.md) refeito com estados e remissões.
- **Novo diagrama:** [00 — modelo declarativo](../diagramas/00-modelo-declarativo.md).
- **Inventário:** as 13 entradas trabalhadas em `dados/inventario.json` foram classificadas (`kind_class`, `scope`, `fontes`, `slug_verbete`, `relacoes`, `verificado_em`, `validacao_cluster`).
- **HomeLab:** não acessado. Nenhum comando foi executado no cluster.

### Próximo lote recomendado na época (categoria 00, lote 2) — concluído

API Server, API Group, API Version, Manifest, YAML, JSON, Metadata, Controller, Control Loop (remissão para Reconciliation), Resource Name, UID e revisão do Namespace (semente → desenvolvido). Lote 3: Project, Label, Annotation, Selector, OwnerReference, Finalizer, Garbage Collection, ResourceVersion, Generation, ObservedGeneration, Conditions, Events.

## Estado inicial — 2026-11-03

- Criadas 18 categorias e 680 entradas candidatas brutas (incluindo sinônimos e remissões).
- Geradas 24 páginas-semente, ainda **não concluídas** sob o modelo editorial completo.
- Criados cinco diagramas Mermaid, prompt mestre, prompt de continuação, prompt de revisão e critérios de qualidade.
- Verificação de suporte real via `oc api-resources` no HomeLab: **não realizada**; este artefato não acessou o cluster.
- Publicação no GitHub: **não realizada** na época; o kit foi publicado na `main` em 2026-11-04.
