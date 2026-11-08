# Init Container

## Definição em uma frase

Um Init Container é um **contêiner que roda até o fim antes dos contêineres da aplicação**, em sequência, para preparar o que o [Pod](pod.md) precisa: esperar uma dependência, gerar configuração, ajustar arquivos num volume.

## Explicação didática

Pense numa cozinha antes da abertura: alguém confere o gás, outro organiza os ingredientes, e só então o restaurante abre. Os init containers são essas tarefas de preparação; a aplicação só começa quando **todas** terminam com sucesso.

- Ficam em `spec.initContainers`.
- Rodam **um por vez**, na ordem declarada.
- Cada um precisa **terminar com sucesso** para o próximo começar.

## Para que existe e qual problema resolve

- Separa a preparação da aplicação: a imagem principal não precisa carregar ferramentas usadas só na inicialização.
- Permite **atrasar** a aplicação até uma condição ser atendida (por exemplo, um Service responder).
- Pode ter permissões ou acesso a Secrets que a aplicação não deveria ter.

## Funcionamento técnico e ciclo de vida

- Se um init container falha, o kubelet o reinicia até ter sucesso, conforme a [Restart Policy](restart-policy.md) do Pod. Com `restartPolicy: Never`, a falha marca o Pod como `Failed`.
- Enquanto rodam, o Pod fica `Pending`, e a condição `Initialized` fica `False`. O `oc get pods` mostra `Init:N/M`.
- **Não suportam** `lifecycle`, `livenessProbe`, `readinessProbe` nem `startupProbe` (ao contrário dos sidecars).
- Recursos: o pedido efetivo do Pod considera o maior pedido entre os init containers ou a soma dos contêineres da aplicação, o que for maior.
- Devem ser **idempotentes**: podem rodar de novo, por exemplo, se o Pod for reiniciado.

## Relações e dependências

- Variante: [Sidecar Container](sidecar-container.md) (init container com `restartPolicy: Always`, que continua rodando).
- Etapa do [Pod Lifecycle](pod-lifecycle.md); refletido na [Pod Condition](pod-condition.md) `Initialized`.

## Exemplo de situação real

Um Pod fica em `Init:0/1` há minutos. O init container espera o DNS de um Service de banco que ainda não existe. `oc logs <pod> -c <init>` mostra as tentativas, e criar o Service destrava o Pod.

## Como visualizar e inspecionar (somente leitura)

```bash
# Init containers declarados
oc get pod <nome> -n <namespace> -o jsonpath='{range .spec.initContainers[*]}{.name}{"\n"}{end}'

# Estado de cada init container
oc get pod <nome> -n <namespace> -o jsonpath='{range .status.initContainerStatuses[*]}{.name}: {.state}{"\n"}{end}'

# Logs de um init container
oc logs <nome> -n <namespace> -c <init-container>
```

## Como interpretar a saída

- `Init:0/2`: nenhum dos dois concluiu ainda.
- `Init:Error` ou `Init:CrashLoopBackOff`: um init container falha repetidamente.
- `PodInitializing`: init containers concluídos; a aplicação está iniciando.

## Diferenças e confusões frequentes

- **Init container × sidecar:** o init termina antes da aplicação; o sidecar continua rodando ao lado dela.
- **Init container × postStart:** o hook `postStart` roda dentro do contêiner da aplicação, sem garantia de ordem em relação ao processo principal.

## No OpenShift 4.22 versus Kubernetes

Mesmo comportamento do Kubernetes 1.35. Os init containers seguem as mesmas SCCs do Pod.

## No HomeLab SNO

Vários Pods do próprio OpenShift usam init containers; `oc get pods -A | grep Init` mostra quem está preso na inicialização.

## Termos relacionados

[Sidecar Container](sidecar-container.md) · [Pod Lifecycle](pod-lifecycle.md) · [Pod Condition](pod-condition.md) · [Restart Policy](restart-policy.md) · [Container](container.md)

## Fontes oficiais

- Kubernetes — Init Containers: <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/> (fonte: `kubernetes/website` `release-1.35`, `concepts/workloads/pods/init-containers.md`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/init-container
- **Termo original:** init container (`spec.initContainers`)
- **Remissões:** Init:N/M, PodInitializing
- **Tradução:** contêiner de inicialização (só como apoio)
- **Classe ontológica:** componente do Pod (campo de configuração)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-08.
- **Pendências:** os textos `Init:N/M`, `Init:Error` e `PodInitializing` são exibição do cliente; confirmar no SNO.

</details>
