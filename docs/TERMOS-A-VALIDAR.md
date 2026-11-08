# Termos e afirmações a validar

> Registro de pendências de verificação. Nada aqui deve ser apresentado como fato confirmado até ser resolvido.

## Limitações da rodada de 2026-11-04 (categoria 00, lote 1)

- **URLs publicadas não abertas:** a rede da sessão bloqueava `kubernetes.io` e `docs.redhat.com`. O conteúdo foi conferido nos **fontes oficiais** dessas documentações, no GitHub:
  - Kubernetes: `kubernetes/website`, branch `release-1.35` (versão usada pelo OCP 4.22);
  - OpenShift: `openshift/openshift-docs`, branch `enterprise-4.22`;
  - convenções da API: `kubernetes/community`, `contributors/devel/sig-architecture/api-conventions.md`.
- **Nenhum comando executado no cluster:** todas as saídas de exemplo são **ilustrativas**.

## Pendências por verbete

| Verbete | O que validar | Como |
|---|---|---|
| [Kubernetes](../categorias/00-fundamentos-e-linguagem/verbetes/kubernetes.md) | Formato de `oc version` no cliente 4.22 | `oc version` no SNO |
| [OpenShift Container Platform](../categorias/00-fundamentos-e-linguagem/verbetes/openshift-container-platform.md) | Colunas de `oc get clusterversion`; URL `html/architecture/architecture` | SNO; abrir URL |
| [Cluster](../categorias/00-fundamentos-e-linguagem/verbetes/cluster.md) | `ROLES` no SNO; campos `controlPlaneTopology`/`infrastructureTopology`; slug da URL do guia de SNO | `oc get nodes`; `oc explain infrastructure.status` |
| [API](../categorias/00-fundamentos-e-linguagem/verbetes/kubernetes-api.md) | Colunas de `oc api-resources -o wide` | SNO |
| [Resource](../categorias/00-fundamentos-e-linguagem/verbetes/resource.md) | Texto exato das mensagens de erro (Forbidden / resource type); `oc auth can-i --subresource` | SNO; `--help` |
| [Kind](../categorias/00-fundamentos-e-linguagem/verbetes/kind.md) | Cabeçalho de `oc explain` | SNO |
| [Spec](../categorias/00-fundamentos-e-linguagem/verbetes/spec.md) | Defaults citados de `Deployment.spec` | `oc explain deployment.spec` |
| [Desired State](../categorias/00-fundamentos-e-linguagem/verbetes/desired-state.md) | `oc diff` como somente leitura no cliente 4.22; URL publicada do "Kubernetes overview" do OCP | `oc diff --help`; abrir docs |
| [Reconciliation](../categorias/00-fundamentos-e-linguagem/verbetes/reconciliation.md) | URL publicada do "Kubernetes overview" do OCP | abrir docs |

### Lote 2

