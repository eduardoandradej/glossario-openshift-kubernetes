# NUMA

## Definição em uma frase

NUMA (*Non-Uniform Memory Access*) é a arquitetura de servidores em que **cada processador tem a sua própria região de memória local**, mais rápida de acessar que a memória dos outros processadores. No Kubernetes, alinhar CPU, memória e dispositivos na mesma região NUMA melhora o desempenho de cargas sensíveis à latência.

## Explicação didática

Num servidor com dois soquetes, cada CPU tem a sua "memória perto". Se um processo roda na CPU do soquete 0 mas usa memória ou uma placa de rede ligada ao soquete 1, cada acesso atravessa a ligação entre os soquetes e fica mais lento. Para a maioria das aplicações isso é irrelevante; para telecomunicações, finanças e computação científica, faz diferença.

## Para que existe e qual problema resolve

Evita alocações espalhadas entre regiões NUMA, que adicionam latência e tornam o desempenho imprevisível.

## Funcionamento técnico e ciclo de vida

- **Topology Manager (kubelet):** componente do kubelet que coordena as decisões de alocação dos gerenciadores de CPU e de dispositivos, para que fiquem na mesma região NUMA. Antes dele, essas decisões eram independentes e podiam espalhar os recursos.
- **Limite do scheduler padrão:** segundo a documentação do OCP, o scheduler padrão considera os recursos do **nó inteiro**, e não de cada região NUMA. Com a política mais restritiva do Topology Manager, isso pode gerar erros de admissão como `Topology Affinity Error`, com Pods criados repetidamente.
- **No OpenShift:** o **NUMA Resources Operator** implanta um *scheduler secundário* que sabe de NUMA e as peças de apoio:
  - API **`NodeResourceTopology`**, que descreve os recursos de cada região NUMA por nó;
  - *node topology exporter*, que publica esses recursos a partir da API **`PodResources`** do kubelet.
- Combinado com o *performance profile* do Node Tuning Operator, permite configurar a afinidade de CPU para cargas sensíveis à latência.

## Relações e dependências

- Envolve o [kubelet](../../01-arquitetura-e-control-plane/verbetes/kubelet.md) (Topology Manager), [HugePages](hugepages.md), [Device Plugins](device-plugin.md) e a [QoS Class](qos-class.md) `Guaranteed` (necessária para CPUs exclusivas).
- O scheduler NUMA é um agendador adicional ao [kube-scheduler](../../01-arquitetura-e-control-plane/verbetes/kube-scheduler.md).

## Exemplo de situação real

Uma função de rede virtualizada perde pacotes sob carga. A análise mostra CPUs de um soquete e a placa de rede de outro. Com Topology Manager e o scheduler NUMA, os Pods passam a receber CPU, memória e placa do mesmo soquete.

## Como visualizar e inspecionar (somente leitura)

```bash
# A API de topologia NUMA existe? (depende do NUMA Resources Operator)
oc api-resources | grep -i noderesourcetopolog

# Topologia NUMA por nó (somente se a API existir)
oc get noderesourcetopologies

# Pods recusados por alinhamento de topologia
oc get events -A --field-selector reason=TopologyAffinityError
```

## Como interpretar a saída

- API ausente: o NUMA Resources Operator não está instalado, que é o normal fora de clusters de alto desempenho.
- Eventos `TopologyAffinityError` indicam Pods que o kubelet não conseguiu alinhar no nó escolhido.

## Diferenças e confusões frequentes

- **Nó NUMA × Node do Kubernetes:** a "região NUMA" (às vezes chamada de nó NUMA) é parte de **uma** máquina; o Node é a máquina inteira.
- **Topology Manager × scheduler NUMA:** o primeiro decide **dentro** do nó; o segundo escolhe o nó levando NUMA em conta.

## No OpenShift 4.22 versus Kubernetes

O Topology Manager é do Kubernetes. O NUMA Resources Operator, o scheduler secundário e o `NodeResourceTopology` fazem parte das soluções do OpenShift para cargas de alto desempenho (categoria 11).

## No HomeLab SNO

**Não aplicável na prática:** uma VM pequena num KVM costuma ter uma única região NUMA, e o Operator não está instalado.

## Termos relacionados

[HugePages](hugepages.md) · [Device Plugin](device-plugin.md) · [QoS Class](qos-class.md) · [kubelet](../../01-arquitetura-e-control-plane/verbetes/kubelet.md) · [kube-scheduler](../../01-arquitetura-e-control-plane/verbetes/kube-scheduler.md)

## Fontes oficiais

- Kubernetes — Control Topology Management Policies on a node (Topology Manager): <https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/> (fonte: `kubernetes/website` `release-1.35`, `tasks/administer-cluster/topology-manager.md`)
- OCP 4.22 — Scheduling NUMA-aware workloads, "About NUMA-aware scheduling" (fontes: `scalability_and_performance/cnf-numa-aware-scheduling.adoc`, `modules/cnf-about-numa-aware-scheduling.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/numa
- **Termo original:** NUMA (Non-Uniform Memory Access)
- **Remissões:** Topology Manager, NUMA Resources Operator, NodeResourceTopology
- **Tradução:** acesso não uniforme à memória (só como apoio)
- **Classe ontológica:** conceito (arquitetura de hardware) / recurso opcional (Operator)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** Topology Manager nativo; scheduler NUMA depende do NUMA Resources Operator
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** avançado
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** o `reason` `TopologyAffinityError` do evento foi derivado da mensagem "Topology Affinity Error" da documentação; confirmar o texto exato. O nome do recurso `noderesourcetopologies` deve ser confirmado num cluster com o Operator.

</details>
