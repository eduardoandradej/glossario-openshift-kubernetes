# Índice por categoria

Os termos publicados, organizados por categoria e por assunto. *(versão inicial)* indica um termo ainda em aprofundamento.

## [00 — Fundamentos, linguagem e modelo declarativo](../categorias/00-fundamentos-e-linguagem/README.md)

**Plataforma**
- [Kubernetes](../categorias/00-fundamentos-e-linguagem/verbetes/kubernetes.md) (também: K8s)
- [OpenShift Container Platform](../categorias/00-fundamentos-e-linguagem/verbetes/openshift-container-platform.md) (também: OCP)
- [Cluster](../categorias/00-fundamentos-e-linguagem/verbetes/cluster.md)

**Linguagem da API**
- [API (Kubernetes API)](../categorias/00-fundamentos-e-linguagem/verbetes/kubernetes-api.md) · [API Server](../categorias/00-fundamentos-e-linguagem/verbetes/api-server.md) · [API Group](../categorias/00-fundamentos-e-linguagem/verbetes/api-group.md) · [API Version](../categorias/00-fundamentos-e-linguagem/verbetes/api-version.md)
- [Object](../categorias/00-fundamentos-e-linguagem/verbetes/object.md)
- [Resource](../categorias/00-fundamentos-e-linguagem/verbetes/resource.md)
- [Kind](../categorias/00-fundamentos-e-linguagem/verbetes/kind.md)
- [Spec](../categorias/00-fundamentos-e-linguagem/verbetes/spec.md)
- [Status](../categorias/00-fundamentos-e-linguagem/verbetes/status.md)
- [Metadata](../categorias/00-fundamentos-e-linguagem/verbetes/metadata.md) · [Resource Name](../categorias/00-fundamentos-e-linguagem/verbetes/resource-name.md) · [UID](../categorias/00-fundamentos-e-linguagem/verbetes/uid.md)

**Formatos e artefatos**
- [Manifest](../categorias/00-fundamentos-e-linguagem/verbetes/manifest.md) · [YAML](../categorias/00-fundamentos-e-linguagem/verbetes/yaml.md) · [JSON](../categorias/00-fundamentos-e-linguagem/verbetes/json.md)

**Modelo declarativo**
- [Desired State](../categorias/00-fundamentos-e-linguagem/verbetes/desired-state.md)
- [Current State](../categorias/00-fundamentos-e-linguagem/verbetes/current-state.md)
- [Reconciliation](../categorias/00-fundamentos-e-linguagem/verbetes/reconciliation.md)
- [Controller](../categorias/00-fundamentos-e-linguagem/verbetes/controller.md) (também: Control Loop)

**Organização**
- [Namespace](../categorias/00-fundamentos-e-linguagem/verbetes/namespace.md) · [Project](../categorias/00-fundamentos-e-linguagem/verbetes/project.md)
- [Label](../categorias/00-fundamentos-e-linguagem/verbetes/label.md) · [Annotation](../categorias/00-fundamentos-e-linguagem/verbetes/annotation.md) · [Selector](../categorias/00-fundamentos-e-linguagem/verbetes/selector.md)

**Ciclo de vida e relações entre objetos**
- [OwnerReference](../categorias/00-fundamentos-e-linguagem/verbetes/owner-reference.md) · [Finalizer](../categorias/00-fundamentos-e-linguagem/verbetes/finalizer.md) · [Garbage Collection](../categorias/00-fundamentos-e-linguagem/verbetes/garbage-collection.md)

**Versionamento e sinais de status**
- [ResourceVersion](../categorias/00-fundamentos-e-linguagem/verbetes/resource-version.md) · [Generation](../categorias/00-fundamentos-e-linguagem/verbetes/generation.md) · [ObservedGeneration](../categorias/00-fundamentos-e-linguagem/verbetes/observed-generation.md)
- [Conditions](../categorias/00-fundamentos-e-linguagem/verbetes/conditions.md) · [Events](../categorias/00-fundamentos-e-linguagem/verbetes/events.md)

## [01 — Arquitetura e Control Plane](../categorias/01-arquitetura-e-control-plane/README.md)

