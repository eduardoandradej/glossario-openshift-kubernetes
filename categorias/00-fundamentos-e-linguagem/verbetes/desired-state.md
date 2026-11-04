# Desired State (estado desejado)

> **ID:** 00-fundamentos-e-linguagem/desired-state | **Termo original:** desired state | **Tradução:** estado desejado | **Classe ontológica:** conceito / padrão (modelo declarativo) | **Plataforma:** Kubernetes / OpenShift | **Escopo:** não aplicável | **Disponibilidade:** nativo | **Versões validadas:** Kubernetes 1.35 / OCP 4.22 | **Nível:** básico | **Atualizado em:** 2026-11-04

## Definição em uma frase

Desired state é a **descrição de como algo deve estar**, registrada num [objeto](object.md), normalmente no seu [`spec`](spec.md), e que o sistema trabalha continuamente para tornar realidade.

## Explicação didática

A analogia oficial é o **termostato**. Você ajusta 22 °C: esse é o desired state. A temperatura real da sala é o [current state](current-state.md). O termostato liga e desliga o equipamento para aproximar um do outro. Você não diz "ligue o aquecedor por 10 minutos"; diz "quero 22 °C".

No Kubernetes é igual: "quero 3 réplicas desta imagem, expostas na porta 8080". Como chegar lá é problema dos controllers.

**Não existe objeto chamado "DesiredState".** É um conceito, materializado no `spec` (ou em campos equivalentes, como `data` ou `rules`) de cada objeto.

## Para que existe e qual problema resolve

O modelo **declarativo** resolve problemas do modelo **imperativo** (sequências de comandos):

| Imperativo ("faça X") | Declarativo ("quero X") |
|---|---|
| Se um passo falha, o estado fica pela metade | O sistema continua tentando até convergir |
| Repetir o comando pode duplicar o efeito | Reaplicar o mesmo estado não muda nada (**idempotente**) |
| Desvios posteriores passam despercebidos | Desvios são detectados e corrigidos |
| Difícil auditar "como deveria estar" | O próprio objeto **é** a documentação da intenção |

## Funcionamento técnico e ciclo de vida

1. O desired state é **declarado**: um manifesto aplicado, um comando do CLI ou outro controller (um Deployment declara o desired state de um ReplicaSet, que declara o de Pods).
2. Fica **persistido** na API, e não na memória de um processo.
3. **Controllers** comparam esse estado com o observado e agem. Ver [Reconciliation](reconciliation.md).
4. Quando o `spec` muda, o novo desired state substitui o anterior. O sistema persegue sempre o **mais recente**, sem precisar passar por estados intermediários.
5. Pode haver **cascata**: o current state de um nível (Pods criados) vira o desired state de outro. Após o scheduling, por exemplo, o Pod passa a fazer parte do desired state do kubelet do nó.

## Relações e dependências

- Materializado em [`spec`](spec.md); comparado com o [current state](current-state.md) relatado em [`status`](status.md).
- Imposto pela [reconciliation](reconciliation.md).
- Hierarquia: Deployment → ReplicaSet → Pod. Ver [Deployment](../../03-workloads/verbetes/deployment.md) e [ReplicaSet](../../03-workloads/verbetes/replicaset.md).

## Exemplo de situação real

Um administrador apaga um Pod para "reiniciá-lo". O Pod volta com outro nome. Não é falha: o desired state (3 réplicas, no ReplicaSet) continua igual, e o controller recriou o que faltava. Para mudar de verdade, é preciso alterar o desired state, por exemplo `spec.replicas` no Deployment.

## Como visualizar e inspecionar (somente leitura)

O desired state se lê no `spec` dos objetos:

```bash
# Desired state de réplicas de um Deployment
oc get deployment <nome> -n <namespace> -o jsonpath='{.spec.replicas}{"\n"}'

# Comparação lado a lado: desejado × pronto
oc get deployment <nome> -n <namespace> \
  -o custom-columns=NOME:.metadata.name,DESEJADO:.spec.replicas,PRONTO:.status.readyReplicas

# Quanto o seu manifesto local difere do desired state guardado no cluster
# (somente leitura: oc diff não aplica nada)
oc diff -f <arquivo>.yaml
```

## Como interpretar a saída

- Em `custom-columns`, `DESEJADO` diferente de `PRONTO` significa que a reconciliation está em curso ou bloqueada; investigue `status.conditions` e os Events.
- O `oc diff` mostra no formato *diff* o que **mudaria** no desired state se o arquivo fosse aplicado. Saída vazia indica que o manifesto local já coincide com o armazenado.
- Um valor `<none>` em `PRONTO` costuma significar que o campo ainda não foi preenchido pelo controller.

## Diferenças e confusões frequentes

- **Desired state ≠ manifesto local:** o que vale é o que está **na API**. Um YAML no seu disco ou no Git só vira desired state quando é aplicado (base do GitOps, categoria 15).
- **Desired state ≠ resultado garantido:** declarar 3 réplicas não garante 3 Pods prontos (pode faltar CPU, a imagem pode não existir...).
- **Declarativo × imperativo no CLI:** `oc apply -f` trabalha com o desired state completo; `oc scale`, `oc set image` são atalhos imperativos que **também** alteram o desired state. O efeito final está sempre no objeto.

## No OpenShift 4.22 versus Kubernetes

O OpenShift aplica o mesmo modelo **à própria plataforma**: a versão desejada do cluster é declarada em `ClusterVersion` e a configuração em objetos de `config.openshift.io`. Os Operators reconciliam os componentes até esse estado. Em clusters gerenciados por Operators, alterar recursos internos à mão pode ser desfeito pela reconciliation.

## No HomeLab SNO

Observe o desired state à vontade com `get`, `-o jsonpath` e `oc diff`. **Não** altere o desired state de objetos em `openshift-*`: o Operator correspondente pode reverter a mudança, ou pior, a configuração passa a divergir do suportado.

## Diagrama Mermaid

```mermaid
flowchart LR
    D["Desired state<br/>(spec)"] --> CMP{"Controller compara"}
    O["Current state<br/>(status / mundo real)"] --> CMP
    CMP -->|"diferença"| ACT["Ação: criar, remover, atualizar"]
    ACT --> O
    CMP -->|"sem diferença"| W["Aguarda novo evento"]
```

## Termos relacionados

[Current State](current-state.md) · [Reconciliation](reconciliation.md) · [Spec](spec.md) · [Status](status.md) · [Object](object.md) · [Deployment](../../03-workloads/verbetes/deployment.md)

## Fontes oficiais

- Kubernetes — Controllers (control loop, termostato, "Desired versus current state"): <https://kubernetes.io/docs/concepts/architecture/controller/> (fonte: `kubernetes/website` `release-1.35`, `content/en/docs/concepts/architecture/controller.md`)
- Kubernetes — Objects In Kubernetes ("record of intent"): <https://kubernetes.io/docs/concepts/overview/working-with-objects/>
- Kubernetes API Conventions — "Spec and Status" (*level-based*): <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md>
- OCP 4.22 — "Kubernetes overview", seção "Kubernetes resources" (modelo declarativo e Operators como control loop). Fonte conferida: `openshift-docs` `enterprise-4.22`, `welcome/kubernetes-overview.adoc` → `modules/kubernetes-resources.adoc`. URL publicada **a verificar**: <https://docs.redhat.com/en/documentation/openshift_container_platform/4.22>

<details>
<summary>Notas de revisão</summary>

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** confirmar com `oc diff --help` no cliente 4.22 que o comportamento é somente leitura (assim está documentado no `kubectl diff`). Exemplos **não executados**.

</details>
