# JSON

## Definição em uma frase

JSON é o **formato de dados padrão da API do Kubernetes**: é nele que os objetos trafegam por HTTP, salvo quando o cliente pede outro formato.

## Explicação didática

Quando você usa YAML, ele é convertido. O formato "nativo" da conversa com a API é o JSON:

```json
{
  "apiVersion": "v1",
  "kind": "ConfigMap",
  "metadata": { "name": "exemplo" },
  "data": { "modo": "estudo" }
}
```

JSON é mais verboso para pessoas, mas é **inequívoco** (strings sempre entre aspas) e ideal para máquinas, scripts e filtros.

## Para que existe e qual problema resolve

- **Interoperabilidade:** qualquer linguagem lê e escreve JSON.
- **Automação:** a saída `-o json` pode ser filtrada com precisão (`jsonpath`, `jq`), sem depender do formato de tabela, que pode mudar.

## Funcionamento técnico e ciclo de vida

- Por padrão, a API responde com `Content-Type: application/json`. Todos os tipos nativos suportam JSON.
- Outros formatos negociáveis: YAML, Protobuf (binário, mais eficiente em grande escala) e CBOR.
- O cliente pede o formato pelo cabeçalho `Accept`; se o servidor não suportar nenhum, responde `406 Not Acceptable`.

## Relações e dependências

- Equivalente ao [YAML](yaml.md) em conteúdo.
- Usado pelo [API server](api-server.md) e pelas expressões **JSONPath** do `oc` (`-o jsonpath=...`).

## Exemplo de situação real

Um script de monitoramento precisa do número de réplicas prontas. Em vez de recortar a tabela de `oc get`, ele usa `-o jsonpath='{.status.readyReplicas}'` e recebe só o número, de forma estável entre versões do cliente.

## Como visualizar e inspecionar (somente leitura)

```bash
# Objeto completo em JSON
oc get deployment <nome> -n <namespace> -o json

# Campo específico com JSONPath (nativo do oc)
oc get deployment <nome> -n <namespace> -o jsonpath='{.metadata.name} {.status.readyReplicas}{"\n"}'

# Um campo por item de uma lista
oc get pods -n <namespace> -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.phase}{"\n"}{end}'

# Com jq, se estiver instalado na sua estação (ferramenta externa ao oc)
oc get pods -n <namespace> -o json | jq -r '.items[].metadata.name'
```

## Como interpretar a saída

- Uma listagem em JSON tem `"kind": "List"` (montado pelo cliente) ou `"<Kind>List"`, com os objetos em `items`.
- No JSONPath, `{.items[*]}` percorre a lista e `{range ...}{end}` repete o modelo para cada item. Campo inexistente volta **vazio**, sem erro, então confira o caminho com `oc explain`.
- Valores entre aspas no JSON são strings; sem aspas, números ou booleanos. É assim que se percebe um erro de tipo.

## Diferenças e confusões frequentes

- **JSON × YAML:** mesmo modelo de dados; o JSON é o padrão da API, e o YAML, o padrão de escrita humana. Todo JSON válido também é YAML válido.
- **JSONPath do `oc` ≠ `jq`:** sintaxes diferentes. O JSONPath vem embutido; o `jq` é externo.
- **`-o json` de Secret** mostra `data` em base64, que não é cifragem. Evite.

## No OpenShift 4.22 versus Kubernetes

Sem diferença de formato. As APIs `*.openshift.io` seguem as mesmas regras de serialização.

## No HomeLab SNO

`-o json` e `-o jsonpath` são leituras. Prefira JSONPath para estudar campos específicos sem despejar objetos enormes no terminal.

## Termos relacionados

[YAML](yaml.md) · [Manifest](manifest.md) · [API](kubernetes-api.md) · [API Server](api-server.md) · [Status](status.md)

## Fontes oficiais

- Kubernetes — API Concepts, "HTTP media types" e "JSON resource encoding": <https://kubernetes.io/docs/reference/using-api/api-concepts/> (fonte: `kubernetes/website` `release-1.35`)
- Kubernetes — JSONPath Support (kubectl): <https://kubernetes.io/docs/reference/kubectl/jsonpath/>
- Especificação JSON (fonte externa): <https://www.json.org/json-en.html>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 00-fundamentos-e-linguagem/json
- **Termo original:** JSON (JavaScript Object Notation)
- **Tradução:** não se traduz
- **Classe ontológica:** tecnologia (formato de serialização)
- **Plataforma:** padrão externo, usado por Kubernetes e OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo (formato padrão da API)
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-04

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** a sintaxe `range`/`end` foi conferida na página "JSONPath Support" (`reference/kubectl/jsonpath.md`, `release-1.35`). Validar os exemplos no SNO, onde **não foram executados**.

</details>
