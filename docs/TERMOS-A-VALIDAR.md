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

## Decisões de nomenclatura a confirmar com o autor

- **Termos técnicos em inglês (decisão do autor, 2026-11-04):** títulos e termos técnicos ficam no original em inglês (Control Plane, Desired State, Current State, Reconciliation, Object, Resource...). A explicação é em português. A tradução aparece só como apoio, entre parênteses ou no campo **Tradução**.
- **API:** slug `kubernetes-api`, título "API (Kubernetes API)". O verbete *API Server* fica separado, no próximo lote.
- **Object/Resource:** slugs e títulos em inglês (`object`, `resource`).
- **Control Loop:** sem página própria; remissão para Controller e Reconciliation.
- **Resource Name / UID:** slugs `resource-name` e `uid`; títulos com o campo (`metadata.name`, `metadata.uid`).