| Verbete | O que validar | Como |
|---|---|---|
| [API Server](../categorias/00-fundamentos-e-linguagem/verbetes/api-server.md) | `oc get apiservices` com `SERVICE` = `openshift-apiserver/api` nos grupos `*.openshift.io`; permissão de `/readyz?verbose`; URL `html/architecture/control-plane` | SNO / `--help` / docs |
| [API Group](../categorias/00-fundamentos-e-linguagem/verbetes/api-group.md) | Tabela de grupos/kinds do OpenShift (`config.openshift.io`) | SNO / `--help` / docs |
| [API Version](../categorias/00-fundamentos-e-linguagem/verbetes/api-version.md) | Texto das mensagens `Warning:` e `no matches for kind` | SNO / `--help` / docs |
| [Manifest](../categorias/00-fundamentos-e-linguagem/verbetes/manifest.md) | Resposta de `oc apply --dry-run=server` | SNO / `--help` / docs |
| [YAML](../categorias/00-fundamentos-e-linguagem/verbetes/yaml.md) | Erros de tipo/`strict decoding` reproduzidos no cliente 4.22 | SNO / `--help` / docs |
| [JSON](../categorias/00-fundamentos-e-linguagem/verbetes/json.md) | Exemplos de `jsonpath` com `range` no SNO | SNO / `--help` / docs |
| [Metadata](../categorias/00-fundamentos-e-linguagem/verbetes/metadata.md) | Annotations `openshift.io/sa.scc.*` (aprofundar na categoria 08) | SNO / `--help` / docs |
| [Controller](../categorias/00-fundamentos-e-linguagem/verbetes/controller.md) | Namespace dos Leases de eleição de líder; campo de origem dos Events | SNO / `--help` / docs |
| [Resource Name](../categorias/00-fundamentos-e-linguagem/verbetes/resource-name.md) | Coluna "Usada por" (inferida); URL de "Working with projects" | SNO / `--help` / docs |
| [UID](../categorias/00-fundamentos-e-linguagem/verbetes/uid.md) | Adoção após `--cascade=orphan` (lote 3: OwnerReference, Garbage Collection) | SNO / `--help` / docs |
| [Namespace](../categorias/00-fundamentos-e-linguagem/verbetes/namespace.md) | Label `kubernetes.io/metadata.name` e annotations `openshift.io/*` em `oc describe namespace` | SNO / `--help` / docs |

### Lote 3

| Verbete | O que validar | Como |
|---|---|---|
| [Project](../categorias/00-fundamentos-e-linguagem/verbetes/project.md) | `project.config.openshift.io/cluster`; colunas de `oc get projects`; self-provisioner (cat. 07) | SNO / docs |
| [Label](../categorias/00-fundamentos-e-linguagem/verbetes/label.md) | Páginas Recommended/Well-Known Labels não lidas; `app.kubernetes.io/part-of` na Topology | SNO / docs |
| [Annotation](../categorias/00-fundamentos-e-linguagem/verbetes/annotation.md) | `last-applied-configuration` e `deployment.kubernetes.io/revision` | SNO / docs |
| [Selector](../categorias/00-fundamentos-e-linguagem/verbetes/selector.md) | Label `kubernetes.io/service-name` em EndpointSlices (cat. 04) | SNO / docs |
| [OwnerReference](../categorias/00-fundamentos-e-linguagem/verbetes/owner-reference.md) | Regras de adoção do ReplicaSet (cat. 03) | SNO / docs |
| [Finalizer](../categorias/00-fundamentos-e-linguagem/verbetes/finalizer.md) | Nomes das condições de Namespace; finalizer `kubernetes` em `spec.finalizers` | SNO / docs |
| [Garbage Collection](../categorias/00-fundamentos-e-linguagem/verbetes/garbage-collection.md) | GC de imagens via `KubeletConfig` no OCP (cat. 02) | SNO / docs |
| [ResourceVersion](../categorias/00-fundamentos-e-linguagem/verbetes/resource-version.md) | Mensagem de conflito; ordenação em grupos agregados `*.openshift.io` | SNO / docs |
| [Generation](../categorias/00-fundamentos-e-linguagem/verbetes/generation.md) | Regra de CRDs com subrecurso `status` (cat. 09) | SNO / docs |
| [ObservedGeneration](../categorias/00-fundamentos-e-linguagem/verbetes/observed-generation.md) | `oc rollout status` e `observedGeneration` | SNO / docs |
| [Conditions](../categorias/00-fundamentos-e-linguagem/verbetes/conditions.md) | Lista de condições de Pod no 1.35 (cat. 03); `Upgradeable` em ClusterOperators | SNO / docs |
| [Events](../categorias/00-fundamentos-e-linguagem/verbetes/events.md) | `--event-ttl` (padrão K8s e valor no OCP); `oc events`; field selectors | SNO / docs |

## Categoria 01 — lote 1

