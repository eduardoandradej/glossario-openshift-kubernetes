# API Version (apiVersion)

> **ID:** 00-fundamentos-e-linguagem/api-version | **Termo original:** API version, `apiVersion` | **Tradução:** versão de API | **Classe ontológica:** conceito (campo e versionamento da API) | **Plataforma:** Kubernetes / OpenShift | **Escopo:** não aplicável | **Disponibilidade:** nativo | **Versões validadas:** Kubernetes 1.35 / OCP 4.22 | **Nível:** básico → intermediário | **Atualizado em:** 2026-11-04

## Definição em uma frase

A versão de API indica **qual versão do esquema de um [grupo](api-group.md)** está sendo usada (ex.: `v1`, `v1beta1`). O campo `apiVersion` de um objeto combina grupo e versão (`apps/v1`).

## Explicação didática

O Kubernetes não versiona campo por campo, e sim **o grupo inteiro**. Cada versão tem um nível de estabilidade estampado no nome:

| Nível | Nome | O que esperar |
|---|---|---|
| **Alpha** | contém `alpha` (`v1alpha1`) | APIs nativas vêm **desabilitadas** por padrão; podem mudar ou sumir sem aviso; só para testes |
| **Beta** | contém `beta` (`v2beta3`) | Bem testada; APIs nativas novas vêm desabilitadas por padrão (exceto as betas anteriores ao 1.22); pode haver mudança incompatível, com instrução de migração |
| **Estável (GA)** | `vX` (`v1`, `v2`) | Permanece disponível em todas as versões futuras dentro da mesma versão principal do Kubernetes |

**Versão da API ≠ versão do software.** `apps/v1` não significa "Kubernetes 1". A relação entre as duas é indireta.

## Para que existe e qual problema resolve

Permite que a API **evolua sem quebrar clientes**: uma versão nova pode reorganizar campos, enquanto a antiga continua servida por um tempo definido pela política de descontinuação (*deprecation policy*).

## Funcionamento técnico e ciclo de vida

- **Mesmos dados, várias representações:** o API server pode servir o mesmo objeto armazenado em mais de uma versão e converte entre elas. Um objeto criado em `v1beta1` pode ser lido em `v1`.
- **Versão de armazenamento:** internamente, cada recurso é gravado no etcd numa versão; os clientes não precisam saber qual.
- **Ciclo:** introdução → (beta) → estável; versões antigas são **deprecated** e depois **removidas**. Após a remoção, manifestos com a versão antiga passam a ser rejeitados.
- **Versão preferida:** cada grupo anuncia a versão preferida, que os clientes usam por padrão.

## Relações e dependências

- Faz parte do [grupo](api-group.md); com o [kind](kind.md), identifica o esquema (GVK).
- Campo obrigatório de todo [manifesto](manifest.md) e [objeto](object.md).

## Exemplo de situação real

Um manifesto antigo usa `apiVersion: extensions/v1beta1` para um Deployment. No Kubernetes 1.35 ele é rejeitado (`no matches for kind "Deployment" in version "extensions/v1beta1"`), porque essa versão foi removida há muitas versões. A correção é migrar para `apps/v1`, ajustando os campos que mudaram (ex.: `spec.selector` passou a ser obrigatório).

## Como visualizar e inspecionar (somente leitura)

```bash
# Todas as combinações grupo/versão servidas
oc api-versions

# Versão usada por cada tipo
oc api-resources | head -20

# Esquema numa versão específica
oc explain deployment --api-version=apps/v1

# Versão com que um objeto é devolvido
oc get deployment <nome> -n <namespace> -o jsonpath='{.apiVersion}{"\n"}'

# Avisos de API deprecated aparecem como "Warning:" na saída dos comandos
```

## Como interpretar a saída

- A mensagem `Warning: <grupo>/<versão> <Kind> is deprecated in v1.XX+, unavailable in v1.YY+; use <grupo>/<versão> <Kind>` é emitida pelo servidor quando você usa uma versão descontinuada. É hora de migrar o manifesto.
- `error: resource mapping not found` ou `no matches for kind "X" in version "Y"` significa que a combinação grupo/versão/kind não é servida: a versão foi removida, a CRD não está instalada ou há erro de digitação.
- `oc api-versions` listando `v1beta1` e `v1` do mesmo grupo é normal durante a transição.

## Diferenças e confusões frequentes

- **`apiVersion` (campo) ≠ versão do cluster:** use `oc version` para a versão do Kubernetes e do OpenShift.
- **`v1` sozinho = grupo *core*** (Pod, Service...). `apps/v1` = grupo `apps`.
- **Beta ≠ "quase GA, pode usar em produção":** a documentação Kubernetes não recomenda betas em produção, por possíveis mudanças incompatíveis.

## No OpenShift 4.22 versus Kubernetes

O OCP 4.22 segue a política do Kubernetes 1.35 para as APIs nativas. As APIs do OpenShift têm o seu próprio ciclo, comunicado nas release notes (tabelas de deprecated e removed). Antes de atualizar o cluster, a Red Hat costuma exigir que se verifiquem os usos de APIs que serão removidas.

## No HomeLab SNO

Os avisos `Warning:` não alteram nada e são uma ótima fonte de estudo: anote quais manifestos os disparam e migre-os no seu repositório de YAML, não no cluster de plataforma.

## Termos relacionados

[API Group](api-group.md) · [Kind](kind.md) · [Manifest](manifest.md) · [API](kubernetes-api.md) · [Objeto](object.md)

## Fontes oficiais

- Kubernetes — API Overview, "API versioning" (alpha/beta/stable): <https://kubernetes.io/docs/reference/using-api/> (fonte: `kubernetes/website` `release-1.35`, `reference/using-api/_index.md`)
- Kubernetes — The Kubernetes API, "API groups and versioning": <https://kubernetes.io/docs/concepts/overview/kubernetes-api/>
- Kubernetes — Deprecation Policy: <https://kubernetes.io/docs/reference/using-api/deprecation-policy/>
- OCP 4.22 — Release notes, tabelas de deprecated e removed: <https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/release_notes/ocp-4-22-release-notes>

## Revisão editorial

- **Estado:** 🟡 desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** os textos das mensagens `Warning:` e `no matches for kind` seguem o formato conhecido do cliente, mas **não foram reproduzidos** no SNO. Verificar a orientação atual da Red Hat sobre a checagem de APIs removidas antes de atualizar o cluster (categoria 13).
