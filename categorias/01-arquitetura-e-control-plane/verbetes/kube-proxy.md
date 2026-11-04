# kube-proxy

## Definição em uma frase

O kube-proxy é um proxy de rede que roda em cada nó e **implementa parte do conceito de [Service](../../04-networking/verbetes/service.md)**: ele mantém regras de rede que levam o tráfego destinado a um Service até os Pods que estão por trás dele.

## Explicação didática

Um Service tem um IP virtual estável (ClusterIP), mas nenhum processo "escuta" nesse IP. Alguém precisa programar os nós para que um pacote enviado ao ClusterIP chegue a um dos Pods certos. No Kubernetes tradicional, esse alguém é o kube-proxy: ele observa Services e EndpointSlices e escreve regras na camada de filtragem de pacotes do sistema operacional. Se essa camada não estiver disponível, ele mesmo encaminha o tráfego.

## Para que existe e qual problema resolve

Transforma o objeto Service, que é só uma declaração na API, em comportamento real de rede em todos os nós.

## Funcionamento técnico e ciclo de vida

- Observa Services e EndpointSlices pela API.
- Em cada nó, escreve as regras correspondentes e as atualiza quando os Pods mudam.
- A documentação do Kubernetes 1.35 o classifica como **opcional**: se o plugin de rede já implementa o encaminhamento de pacotes dos Services com comportamento equivalente, o kube-proxy não é necessário.

## Relações e dependências

- Implementa [Service](../../04-networking/verbetes/service.md) junto com os EndpointSlices (categoria 04).
- Alternativa no OpenShift: o [OVN-Kubernetes](ovn-kubernetes.md), que implementa os Services pelo próprio plugin.

## Exemplo de situação real

Num Kubernetes genérico, Services param de responder num nó específico enquanto os Pods estão saudáveis. A causa está no kube-proxy daquele nó (parado ou com regras desatualizadas), e não na aplicação.

## Como visualizar e inspecionar (somente leitura)

```bash
# Há Pods de kube-proxy neste cluster?
oc get pods -A -l k8s-app=kube-proxy

# Qual plugin de rede o cluster usa (OpenShift)
oc get network.config.openshift.io cluster -o jsonpath='{.status.networkType}{"\n"}'

# Configuração do Cluster Network Operator, incluindo a opção de implantar o kube-proxy
oc explain network.operator.openshift.io.spec.deployKubeProxy
```

## Como interpretar a saída

- `No resources found` na busca por kube-proxy, num OpenShift com `networkType` `OVNKubernetes`, é o esperado: os Services são implementados pelo OVN-Kubernetes.
- O campo `deployKubeProxy` existe para cenários com plugins de terceiros. Leia a descrição no `oc explain`, sem alterá-lo.

## Diferenças e confusões frequentes

- **kube-proxy ≠ proxy HTTP:** ele não inspeciona requisições de aplicação; trabalha em nível de pacotes e conexões.
- **kube-proxy ≠ router/Ingress:** a publicação externa via Route e Ingress é outro mecanismo (categoria 04).
- **"Service proxy" no OpenShift:** a documentação de papéis de máquina cita "um service proxy" em cada worker. Com OVN-Kubernetes, essa função é exercida pelo próprio plugin.

## No OpenShift 4.22 versus Kubernetes

O plugin padrão do OCP 4.22 é o **OVN-Kubernetes**, que trata do encaminhamento dos Services. Por isso, em geral, não se encontra kube-proxy num cluster OpenShift padrão.

## No HomeLab SNO

O SNO usa OVN-Kubernetes (o padrão para SNO, segundo a documentação). Use os comandos acima para confirmar; não altere a configuração do Cluster Network Operator.

## Termos relacionados

[OVN-Kubernetes](ovn-kubernetes.md) · [Service](../../04-networking/verbetes/service.md) · [Worker Node](worker-node.md) · [Cluster DNS](cluster-dns.md)

## Fontes oficiais

- Kubernetes Glossary — kube-proxy: <https://kubernetes.io/docs/reference/glossary/?all=true#term-kube-proxy> (fonte: `kubernetes/website` `release-1.35`, `reference/glossary/kube-proxy.md`)
- Kubernetes — Cluster Architecture, "kube-proxy (optional)": <https://kubernetes.io/docs/concepts/architecture/#kube-proxy>
- OCP 4.22 — About the OVN-Kubernetes network plugin (fonte: `networking/ovn_kubernetes_network_provider/about-ovn-kubernetes.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 01-arquitetura-e-control-plane/kube-proxy
- **Termo original:** kube-proxy
- **Remissões:** Kube Proxy, service proxy
- **Tradução:** não se traduz
- **Classe ontológica:** componente
- **Plataforma:** Kubernetes (opcional)
- **Escopo:** não aplicável (roda em cada nó)
- **Disponibilidade:** **opcional**; dispensável quando o plugin de rede implementa os Services
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-04

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** a ausência de kube-proxy com OVN-Kubernetes e o campo `deployKubeProxy` são conhecidos da configuração do Cluster Network Operator, mas **não foram conferidos** em texto da documentação 4.22 nem no SNO; validar com os comandos acima. A label `k8s-app=kube-proxy` é a convenção upstream.

</details>