| Verbete | O que validar | Como |
|---|---|---|
| [Control Plane](../categorias/01-arquitetura-e-control-plane/verbetes/control-plane.md) | Label `node-role.kubernetes.io/control-plane`; nomes dos ClusterOperators | SNO / docs |
| [Worker Node](../categorias/01-arquitetura-e-control-plane/verbetes/worker-node.md) | Label `node-role.kubernetes.io/worker`; seções do `describe node` | SNO / docs |
| [Master Node](../categorias/01-arquitetura-e-control-plane/verbetes/master-node.md) | Labels de papel com valor vazio em `-L` | SNO / docs |
| [etcd](../categorias/01-arquitetura-e-control-plane/verbetes/etcd.md) | Label `app=etcd`; texto das condições do Operator; backup (cat. 13) | SNO / docs |
| [kube-scheduler](../categorias/01-arquitetura-e-control-plane/verbetes/kube-scheduler.md) | `scheduler.config.openshift.io/cluster` e `mastersSchedulable` | SNO / docs |
| [kube-controller-manager](../categorias/01-arquitetura-e-control-plane/verbetes/kube-controller-manager.md) | Garbage collector dentro do KCM | SNO / docs |
| [cloud-controller-manager](../categorias/01-arquitetura-e-control-plane/verbetes/cloud-controller-manager.md) | Plataforma do SNO (hipótese `None`); ClusterOperator; caminho das capabilities | SNO / docs |
| [kubelet](../categorias/01-arquitetura-e-control-plane/verbetes/kubelet.md) | `oc adm node-logs -u kubelet --tail`; `reason` dos eventos | SNO / docs |
| [Container Runtime](../categorias/01-arquitetura-e-control-plane/verbetes/container-runtime.md) | Formato `cri-o://`; `waiting.reason` | SNO / docs |
| [CRI](../categorias/01-arquitetura-e-control-plane/verbetes/cri.md) | Unidade `crio` em `node-logs`; mensagens | SNO / docs |
| [CRI-O](../categorias/01-arquitetura-e-control-plane/verbetes/cri-o.md) | Versão 1.35 no 4.22; `containerruntimeconfigs`; `/var/lib/containers` | SNO / docs |
| [Static Pod](../categorias/01-arquitetura-e-control-plane/verbetes/static-pod.md) | Dono `Node` e annotations `kubernetes.io/config.*` dos mirror Pods | SNO / docs |

## Categoria 01 — lote 2

| Verbete | O que validar | Como |
|---|---|---|
| [kube-proxy](../categorias/01-arquitetura-e-control-plane/verbetes/kube-proxy.md) | Ausência de kube-proxy com OVN-K; campo `deployKubeProxy` | SNO / docs |
| [OVN-Kubernetes](../categorias/01-arquitetura-e-control-plane/verbetes/ovn-kubernetes.md) | Namespace/Pods `openshift-ovn-kubernetes`; `status.clusterNetwork`; nº de `ovnkube-control-plane` no SNO | SNO / docs |
| [Cluster DNS](../categorias/01-arquitetura-e-control-plane/verbetes/cluster-dns.md) | Linha `search` do `resolv.conf` | SNO / docs |
| [CoreDNS](../categorias/01-arquitetura-e-control-plane/verbetes/coredns.md) | Nomes `dns-default`, namespace `openshift-dns`, contêiner `dns` | SNO / docs |
| [DNS Operator](../categorias/01-arquitetura-e-control-plane/verbetes/dns-operator.md) | Contêiner dos logs; `dns.operator` × `dns.config` | SNO / docs |
| [Cluster Version Operator](../categorias/01-arquitetura-e-control-plane/verbetes/cluster-version-operator.md) | Namespace `openshift-cluster-version`; `status.history[].state`; `oc adm upgrade` | SNO / docs |
| [Machine Config Operator](../categorias/01-arquitetura-e-control-plane/verbetes/machine-config-operator.md) | Annotation `machineconfiguration.openshift.io/state`; nomes do CO e namespace | SNO / docs |
| [MachineConfig](../categorias/01-arquitetura-e-control-plane/verbetes/machineconfig.md) | Colunas de `oc get mc`; `status.configuration.name` | SNO / docs |
| [MachineConfigPool](../categorias/01-arquitetura-e-control-plane/verbetes/machineconfigpool.md) | Colunas de `oc get mcp`; pool `worker` com 0 máquinas no SNO | SNO / docs |

