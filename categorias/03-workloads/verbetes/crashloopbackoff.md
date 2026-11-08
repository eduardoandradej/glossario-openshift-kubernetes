# CrashLoopBackOff

## Definição em uma frase

CrashLoopBackOff é o **motivo exibido quando um contêiner termina repetidamente e o kubelet espera um intervalo crescente (*backoff*) antes de reiniciá-lo de novo**; indica um ciclo de falha e reinício, não uma causa específica.

## Explicação didática

O ciclo é: o contêiner inicia, falha, o kubelet espera e tenta de novo. A cada falha, a espera dobra: 10 s, 20 s, 40 s..., até o teto de **5 minutos**. Enquanto espera, o contêiner fica em `Waiting` com `reason: CrashLoopBackOff`.

É um **sintoma**: a pergunta certa é "por que o contêiner termina?".

## Para que existe e qual problema resolve

O backoff evita que um contêiner defeituoso seja reiniciado sem pausa, gastando recursos do nó e inundando os logs.

## Funcionamento técnico e ciclo de vida

- Só acontece quando a [Restart Policy](restart-policy.md) manda reiniciar (`Always` ou `OnFailure` com falha).
- O contador de backoff zera depois que o contêiner roda bem por cerca de **10 minutos**.
- *Feature gates* alfa (`ReduceDefaultCrashLoopBackOffDecay` e `KubeletCrashLoopBackOffMax`) permitem ajustar os intervalos; não estão ativos por padrão.
- **Causas comuns:** erro da aplicação ao iniciar; configuração ausente ou errada (variáveis, ConfigMaps, Secrets); falta de recursos ([OOMKill](../../02-compute-e-nodes/verbetes/oomkill.md)); *liveness* ou *startup probes* mal ajustadas; comando de início incorreto; problema de permissão (no OpenShift, frequentemente o UID aleatório das SCCs).

## Relações e dependências

- `reason` do estado `Waiting` no [Container Lifecycle](container-lifecycle.md).
- Aparece na coluna `STATUS`, mas a [Pod Phase](pod-phase.md) costuma continuar `Running`.

## Exemplo de situação real

Uma imagem que funciona no laptop entra em CrashLoopBackOff no OpenShift. `oc logs --previous` mostra "permission denied" ao gravar num diretório da imagem. Ela pressupunha rodar como root, e o OpenShift a executa com um UID arbitrário. A correção é ajustar as permissões da imagem.

## Como visualizar e inspecionar (somente leitura)

```bash
# Por que a última execução terminou
oc get pod <nome> -n <namespace> -o jsonpath='{range .status.containerStatuses[*]}{.name}: {.lastState.terminated.reason} exit={.lastState.terminated.exitCode}{"\n"}{end}'

# Logs da execução que falhou
oc logs <nome> -n <namespace> -c <contêiner> --previous

# Eventos (falhas de probe, OOM, BackOff)
oc describe pod <nome> -n <namespace>
```

## Como interpretar a saída

- `reason: Error` e `exit` diferente de 0: a aplicação saiu com erro; leia os logs.
- `reason: OOMKilled` (exit 137): falta de memória; revise o *limit*.
- Eventos `Liveness probe failed` seguidos de `Killing`: a probe está matando o contêiner.
- `reason: Completed` em loop: o processo termina com sucesso, mas a política `Always` o reinicia. É um contêiner de tarefa num controller de serviço.

## Diferenças e confusões frequentes

- **CrashLoopBackOff × Error:** `Error` descreve uma execução que falhou; CrashLoopBackOff, a espera entre tentativas.
- **CrashLoopBackOff × [ImagePullBackOff](imagepullbackoff.md):** no primeiro, o contêiner chega a rodar; no segundo, nem a imagem foi obtida.

## No OpenShift 4.22 versus Kubernetes

Mesmo mecanismo do Kubernetes 1.35. No OpenShift, as SCCs (UID arbitrário, sem root) são uma causa frequente com imagens feitas para outras plataformas.

## No HomeLab SNO

Sempre comece por `oc logs --previous`: os logs atuais podem estar vazios, porque o contêiner ainda não reiniciou.

## Termos relacionados

[Container Lifecycle](container-lifecycle.md) · [Restart Policy](restart-policy.md) · [ImagePullBackOff](imagepullbackoff.md) · [OOMKill](../../02-compute-e-nodes/verbetes/oomkill.md) · [Pod Phase](pod-phase.md)

## Fontes oficiais

- Kubernetes — Pod Lifecycle, "Container restarts" e "How Pods handle problems with containers": <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-restarts> (fonte: `kubernetes/website` `release-1.35`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/crashloopbackoff
- **Termo original:** CrashLoopBackOff
- **Remissões:** backoff, restartCount, Error
- **Tradução:** não se traduz
- **Classe ontológica:** estado (motivo de `Waiting`)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-08.
- **Pendências:** a relação com o UID arbitrário das SCCs vem da documentação geral do OpenShift sobre imagens; conferir na categoria de segurança.

</details>
