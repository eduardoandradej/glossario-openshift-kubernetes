# Job

## Definição em uma frase

O Job executa **tarefas que terminam**: cria um ou mais [Pods](pod.md) e continua tentando até que um número definido deles **conclua com sucesso**.

## Explicação didática

Um Deployment existe para ficar rodando; um Job existe para **terminar**: uma migração de banco, um processamento em lote, um relatório. Quando o trabalho acaba, os Pods ficam com estado `Completed`, e o Job é marcado como concluído.

Remissão: **Batch** (processamento em lote) é o tipo de carga que Jobs e CronJobs executam; o grupo da API se chama `batch`.

## Para que existe e qual problema resolve

Dá ao Kubernetes suporte a cargas **em lote**, com novas tentativas automáticas em caso de falha.

## Funcionamento técnico e ciclo de vida

- **Conclusões:** `.spec.completions` define quantas execuções bem-sucedidas são necessárias; `.spec.parallelism`, quantos Pods podem rodar ao mesmo tempo.
- **Modo de conclusão:** `NonIndexed` (padrão: conclui quando houver `completions` Pods bem-sucedidos) ou `Indexed` (cada Pod recebe um índice de 0 a `completions-1`).
- **Falhas:** `.spec.backoffLimit` define quantas novas tentativas são feitas antes de marcar o Job como falho. O **padrão é 6**.
- **`restartPolicy`:** no template do Job, só são aceitos `Never` ou `OnFailure`.
- **Limpeza:** Jobs concluídos e os seus Pods ficam até serem apagados; `ttlSecondsAfterFinished` permite a remoção automática (ver [Garbage Collection](../../00-fundamentos-e-linguagem/verbetes/garbage-collection.md)).

## Relações e dependências

- Cria [Pods](pod.md) a partir de um [Pod Template](pod-template.md); pode ser criado por um [CronJob](cronjob.md).
- Exemplo clássico de controller na documentação do Kubernetes. Ver [Controller](../../00-fundamentos-e-linguagem/verbetes/controller.md).

## Exemplo de situação real

Um Job de migração falha seis vezes seguidas por erro de credencial e fica marcado como falho (`BackoffLimitExceeded`). Os logs de um dos Pods mostram o erro. Corrigido o Secret, o Job é recriado.

## Como visualizar e inspecionar (somente leitura)

```bash
# Jobs: conclusões e duração
oc get jobs -n <namespace>

# Condições e eventos (Complete, Failed)
oc describe job <nome> -n <namespace>

# Pods do Job e logs
oc get pods -n <namespace> -l job-name=<nome>
oc logs job/<nome> -n <namespace>
```

## Como interpretar a saída

- `COMPLETIONS 1/1` e `STATUS Complete`: concluído.
- Condição `Failed=True` com `reason: BackoffLimitExceeded`: as tentativas se esgotaram.
- Pods em `Completed` são o resultado normal de um Job e não precisam ser "consertados".

## Diferenças e confusões frequentes

- **Job × Deployment:** termina × fica rodando.
- **Job × CronJob:** execução única × execução agendada e repetida.
- **`Completed` não é erro:** é o estado final esperado do Pod de um Job.

## No OpenShift 4.22 versus Kubernetes

Mesmo objeto (`batch/v1`).

## No HomeLab SNO

Jobs curtos são ótimos para estudo. Defina `ttlSecondsAfterFinished` para não acumular Pods `Completed` no nó único.

## Termos relacionados

[CronJob](cronjob.md) · [Pod](pod.md) · [Pod Template](pod-template.md) · [Controller](../../00-fundamentos-e-linguagem/verbetes/controller.md) · [Garbage Collection](../../00-fundamentos-e-linguagem/verbetes/garbage-collection.md)

## Fontes oficiais

- Kubernetes — Jobs (`completions`, `parallelism`, `completionMode`, `backoffLimit` padrão 6, `restartPolicy`): <https://kubernetes.io/docs/concepts/workloads/controllers/job/> (fonte: `kubernetes/website` `release-1.35`, `concepts/workloads/controllers/job.md`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/job
- **Termo original:** Job
- **Remissões:** Batch, backoffLimit, completionMode
- **Tradução:** tarefa (só como apoio)
- **Classe ontológica:** objeto da API
- **API:** `apiVersion: batch/v1`, `kind: Job`
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** namespaced
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido (antes era uma versão inicial). Fontes conferidas em 2026-11-08.
- **Pendências:** a label `job-name` e a `reason: BackoffLimitExceeded` são conhecidas da documentação; confirmar no SNO.

</details>