## Categoria 01 — lote 3

| Verbete | O que validar | Como |
|---|---|---|
| [Bootstrap](../categorias/01-arquitetura-e-control-plane/verbetes/bootstrap.md) | Requisitante dos CSRs `node-bootstrapper`; `controlPlaneTopology` | SNO / docs |
| [Quorum](../categorias/01-arquitetura-e-control-plane/verbetes/quorum.md) | Texto das condições do ClusterOperator `etcd` | SNO / docs |
| [High Availability](../categorias/01-arquitetura-e-control-plane/verbetes/high-availability.md) | Valores de `controlPlaneTopology` (árbitro); ausência de etcd externo no OCP | SNO / docs |
| [SNO](../categorias/01-arquitetura-e-control-plane/verbetes/sno.md) | `SingleReplica`, `platformStatus.type`, `Allocated resources` | SNO / docs |
| [Hosted Control Plane](../categorias/01-arquitetura-e-control-plane/verbetes/hosted-control-plane.md) | Escopo de `HostedCluster`/`NodePool`; colunas (requer management cluster) | SNO / docs |
| [HyperShift](../categorias/01-arquitetura-e-control-plane/verbetes/hypershift.md) | Namespace do HyperShift Operator; implantação pelo MCE | SNO / docs |
| [Infrastructure Node](../categorias/01-arquitetura-e-control-plane/verbetes/infrastructure-node.md) | Taint `node-role.kubernetes.io/infra` | SNO / docs |

## Categoria 02 — lote 1

| Verbete | O que validar | Como |
|---|---|---|
| [Node](../categorias/02-compute-e-nodes/verbetes/node.md) | Colunas de `oc get nodes -o wide`; `oc adm top nodes` | SNO / docs |
| [Node Condition](../categorias/02-compute-e-nodes/verbetes/node-condition.md) | Mensagem de despejo; `NodeMonitorGracePeriod` no OCP | SNO / docs |
| [Capacity](../categorias/02-compute-e-nodes/verbetes/capacity.md) | Valores reais do nó | SNO / docs |
| [Allocatable](../categorias/02-compute-e-nodes/verbetes/allocatable.md) | Reserva automática ativa no SNO; valores reais | SNO / docs |
| [CPU](../categorias/02-compute-e-nodes/verbetes/cpu.md) | `oc adm top pods` | SNO / docs |
| [Memory](../categorias/02-compute-e-nodes/verbetes/memory.md) | Exemplos no SNO | SNO / docs |
| [Ephemeral Storage](../categorias/02-compute-e-nodes/verbetes/ephemeral-storage.md) | Página Ephemeral Storage; `/var` no RHCOS | SNO / docs |
| [Resource Request](../categorias/02-compute-e-nodes/verbetes/resource-request.md) | Maturidade de pod-level resources no 4.22 | SNO / docs |
| [Resource Limit](../categorias/02-compute-e-nodes/verbetes/resource-limit.md) | Despejo por limite de ephemeral-storage | SNO / docs |
| [QoS Class](../categorias/02-compute-e-nodes/verbetes/qos-class.md) | Regra com pod-level resources | SNO / docs |
| [OOMKill](../categorias/02-compute-e-nodes/verbetes/oomkill.md) | exitCode 137 num caso real | SNO / docs |
| [cgroups](../categorias/02-compute-e-nodes/verbetes/cgroups.md) | `nodes.config.openshift.io` `spec.cgroupMode` | SNO / docs |

