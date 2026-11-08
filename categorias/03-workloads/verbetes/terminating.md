# Terminating

## Definição em uma frase

Terminating é **como o cliente exibe um [Pod](pod.md) (ou outro objeto) que já recebeu o pedido de remoção e está em encerramento**; não é uma [Pod Phase](pod-phase.md), mas a consequência de `metadata.deletionTimestamp` estar preenchido.

## Explicação didática

Ao apagar um Pod, ele não some na hora. A API marca o objeto com um `deletionTimestamp`, e o `oc get pods` passa a mostrar `Terminating` na coluna `STATUS`, durante o [Termination Grace Period](termination-grace-period.md) e o trabalho dos [Finalizers](../../00-fundamentos-e-linguagem/verbetes/finalizer.md), se houver.

## Para que existe e qual problema resolve

Torna visível que o objeto está **saindo**: ele pode ainda estar rodando e não deve receber tráfego novo.

## Funcionamento técnico e ciclo de vida

- Um Pod fica `Terminating` enquanto os contêineres encerram ou, se houver finalizers, até que todos sejam removidos.
- **Pod preso em Terminating:** causas comuns são um nó que não responde (o kubelet não confirma o término), um finalizer que nenhum controller remove ou uma aplicação demorada dentro de um grace period longo.
- O mesmo nome aparece para Namespaces em remoção (`status.phase: Terminating`, nesse caso de fato uma fase do Namespace).

## Relações e dependências

- Dura o [Termination Grace Period](termination-grace-period.md); pode ser prolongado por [Finalizers](../../00-fundamentos-e-linguagem/verbetes/finalizer.md).

## Exemplo de situação real

Depois de uma falha de nó, os Pods dele ficam `Terminating` por muito tempo. O kubelet não pode confirmar o fim dos contêineres. Com o nó definitivamente perdido, remover o objeto Node ou forçar a remoção dos Pods libera os controllers, com cuidado redobrado em StatefulSets.

## Como visualizar e inspecionar (somente leitura)

```bash
# Desde quando o Pod está em encerramento, e finalizers pendentes
oc get pod <nome> -n <namespace> -o jsonpath='deletion={.metadata.deletionTimestamp} finalizers={.metadata.finalizers}{"\n"}'

# Em que nó está e se o nó está Ready
oc get pod <nome> -n <namespace> -o jsonpath='{.spec.nodeName}{"\n"}'
oc get node <nó>
```

## Como interpretar a saída

- `deletionTimestamp` antigo e nó `NotReady`: o nó não confirma o término.
- `finalizers` não vazio com o nó saudável: algum controller ainda não concluiu a limpeza.

## Diferenças e confusões frequentes

- **Terminating do Pod × do Namespace:** exibição para o Pod; fase real para o Namespace.
- **Terminating × Failed/Succeeded:** essas são fases terminais; Terminating é um processo em curso.

## No OpenShift 4.22 versus Kubernetes

Mesmo comportamento do Kubernetes 1.35.

## No HomeLab SNO

Não remova finalizers à força para "destravar" objetos: entenda primeiro qual controller deveria removê-los.

## Termos relacionados

[Termination Grace Period](termination-grace-period.md) · [Finalizer](../../00-fundamentos-e-linguagem/verbetes/finalizer.md) · [Pod Phase](pod-phase.md) · [Pod Lifecycle](pod-lifecycle.md) · [Node](../../02-compute-e-nodes/verbetes/node.md)

## Fontes oficiais

- Kubernetes — Pod Lifecycle, "Termination of Pods" (nota sobre o `Terminating` exibido pelo kubectl): <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination> (fonte: `kubernetes/website` `release-1.35`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/terminating
- **Termo original:** Terminating
- **Remissões:** deletionTimestamp, stuck Terminating
- **Tradução:** em encerramento (só como apoio)
- **Classe ontológica:** estado (exibição do cliente)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-08.
- **Pendências:** a fase `Terminating` do Namespace é conhecida da API core; não conferida nesta rodada.

</details>
