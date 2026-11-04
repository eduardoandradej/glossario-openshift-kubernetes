# Índice por categoria

> Só páginas existentes. Legenda: 🟡 desenvolvido (fontes conferidas, sem validação no cluster) · 🌱 semente · ↪ remissão. O checklist completo de candidatos fica no README de cada categoria.

## [00 — Fundamentos, linguagem e modelo declarativo](../categorias/00-fundamentos-e-linguagem/README.md)

**Plataforma**
- 🟡 [Kubernetes](../categorias/00-fundamentos-e-linguagem/verbetes/kubernetes.md) (↪ K8s)
- 🟡 [OpenShift Container Platform](../categorias/00-fundamentos-e-linguagem/verbetes/openshift-container-platform.md) (↪ OCP)
- 🟡 [Cluster](../categorias/00-fundamentos-e-linguagem/verbetes/cluster.md)

**Linguagem da API**
- 🟡 [API (Kubernetes API)](../categorias/00-fundamentos-e-linguagem/verbetes/kubernetes-api.md) · [API Server](../categorias/00-fundamentos-e-linguagem/verbetes/api-server.md) · [API Group](../categorias/00-fundamentos-e-linguagem/verbetes/api-group.md) · [API Version](../categorias/00-fundamentos-e-linguagem/verbetes/api-version.md)
- 🟡 [Object](../categorias/00-fundamentos-e-linguagem/verbetes/object.md)
- 🟡 [Resource](../categorias/00-fundamentos-e-linguagem/verbetes/resource.md)
- 🟡 [Kind](../categorias/00-fundamentos-e-linguagem/verbetes/kind.md)
- 🟡 [Spec](../categorias/00-fundamentos-e-linguagem/verbetes/spec.md)
- 🟡 [Status](../categorias/00-fundamentos-e-linguagem/verbetes/status.md)
- 🟡 [Metadata](../categorias/00-fundamentos-e-linguagem/verbetes/metadata.md) · [Resource Name](../categorias/00-fundamentos-e-linguagem/verbetes/resource-name.md) · [UID](../categorias/00-fundamentos-e-linguagem/verbetes/uid.md)

**Formatos e artefatos**
- 🟡 [Manifest](../categorias/00-fundamentos-e-linguagem/verbetes/manifest.md) · [YAML](../categorias/00-fundamentos-e-linguagem/verbetes/yaml.md) · [JSON](../categorias/00-fundamentos-e-linguagem/verbetes/json.md)

**Modelo declarativo**
- 🟡 [Desired State](../categorias/00-fundamentos-e-linguagem/verbetes/desired-state.md)
- 🟡 [Current State](../categorias/00-fundamentos-e-linguagem/verbetes/current-state.md)
- 🟡 [Reconciliation](../categorias/00-fundamentos-e-linguagem/verbetes/reconciliation.md)
- 🟡 [Controller](../categorias/00-fundamentos-e-linguagem/verbetes/controller.md) (↪ Control Loop)

**Organização**
- 🟡 [Namespace](../categorias/00-fundamentos-e-linguagem/verbetes/namespace.md) · [Project](../categorias/00-fundamentos-e-linguagem/verbetes/project.md)
- 🟡 [Label](../categorias/00-fundamentos-e-linguagem/verbetes/label.md) · [Annotation](../categorias/00-fundamentos-e-linguagem/verbetes/annotation.md) · [Selector](../categorias/00-fundamentos-e-linguagem/verbetes/selector.md)

**Ciclo de vida e relações entre objetos**
- 🟡 [OwnerReference](../categorias/00-fundamentos-e-linguagem/verbetes/owner-reference.md) · [Finalizer](../categorias/00-fundamentos-e-linguagem/verbetes/finalizer.md) · [Garbage Collection](../categorias/00-fundamentos-e-linguagem/verbetes/garbage-collection.md)

**Versionamento e sinais de status**
- 🟡 [ResourceVersion](../categorias/00-fundamentos-e-linguagem/verbetes/resource-version.md) · [Generation](../categorias/00-fundamentos-e-linguagem/verbetes/generation.md) · [ObservedGeneration](../categorias/00-fundamentos-e-linguagem/verbetes/observed-generation.md)
- 🟡 [Conditions](../categorias/00-fundamentos-e-linguagem/verbetes/conditions.md) · [Events](../categorias/00-fundamentos-e-linguagem/verbetes/events.md)

## [02 — Compute, nodes e capacidade](../categorias/02-compute-e-nodes/README.md)
- 🌱 [Node](../categorias/02-compute-e-nodes/verbetes/node.md)

## [03 — Workloads](../categorias/03-workloads/README.md)
- 🌱 [Pod](../categorias/03-workloads/verbetes/pod.md) · [Deployment](../categorias/03-workloads/verbetes/deployment.md) · [ReplicaSet](../categorias/03-workloads/verbetes/replicaset.md) · [StatefulSet](../categorias/03-workloads/verbetes/statefulset.md) · [DaemonSet](../categorias/03-workloads/verbetes/daemonset.md) · [Job](../categorias/03-workloads/verbetes/job.md)

## [04 — Networking](../categorias/04-networking/README.md)
- 🌱 [Service](../categorias/04-networking/verbetes/service.md) · [Route](../categorias/04-networking/verbetes/route.md) · [Ingress](../categorias/04-networking/verbetes/ingress.md) · [IngressController](../categorias/04-networking/verbetes/ingresscontroller.md) · [NetworkPolicy](../categorias/04-networking/verbetes/networkpolicy.md)

## [05 — Storage](../categorias/05-storage/README.md)
- 🌱 [PersistentVolume](../categorias/05-storage/verbetes/persistentvolume.md) · [PersistentVolumeClaim](../categorias/05-storage/verbetes/persistentvolumeclaim.md) · [StorageClass](../categorias/05-storage/verbetes/storageclass.md)

## [06 — Configuração e API](../categorias/06-configuracao-e-api/README.md)
- 🌱 [ConfigMap](../categorias/06-configuracao-e-api/verbetes/configmap.md) · [Secret](../categorias/06-configuracao-e-api/verbetes/secret.md)

## [07 — Identidade e RBAC](../categorias/07-identidade-e-rbac/README.md)
- 🌱 [ServiceAccount](../categorias/07-identidade-e-rbac/verbetes/serviceaccount.md)

## [09 — Operators e extensões](../categorias/09-operators-e-extensoes/README.md)
- 🌱 [Operator](../categorias/09-operators-e-extensoes/verbetes/operator.md) · [ClusterOperator](../categorias/09-operators-e-extensoes/verbetes/clusteroperator.md) · [CustomResourceDefinition](../categorias/09-operators-e-extensoes/verbetes/customresourcedefinition.md) · [ClusterExtension](../categorias/09-operators-e-extensoes/verbetes/clusterextension.md)

## [10 — Builds, imagens e registry](../categorias/10-builds-imagens-registry/README.md)
- 🌱 [BuildConfig](../categorias/10-builds-imagens-registry/verbetes/buildconfig.md)

As categorias 01, 08 e 11 a 17 ainda não têm páginas.
