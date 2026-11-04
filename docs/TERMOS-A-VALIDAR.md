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
| [Recurso](../categorias/00-fundamentos-e-linguagem/verbetes/resource.md) | Texto exato das mensagens de erro (Forbidden / resource type); `oc auth can-i --subresource` | SNO; `--help` |
| [Kind](../categorias/00-fundamentos-e-linguagem/verbetes/kind.md) | Cabeçalho de `oc explain` | SNO |
| [Spec](../categorias/00-fundamentos-e-linguagem/verbetes/spec.md) | Defaults citados de `Deployment.spec` | `oc explain deployment.spec` |
| [Estado desejado](../categorias/00-fundamentos-e-linguagem/verbetes/desired-state.md) | `oc diff` como somente leitura no cliente 4.22; URL publicada do "Kubernetes overview" do OCP | `oc diff --help`; abrir docs |
| [Reconciliação](../categorias/00-fundamentos-e-linguagem/verbetes/reconciliation.md) | URL publicada do "Kubernetes overview" do OCP | abrir docs |

## Decisões de nomenclatura a confirmar com o autor

- **Estado observado:** slug `current-state` (termo oficial), título PT "Estado observado", remissões *actual state* e *observed state*.
- **API:** slug `kubernetes-api`, título "API (Kubernetes API)". O verbete *API Server* fica separado, no próximo lote.
- **Objeto/Recurso:** slugs em inglês (`object`, `resource`) e títulos em português.
