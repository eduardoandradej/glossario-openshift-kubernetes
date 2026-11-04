# Annotation

> **ID:** 00-fundamentos-e-linguagem/annotation | **Termo original:** annotation | **Tradução:** anotação | **Classe ontológica:** conceito (campo `metadata.annotations`) | **Plataforma:** Kubernetes / OpenShift | **Escopo:** não aplicável | **Disponibilidade:** nativo | **Versões validadas:** Kubernetes 1.35 / OCP 4.22 | **Nível:** básico | **Atualizado em:** 2026-11-04

## Definição em uma frase

Annotations são pares chave/valor que anexam a um objeto **metadados arbitrários e não identificadores**, para serem lidos por ferramentas, bibliotecas e pessoas.

## Explicação didática

Se a [label](label.md) é a etiqueta que você usa para **achar** a pasta, a annotation é o **post-it dentro dela**: informação útil, às vezes longa, mas que **não serve para busca**. Nenhum seletor filtra por annotations.

## Para que existe e qual problema resolve

Dá um lugar padronizado para guardar informação que não cabe, nem deve caber, em labels: valores grandes, estruturados ou com caracteres que labels não aceitam. Exemplos citados pela documentação:

- campos gerenciados por uma camada de configuração declarativa;
- dados de build e release (timestamps, IDs de release, branch, hashes de imagem);
- ponteiros para logging, monitoramento e auditoria;
- informação de ferramentas e bibliotecas cliente, útil para depuração;
- proveniência (quem ou o que criou o objeto);
- metadados leves de ferramentas de rollout.

## Funcionamento técnico e ciclo de vida

- Mapa em `metadata.annotations`. **Chaves e valores precisam ser strings**: números, booleanos ou listas devem ser serializados como texto.
- As chaves seguem a mesma sintaxe de prefixo/nome das labels. Os valores podem ser grandes e conter qualquer caractere.
- Muitos componentes leem annotations como **configuração**: um *router* ou um Operator pode mudar de comportamento conforme uma annotation no objeto. Nesse caso, a annotation passa a ser parte do contrato daquele componente.

## Relações e dependências

- Parte do [metadata](metadata.md), ao lado das [labels](label.md).
- No OpenShift, o [Project](project.md) guarda o nome de exibição e a descrição em annotations.

## Exemplo de situação real

Depois de um `oc apply`, o objeto ganha a annotation `kubectl.kubernetes.io/last-applied-configuration`, com o manifesto aplicado em JSON. É ela que o *apply* do lado do cliente usa para calcular o que remover na próxima aplicação. Apagá-la à mão muda o comportamento do próximo `apply`.

## Como visualizar e inspecionar (somente leitura)

```bash
# Annotations de um objeto
oc get deployment <nome> -n <namespace> -o jsonpath='{.metadata.annotations}' ; echo

# Uma annotation específica (pontos na chave precisam de escape)
oc get namespace <nome> -o jsonpath='{.metadata.annotations.openshift\.io/display-name}{"\n"}'

# Visão humana (seção Annotations)
oc describe deployment <nome> -n <namespace>
```

## Como interpretar a saída

- Annotations com prefixos de ferramentas (`kubectl.kubernetes.io/`, `deployment.kubernetes.io/`, `openshift.io/`) são escritas e lidas por componentes. Trate-as como **parte do funcionamento**, e não como comentário.
- `deployment.kubernetes.io/revision` num Deployment indica a revisão atual do rollout.
- Valores longos em JSON dentro de uma annotation são normais (ex.: `last-applied-configuration`).

## Diferenças e confusões frequentes

- **Annotation × label:** annotation não é usada para selecionar; label é.
- **Annotation × campo do `spec`:** annotations são extensões informais. Quando algo é central para um tipo, a API costuma ganhar um campo de verdade.
- **Annotation ≠ comentário YAML:** comentários `#` se perdem; annotations ficam armazenadas.

## No OpenShift 4.22 versus Kubernetes

O OpenShift usa muitas annotations próprias, como `openshift.io/display-name`, `openshift.io/description` e `openshift.io/requester` em projetos, as faixas `openshift.io/sa.scc.*` em namespaces (categoria 08) e annotations de comportamento em Routes (categoria 04). Consulte a documentação de cada recurso antes de usá-las.

## No HomeLab SNO

Ler annotations é seguro. **Não** edite annotations de objetos de plataforma: muitas são controladas por Operators e seriam revertidas, ou mudariam o comportamento.

## Termos relacionados

[Label](label.md) · [Metadata](metadata.md) · [Project](project.md) · [Manifest](manifest.md) · [Namespace](namespace.md)

## Fontes oficiais

- Kubernetes — Annotations: <https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/> (fonte: `kubernetes/website` `release-1.35`, `concepts/overview/working-with-objects/annotations.md`)
- Kubernetes API Conventions — "Metadata" (labels × annotations): <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md>

## Revisão editorial

- **Estado:** 🟡 desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** a annotation `kubectl.kubernetes.io/last-applied-configuration` e a `deployment.kubernetes.io/revision` são de uso conhecido, mas **não foram conferidas** nesta rodada; validar no SNO. Detalhar a relação com o *server-side apply* (`managedFields`) na categoria 14.
