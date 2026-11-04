# cloud-controller-manager

## Definição em uma frase

O cloud-controller-manager é o componente do [Control Plane](control-plane.md) que **embute a lógica específica do provedor de nuvem**: ele liga o cluster à API da nuvem e separa o que conversa com a nuvem do que só conversa com o cluster.

## Explicação didática

Algumas tarefas dependem de onde o cluster roda: descobrir quando uma VM foi apagada na nuvem, criar um balanceador de carga para um Service `LoadBalancer`, configurar rotas. Essa lógica fica num componente à parte, para que cada provedor evolua no seu ritmo, sem depender do ciclo do Kubernetes principal.

## Para que existe e qual problema resolve

Desacopla o núcleo do Kubernetes das integrações com cada nuvem, usando um mecanismo de *plugins* por provedor.

## Funcionamento técnico e ciclo de vida

- Roda no Control Plane como um conjunto replicado de processos, geralmente contêineres em Pods. Cada CCM implementa vários controllers num processo só; também pode rodar como *addon*.
- Controllers típicos: **node controller** (atualiza os objetos Node conforme os servidores da nuvem), além dos de rotas e de serviços (balanceadores).
- **No OpenShift:** o **Cloud Controller Manager Operator** gerencia e atualiza os CCMs. A documentação do 4.22 o lista como GA em AWS, Google Cloud, IBM Cloud, Azure (global e Azure Stack Hub), Nutanix, Red Hat OpenStack e VMware vSphere, e como Technology Preview em IBM Power Virtual Server.
- **Capability opcional:** com `platform` igual a `Baremetal` ou `None` no `install-config.yaml` (ou `External` com `cloudControllerManager: None`), é possível **desabilitar** a capability `CloudControllerManager`.

## Relações e dependências

- Complementa o [kube-controller-manager](kube-controller-manager.md).
- Afeta Services do tipo `LoadBalancer` (categoria 04) e o ciclo de vida dos Nodes (categoria 02).

## Exemplo de situação real

Num cluster em bare metal sem integração de nuvem, um Service `LoadBalancer` fica com `EXTERNAL-IP` em `<pending>` para sempre: não há CCM nem outra solução (como MetalLB) para provisionar o IP externo.

## Como visualizar e inspecionar (somente leitura)

```bash
# OpenShift: o Operator existe e está saudável?
oc get clusteroperator cloud-controller-manager

# Plataforma do cluster (determina se o CCM faz sentido)
oc get infrastructure cluster -o jsonpath='{.status.platformStatus.type}{"\n"}'

# Capabilities habilitadas
oc get clusterversion version -o jsonpath='{.status.capabilities.enabledCapabilities}{"\n"}'
```

## Como interpretar a saída

- `platformStatus.type` igual a `None` ou `BareMetal`: em geral **não há** CCM de nuvem atuando. O ClusterOperator pode existir sem fazer nada relevante, ou a capability pode estar desabilitada.
- `CloudControllerManager` ausente da lista de capabilities habilitadas: o componente foi desabilitado na instalação.
- Erro `NotFound` em `oc get clusteroperator cloud-controller-manager` é coerente com capability desabilitada. Não é falha.

## Diferenças e confusões frequentes

- **CCM ≠ kube-controller-manager:** lógica de nuvem × controllers genéricos.
- **"Não tem CCM" ≠ cluster quebrado:** em bare metal é normal.
- **CCM ≠ Machine API:** a Machine API cria e apaga máquinas; o CCM integra Nodes e serviços com a nuvem.

## No OpenShift 4.22 versus Kubernetes

O OpenShift empacota o CCM por plataforma e o gerencia por Operator, controlado como *capability* da instalação.

## No HomeLab SNO

Um SNO em KVM costuma ter plataforma `None`: não espere CCM nem Services `LoadBalancer` funcionando sem uma solução extra. Confira com o comando de `infrastructure`.

## Termos relacionados

[kube-controller-manager](kube-controller-manager.md) · [Control Plane](control-plane.md) · [Controller](../../00-fundamentos-e-linguagem/verbetes/controller.md) · [Service](../../04-networking/verbetes/service.md) · [Node](../../02-compute-e-nodes/verbetes/node.md)

## Fontes oficiais

- Kubernetes — Cloud Controller Manager: <https://kubernetes.io/docs/concepts/architecture/cloud-controller/> (fonte: `kubernetes/website` `release-1.35`, `concepts/architecture/cloud-controller.md`)
- Kubernetes Glossary — cloud-controller-manager: <https://kubernetes.io/docs/reference/glossary/?all=true#term-cloud-controller-manager>
- OCP 4.22 — Cluster Operators reference / Cluster capabilities, "Cloud Controller Manager Operator" (fonte: `modules/cluster-cloud-controller-manager-operator.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 01-arquitetura-e-control-plane/cloud-controller-manager
- **Termo original:** cloud-controller-manager (CCM)
- **Remissões:** Cloud Controller Manager Operator
- **Tradução:** gerenciador de controllers de nuvem (só como apoio)
- **Classe ontológica:** componente / extensão dependente de plataforma
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** **depende da plataforma**; pode não existir em bare metal ou na plataforma `None`
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-04

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** confirmar no SNO a plataforma (`None` é uma hipótese, porque a topologia do HomeLab não foi inspecionada), o nome do ClusterOperator e o caminho `status.capabilities.enabledCapabilities`, que **não foram executados**.

</details>
