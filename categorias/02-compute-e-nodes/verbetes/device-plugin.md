# Device Plugin

## Definição em uma frase

Um Device Plugin é um componente, normalmente um DaemonSet, que **anuncia hardware especializado ao [kubelet](../../01-arquitetura-e-control-plane/verbetes/kubelet.md)**, como GPUs, placas de rede de alto desempenho, FPGAs e adaptadores InfiniBand, e o entrega aos contêineres que o pedem.

## Explicação didática

O Kubernetes não sabe falar com cada tipo de placa. O *device plugin framework* resolve isso: o fornecedor escreve um plugin que conversa com o kubelet por **gRPC**, informa quantos dispositivos existem no nó e, quando um Pod pede um, prepara o acesso a ele dentro do contêiner. Para o usuário, o dispositivo aparece como um [Extended Resource](extended-resource.md).

## Para que existe e qual problema resolve

Permite suportar hardware de qualquer fornecedor **sem alterar o código do Kubernetes**.

## Funcionamento técnico e ciclo de vida

1. O plugin roda no nó (instalado manualmente ou como DaemonSet).
2. Ele se **registra** no kubelet pelo serviço gRPC `Registration`, informando o *socket* Unix e a versão da API de device plugin.
3. Ele informa os dispositivos disponíveis e a saúde deles; o kubelet anuncia o recurso no `status` do nó.
4. Quando um contêiner que pede o recurso é criado, o kubelet pede ao plugin que aloque o dispositivo e prepare o acesso.

## Relações e dependências

- Anuncia [Extended Resources](extended-resource.md); conversa com o [kubelet](../../01-arquitetura-e-control-plane/verbetes/kubelet.md).
- Coordenado com a localidade de hardware pelo Topology Manager (ver [NUMA](numa.md)).

## Exemplo de situação real

Depois de instalar o Operator de GPU de um fornecedor, os nós com GPU passam a mostrar `nvidia.com/gpu` em `allocatable`. Quem anunciou o recurso foram os Pods do device plugin implantados pelo Operator, como DaemonSet.

## Como visualizar e inspecionar (somente leitura)

```bash
# DaemonSets de device plugins (o nome varia por fornecedor)
oc get daemonsets -A | grep -i -E 'device-plugin|gpu'

# Recursos estendidos anunciados no nó
oc get node <nó> -o jsonpath='{.status.allocatable}{"\n"}'
```

## Como interpretar a saída

- Pods do device plugin em `Running` em cada nó com o hardware, e o recurso correspondente em `allocatable`, significam que o anúncio está funcionando.
- Recurso ausente com o plugin rodando: veja os logs do plugin, que podem indicar falta de driver ou de dispositivo.

## Diferenças e confusões frequentes

- **Device plugin × driver:** o driver opera o hardware no kernel; o plugin integra o dispositivo ao kubelet.
- **Device plugin × DRA:** a *Dynamic Resource Allocation* é um mecanismo mais novo e flexível de alocação de dispositivos (no OCP 4.22, há documentação de GPUs por DRA).

## No OpenShift 4.22 versus Kubernetes

O framework é o mesmo. No OpenShift, os plugins geralmente vêm por Operators certificados de fornecedores (categoria 16).

## No HomeLab SNO

Sem hardware especial, não há device plugins para observar.

## Termos relacionados

[Extended Resource](extended-resource.md) · [kubelet](../../01-arquitetura-e-control-plane/verbetes/kubelet.md) · [NUMA](numa.md) · [DaemonSet](../../03-workloads/verbetes/daemonset.md)

## Fontes oficiais

- Kubernetes — Device Plugins: <https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/> (fonte: `kubernetes/website` `release-1.35`, `concepts/extend-kubernetes/compute-storage-net/device-plugins.md`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/device-plugin
- **Termo original:** device plugin
- **Remissões:** device plugin framework
- **Tradução:** plugin de dispositivo (só como apoio)
- **Classe ontológica:** componente (extensão do kubelet)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável (roda em cada nó com o hardware)
- **Disponibilidade:** opcional; depende do fornecedor do hardware
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** avançado
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** o passo de alocação foi resumido; os detalhes do protocolo (`ListAndWatch`, `Allocate`) estão na página do Kubernetes e não foram lidos por inteiro. Detalhar DRA na categoria 16.

</details>
