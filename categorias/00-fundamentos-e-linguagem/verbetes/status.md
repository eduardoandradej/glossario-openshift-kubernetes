# Status

> **ID:** 00-fundamentos-e-linguagem/status | **Termo original:** status | **Tradução:** status, estado (atual) | **Classe ontológica:** conceito (campo convencional dos objetos) | **Plataforma:** Kubernetes / OpenShift | **Escopo:** não aplicável | **Disponibilidade:** nativo | **Versões validadas:** Kubernetes 1.35 / OCP 4.22 | **Nível:** básico | **Atualizado em:** 2026-11-04

## Definição em uma frase

`status` é o campo de um [objeto](object.md) em que **o sistema** registra o [estado observado](current-state.md): o que de fato aconteceu em resposta ao [`spec`](spec.md).

## Explicação didática

Se o `spec` é o pedido, o `status` é o **relatório de andamento**. Quem escreve nele não é você, e sim o controller responsável pelo objeto (ou o kubelet, no caso dos Pods). Por isso o `status` é a primeira coisa a ler quando algo "não funciona": ele diz o que o sistema conseguiu e o que não conseguiu fazer.

## Para que existe e qual problema resolve

- **Transparência:** o resultado das ações automáticas fica visível para pessoas e ferramentas.
- **Coordenação:** outros controllers leem o `status` de um objeto para decidir as suas próprias ações.
- **Segurança de escrita:** o `status` é atualizado por um subrecurso separado (`/status`), com permissões próprias. Gravações normais (PUT/POST no objeto) **ignoram** o `status`, o que evita sobrescrevê-lo por acidente.

## Funcionamento técnico e ciclo de vida

Pelas convenções da API, o `status` contém as **observações mais recentes** do estado real. Pode também guardar resultados de alocações feitas em resposta ao `spec`. Na maioria dos tipos ele é persistido com o objeto, mas pode ser gerado na hora.

Campos típicos (variam por kind):

- **`conditions`:** lista de condições, cada uma com `type`, `status` (`True`/`False`/`Unknown`), `reason`, `message` e `lastTransitionTime`. É o mecanismo padrão de resumo de saúde (verbete futuro: *Conditions*).
- **`observedGeneration`:** qual `metadata.generation` do `spec` o controller já processou (verbete futuro).
- **Contadores e fases:** por exemplo `readyReplicas`, ou `phase` num Pod.

Detalhes importantes sobre `conditions`:
- Algumas são "normais quando `True`" (`Ready`, `Available`); outras, "normais quando `False`" (`Degraded`, `MemoryPressure`). Sem conhecer o tipo, não dá para resumir a saúde.
- A **ausência** de uma condição conhecida deve ser lida como `Unknown`: em geral, a reconciliação ainda não terminou.

## Relações e dependências

- Contraparte: [`spec`](spec.md).
- Conceitos: [estado observado](current-state.md) e [reconciliação](reconciliation.md).
- Os Events complementam o `status` com um histórico do que aconteceu; o `status` é a "foto" atual.

## Exemplo de situação real

Um Deployment mostra `0/3` réplicas prontas. No `status.conditions` aparece `type: Progressing`, `status: "False"`, `reason: ProgressDeadlineExceeded`. O Deployment não conseguiu concluir o rollout dentro do prazo, e a causa costuma estar nos Pods (imagem inexistente, falta de recursos...), visível nos Events.

## Como visualizar e inspecionar (somente leitura)

```bash
# Status completo do objeto
oc get deployment <nome> -n <namespace> -o jsonpath='{.status}' ; echo

# Condições, uma por linha
oc get deployment <nome> -n <namespace> \
  -o jsonpath='{range .status.conditions[*]}{.type}={.status} ({.reason}){"\n"}{end}'

# Resumo legível, com Conditions e Events
oc describe deployment <nome> -n <namespace>

# Plataforma OpenShift: condições Available/Progressing/Degraded de cada Operator
oc get clusteroperators

# Esquema do status de um kind
oc explain deployment.status
```

## Como interpretar a saída

Trecho **ilustrativo** de `-o yaml` de um Deployment saudável:

```yaml
status:
  observedGeneration: 4
  replicas: 3
  readyReplicas: 3
  availableReplicas: 3
  conditions:
  - type: Available
    status: "True"
    reason: MinimumReplicasAvailable
  - type: Progressing
    status: "True"
    reason: NewReplicaSetAvailable
```

- Se `observedGeneration` for **igual** a `metadata.generation`, o controller já viu o último `spec`. Se for **menor**, o `status` está desatualizado em relação ao pedido.
- Em `oc get clusteroperators`, o normal é `AVAILABLE=True`, `PROGRESSING=False`, `DEGRADED=False`.
- `status` vazio num objeto recém-criado costuma significar só que ainda não houve reconciliação. Se continuar vazio, verifique se existe controller para aquele tipo (por exemplo, um Operator que não está instalado).

## Diferenças e confusões frequentes

- **`status` (campo) ≠ coluna `STATUS` do `oc get pods`:** a coluna é um **resumo calculado pelo cliente/servidor** (ex.: `CrashLoopBackOff`), e não um campo literal. `CrashLoopBackOff` aparece no `status` do contêiner (`state.waiting.reason`), e não em `status.phase`.
- **`status` ≠ kind `Status`:** `Status` é o kind de resposta de erro da API (ex.: em um `404`).
- **Não edite o `status`:** ele é reescrito pelo controller.

## No OpenShift 4.22 versus Kubernetes

O OpenShift usa intensamente o padrão de condições `Available` / `Progressing` / `Degraded` (às vezes `Upgradeable`) em `ClusterOperator` e `ClusterVersion`. É a forma padrão de ver a saúde da plataforma.

## No HomeLab SNO

`oc get clusteroperators` é o termômetro mais rápido do SNO e não altera nada. Um Operator em `Degraded=True` merece investigação com `oc describe clusteroperator <nome>`, não ações corretivas automáticas.

## Termos relacionados

[Spec](spec.md) · [Estado observado](current-state.md) · [Reconciliação](reconciliation.md) · [Objeto](object.md) · [ClusterOperator](../../09-operators-e-extensoes/verbetes/clusteroperator.md) · [Deployment](../../03-workloads/verbetes/deployment.md)

## Fontes oficiais

- Kubernetes — Objects In Kubernetes, "Object spec and status": <https://kubernetes.io/docs/concepts/overview/working-with-objects/> (fonte: `kubernetes/website` `release-1.35`)
- Kubernetes API Conventions — "Spec and Status", "Typical status properties": <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md>

## Revisão editorial

- **Estado:** 🟡 desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** os `reason` do Deployment (`MinimumReplicasAvailable`, `NewReplicaSetAvailable`, `ProgressDeadlineExceeded`) foram conferidos na página Deployments da documentação Kubernetes 1.35 (`concepts/workloads/controllers/deployment.md`). O YAML é **ilustrativo** e não foi coletado no SNO. Aprofundar nos verbetes *Conditions* e *ObservedGeneration*.
