# YAML

> **ID:** 00-fundamentos-e-linguagem/yaml | **Termo original:** YAML ("YAML Ain't Markup Language") | **Tradução:** não se traduz | **Classe ontológica:** tecnologia (formato de serialização) | **Plataforma:** padrão externo, usado por Kubernetes e OpenShift | **Escopo:** não aplicável | **Disponibilidade:** nativo (aceito pela API e pelos clientes) | **Versões validadas:** Kubernetes 1.35 / OCP 4.22 | **Nível:** básico | **Atualizado em:** 2026-11-04

## Definição em uma frase

YAML é um **formato de texto para dados estruturados**, baseado em indentação, e é o formato **convencional** dos [manifestos](manifest.md) Kubernetes.

## Explicação didática

YAML representa os mesmos dados que o [JSON](json.md), mas de um jeito mais legível para pessoas: sem chaves nem aspas obrigatórias, com a hierarquia dada pela **indentação**.

```yaml
# Mapas (chave: valor), listas (- item) e escalares
metadata:
  name: web            # string
  labels:
    app: web
spec:
  replicas: 3          # número
  paused: false        # booleano
  template:
    spec:
      containers:      # lista de mapas
      - name: web
        image: <imagem>
```

Regras que mais causam erro:

- **Indentação só com espaços**, nunca tabulação; a quantidade define o nível.
- **Listas** começam com `- ` no mesmo nível de indentação.
- **Tipos implícitos:** `true`, `10`, `1.0` viram booleano ou número. Valores que **precisam** ser texto (por exemplo, valores de `labels`, `annotations` e de ConfigMap `data`) devem ir entre aspas quando parecem número ou booleano: `"true"`, `"8080"`.
- **Vários documentos** num arquivo são separados por `---`.

## Para que existe e qual problema resolve

Escrever e revisar configuração à mão em JSON é cansativo. O YAML torna os manifestos legíveis, comentáveis (`#`) e fáceis de comparar em revisões de código.

## Funcionamento técnico e ciclo de vida

- O cliente (`oc`/`kubectl`) **converte o YAML em JSON** (ou em outro formato suportado) antes de enviar à API. A API também aceita o tipo de mídia `application/yaml` em requisições e respostas.
- Na saída, `-o yaml` pede a representação YAML do objeto.
- Comentários `#` **não são preservados**: não fazem parte do objeto armazenado.

## Relações e dependências

- Formato do [manifesto](manifest.md); equivalente ao [JSON](json.md).
- A estrutura (quais chaves existem) vem do esquema do [kind](kind.md), consultável com `oc explain`.

## Exemplo de situação real

Um ConfigMap com `data: { DEBUG: true }` é rejeitado: `data` exige strings, e `true` sem aspas é booleano em YAML. A correção é `DEBUG: "true"`.

## Como visualizar e inspecionar (somente leitura)

```bash
# Representação YAML de um objeto
oc get service <nome> -n <namespace> -o yaml

# Estrutura e tipos esperados dos campos (string, integer, boolean, []Object...)
oc explain configmap.data
oc explain deployment.spec.replicas
```

## Como interpretar a saída

- Em `oc explain`, o tipo de cada campo (`<string>`, `<integer>`, `<boolean>`, `<map[string]string>`, `<[]Object>`) diz como escrevê-lo no YAML. `map[string]string` exige valores texto, por isso as aspas.
- Erros de sintaxe YAML aparecem **antes** de chegar ao servidor, como mensagens de conversão do cliente que citam a linha. Erros de esquema vêm **do servidor**, como `strict decoding error: unknown field` ou erros de tipo.

## Diferenças e confusões frequentes

- **YAML ≠ manifesto:** o manifesto é o conteúdo; o YAML, o formato.
- **YAML ≠ "linguagem de programação":** não há lógica; quem gera YAML com lógica são ferramentas como Helm e Kustomize.
- **Comentários se perdem:** ao fazer `oc get -o yaml`, os comentários do arquivo original não voltam.

## No OpenShift 4.22 versus Kubernetes

Sem diferença. O console web do OpenShift tem um editor YAML que valida o esquema enquanto se digita; isso é ajuda da interface, e não outro formato.

## No HomeLab SNO

Estude YAML com `-o yaml` em objetos não sensíveis e com `oc explain`. **Não** use `-o yaml` em Secrets.

## Termos relacionados

[JSON](json.md) · [Manifest](manifest.md) · [Object](object.md) · [Kind](kind.md) · [Metadata](metadata.md)

## Fontes oficiais

- Kubernetes — API Concepts, "YAML resource encoding": <https://kubernetes.io/docs/reference/using-api/api-concepts/> (fonte: `kubernetes/website` `release-1.35`)
- Kubernetes — Objects In Kubernetes ("By convention, manifests are YAML"): <https://kubernetes.io/docs/concepts/overview/working-with-objects/>
- Especificação YAML (fonte externa ao Kubernetes): <https://yaml.org/>

## Revisão editorial

- **Estado:** 🟡 desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** a regra dos tipos implícitos depende da versão do YAML usada pelo parser do cliente. Os exemplos de erro de ConfigMap e de `strict decoding error` seguem o comportamento documentado da validação de campos, mas **não foram reproduzidos** no SNO.