**Papéis e camadas**
- [Control Plane](../categorias/01-arquitetura-e-control-plane/verbetes/control-plane.md) · [Worker Node](../categorias/01-arquitetura-e-control-plane/verbetes/worker-node.md) · [Master Node (legado)](../categorias/01-arquitetura-e-control-plane/verbetes/master-node.md)

**Componentes do Control Plane**
- [etcd](../categorias/01-arquitetura-e-control-plane/verbetes/etcd.md) · [kube-scheduler](../categorias/01-arquitetura-e-control-plane/verbetes/kube-scheduler.md) · [kube-controller-manager](../categorias/01-arquitetura-e-control-plane/verbetes/kube-controller-manager.md) · [cloud-controller-manager](../categorias/01-arquitetura-e-control-plane/verbetes/cloud-controller-manager.md) · [kube-apiserver](../categorias/00-fundamentos-e-linguagem/verbetes/api-server.md) (também: API Server)

**Componentes do nó**
- [kubelet](../categorias/01-arquitetura-e-control-plane/verbetes/kubelet.md) (também: Node Agent) · [Container Runtime](../categorias/01-arquitetura-e-control-plane/verbetes/container-runtime.md) · [CRI](../categorias/01-arquitetura-e-control-plane/verbetes/cri.md) · [CRI-O](../categorias/01-arquitetura-e-control-plane/verbetes/cri-o.md) · [Static Pod](../categorias/01-arquitetura-e-control-plane/verbetes/static-pod.md)

**Rede e DNS do cluster**
- [kube-proxy](../categorias/01-arquitetura-e-control-plane/verbetes/kube-proxy.md) · [OVN-Kubernetes](../categorias/01-arquitetura-e-control-plane/verbetes/ovn-kubernetes.md) · [Cluster DNS](../categorias/01-arquitetura-e-control-plane/verbetes/cluster-dns.md) · [CoreDNS](../categorias/01-arquitetura-e-control-plane/verbetes/coredns.md) · [DNS Operator](../categorias/01-arquitetura-e-control-plane/verbetes/dns-operator.md)

**Gestão da plataforma**
- [Cluster Version Operator](../categorias/01-arquitetura-e-control-plane/verbetes/cluster-version-operator.md) · [Machine Config Operator](../categorias/01-arquitetura-e-control-plane/verbetes/machine-config-operator.md) · [MachineConfig](../categorias/01-arquitetura-e-control-plane/verbetes/machineconfig.md) · [MachineConfigPool](../categorias/01-arquitetura-e-control-plane/verbetes/machineconfigpool.md)

**Topologias, instalação e disponibilidade**
- [Bootstrap](../categorias/01-arquitetura-e-control-plane/verbetes/bootstrap.md) · [Quorum](../categorias/01-arquitetura-e-control-plane/verbetes/quorum.md) · [High Availability](../categorias/01-arquitetura-e-control-plane/verbetes/high-availability.md) · [SNO](../categorias/01-arquitetura-e-control-plane/verbetes/sno.md) · [Hosted Control Plane](../categorias/01-arquitetura-e-control-plane/verbetes/hosted-control-plane.md) · [HyperShift](../categorias/01-arquitetura-e-control-plane/verbetes/hypershift.md) · [Infrastructure Node](../categorias/01-arquitetura-e-control-plane/verbetes/infrastructure-node.md)

## [02 — Compute, Nodes e capacidade](../categorias/02-compute-e-nodes/README.md)

**Nós e saúde**
- [Node](../categorias/02-compute-e-nodes/verbetes/node.md) · [Node Condition](../categorias/02-compute-e-nodes/verbetes/node-condition.md)

**Capacidade e recursos**
- [Capacity](../categorias/02-compute-e-nodes/verbetes/capacity.md) · [Allocatable](../categorias/02-compute-e-nodes/verbetes/allocatable.md) · [CPU](../categorias/02-compute-e-nodes/verbetes/cpu.md) · [Memory](../categorias/02-compute-e-nodes/verbetes/memory.md) · [Ephemeral Storage](../categorias/02-compute-e-nodes/verbetes/ephemeral-storage.md)

