# API Group

## Definição em uma frase

Um API group é um **conjunto de caminhos relacionados da API**, que agrupa tipos de recurso afins (ex.: `apps` para Deployments e StatefulSets) e é versionado como uma unidade.

## Explicação didática

Imagine a API como um prédio e os grupos como andares temáticos. No andar `apps` ficam os controladores de aplicação; em `batch`, Jobs e CronJobs; em `networking.k8s.io`, as políticas de rede e o Ingress; em `route.openshift.io`, as Routes do OpenShift.

O grupo aparece em dois lugares:

- **na URL:** `/apis/apps/v1/...`;
- **no campo `apiVersion` do objeto:** `apiVersion: apps/v1` (grupo `apps`, versão `v1`).

Existe um grupo especial **sem nome**, o *core* ou *legacy*. Ele fica em `/api/v1`, e o `apiVersion` dele é só `v1`, como em Pod, Service, ConfigMap, Namespace e Node.

## Para que existe e qual problema resolve

- **Evolução independente:** cada grupo ganha versões novas no seu próprio ritmo.
- **Extensibilidade:** terceiros podem criar grupos próprios (ex.: `*.openshift.io`, ou grupos de CRDs de Operators) sem colidir com os nomes nativos.
- **Controle:** grupos e versões podem ser habilitados ou desabilitados na configuração do API server (`--runtime-config`). Num cluster gerenciado como o OpenShift, isso é responsabilidade da plataforma, e não do usuário.

## Funcionamento técnico e ciclo de vida

- **Nome:** por convenção, nomes no formato de domínio (`networking.k8s.io`, `route.openshift.io`). Grupos históricos do Kubernetes têm nomes curtos (`apps`, `batch`).
- **Identificação de um tipo:** grupo + versão + kind (GVK). Ver [Kind](kind.md).
- **Origem:** um grupo pode ser servido pelo próprio kube-apiserver, por uma **CRD** ou por um **servidor agregado** (APIService).

| Grupo | Exemplos de kind | Origem |
|---|---|---|
| *core* (`""`) | Pod, Service, ConfigMap, Secret, Namespace, Node | Kubernetes |
| `apps` | Deployment, ReplicaSet, StatefulSet, DaemonSet | Kubernetes |
| `batch` | Job, CronJob | Kubernetes |
| `rbac.authorization.k8s.io` | Role, RoleBinding, ClusterRole | Kubernetes |
| `route.openshift.io` | Route | OpenShift |
| `project.openshift.io` | Project | OpenShift |
| `config.openshift.io` | ClusterVersion, ClusterOperator, Infrastructure | OpenShift |

## Relações e dependências

- Contém [versões](api-version.md), que contêm [tipos de recurso](resource.md).
- Servido pelo [API server](api-server.md), ou agregado a ele.
- Grupos novos chegam por [CustomResourceDefinition](../../09-operators-e-extensoes/verbetes/customresourcedefinition.md).

## Exemplo de situação real

Uma regra de RBAC que concede acesso a `deployments` com `apiGroups: [""]` não funciona: Deployment pertence ao grupo `apps`. Em RBAC, `""` significa o grupo *core*.

## Como visualizar e inspecionar (somente leitura)

```bash
# Grupos/versões servidos
oc api-versions

# Recursos de um grupo
oc api-resources --api-group=apps
oc api-resources --api-group=config.openshift.io

# Recursos do grupo core (grupo vazio)
oc api-resources --api-group=''

# Documento de descoberta de um grupo (JSON)
oc get --raw /apis/route.openshift.io
```

## Como interpretar a saída

- Em `oc api-versions`, cada linha é `<grupo>/<versão>`. A linha `v1` sozinha é o grupo *core*.
- Em `oc api-resources`, a coluna `APIVERSION` mostra `<grupo>/<versão>` de cada tipo.
- O documento de descoberta (`/apis/<grupo>`) lista as versões do grupo e a **versão preferida** (`preferredVersion`), que é a usada por padrão pelos clientes.
- Grupo ausente em `api-versions` significa que o cluster **não serve** essa API (Operator não instalado, *capability* desabilitada...). Não é problema de permissão.

## Diferenças e confusões frequentes

- **API group ≠ grupo de usuários:** "Group" em RBAC/identidade é outro conceito (categoria 07).
- **`apiGroups` no RBAC usa só o nome**, sem a versão.
- **`apps` ≠ "aplicações do OpenShift":** é o grupo Kubernetes dos controladores de workload. O `DeploymentConfig` (deprecated) mora em `apps.openshift.io`.

## No OpenShift 4.22 versus Kubernetes

O OpenShift acrescenta muitos grupos `*.openshift.io` (`route`, `project`, `build`, `image`, `config`, `operator`, `security`...). A lista exata depende do cluster: consulte `oc api-versions` em vez de presumir.

## No HomeLab SNO

`oc api-versions` mostra os grupos do seu SNO e não altera nada. Use o resultado para saber se um conceito opcional existe ali antes de estudá-lo na prática.

## Termos relacionados

[API Version](api-version.md) · [API](kubernetes-api.md) · [Kind](kind.md) · [Resource](resource.md) · [API Server](api-server.md) · [CustomResourceDefinition](../../09-operators-e-extensoes/verbetes/customresourcedefinition.md)

## Fontes oficiais

- Kubernetes — API Overview, "API groups" e "Enabling or disabling API groups": <https://kubernetes.io/docs/reference/using-api/> (fonte: `kubernetes/website` `release-1.35`, `reference/using-api/_index.md`)
- Kubernetes Glossary — API Group: <https://kubernetes.io/docs/reference/glossary/?all=true#term-api-group>
- Kubernetes — The Kubernetes API, "API groups and versioning": <https://kubernetes.io/docs/concepts/overview/kubernetes-api/>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 00-fundamentos-e-linguagem/api-group
- **Termo original:** API group
- **Tradução:** grupo de API
- **Classe ontológica:** conceito (organização da API)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-04

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** a tabela de grupos combina a documentação Kubernetes com o conhecimento dos grupos do OpenShift. Conferir no SNO com `oc api-resources --api-group=<grupo>`, especialmente `config.openshift.io`, que **não foi executado**.

</details>