## Categoria 02 — lote 2

| Verbete | O que validar | Como |
|---|---|---|
| [Node Label](../categorias/02-compute-e-nodes/verbetes/node-label.md) | Labels `node.openshift.io/*` | SNO / docs |
| [Node Annotation](../categorias/02-compute-e-nodes/verbetes/node-annotation.md) | Annotations do MCO no nó | SNO / docs |
| [Taint](../categorias/02-compute-e-nodes/verbetes/taint.md) | Taint de master/control-plane; feature gate dos operadores numéricos | SNO / docs |
| [Toleration](../categorias/02-compute-e-nodes/verbetes/toleration.md) | Tolerations automáticas num Pod comum | SNO / docs |
| [Node Selector](../categorias/02-compute-e-nodes/verbetes/node-selector.md) | `scheduler.spec.defaultNodeSelector` | SNO / docs |
| [Node Affinity](../categorias/02-compute-e-nodes/verbetes/node-affinity.md) | Exemplos no SNO | SNO / docs |
| [Cordon](../categorias/02-compute-e-nodes/verbetes/cordon.md) | Taint `unschedulable` automático | SNO / docs |
| [Drain](../categorias/02-compute-e-nodes/verbetes/drain.md) | Field selector `spec.nodeName`; PDB (cat. 17) | SNO / docs |
| [Node Debug](../categorias/02-compute-e-nodes/verbetes/node-debug.md) | Página `kubectl debug node`; namespace temporário | SNO / docs |
| [LimitRange](../categorias/02-compute-e-nodes/verbetes/limitrange.md) | Tipos extras do OpenShift | SNO / docs |
| [ResourceQuota](../categorias/02-compute-e-nodes/verbetes/resourcequota.md) | `appliedclusterresourcequotas`; texto `exceeded quota` | SNO / docs |

## Categoria 02 — lote 3

| Verbete | O que validar | Como |
|---|---|---|
| [Machine](../categorias/02-compute-e-nodes/verbetes/machine.md) | Versão `v1beta1`; fases; comportamento com `platform: none` | cluster / docs |
| [MachineSet](../categorias/02-compute-e-nodes/verbetes/machineset.md) | Colunas (cluster com Machine API) | cluster / docs |
| [MachineHealthCheck](../categorias/02-compute-e-nodes/verbetes/machinehealthcheck.md) | Colunas (cluster com Machine API) | cluster / docs |
| [BareMetalHost](../categorias/02-compute-e-nodes/verbetes/baremetalhost.md) | Versão `metal3.io`; estados de provisionamento | cluster / docs |
| [RHCOS](../categorias/02-compute-e-nodes/verbetes/rhcos.md) | Versão do RHEL base no 4.22 | cluster / docs |
| [HugePages](../categorias/02-compute-e-nodes/verbetes/hugepages.md) | Um × vários tamanhos por nó (divergência) | cluster / docs |
| [Extended Resource](../categorias/02-compute-e-nodes/verbetes/extended-resource.md) | Documentação de DRA (cat. 16) | cluster / docs |
| [Device Plugin](../categorias/02-compute-e-nodes/verbetes/device-plugin.md) | Detalhes do protocolo | cluster / docs |
| [NUMA](../categorias/02-compute-e-nodes/verbetes/numa.md) | `reason` do evento; recurso `noderesourcetopologies` | cluster / docs |

## Categoria 03 — lote 1

