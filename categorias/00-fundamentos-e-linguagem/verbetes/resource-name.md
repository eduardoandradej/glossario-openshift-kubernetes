# Resource Name (metadata.name)

> **ID:** 00-fundamentos-e-linguagem/resource-name | **Termo original:** name, object name, resource name | **Remissões:** generateName | **Tradução:** nome (do objeto) | **Classe ontológica:** conceito (campo de identidade) | **Plataforma:** Kubernetes / OpenShift | **Escopo:** único por tipo **dentro do namespace** (namespaced) ou **no cluster** (cluster-scoped) | **Disponibilidade:** nativo | **Versões validadas:** Kubernetes 1.35 / OCP 4.22 | **Nível:** básico | **Atualizado em:** 2026-11-04

## Definição em uma frase

O nome (`metadata.name`) é a string, escolhida pelo cliente, que **identifica um objeto dentro do seu tipo e escopo** e aparece na URL (`/api/v1/namespaces/<ns>/pods/<nome>`).

## Explicação didática

Num mesmo namespace só pode existir **um** Pod chamado `web-1`. Mas um Pod e um Deployment podem ambos se chamar `web-1`, porque são tipos diferentes. Em tipos cluster-scoped (como Node ou Namespace), o nome é único no cluster todo.

O nome identifica o objeto **agora**. Se você apagar e recriar `web-1`, o nome se repete, mas é **outro objeto**, com outro [UID](uid.md).

## Para que existe e qual problema resolve

Permite criação e consulta **idempotentes**: tentar criar de novo um objeto com o mesmo nome falha com conflito em vez de duplicar, e `oc get pod web-1` sempre aponta para o objeto atual com esse nome.

## Funcionamento técnico e ciclo de vida

- **Unicidade:** um objeto é distinguido por grupo, tipo de recurso, namespace (se houver) e nome. **A versão da API não importa**: o nome é único entre todas as versões do mesmo recurso.
- **`generateName`:** em vez de `name`, o cliente pode mandar um prefixo; o servidor acrescenta um sufixo aleatório. Pode haver conflito (HTTP 409). A partir do Kubernetes 1.31, o servidor tenta até 8 vezes antes de devolver o erro. É o que gera nomes como `web-7d9c6b8f5-x2kqp` em Pods de ReplicaSets.
- **Regras de formato** (dependem do tipo):

| Restrição | Regras principais | Usada por (exemplos) |
|---|---|---|
| DNS subdomain (RFC 1123) | até 253 caracteres; minúsculas, dígitos, `-` e `.`; começa e termina com alfanumérico | a maioria dos tipos |
| RFC 1123 label | até 63 caracteres; minúsculas, dígitos e `-`; começa com **letra** (na implementação atual) e termina com alfanumérico | Namespace |
| RFC 1035 label | até 63 caracteres; minúsculas, dígitos e `-`; começa com letra e termina com alfanumérico | Service (há exceção com uma *feature gate*) |
| Path segment | não pode ser `.` nem `..` e não pode conter `/` nem `%` | alguns tipos |

Alguns tipos têm restrições adicionais.

## Relações e dependências

- Parte do [metadata](metadata.md), ao lado de `namespace` e [`uid`](uid.md).
- O escopo do nome depende do [Namespace](namespace.md) e de o [recurso](resource.md) ser namespaced ou não.

## Exemplo de situação real

`oc create -f` falha com `AlreadyExists` porque já existe um ConfigMap com aquele nome no namespace. O nome é único por tipo e namespace. A solução é escolher outro nome ou gerenciar o objeto existente (por exemplo, com `apply`), e não "forçar" a criação.

## Como visualizar e inspecionar (somente leitura)

```bash
# Nomes no formato <recurso>.<grupo>/<nome>
oc get pods -n <namespace> -o name

# Nome e prefixo gerado (generateName) de um Pod criado por controller
oc get pod <nome> -n <namespace> -o jsonpath='{.metadata.name}  prefixo={.metadata.generateName}{"\n"}'

# Regras do campo name no esquema
oc explain pod.metadata.name
```

## Como interpretar a saída

- `-o name` imprime `pod/<nome>` ou `deployment.apps/<nome>`: o prefixo é o tipo de recurso, e o grupo aparece quando não é o *core*.
- `generateName` preenchido (ex.: `web-7d9c6b8f5-`) indica que o nome foi **gerado pelo servidor** a partir do prefixo informado pelo controller.
- Erros como `metadata.name: Invalid value: "Web_1": a lowercase RFC 1123 subdomain must consist of...` indicam violação das regras de formato.

## Diferenças e confusões frequentes

- **Nome ≠ UID:** o nome se repete ao longo do tempo; o UID nunca.
- **Nome ≠ label:** para atributos não únicos e para agrupar objetos, use labels.
- **Nome de Node e host físico:** a documentação alerta que, se um host é recriado com o mesmo nome sem recriar o objeto Node, o Kubernetes o trata como o host antigo, o que pode causar inconsistências.
- **`display-name` de Project (OpenShift)** é uma annotation para exibição, e não o nome do objeto.

## No OpenShift 4.22 versus Kubernetes

As regras são as mesmas. Diferença prática: o OpenShift **não deixa** usuários criarem projetos com prefixo `openshift-` ou `kube-` via `oc new-project`; esses nomes são reservados para projetos de plataforma.

## No HomeLab SNO

Observe nomes com `-o name` e `oc explain`; nada disso altera o cluster.

## Termos relacionados

[UID](uid.md) · [Metadata](metadata.md) · [Namespace](namespace.md) · [Recurso](resource.md) · [Objeto](object.md)

## Fontes oficiais

- Kubernetes — Object Names and IDs (nomes, `generateName`, restrições DNS/RFC, UIDs): <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/> (fonte: `kubernetes/website` `release-1.35`, `concepts/overview/working-with-objects/names.md`)
- Kubernetes — API Concepts, "Object names": <https://kubernetes.io/docs/reference/using-api/api-concepts/>
- OCP 4.22 — Working with projects (prefixos reservados): <https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/building_applications/projects> (fonte: `applications/projects/working-with-projects.adoc`)

## Revisão editorial

- **Estado:** 🟡 desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** a coluna "Usada por" da tabela de restrições foi inferida (a página oficial não lista os tipos para cada regra). Confirmar a regra de Namespace (RFC 1123 label) na página de Namespaces, onde está documentada, e as demais no esquema de cada tipo. A mensagem de erro é ilustrativa; a URL publicada de "Working with projects" está **a verificar**.
