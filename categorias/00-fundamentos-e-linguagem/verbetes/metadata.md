# Metadata

> **ID:** 00-fundamentos-e-linguagem/metadata | **Termo original:** metadata, ObjectMeta | **Tradução:** metadados | **Classe ontológica:** conceito (campo padrão dos objetos) | **Plataforma:** Kubernetes / OpenShift | **Escopo:** não aplicável | **Disponibilidade:** nativo | **Versões validadas:** Kubernetes 1.35 / OCP 4.22 | **Nível:** básico → intermediário | **Atualizado em:** 2026-11-04

## Definição em uma frase

`metadata` é o bloco de **identidade e controle** comum a todos os [objetos](object.md): nome, namespace, UID, labels, annotations e campos usados pelo sistema para versionar, encadear e excluir objetos.

## Explicação didática

Se `spec` é "o que eu quero" e `status` é "o que aconteceu", o `metadata` é a **carteira de identidade** do objeto, mais algumas etiquetas de controle. É a parte do objeto que funciona igual para **todos** os kinds, e é por isso que ferramentas genéricas (coleta de lixo, quotas, o próprio `oc`) conseguem tratar qualquer tipo.

## Para que existe e qual problema resolve

Padronizar a identidade e o controle permite que mecanismos transversais funcionem para qualquer kind: seleção por labels, dono e dependentes, exclusão em cascata, controle de concorrência.

## Funcionamento técnico e ciclo de vida

Campos que as convenções da API exigem (**MUST**) e recomendam (**SHOULD**):

| Campo | Quem define | Para que serve | Verbete |
|---|---|---|---|
| `name` | usuário (ou `generateName`) | identifica o objeto no seu escopo | [Resource Name](resource-name.md) |
| `namespace` | usuário | escopo do objeto (só tipos namespaced) | [Namespace](namespace.md) |
| `uid` | sistema | identidade única no tempo e no espaço | [UID](uid.md) |
| `resourceVersion` | sistema | versão interna, **opaca**, para concorrência e watch | futuro: *ResourceVersion* |
| `generation` | sistema | número crescente de versões do estado desejado | futuro: *Generation* |
| `creationTimestamp` | sistema | data de criação (RFC 3339) | — |
| `deletionTimestamp` | sistema | marca a exclusão em andamento | futuro: *Finalizer* |
| `labels` | usuário/ferramentas | organizar e **selecionar** | futuro: *Label* |
| `annotations` | ferramentas | metadados livres para automação | futuro: *Annotation* |

Outros campos frequentes: `ownerReferences` (dono do objeto), `finalizers` (pendências antes da exclusão) e `managedFields` (registro de quais gestores escreveram quais campos, usado pelo *server-side apply*).

**Labels × annotations:** labels servem para **organização e seleção** pelo usuário; annotations servem para **ferramentas e automação** guardarem dados próprios. Só labels são usadas em seletores.

## Relações e dependências

- Parte de todo [objeto](object.md), ao lado de [`spec`](spec.md) e [`status`](status.md).
- Base de [Resource Name](resource-name.md), [UID](uid.md) e [Namespace](namespace.md); próximos verbetes: Label, Annotation, Selector, OwnerReference, Finalizer, ResourceVersion e Generation.

## Exemplo de situação real

Um Service não encontra os Pods. O `spec.selector` pede `app: loja`, mas os Pods têm `metadata.labels.app: Loja`. Labels diferenciam maiúsculas de minúsculas, e a seleção falha em silêncio.

## Como visualizar e inspecionar (somente leitura)

```bash
# Metadados completos de um objeto
oc get deployment <nome> -n <namespace> -o jsonpath='{.metadata}' ; echo

# Labels em forma de coluna
oc get pods -n <namespace> --show-labels

# Annotations
oc get deployment <nome> -n <namespace> -o jsonpath='{.metadata.annotations}' ; echo

# Campos de controle
oc get deployment <nome> -n <namespace> \
  -o jsonpath='uid={.metadata.uid} rv={.metadata.resourceVersion} gen={.metadata.generation}{"\n"}'

# Esquema do ObjectMeta
oc explain deployment.metadata
```

## Como interpretar a saída

- `resourceVersion` muda a **cada** gravação, inclusive nas de `status`. `generation` normalmente só muda quando o `spec` muda. Por isso o controller compara `generation` com `status.observedGeneration`.
- `deletionTimestamp` preenchido com o objeto ainda visível significa exclusão **pendente**, em geral à espera de `finalizers`.
- `managedFields` costuma ser longo; numa leitura rápida pode ser ignorado.
- Annotations com prefixos como `kubectl.kubernetes.io/` ou `openshift.io/` são escritas por ferramentas; não as edite à mão sem saber quem as usa.

## Diferenças e confusões frequentes

- **`metadata.labels` ≠ `spec.selector`:** uma é a etiqueta; o outro, o filtro que a procura.
- **`metadata.name` ≠ nome do contêiner:** `spec.containers[].name` é outra coisa.
- **`resourceVersion` não é um número para comparar:** deve ser tratado como opaco.
- **Metadata de lista** (`ListMeta`) é mais simples que a de objeto (`ObjectMeta`).

## No OpenShift 4.22 versus Kubernetes

O OpenShift usa muitas annotations próprias. Exemplos: o projeto guarda `openshift.io/display-name` e `openshift.io/description`, e os namespaces recebem annotations de faixas de UID usadas pelas SCCs. Ver [Namespace](namespace.md).

## No HomeLab SNO

Ler metadados é seguro. Não remova `finalizers` nem `ownerReferences` de objetos para "destravar" algo: isso interfere na coleta de lixo e na reconciliação.

## Termos relacionados

[Objeto](object.md) · [Resource Name](resource-name.md) · [UID](uid.md) · [Namespace](namespace.md) · [Spec](spec.md) · [Status](status.md)

## Fontes oficiais

- Kubernetes API Conventions — "Metadata": <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md>
- Kubernetes — Object Names and IDs: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/> (fonte: `kubernetes/website` `release-1.35`)
- Kubernetes — Objects In Kubernetes, "Required fields": <https://kubernetes.io/docs/concepts/overview/working-with-objects/>

## Revisão editorial

- **Estado:** 🟡 desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** as annotations de SCC citadas devem ser detalhadas e conferidas na categoria 08. Exemplos **não executados** no SNO.
