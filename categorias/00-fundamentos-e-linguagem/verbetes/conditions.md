# Conditions (status.conditions)

> **ID:** 00-fundamentos-e-linguagem/conditions | **Termo original:** conditions | **Remissões:** condition, phase (padrão antigo) | **Tradução:** condições | **Classe ontológica:** conceito / estado (campo de status) | **Plataforma:** Kubernetes / OpenShift | **Escopo:** não aplicável | **Disponibilidade:** nativo; cada tipo define as suas | **Versões validadas:** Kubernetes 1.35 / OCP 4.22 | **Nível:** intermediário | **Atualizado em:** 2026-11-04

## Definição em uma frase

Conditions são uma **lista padronizada no `status`** em que os controllers relatam aspectos da saúde de um objeto (ex.: `Ready`, `Available`, `Degraded`), cada um com valor `True`, `False` ou `Unknown`, um motivo e uma mensagem.

## Explicação didática

Em vez de cada tipo inventar seu próprio formato de "está tudo bem?", a API adotou um formato comum. Um Pod diz se está `Ready`; um Deployment, se está `Available` e `Progressing`; um ClusterOperator, se está `Available`, `Progressing` ou `Degraded`. Ferramentas e pessoas leem todos do mesmo jeito.

Cada condição tem:

| Campo | Significado |
|---|---|
| `type` | Nome da condição, em PascalCase (`Ready`, `Available`) |
| `status` | `True`, `False` ou `Unknown` |
| `reason` | Motivo curto, em CamelCase, para leitura por máquina e em resumos (`MinimumReplicasAvailable`) |
| `message` | Frase legível, com detalhes da ocorrência |
| `lastTransitionTime` | Quando o `status` da condição mudou pela última vez |
| `observedGeneration` | (opcional) Geração com base na qual a condição foi calculada |

## Para que existe e qual problema resolve

Dá a outros componentes um **resumo pronto** sem que precisem entender os detalhes de cada tipo. O exemplo da convenção: dá para deduzir a disponibilidade de um Deployment pelos contadores de réplicas, mas a condição `Available` evita que cada ferramenta reimplemente essa lógica.

## Funcionamento técnico e ciclo de vida

- A lista é tratada como um **mapa por `type`**: no máximo uma condição de cada tipo.
- Condições **complementam** o status detalhado, sem substituí-lo.
- **Polaridade:** algumas são normais quando `True` (`Ready`, `Available`), e outras quando `False` (`Degraded`, `MemoryPressure`). Sem conhecer o tipo, não dá para resumir genericamente.
- **Ausência de uma condição conhecida** equivale a `Unknown`; em geral, a reconciliation ainda não terminou.
- O significado de uma condição, depois de definido, faz parte da API e não pode mudar arbitrariamente.
- **`phase` é padrão antigo:** alguns tipos v1 (como Pod e Namespace) têm o campo `phase`; a convenção o considera **deprecated** para tipos novos, que devem usar conditions.

## Relações e dependências

- Ficam em [Status](status.md); relacionam-se com [ObservedGeneration](observed-generation.md).
- Complementadas pelos [Events](events.md), que contam a história, enquanto as condições mostram o momento atual.

## Exemplo de situação real

`oc get clusteroperators` mostra `ingress` com `DEGRADED=True`. Em `oc describe clusteroperator ingress`, a condição `Degraded` traz `reason` e `message` explicando, por exemplo, que réplicas do roteador não estão disponíveis. O `lastTransitionTime` mostra desde quando.

## Como visualizar e inspecionar (somente leitura)

```bash
# Condições de um objeto, uma por linha
oc get <tipo> <nome> -n <namespace> \
  -o jsonpath='{range .status.conditions[*]}{.type}={.status} [{.reason}] {.message} ({.lastTransitionTime}){"\n"}{end}'

# Condições de um Pod
oc get pod <nome> -n <namespace> \
  -o jsonpath='{range .status.conditions[*]}{.type}={.status}{"\n"}{end}'

# Visão humana: seção Conditions
oc describe deployment <nome> -n <namespace>

# OpenShift: condições resumidas da plataforma
oc get clusteroperators
```

## Como interpretar a saída

- Leia `type` + `status` + **polaridade**: `Degraded=False` é bom, e `Ready=False` é ruim.
- O `reason` é a melhor palavra-chave para buscar na documentação; a `message` dá o detalhe.
- Um `lastTransitionTime` recente numa condição ruim indica um problema novo; um antigo indica um problema persistente.
- Condições de Pod comuns: `PodScheduled`, `Initialized`, `ContainersReady` e `Ready`. A ordem em que ficam `True` conta a história da inicialização.

## Diferenças e confusões frequentes

- **Conditions × phase:** a lista de condições é o padrão atual; a `phase` é um resumo enumerado mais antigo.
- **Conditions × Events:** foto atual × histórico de ocorrências.
- **`status` da condição × campo `status` do objeto:** mesma palavra, níveis diferentes.

## No OpenShift 4.22 versus Kubernetes

O OpenShift padroniza `Available`, `Progressing`, `Degraded` e, quando faz sentido, `Upgradeable` nos `ClusterOperator`s. É isso que as colunas de `oc get clusteroperators` resumem.

## No HomeLab SNO

Condições são a leitura de saúde mais rica e segura. Comece por `oc get clusteroperators` e desça para `oc describe` no que não estiver normal.

## Termos relacionados

[Status](status.md) · [ObservedGeneration](observed-generation.md) · [Events](events.md) · [Current State](current-state.md) · [ClusterOperator](../../09-operators-e-extensoes/verbetes/clusteroperator.md) · [Pod](../../03-workloads/verbetes/pod.md)

## Fontes oficiais

- Kubernetes API Conventions — "Typical status properties" (conditions, polaridade, campos, `phase` deprecated): <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md>
- Kubernetes — Pod Lifecycle, "Pod conditions": <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/>

<details>
<summary>Notas de revisão</summary>

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** as condições de Pod listadas são as conhecidas da página Pod Lifecycle, que **não foi lida** nesta rodada (o 1.35 pode listar outras, como `PodReadyToStartContainers`); conferir na categoria 03. Confirmar a condição `Upgradeable` em ClusterOperators (categoria 09).

</details>
