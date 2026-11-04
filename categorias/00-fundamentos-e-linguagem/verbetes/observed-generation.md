# ObservedGeneration (status.observedGeneration)

> **ID:** 00-fundamentos-e-linguagem/observed-generation | **Termo original:** observedGeneration | **Tradução:** geração observada | **Classe ontológica:** conceito (campo de status) | **Plataforma:** Kubernetes / OpenShift | **Escopo:** não aplicável | **Disponibilidade:** nativo, mas **depende do tipo** (nem todos publicam) | **Versões validadas:** Kubernetes 1.35 / OCP 4.22 | **Nível:** intermediário | **Atualizado em:** 2026-11-04

## Definição em uma frase

`observedGeneration` é o campo em que o componente responsável registra **qual [generation](generation.md) do objeto ele observou por último**, e permite saber se o `status` reflete o desired state mais recente.

## Explicação didática

É o "recebi o seu pedido nº 5" do controller. Sem ele, você olharia um `status` saudável sem saber se ele é sobre o pedido atual ou sobre o anterior. Com ele, a comparação é direta: `observedGeneration` igual à `generation` significa que o controller está em dia.

## Para que existe e qual problema resolve

Evita conclusões erradas logo após uma mudança. Um Deployment pode exibir `Available=True` enquanto o controller ainda nem processou a nova imagem: essa condição é sobre a geração anterior.

## Funcionamento técnico e ciclo de vida

Pode aparecer em dois níveis:

- **No `status` do objeto** (`status.observedGeneration`): a geração mais recente observada pelo controller.
- **Em cada condição** (`status.conditions[].observedGeneration`): a geração com base na qual **aquela condição** foi calculada. A convenção traz um exemplo: se `metadata.generation` é 12 e a condição diz 9, a condição está **desatualizada** em relação ao estado atual.

Quem preenche é o controller do tipo. O campo é **opcional**, e nem todo tipo ou Operator o publica.

## Relações e dependências

- Comparado com [Generation](generation.md); fica em [Status](status.md) e em [Conditions](conditions.md).
- Sinal direto do andamento da [reconciliation](reconciliation.md).

## Exemplo de situação real

Um pipeline aplica um Deployment e espera `Available=True` para seguir. Às vezes passa cedo demais e quebra. A correção é esperar **também** `observedGeneration == generation`. É isso que comandos de espera de rollout fazem internamente.

## Como visualizar e inspecionar (somente leitura)

```bash
# No objeto
oc get deployment <nome> -n <namespace> \
  -o jsonpath='gen={.metadata.generation} obs={.status.observedGeneration}{"\n"}'

# Em cada condição, quando o tipo publica
oc get <tipo> <nome> -n <namespace> \
  -o jsonpath='{range .status.conditions[*]}{.type}={.status} obsGen={.observedGeneration}{"\n"}{end}'

# Acompanhar o rollout até terminar (leitura; sai quando conclui ou falha)
oc rollout status deployment/<nome> -n <namespace>
```

## Como interpretar a saída

- `obs` < `gen`: o `status` ainda é do pedido anterior. Espere ou investigue o controller.
- `obsGen` de uma condição menor que `gen`: **aquela condição** está velha, mesmo que outras estejam em dia.
- `obsGen` vazio nas condições: o tipo não preenche esse subcampo, o que é comum em tipos antigos. Use o `status.observedGeneration` do objeto.

## Diferenças e confusões frequentes

- **ObservedGeneration × Generation:** quem pede (sistema, a cada mudança do desejado) × quem confirma (controller).
- **ObservedGeneration × resourceVersion:** nada a ver com a versão interna de armazenamento.
- **Ausência ≠ erro:** muitos tipos simplesmente não têm o campo.

## No OpenShift 4.22 versus Kubernetes

Mesmo conceito. Em objetos do OpenShift e de Operators, procure `observedGeneration` no `status` ou nas condições; a presença varia por tipo.

## No HomeLab SNO

`oc rollout status` é leitura e ótimo para estudo; nos seus próprios Deployments, mostra a reconciliation acontecendo.

## Termos relacionados

[Generation](generation.md) · [Conditions](conditions.md) · [Status](status.md) · [Reconciliation](reconciliation.md) · [ResourceVersion](resource-version.md)

## Fontes oficiais

- Kubernetes API Conventions — "Typical status properties" (`observedGeneration` no objeto e na condição, com o exemplo 12 × 9): <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md>
- Kubernetes — Deployments, "Deployment status": <https://kubernetes.io/docs/concepts/workloads/controllers/deployment/> (fonte: `kubernetes/website` `release-1.35`)

## Revisão editorial

- **Estado:** 🟡 desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** confirmar que `oc rollout status` considera `observedGeneration` (comportamento conhecido do `kubectl`), o que **não foi verificado** no código ou na documentação desta rodada.
