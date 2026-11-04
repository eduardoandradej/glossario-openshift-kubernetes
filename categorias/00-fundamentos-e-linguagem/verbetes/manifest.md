# Manifest

> **ID:** 00-fundamentos-e-linguagem/manifest | **Termo original:** manifest (Kubernetes manifest) | **Tradução:** manifesto | **Classe ontológica:** conceito (artefato de configuração) | **Plataforma:** Kubernetes / OpenShift | **Escopo:** não aplicável | **Disponibilidade:** nativo | **Versões validadas:** Kubernetes 1.35 / OCP 4.22 | **Nível:** básico | **Atualizado em:** 2026-11-04

## Definição em uma frase

Manifesto é a **especificação de um objeto da API num arquivo [YAML](yaml.md) ou [JSON](json.md)**: descreve o desired state que o Kubernetes vai manter quando o manifesto for aplicado.

## Explicação didática

O manifesto é a "receita escrita" do objeto. Ele mora fora do cluster (no seu disco, num repositório Git) até ser enviado à API. Depois de aplicado, o que passa a valer é o **[objeto](object.md) armazenado**, que tem mais coisas que o arquivo: `uid`, `status`, valores padrão.

Um arquivo YAML pode conter **vários manifestos**, separados por `---` (o separador de documentos do YAML).

```yaml
# Exemplo didático (não aplicar): dois manifestos num mesmo arquivo
apiVersion: v1
kind: ConfigMap
metadata:
  name: exemplo-config
data:
  modo: "estudo"
---
apiVersion: v1
kind: Service
metadata:
  name: exemplo-svc
spec:
  selector:
    app: exemplo
  ports:
  - port: 8080
```

## Para que existe e qual problema resolve

- **Reprodutibilidade:** o mesmo arquivo cria o mesmo objeto em outro namespace ou cluster.
- **Revisão e versionamento:** manifestos entram em Git, passam por revisão e têm histórico, o que é a base de GitOps (categoria 15).
- **Gestão declarativa:** com `oc apply`, o arquivo vira a fonte do [desired state](desired-state.md).

## Funcionamento técnico e ciclo de vida

A documentação descreve **três técnicas** de gestão de objetos:

| Técnica | Opera sobre | Ambiente recomendado |
|---|---|---|
| Comandos imperativos (`oc create deployment ...`) | Objetos vivos | Desenvolvimento |
| Configuração imperativa por arquivo (`oc create -f`, `oc replace -f`) | Arquivos individuais | Produção |
| Configuração declarativa (`oc apply -f <dir>`) | Diretórios de arquivos | Produção |

**Atenção:** um mesmo objeto deve ser gerenciado por **uma só técnica**. Misturar técnicas no mesmo objeto leva a comportamento indefinido.

Campos obrigatórios num manifesto: `apiVersion`, `kind`, `metadata` (com `name`, ou `generateName`) e, nos tipos que o têm, `spec`. Ver [Object](object.md).

## Relações e dependências

- Descreve um [objeto](object.md) de um [kind](kind.md), numa [versão de API](api-version.md).
- Formatos: [YAML](yaml.md) (convenção) ou [JSON](json.md).
- Ferramentas que geram manifestos: Kustomize, Helm, Templates do OpenShift (categoria 15).

## Exemplo de situação real

Uma equipe mantém os manifestos da aplicação em Git. Alguém faz `oc edit` direto no cluster para um ajuste urgente. Na próxima aplicação do Git, o ajuste some. O manifesto e o objeto divergiram porque duas técnicas foram misturadas.

## Como visualizar e inspecionar (somente leitura)

```bash
# Obter o "manifesto" de um objeto existente (inclui campos gerados pelo sistema)
oc get configmap <nome> -n <namespace> -o yaml

# O que mudaria se o manifesto local fosse aplicado (não aplica nada)
oc diff -f <arquivo>.yaml

# Estrutura esperada dos campos
oc explain configmap
```

**Validação sem persistir** (não altera o cluster, mas exige permissão de escrita no recurso e passa pelo *admission*):

```bash
# NÃO EXECUTAR AUTOMATICAMENTE em namespaces de plataforma
oc apply --dry-run=server -f <arquivo>.yaml
```

## Como interpretar a saída

- Num `-o yaml` de objeto vivo aparecem `metadata.uid`, `resourceVersion`, `creationTimestamp`, `managedFields` e `status`. **Remova** esses campos antes de reutilizar o YAML como manifesto em outro lugar.
- `oc diff` sem saída significa que o arquivo e o objeto coincidem; as linhas `+`/`-` mostram o que seria acrescentado ou retirado.
- `--dry-run=server` respondendo `<tipo>/<nome> created (server dry run)` indica que o manifesto passaria pela validação e pelo admission, **sem** ter sido gravado.

## Diferenças e confusões frequentes

- **Manifesto ≠ objeto** (arquivo × entidade armazenada).
- **Manifesto ≠ YAML:** YAML é só o formato; o manifesto é o conteúdo com a estrutura de um objeto.
- **"Manifest" de imagem de contêiner** (OCI/registry) é outro conceito, da categoria 10.
- **`kind: List`** num arquivo é um artifício dos clientes para agrupar itens, e não um kind da API.

## No OpenShift 4.22 versus Kubernetes

Manifestos funcionam igual. O OpenShift oferece também **Templates** (`template.openshift.io`), que geram manifestos a partir de parâmetros, e ferramentas próprias no console para importar YAML.

## No HomeLab SNO

Leia manifestos de objetos à vontade com `-o yaml`, **exceto Secrets** (o `data` sai em base64, que não é cifragem). Aplicar manifestos é alteração: faça isso só em projetos de estudo próprios, nunca em `openshift-*`.

## Termos relacionados

[Object](object.md) · [YAML](yaml.md) · [JSON](json.md) · [Spec](spec.md) · [Desired State](desired-state.md) · [API Version](api-version.md)

## Fontes oficiais

- Kubernetes Glossary — Manifest: <https://kubernetes.io/docs/reference/glossary/?all=true#term-manifest> (fonte: `kubernetes/website` `release-1.35`, `reference/glossary/manifest.md`)
- Kubernetes — Kubernetes Object Management (três técnicas e o aviso de não misturá-las): <https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/>
- Kubernetes — Objects In Kubernetes, "Describing a Kubernetes object": <https://kubernetes.io/docs/concepts/overview/working-with-objects/>
- OCP 4.22 — Glossary, "kubernetes manifest" (fonte: `welcome/glossary.adoc`)

## Revisão editorial

- **Estado:** 🟡 desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** confirmar o texto exato da resposta de `--dry-run=server` no cliente 4.22, que **não foi executado**.
