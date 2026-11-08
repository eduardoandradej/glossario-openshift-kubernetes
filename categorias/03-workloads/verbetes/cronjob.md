# CronJob

## Definição em uma frase

O CronJob **cria [Jobs](job.md) numa agenda repetida**, descrita no formato do *cron* do Unix, para tarefas periódicas como backups e relatórios.

## Explicação didática

Um CronJob é como uma linha do `crontab`: "todo dia às 2h, rode este Job". A cada horário, ele cria um Job, e o Job cria os Pods que fazem o trabalho.

```yaml
# Trecho didático
spec:
  schedule: "0 2 * * *"        # todo dia às 02:00
  concurrencyPolicy: Forbid    # não sobrepor execuções
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: <imagem>
          restartPolicy: OnFailure
```

## Para que existe e qual problema resolve

Leva para o cluster a execução agendada de tarefas, com o histórico e a observabilidade dos Jobs.

## Funcionamento técnico e ciclo de vida

- **`schedule`:** expressão no formato cron.
- **`concurrencyPolicy`:** o que fazer se a execução anterior ainda estiver rodando:
  - `Allow` (padrão): permite execuções simultâneas;
  - `Forbid`: pula a nova execução;
  - `Replace`: substitui a execução em curso pela nova.
- **`startingDeadlineSeconds`:** quanto atraso é tolerado para iniciar uma execução perdida. Sem esse campo, não há prazo.
- O nome do CronJob compõe o nome dos Jobs e Pods criados.
- **Limitações:** a documentação alerta que, em certas circunstâncias, um único CronJob pode criar **vários Jobs simultâneos**. As tarefas devem ser **idempotentes**.

## Relações e dependências

- Cria [Jobs](job.md), que criam [Pods](pod.md).

## Exemplo de situação real

Um backup diário demora mais de 24 horas num dia de pico. Com `concurrencyPolicy: Allow`, a execução seguinte começa junto e as duas disputam o banco. A solução é `Forbid` ou `Replace`, conforme o caso.

## Como visualizar e inspecionar (somente leitura)

```bash
# CronJobs: agenda, suspensão, ativos, última execução
oc get cronjobs -n <namespace>

# Jobs criados pelo CronJob
oc get jobs -n <namespace> --sort-by=.metadata.creationTimestamp

# Detalhes e eventos
oc describe cronjob <nome> -n <namespace>
```

## Como interpretar a saída

- `SUSPEND True`: o CronJob está pausado e não cria Jobs.
- `ACTIVE` maior que 1: há execuções simultâneas (possível com `Allow`).
- `LAST SCHEDULE` antigo demais: o CronJob pode estar suspenso, com a agenda errada ou perdendo execuções.

## Diferenças e confusões frequentes

- **CronJob × Job:** agenda × execução.
- **CronJob × cron do SO do nó:** não se agenda nada no SO dos nós no OpenShift. Use CronJob.

## No OpenShift 4.22 versus Kubernetes

Mesmo objeto (`batch/v1`).

## No HomeLab SNO

Agendas muito frequentes acumulam Jobs e Pods no nó único. Ajuste os limites de histórico e use `Forbid` em tarefas pesadas.

## Termos relacionados

[Job](job.md) · [Pod](pod.md) · [Garbage Collection](../../00-fundamentos-e-linguagem/verbetes/garbage-collection.md)

## Fontes oficiais

- Kubernetes — CronJob (agenda, `concurrencyPolicy`, `startingDeadlineSeconds`, limitações): <https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/> (fonte: `kubernetes/website` `release-1.35`, `concepts/workloads/controllers/cron-jobs.md`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/cronjob
- **Termo original:** CronJob
- **Remissões:** concurrencyPolicy, schedule
- **Tradução:** tarefa agendada (só como apoio)
- **Classe ontológica:** objeto da API
- **API:** `apiVersion: batch/v1`, `kind: CronJob`
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** namespaced
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-08.
- **Pendências:** os campos de histórico (`successfulJobsHistoryLimit`, `failedJobsHistoryLimit`) e o fuso (`timeZone`) não foram detalhados; confirmar com `oc explain cronjob.spec`.

</details>