**Requests, limits e consequências**
- [Resource Request](../categorias/02-compute-e-nodes/verbetes/resource-request.md) · [Resource Limit](../categorias/02-compute-e-nodes/verbetes/resource-limit.md) · [QoS Class](../categorias/02-compute-e-nodes/verbetes/qos-class.md) · [OOMKill](../categorias/02-compute-e-nodes/verbetes/oomkill.md) · [cgroups](../categorias/02-compute-e-nodes/verbetes/cgroups.md)

**Posicionamento de Pods nos nós**
- [Node Label](../categorias/02-compute-e-nodes/verbetes/node-label.md) · [Node Annotation](../categorias/02-compute-e-nodes/verbetes/node-annotation.md) · [Node Selector](../categorias/02-compute-e-nodes/verbetes/node-selector.md) · [Node Affinity](../categorias/02-compute-e-nodes/verbetes/node-affinity.md) · [Taint](../categorias/02-compute-e-nodes/verbetes/taint.md) · [Toleration](../categorias/02-compute-e-nodes/verbetes/toleration.md)

**Manutenção e diagnóstico de nós**
- [Cordon](../categorias/02-compute-e-nodes/verbetes/cordon.md) (também: Uncordon) · [Drain](../categorias/02-compute-e-nodes/verbetes/drain.md) · [Node Debug](../categorias/02-compute-e-nodes/verbetes/node-debug.md)

**Políticas de recursos por namespace**
- [LimitRange](../categorias/02-compute-e-nodes/verbetes/limitrange.md) · [ResourceQuota](../categorias/02-compute-e-nodes/verbetes/resourcequota.md)

## [03 — Workloads](../categorias/03-workloads/README.md)
- [Pod](../categorias/03-workloads/verbetes/pod.md) · [Deployment](../categorias/03-workloads/verbetes/deployment.md) · [ReplicaSet](../categorias/03-workloads/verbetes/replicaset.md) · [StatefulSet](../categorias/03-workloads/verbetes/statefulset.md) · [DaemonSet](../categorias/03-workloads/verbetes/daemonset.md) · [Job](../categorias/03-workloads/verbetes/job.md) *(versão inicial)*

## [04 — Networking](../categorias/04-networking/README.md)
- [Service](../categorias/04-networking/verbetes/service.md) · [Route](../categorias/04-networking/verbetes/route.md) · [Ingress](../categorias/04-networking/verbetes/ingress.md) · [IngressController](../categorias/04-networking/verbetes/ingresscontroller.md) · [NetworkPolicy](../categorias/04-networking/verbetes/networkpolicy.md) *(versão inicial)*

## [05 — Storage](../categorias/05-storage/README.md)
- [PersistentVolume](../categorias/05-storage/verbetes/persistentvolume.md) · [PersistentVolumeClaim](../categorias/05-storage/verbetes/persistentvolumeclaim.md) · [StorageClass](../categorias/05-storage/verbetes/storageclass.md) *(versão inicial)*

## [06 — Configuração e API](../categorias/06-configuracao-e-api/README.md)
- [ConfigMap](../categorias/06-configuracao-e-api/verbetes/configmap.md) · [Secret](../categorias/06-configuracao-e-api/verbetes/secret.md) *(versão inicial)*

## [07 — Identidade e RBAC](../categorias/07-identidade-e-rbac/README.md)
- [ServiceAccount](../categorias/07-identidade-e-rbac/verbetes/serviceaccount.md) *(versão inicial)*

## [09 — Operators e extensões](../categorias/09-operators-e-extensoes/README.md)
- [Operator](../categorias/09-operators-e-extensoes/verbetes/operator.md) · [ClusterOperator](../categorias/09-operators-e-extensoes/verbetes/clusteroperator.md) · [CustomResourceDefinition](../categorias/09-operators-e-extensoes/verbetes/customresourcedefinition.md) · [ClusterExtension](../categorias/09-operators-e-extensoes/verbetes/clusterextension.md) *(versão inicial)*

## [10 — Builds, imagens e registry](../categorias/10-builds-imagens-registry/README.md)
- [BuildConfig](../categorias/10-builds-imagens-registry/verbetes/buildconfig.md) *(versão inicial)*

As demais categorias estão planejadas e ainda não têm termos publicados.
