# Node Annotation

## Definição em uma frase

Node Annotations são as [annotations](../../00-fundamentos-e-linguagem/verbetes/annotation.md) de um objeto [Node](node.md): metadados chave/valor que **não servem para seleção** e são usados por componentes da plataforma para registrar o estado e a configuração do nó.

## Explicação didática

As labels do nó são para escolher onde rodar; as annotations do nó são "anotações de bastidor". No OpenShift, por exemplo, o [Machine Config Operator](../../01-arquitetura-e-control-plane/verbetes/machine-config-operator.md) grava nelas qual configuração o nó tem e em que estado de atualização está. Outros componentes, como a rede e a Machine API, também registram informações ali.

## Para que existe e qual problema resolve

Dá aos controllers um lugar padronizado para guardar informações sobre o nó, sem criar campos novos na API para cada necessidade.

## Funcionamento técnico e ciclo de vida

- Ficam em `metadata.annotations` do Node.
- São escritas e lidas por componentes. **Editá-las à mão** pode confundir o componente que as usa, ou ser revertido por ele.
- Exemplos típicos no OpenShift: `machineconfiguration.openshift.io/currentConfig`, `.../desiredConfig` e `.../state`, gravadas pelo MCO.

## Relações e dependências

- Caso de [Annotation](../../00-fundamentos-e-linguagem/verbetes/annotation.md) aplicado a um [Node](node.md).
- Usadas pelo [Machine Config Operator](../../01-arquitetura-e-control-plane/verbetes/machine-config-operator.md) e por outros controllers da plataforma.

## Exemplo de situação real

Um pool mostra `UPDATING=True` por muito tempo. Nas annotations de um nó, `currentConfig` e `desiredConfig` são diferentes, e `state` está em `Working` ou `Degraded`. Esse é o nó que ainda não aplicou a nova configuração.

## Como visualizar e inspecionar (somente leitura)

```bash
# Annotations do nó
oc get node <nó> -o jsonpath='{.metadata.annotations}' ; echo

# Estado do MCO no nó
oc get node <nó> -o jsonpath='current={.metadata.annotations.machineconfiguration\.openshift\.io/currentConfig}{"\n"}desired={.metadata.annotations.machineconfiguration\.openshift\.io/desiredConfig}{"\n"}state={.metadata.annotations.machineconfiguration\.openshift\.io/state}{"\n"}'
```

## Como interpretar a saída

- `current` igual a `desired` e `state=Done`: o nó está com a configuração em dia.
- `state=Degraded`: veja a annotation de motivo do MCO, se houver, e o pool correspondente.

## Diferenças e confusões frequentes

- **Annotation × label:** não é possível selecionar nós por annotation.
- **Annotation × condition:** a condição é o padrão da API para saúde; a annotation é um registro específico de um componente.

## No OpenShift 4.22 versus Kubernetes

O mecanismo é do Kubernetes. O OpenShift usa muitas annotations de nó próprias, principalmente do MCO.

## No HomeLab SNO

Ler é seguro e útil para acompanhar atualizações de configuração. **Não** edite annotations do nó.

## Termos relacionados

[Annotation](../../00-fundamentos-e-linguagem/verbetes/annotation.md) · [Node Label](node-label.md) · [Node](node.md) · [Machine Config Operator](../../01-arquitetura-e-control-plane/verbetes/machine-config-operator.md)

## Fontes oficiais

- Kubernetes — Annotations: <https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/> (fonte: `kubernetes/website` `release-1.35`)
- Kubernetes — Well-Known Labels, Annotations and Taints: <https://kubernetes.io/docs/reference/labels-annotations-taints/>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/node-annotation
- **Termo original:** node annotation
- **Tradução:** annotation de nó (só como apoio)
- **Classe ontológica:** conceito (campo `metadata.annotations` do Node)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** as annotations do MCO (`currentConfig`, `desiredConfig`, `state`) são conhecidas da documentação de status do MCO, mas **não foram lidas** nesta rodada; validar no SNO.

</details>
