# Generation (metadata.generation)

> **ID:** 00-fundamentos-e-linguagem/generation | **Termo original:** generation | **Tradução:** geração | **Classe ontológica:** conceito (campo de metadata) | **Plataforma:** Kubernetes / OpenShift | **Escopo:** não aplicável | **Disponibilidade:** nativo (preenchido pelo sistema) | **Versões validadas:** Kubernetes 1.35 / OCP 4.22 | **Nível:** intermediário | **Atualizado em:** 2026-11-04

## Definição em uma frase

`metadata.generation` é um **número sequencial, definido pelo sistema e sempre crescente**, que representa uma versão específica do **[estado desejado](desired-state.md)** de um objeto.

## Explicação didática

Toda vez que você muda o que **pede** (o `spec`), a geração sobe: 1, 2, 3... Mudanças que não alteram o pedido, como atualizações de `status`, normalmente **não** mudam a geração. Por isso ela é a régua ideal para responder: "o controller já viu o meu último pedido?". Basta compará-la com a [observedGeneration](observed-generation.md).

## Para que existe e qual problema resolve

A [resourceVersion](resource-version.md) muda com qualquer escrita, até as do próprio controller, e não diz se o **pedido** mudou. A `generation` isola esse sinal: ela só avança quando o estado desejado muda.

## Funcionamento técnico e ciclo de vida

- **Definida pelo sistema:** começa em 1 na criação e cresce de forma monotônica, por objeto.
- **Quando sobe:** em mudanças no estado desejado, que na maioria dos tipos é o `spec`. Quais campos contam depende do tipo. Para recursos personalizados com o subrecurso `status` habilitado, mudanças em `metadata` e `status` não incrementam a geração.
- **Uso típico:** o controller copia a geração que acabou de processar para `status.observedGeneration`, e para `observedGeneration` dentro de cada condição quando o tipo suporta.

## Relações e dependências

- Campo de [metadata](metadata.md), comparado com [ObservedGeneration](observed-generation.md).
- Ligado ao [spec](spec.md) e à [reconciliação](reconciliation.md).

## Exemplo de situação real

Você troca a imagem de um Deployment. A `generation` vai de 4 para 5. Por alguns segundos, `status.observedGeneration` ainda mostra 4: o status que você vê **é sobre o pedido antigo**. Quando passa para 5, o controller começou a tratar o novo pedido, e aí sim as condições de rollout passam a falar da nova imagem.

## Como visualizar e inspecionar (somente leitura)

```bash
# Geração atual × geração observada pelo controller
oc get deployment <nome> -n <namespace> \
  -o jsonpath='generation={.metadata.generation} observed={.status.observedGeneration}{"\n"}'

# Em vários objetos de uma vez
oc get deployments -n <namespace> \
  -o custom-columns=NOME:.metadata.name,GEN:.metadata.generation,OBS:.status.observedGeneration
```

## Como interpretar a saída

| Situação | Leitura |
|---|---|
| `GEN` = `OBS` | O controller já processou o último pedido; o `status` é atual |
| `GEN` > `OBS` | O último pedido ainda não foi processado (instantes após a mudança) ou o controller está com problema |
| `OBS` vazio | O tipo não publica `observedGeneration`, ou o controller ainda não agiu |

## Diferenças e confusões frequentes

- **Generation × resourceVersion:** pedido × qualquer escrita.
- **Generation × revisão do Deployment:** a revisão (`deployment.kubernetes.io/revision`) conta rollouts do template; mudar só `replicas` sobe a `generation`, mas não cria revisão nova.
- **Nem todo tipo usa `generation` da mesma forma**, e alguns não publicam `observedGeneration`.

## No OpenShift 4.22 versus Kubernetes

Igual. ClusterOperators e muitos objetos de configuração do OpenShift também publicam gerações observadas no status; o formato exato varia por tipo.

## No HomeLab SNO

Comparar `generation` e `observedGeneration` é o diagnóstico mais barato e seguro para saber se "a mudança pegou".

## Termos relacionados

[ObservedGeneration](observed-generation.md) · [ResourceVersion](resource-version.md) · [Spec](spec.md) · [Status](status.md) · [Reconciliação](reconciliation.md) · [Deployment](../../03-workloads/verbetes/deployment.md)

## Fontes oficiais

- Kubernetes API Conventions — "Metadata" (`generation`) e "Typical status properties" (`observedGeneration`): <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md>
- Kubernetes — Deployments, "Deployment status" (`observedGeneration`): <https://kubernetes.io/docs/concepts/workloads/controllers/deployment/> (fonte: `kubernetes/website` `release-1.35`)

## Revisão editorial

- **Estado:** 🟡 desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** a regra sobre CRDs com subrecurso `status` vem da documentação de CustomResourceDefinitions, que **não foi lida** nesta rodada; conferir na categoria 09. Exemplos **não executados** no SNO.
