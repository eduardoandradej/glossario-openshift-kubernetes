# Infrastructure Node

## Definição em uma frase

Um Infrastructure Node (*infra node*) é um nó de compute dedicado a rodar **apenas componentes de infraestrutura do cluster** (router, registry, monitoramento, logging...), separando essas cargas das aplicações.

## Explicação didática

Não existe um tipo especial de máquina "infra": é um worker com a **label de papel `infra`**, geralmente com *taints* que afastam as aplicações, para onde se movem os componentes de suporte da plataforma. A separação tem efeito operacional (isolamento e previsibilidade) e de licenciamento, porque nós que só rodam infraestrutura não entram na conta da assinatura.

## Para que existe e qual problema resolve

- **Custo de assinatura:** segundo a documentação, as assinaturas do OpenShift já incluem o direito de rodar o Control Plane e as cargas de infraestrutura. Nós que rodam **somente** esses componentes não precisam ser contabilizados no dimensionamento.
- **Isolamento:** picos de consumo das aplicações não afetam o router, o registry ou o monitoramento.

## Funcionamento técnico e ciclo de vida

- **Criação:** normalmente por *infrastructure machine sets*, nas plataformas com Machine API, ou acrescentando a label e os taints a nós existentes.
- **Pool:** a documentação recomenda criar um **MachineConfigPool personalizado `infra`** para esses nós. Um nó com as labels `worker` e `infra` passa a ser gerenciado pelo pool `infra`. Ver [MachineConfigPool](machineconfigpool.md).
- **O que pode rodar** (exemplos da documentação, para se qualificar como infra): serviços do Control Plane do Kubernetes e do OpenShift, o router padrão, o registry integrado, o Ingress Controller baseado em HAProxy, o monitoramento (inclusive de projetos de usuário), o logging agregado e produtos como Quay, OpenShift Data Foundation, RHACM, RHACS, OpenShift GitOps, OpenShift Pipelines e Service Mesh.
- **Qualquer outro contêiner** no nó faz dele um worker comum, que entra na contagem da assinatura.
- Mover os componentes de infraestrutura para esses nós é configuração de cada componente (seletores de nó e tolerations), tratada nas categorias 04, 10 e 12.

## Relações e dependências

- É um [Worker Node](worker-node.md) com papel adicional; tem pool próprio em [MachineConfigPool](machineconfigpool.md).
- Usa [labels](../../00-fundamentos-e-linguagem/verbetes/label.md) de papel e taints (categoria 11).

## Exemplo de situação real

Um cluster de produção tem três infra nodes. O router, o registry e o monitoramento rodam só neles, e as aplicações ficam nos demais workers. Quando uma aplicação consome toda a CPU dos workers, a entrada de tráfego (router) e o monitoramento continuam saudáveis.

## Como visualizar e inspecionar (somente leitura)

```bash
# Nós com papel infra
oc get nodes -l node-role.kubernetes.io/infra

# Pool infra, se existir
oc get machineconfigpools

# Taints de um nó
oc get node <nó> -o jsonpath='{.spec.taints}{"\n"}'
```

## Como interpretar a saída

- `ROLES` com `infra,worker`: o nó tem os dois papéis, e o pool que o gerencia é o `infra`, se houver.
- Taints como `node-role.kubernetes.io/infra:NoSchedule` impedem que Pods sem toleration correspondente sejam agendados ali. Confirme os nomes usados no seu cluster.
- Sem pool `infra`, o nó continua no pool `worker`, o que a documentação desaconselha.

## Diferenças e confusões frequentes

- **Infra node × Control Plane:** o infra node é compute dedicado a serviços de suporte; não roda etcd nem API server.
- **Label `infra` × contagem de assinatura:** a documentação observa que a classificação para fins de assinatura independe do pool. O que conta é **o que roda** no nó.
- **Infra node × "nó com o router":** só mover o router não qualifica o nó se aplicações também rodarem nele.

## No OpenShift 4.22 versus Kubernetes

O conceito de papel de nó existe no Kubernetes (labels), mas a definição de infra node, o pool personalizado e as regras de assinatura são do OpenShift.

## No HomeLab SNO

**Não aplicável:** o único nó roda tudo. Estude o conceito para clusters com vários nós.

## Termos relacionados

[Worker Node](worker-node.md) · [MachineConfigPool](machineconfigpool.md) · [Label](../../00-fundamentos-e-linguagem/verbetes/label.md) · [Control Plane](control-plane.md) · [IngressController](../../04-networking/verbetes/ingresscontroller.md)

## Fontes oficiais

- OCP 4.22 — Machine management, "Creating infrastructure machine sets" e "Move components to infrastructure nodes to reduce costs": <https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/creating-infrastructure-machinesets> (fontes: `machine_management/creating-infrastructure-machinesets.adoc`, `modules/infrastructure-components.adoc`)
- OCP 4.22 — "Node configuration management with machine config pools" (pool `infra` recomendado; contagem de assinatura; fonte: `modules/architecture-machine-config-pools.adoc`)
- Red Hat — OpenShift sizing and subscription guide for enterprise Kubernetes (fonte externa à documentação do produto): <https://www.redhat.com/en/resources/openshift-subscription-sizing-guide>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 01-arquitetura-e-control-plane/infrastructure-node
- **Termo original:** infrastructure node (infra node)
- **Remissões:** infrastructure machine set
- **Tradução:** nó de infraestrutura (só como apoio)
- **Classe ontológica:** conceito (papel de nó)
- **Plataforma:** OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** opcional (criado pelo administrador)
- **Versões validadas:** OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-05

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-05.
- **Pendências:** o nome do taint `node-role.kubernetes.io/infra` é o usado nos exemplos de infra machine sets, mas **não foi conferido** nos módulos lidos; validar na documentação "Creating an infrastructure node". A URL publicada está **a verificar**.

</details>
