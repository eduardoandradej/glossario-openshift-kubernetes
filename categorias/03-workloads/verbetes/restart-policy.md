# Restart Policy

## Definição em uma frase

A Restart Policy (`spec.restartPolicy`) define **se o kubelet deve reiniciar os contêineres de um [Pod](pod.md) quando eles terminam**: sempre (`Always`), só em caso de falha (`OnFailure`) ou nunca (`Never`).

## Explicação didática

| Valor | O kubelet reinicia o contêiner... | Uso típico |
|---|---|---|
| `Always` (padrão) | Sempre que ele termina, com sucesso ou não | Serviços de longa duração ([Deployment](deployment.md), [StatefulSet](statefulset.md), [DaemonSet](daemonset.md)) |
| `OnFailure` | Só quando sai com erro (código diferente de zero) | [Jobs](job.md) que devem tentar de novo no mesmo Pod |
| `Never` | Nunca | Jobs em que cada falha deve gerar um Pod novo, tarefas avulsas |

A política vale para o Pod inteiro: contêineres de aplicação e [init containers](init-container.md) regulares.

## Para que existe e qual problema resolve

Separa dois tipos de carga: as que **nunca deveriam parar** (serviços) e as que **devem terminar** (tarefas). Sem ela, um Job concluído seria reiniciado sem fim.

## Funcionamento técnico e ciclo de vida

- O reinício é **local**: o kubelet recria o contêiner **no mesmo Pod e no mesmo nó**. O `restartCount` aumenta.
- Os reinícios seguem um *backoff* exponencial (10 s, 20 s, 40 s..., até 5 minutos). Enquanto espera, o contêiner fica em [CrashLoopBackOff](crashloopbackoff.md).
- **Restrições dos controllers:** o template de um Deployment só aceita `Always`; Jobs aceitam `OnFailure` ou `Never`.
- **Sidecars:** um [Sidecar Container](sidecar-container.md) é um init container com `restartPolicy: Always` **no próprio contêiner**, e é reiniciado independentemente da política do Pod.
- Regras de reinício por contêiner, mais finas, existem atrás do *feature gate* `ContainerRestartRules`, não ativo por padrão.

## Relações e dependências

- Define a transição `Terminated` → `Waiting` no [Container Lifecycle](container-lifecycle.md).
- Determina se o Pod chega a `Succeeded`/`Failed` na [Pod Phase](pod-phase.md).

## Exemplo de situação real

Um Job de migração com `restartPolicy: OnFailure` falha por indisponibilidade momentânea do banco. O kubelet reinicia o contêiner no mesmo Pod, e a segunda tentativa conclui. Com `Never`, o controller do Job criaria um Pod novo a cada tentativa.

## Como visualizar e inspecionar (somente leitura)

```bash
# Política do Pod e reinícios por contêiner
oc get pod <nome> -n <namespace> -o jsonpath='policy={.spec.restartPolicy}{"\n"}{range .status.containerStatuses[*]}{.name} restarts={.restartCount}{"\n"}{end}'

# Documentação do campo
oc explain pod.spec.restartPolicy
```

## Como interpretar a saída

- `restartCount` alto com `Always`: aplicação caindo repetidamente; veja os logs `--previous`.
- Pod `Completed` com `Never` ou `OnFailure`: término normal de tarefa.

## Diferenças e confusões frequentes

- **Reiniciar contêiner × recriar Pod:** a Restart Policy só reinicia contêineres; recriar Pods é papel dos controllers.
- **`restartPolicy` do Pod × do contêiner:** no contêiner, o campo só existe para sidecars (init containers).

## No OpenShift 4.22 versus Kubernetes

Mesmo comportamento do Kubernetes 1.35.

## No HomeLab SNO

Um `restartCount` crescente em Pods do sistema é sinal de problema no nó; vale observar sem intervir.

## Termos relacionados

[Container Lifecycle](container-lifecycle.md) · [CrashLoopBackOff](crashloopbackoff.md) · [Job](job.md) · [Deployment](deployment.md) · [Sidecar Container](sidecar-container.md) · [Init Container](init-container.md)

## Fontes oficiais

- Kubernetes — Pod Lifecycle, "Container restart policy" e "How Pods handle problems with containers": <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy> (fonte: `kubernetes/website` `release-1.35`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/restart-policy
- **Termo original:** restart policy (`spec.restartPolicy`)
- **Remissões:** Always, OnFailure, Never, restartCount
- **Tradução:** política de reinício (só como apoio)
- **Classe ontológica:** campo de configuração
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-08.
- **Pendências:** estado do *feature gate* `ContainerRestartRules` no OCP 4.22 não conferido.

</details>
