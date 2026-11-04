# kube-controller-manager

> **ID:** 01-arquitetura-e-control-plane/kube-controller-manager | **Termo original:** kube-controller-manager | **Remissões:** controller manager, KCM | **Tradução:** gerenciador de controllers (só como apoio) | **Classe ontológica:** componente | **Plataforma:** Kubernetes / OpenShift | **Escopo:** não aplicável (roda no Control Plane) | **Disponibilidade:** nativo | **Versões validadas:** Kubernetes 1.35 / OCP 4.22 | **Nível:** intermediário | **Atualizado em:** 2026-11-04

## Definição em uma frase

O kube-controller-manager é o componente do [Control Plane](control-plane.md) que **roda os controllers nativos** do Kubernetes, como os de Deployment, ReplicaSet, Job, Namespace e ServiceAccount.

## Explicação didática

Cada [Controller](../../00-fundamentos-e-linguagem/verbetes/controller.md) é um control loop independente. Para simplificar a operação, os controllers nativos são **compilados num único binário** e rodam **num único processo**: o kube-controller-manager. Logicamente são muitos; fisicamente, um só.

## Para que existe e qual problema resolve

É o "motor" da [Reconciliation](../../00-fundamentos-e-linguagem/verbetes/reconciliation.md) para os tipos nativos: sem ele, Deployments não criariam ReplicaSets, ReplicaSets não manteriam Pods e Namespaces apagados não seriam esvaziados.

## Funcionamento técnico e ciclo de vida

- Observa a API (*watch*) e age pela API; segundo a documentação do OpenShift, ele vigia mudanças em objetos como os de replicação, namespace e service account e usa a API para impor o estado especificado.
- **Eleição de líder:** com várias réplicas (uma por nó de Control Plane), **só uma fica ativa** de cada vez; as outras aguardam para assumir.
- Inclui também o **garbage collector** de objetos. Ver [Garbage Collection](../../00-fundamentos-e-linguagem/verbetes/garbage-collection.md).
- **No OpenShift:** gerenciado pelo Operator `kube-controller-manager`, roda como [Static Pod](static-pod.md) no namespace `openshift-kube-controller-manager`. O OpenShift tem ainda um **OpenShift controller manager** separado, para objetos do OpenShift.

## Relações e dependências

- Hospeda [Controllers](../../00-fundamentos-e-linguagem/verbetes/controller.md) nativos; fala com o [API Server](../../00-fundamentos-e-linguagem/verbetes/api-server.md).
- Contraparte para nuvem: [cloud-controller-manager](cloud-controller-manager.md).

## Exemplo de situação real

Depois de um problema no Control Plane, Deployments param de reagir: escalar não cria Pods novos. `oc get clusteroperator kube-controller-manager` mostra `DEGRADED=True`. Sem o processo líder ativo, nenhum controller nativo reconcilia.

## Como visualizar e inspecionar (somente leitura)

```bash
# OpenShift: saúde do Operator
oc get clusteroperator kube-controller-manager

# Pods do componente (mirror Pods de Static Pods; apenas observar)
oc get pods -n openshift-kube-controller-manager

# Eventos emitidos por controllers nativos num namespace
oc get events -n <namespace> --sort-by=.lastTimestamp
```

## Como interpretar a saída

- Pods `kube-controller-manager-<nó>` em `Running` (um por nó de Control Plane) são as réplicas; só uma é líder.
- Eventos com origem `deployment-controller`, `replicaset-controller` e similares mostram os controllers nativos em ação.
- Pods `installer-*` e `revision-pruner-*` `Completed` no namespace são parte normal da troca de revisões.

## Diferenças e confusões frequentes

- **kube-controller-manager ≠ OpenShift controller manager:** controllers nativos do Kubernetes × controllers dos objetos do OpenShift.
- **kube-controller-manager ≠ cloud-controller-manager:** o segundo concentra a lógica que depende do provedor de nuvem.
- **Controller manager ≠ Operator:** o KCM roda controllers nativos; Operators rodam os seus próprios controllers como Pods.

## No OpenShift 4.22 versus Kubernetes

Mesmo componente, com ciclo de vida automatizado por Operator e revisões de Static Pod gerenciadas pelos Pods `installer-*`.

## No HomeLab SNO

Uma única réplica: se ela reiniciar, a reconciliação dos tipos nativos pausa por alguns instantes. Não há outra para assumir.

## Termos relacionados

[Controller](../../00-fundamentos-e-linguagem/verbetes/controller.md) · [Control Plane](control-plane.md) · [cloud-controller-manager](cloud-controller-manager.md) · [Static Pod](static-pod.md) · [Garbage Collection](../../00-fundamentos-e-linguagem/verbetes/garbage-collection.md)

## Fontes oficiais

- Kubernetes Glossary — kube-controller-manager: <https://kubernetes.io/docs/reference/glossary/?all=true#term-kube-controller-manager> (fonte: `kubernetes/website` `release-1.35`)
- Kubernetes — Controllers, "Ways of running controllers": <https://kubernetes.io/docs/concepts/architecture/controller/>
- OCP 4.22 — Control plane architecture, "Machine roles" (um líder ativo; OpenShift controller manager): <https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/architecture/control-plane>

<details>
<summary>Notas de revisão</summary>

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** a localização do garbage collector dentro do KCM é conhecida da arquitetura do Kubernetes, mas **não foi citada** nas páginas lidas; conferir na referência do `kube-controller-manager`.

</details>
