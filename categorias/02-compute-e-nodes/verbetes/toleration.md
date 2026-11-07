# Toleration

## Definição em uma frase

Uma toleration é a declaração, no Pod, de que ele **aceita um ou mais [taints](taint.md)**. Ela permite, sem obrigar, que o Pod seja agendado e permaneça em nós com esses taints.

## Explicação didática

O taint é o aviso "acesso restrito" no nó; a toleration é a credencial no Pod. Ter a credencial não leva o Pod ao nó: só o autoriza a entrar. Para **levar**, combine com [Node Selector](node-selector.md) ou [Node Affinity](node-affinity.md).

```yaml
# Trecho didático de um Pod
tolerations:
- key: "dedicated"
  operator: "Equal"      # padrão; compara chave e valor
  value: "infra"
  effect: "NoSchedule"
- key: "node.kubernetes.io/unreachable"
  operator: "Exists"     # qualquer valor da chave
  effect: "NoExecute"
  tolerationSeconds: 600 # fica 10 min antes de ser despejado
```

## Para que existe e qual problema resolve

Permite que cargas específicas (componentes de plataforma, agentes de nó, aplicações dedicadas) rodem em nós reservados ou continuem rodando por um tempo em nós com problemas.

## Funcionamento técnico e ciclo de vida

- **Correspondência:** a toleration casa com o taint se a **chave** e o **efeito** forem iguais e:
  - o operador for `Exists` (sem valor); ou
  - o operador for `Equal` e os valores forem iguais.
- **Casos especiais:** chave vazia com `Exists` casa com **todas** as chaves; efeito vazio casa com todos os efeitos da chave.
- **`tolerationSeconds`** (só com `NoExecute`): quanto tempo o Pod continua no nó depois que o taint aparece.
- **Tolerations automáticas:**
  - o Kubernetes acrescenta `node.kubernetes.io/not-ready` e `node.kubernetes.io/unreachable` com `tolerationSeconds=300`. Os Pods ficam **5 minutos** num nó com problema antes de ser despejados, a menos que você defina outro valor;
  - Pods que não são `BestEffort` recebem toleration a `memory-pressure`;
  - DaemonSets recebem tolerations a `memory-pressure`, `disk-pressure` e outras, para não serem quebrados por essas condições.

## Relações e dependências

- Contraparte do [Taint](taint.md); normalmente usada junto de [Node Selector](node-selector.md) ou [Node Affinity](node-affinity.md).
- Ligada à [QoS Class](qos-class.md) (toleration automática a `memory-pressure`).

## Exemplo de situação real

Depois da queda de um nó, os Pods de uma aplicação levam cerca de 5 minutos para ser recriados em outro nó. É o efeito da toleration automática de 300 segundos a `unreachable`. Para reagir mais rápido, defina um `tolerationSeconds` menor no Pod, avaliando o risco de falsos alarmes.

## Como visualizar e inspecionar (somente leitura)

```bash
# Tolerations de um Pod (inclui as automáticas)
oc get pod <nome> -n <namespace> -o jsonpath='{range .spec.tolerations[*]}{.key} {.operator} {.value} {.effect} {.tolerationSeconds}{"\n"}{end}'

# Esquema do campo
oc explain pod.spec.tolerations
```

## Como interpretar a saída

- Linhas `node.kubernetes.io/not-ready Exists NoExecute 300` e `node.kubernetes.io/unreachable Exists NoExecute 300` são as tolerations automáticas.
- Uma toleration com chave vazia e `Exists` tolera **qualquer** taint. É típica de agentes que precisam rodar em todos os nós.

## Diferenças e confusões frequentes

- **Toleration × afinidade:** permissão × direcionamento.
- **Toleration ampla demais** (chave vazia e `Exists`) faz o Pod ignorar todos os taints, inclusive os de nós com problema.

## No OpenShift 4.22 versus Kubernetes

Mesmo mecanismo. O OpenShift permite **tolerations padrão por projeto** com a annotation `scheduler.alpha.kubernetes.io/defaultTolerations` no namespace, que a documentação usa, por exemplo, para iniciar Pods de debug em nós com taint `NoExecute`.

## No HomeLab SNO

Leitura segura. Para estudo, observe as tolerations automáticas dos seus Pods e as dos Pods da plataforma.

## Termos relacionados

[Taint](taint.md) · [Node Selector](node-selector.md) · [Node Affinity](node-affinity.md) · [QoS Class](qos-class.md) · [Node Condition](node-condition.md)

## Fontes oficiais

- Kubernetes — Taints and Tolerations (correspondência, casos especiais, `tolerationSeconds`, tolerations automáticas): <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/> (fonte: `kubernetes/website` `release-1.35`)
- OCP 4.22 — Generating a sosreport archive (annotation `scheduler.alpha.kubernetes.io/defaultTolerations` num namespace; fonte: `modules/support-generating-a-sosreport-archive.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/toleration
- **Termo original:** toleration
- **Remissões:** tolerationSeconds
- **Tradução:** tolerância (só como apoio)
- **Classe ontológica:** conceito (campo `spec.tolerations` do Pod)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** confirmar no SNO as tolerations automáticas num Pod comum, que **não foram executadas**.

</details>