| Verbete | O que validar | Como |
|---|---|---|
| [Pod](../categorias/03-workloads/verbetes/pod.md) | SCC aplicada por padrão (annotation `openshift.io/scc`) | SNO / docs |
| [Container](../categorias/03-workloads/verbetes/container.md) | UID arbitrário / `restricted-v2` (cat. 08) | SNO / docs |
| [Pod Template](../categorias/03-workloads/verbetes/pod-template.md) | Objeto `PodTemplate` no grupo core | SNO / docs |
| [Deployment](../categorias/03-workloads/verbetes/deployment.md) | Padrões `revisionHistoryLimit` e `progressDeadlineSeconds` | SNO / docs |
| [StatefulSet](../categorias/03-workloads/verbetes/statefulset.md) | Nome dos PVCs (cluster com StorageClass) | SNO / docs |
| [DaemonSet](../categorias/03-workloads/verbetes/daemonset.md) | `updateStrategy` (RollingUpdate/OnDelete) | SNO / docs |
| [Job](../categorias/03-workloads/verbetes/job.md) | Label `job-name`; `BackoffLimitExceeded` | SNO / docs |
| [CronJob](../categorias/03-workloads/verbetes/cronjob.md) | Campos de histórico e `timeZone` | SNO / docs |
| [DeploymentConfig](../categorias/03-workloads/verbetes/deploymentconfig.md) | Triggers/hooks no 4.22; dependência de capability | SNO / docs |

## Decisões de nomenclatura a confirmar com o autor

- **Termos técnicos em inglês (decisão do autor, 2026-11-04):** títulos e termos técnicos ficam no original em inglês (Control Plane, Desired State, Current State, Reconciliation, Object, Resource...). A explicação é em português. A tradução aparece só como apoio, entre parênteses ou no campo **Tradução**.
- **API:** slug `kubernetes-api`, título "API (Kubernetes API)". O verbete *API Server* fica separado, no próximo lote.
- **Object/Resource:** slugs e títulos em inglês (`object`, `resource`).
- **Control Loop:** sem página própria; remissão para Controller e Reconciliation.
- **Resource Name / UID:** slugs `resource-name` e `uid`; títulos com o campo (`metadata.name`, `metadata.uid`).

### Categoria 03, lote 2 (2026-11-08)

| Verbete | O que validar | Como |
|---|---|---|
| [Pod Lifecycle](../categorias/03-workloads/verbetes/pod-lifecycle.md) | `reason` dos eventos de preparação | `oc get events` num Pod de estudo |
| [Pod Phase](../categorias/03-workloads/verbetes/pod-phase.md) | `Completed` na coluna STATUS para Pods `Succeeded` | Job de estudo no SNO |
| [Pod Condition](../categorias/03-workloads/verbetes/pod-condition.md) | Presença de `PodReadyToStartContainers` | `oc get pod -o jsonpath` no SNO |
| [Container Lifecycle](../categorias/03-workloads/verbetes/container-lifecycle.md) | `reason` `ContainerCreating` e `Completed` | SNO |
| [Restart Policy](../categorias/03-workloads/verbetes/restart-policy.md) | Estado do *feature gate* `ContainerRestartRules` no 4.22 | `oc get featuregate cluster -o yaml` |
| [Init Container](../categorias/03-workloads/verbetes/init-container.md) | Textos `Init:N/M`, `Init:Error`, `PodInitializing` | SNO |
| [Sidecar Container](../categorias/03-workloads/verbetes/sidecar-container.md) | Forma de injeção de sidecars pelo service mesh no 4.22 | docs do OpenShift Service Mesh |
| [Ephemeral Container](../categorias/03-workloads/verbetes/ephemeral-container.md) | Comportamento de `oc debug pod/<nome>` (cópia do Pod) | `oc debug --help` |
| [Terminating](../categorias/03-workloads/verbetes/terminating.md) | Fase `Terminating` do Namespace | `oc explain namespace.status` |
| [CrashLoopBackOff](../categorias/03-workloads/verbetes/crashloopbackoff.md) | Relação com o UID arbitrário das SCCs | docs de imagens/SCC do OCP 4.22 |
| [ImagePullBackOff](../categorias/03-workloads/verbetes/imagepullbackoff.md) | Pull secret global e configuração de registries no 4.22 | docs de imagens do OCP 4.22 |
