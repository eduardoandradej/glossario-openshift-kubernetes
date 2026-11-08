# Pod Phase

## Definição em uma frase

A Pod Phase (`status.phase`) é o **resumo de alto nível de onde o Pod está no ciclo de vida**, com cinco valores possíveis: `Pending`, `Running`, `Succeeded`, `Failed` e `Unknown`.

## Explicação didática

| Fase | Significado |
|---|---|
| **Pending** | Aceito pelo cluster, mas algum contêiner ainda não está pronto para rodar. Inclui a espera pelo agendamento e o download de imagens |
| **Running** | Agendado num nó, com todos os contêineres criados; ao menos um está rodando, iniciando ou reiniciando |
| **Succeeded** | Todos os contêineres terminaram com sucesso e não serão reiniciados |
| **Failed** | Todos os contêineres terminaram, e ao menos um falhou (saída diferente de zero ou encerrado pelo sistema) e não será reiniciado |
| **Unknown** | O estado do Pod não pôde ser obtido, normalmente por falha de comunicação com o nó |

Remissões: **Pending** e **Running** são fases; **Completed** é como o `oc get pods` mostra, na coluna `STATUS`, um Pod na fase `Succeeded`.

## Para que existe e qual problema resolve

Dá uma leitura rápida e estável do estado geral do Pod.

## Funcionamento técnico e ciclo de vida

- A fase **não é** uma máquina de estados completa nem o resumo de todas as observações. A documentação pede para não presumir nada além do que está descrito para cada valor.
- **Fase × coluna `STATUS`:** a coluna do `oc get pods` é um campo de exibição do cliente. Ela pode mostrar `CrashLoopBackOff`, `ImagePullBackOff` ou `Terminating`, que **não são fases**. A documentação pede para não confundir as duas.
- Pods que usam a fase de forma antiga (sem condições) são o padrão "phase", que as convenções da API desaconselham para tipos novos. Ver [Conditions](../../00-fundamentos-e-linguagem/verbetes/conditions.md).

## Relações e dependências

- Parte do [Pod Lifecycle](pod-lifecycle.md); detalhada por [Pod Condition](pod-condition.md) e [Container Lifecycle](container-lifecycle.md).
- `Succeeded` é o final esperado dos Pods de [Job](job.md).

## Exemplo de situação real

Um Pod aparece como `CrashLoopBackOff` em `oc get pods`, mas `status.phase` é `Running`. Não há contradição: o Pod está em execução, e um dos seus contêineres está num ciclo de falhas e reinícios.

## Como visualizar e inspecionar (somente leitura)

```bash
# Fase real de cada Pod
oc get pods -n <namespace> -o custom-columns=POD:.metadata.name,PHASE:.status.phase

# Pods numa fase específica
oc get pods -n <namespace> --field-selector=status.phase=Pending
```

## Como interpretar a saída

- `Pending` duradouro: agendamento ou preparação (imagem, volumes, init containers). Veja os Events.
- `Failed` com `reason: Evicted`: despejado por pressão no nó.
- `Unknown`: problema de comunicação com o nó, e não com a aplicação.

## Diferenças e confusões frequentes

- **Phase × STATUS do `oc get pods`:** dado da API × exibição do cliente.
- **Completed × Succeeded:** o mesmo estado, em nomes diferentes (exibição × fase).

## No OpenShift 4.22 versus Kubernetes

Mesmos valores do Kubernetes 1.35.

## No HomeLab SNO

`--field-selector=status.phase=Pending` é uma forma rápida de encontrar o que não sobe no nó único.

## Termos relacionados

[Pod Lifecycle](pod-lifecycle.md) · [Pod Condition](pod-condition.md) · [Container Lifecycle](container-lifecycle.md) · [CrashLoopBackOff](crashloopbackoff.md) · [Terminating](terminating.md) · [Job](job.md)

## Fontes oficiais

- Kubernetes — Pod Lifecycle, "Pod phase": <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase> (fonte: `kubernetes/website` `release-1.35`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/pod-phase
- **Termo original:** Pod phase (`status.phase`)
- **Remissões:** Pending, Running, Succeeded, Failed, Unknown, Completed
- **Tradução:** fase do Pod (só como apoio)
- **Classe ontológica:** estado
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-08.
- **Pendências:** a associação "Completed = Succeeded" na coluna `STATUS` é o comportamento conhecido do cliente; confirmar no SNO com um Job.

</details>
