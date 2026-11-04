# CoreDNS

## Definição em uma frase

O CoreDNS é o **servidor DNS** que implementa o [Cluster DNS](cluster-dns.md): responde às consultas dos Pods pelos nomes de Services e Pods e encaminha as demais consultas para os servidores DNS externos.

## Explicação didática

O [Cluster DNS](cluster-dns.md) é a função; o CoreDNS é o software que a executa. No OpenShift você não instala nem configura o CoreDNS diretamente: o [DNS Operator](dns-operator.md) o implanta, cria o Service de DNS e mantém tudo atualizado.

## Para que existe e qual problema resolve

Fornece a resolução de nomes interna do cluster de forma escalável, lendo da API do Kubernetes as informações sobre Services e endpoints.

## Funcionamento técnico e ciclo de vida

- **No OpenShift:** o DNS Operator implanta o CoreDNS como **DaemonSet** (um Pod por nó), cria um Service para ele e configura o kubelet para que os Pods usem o IP desse Service como servidor de nomes.
- Encaminhamento (*forwarding*): consultas a domínios que não são do cluster vão aos servidores externos. O OpenShift permite configurar encaminhamentos específicos por domínio no objeto `dns.operator/default`, uma alteração administrativa.
- O ClusterOperator `dns` fica `Available` quando ao menos um Pod do DaemonSet do CoreDNS reporta disponibilidade e o Service de DNS tem um ClusterIP.

## Relações e dependências

- Implementa o [Cluster DNS](cluster-dns.md); gerenciado pelo [DNS Operator](dns-operator.md).
- Lê Services e EndpointSlices pela [API](../../00-fundamentos-e-linguagem/verbetes/kubernetes-api.md).

## Exemplo de situação real

Consultas DNS de vários Pods ficam lentas. Os Pods `dns-default` estão saudáveis, mas os servidores externos configurados para encaminhamento respondem devagar. O problema está no *upstream*, e não no CoreDNS.

## Como visualizar e inspecionar (somente leitura)

```bash
# DaemonSet e Pods do CoreDNS (apenas observar)
oc get daemonset -n openshift-dns
oc get pods -n openshift-dns -o wide

# Service de DNS do cluster
oc get service -n openshift-dns

# Logs de um Pod do CoreDNS
oc logs -n openshift-dns <pod-dns-default> -c dns --tail=50
```

## Como interpretar a saída

- Espere o DaemonSet `dns-default` com `DESIRED` igual a `READY`, normalmente um Pod por nó.
- O Service `dns-default` com `CLUSTER-IP` igual ao `clusterIP` do objeto `dns.operator/default`.
- Nos logs, erros de *upstream* (timeouts ao encaminhar) indicam problema no DNS externo.

## Diferenças e confusões frequentes

- **CoreDNS × Cluster DNS:** implementação × função.
- **CoreDNS × DNS Operator:** quem responde × quem gerencia.
- **CoreDNS do cluster × DNS do HomeLab:** o segundo resolve os nomes da API e das Routes, fora do cluster.

## No OpenShift 4.22 versus Kubernetes

No Kubernetes, o CoreDNS é implantado como addon (geralmente um Deployment em `kube-system`). No OpenShift, ele roda como DaemonSet em `openshift-dns`, sob o DNS Operator.

## No HomeLab SNO

Há um Pod do CoreDNS no único nó. Observe-o e leia os logs; **não** edite o DaemonSet, porque o Operator o reconcilia.

## Termos relacionados

[Cluster DNS](cluster-dns.md) · [DNS Operator](dns-operator.md) · [Service](../../04-networking/verbetes/service.md) · [kubelet](kubelet.md)

## Fontes oficiais

- OCP 4.22 — DNS Operator ("deploys CoreDNS using a daemon set, creates a service... configures the kubelet"; fontes: `networking/networking_operators/dns-operator.adoc`, `modules/nw-dns-operator.adoc`)
- Kubernetes — DNS for Services and Pods: <https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/>
- Projeto CoreDNS (fonte externa): <https://coredns.io/>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 01-arquitetura-e-control-plane/coredns
- **Termo original:** CoreDNS
- **Tradução:** não se traduz
- **Classe ontológica:** componente (servidor DNS)
- **Plataforma:** Kubernetes (addon comum) / OpenShift (nativo)
- **Escopo:** não aplicável
- **Disponibilidade:** nativo no OpenShift, gerenciado pelo DNS Operator
- **Versões validadas:** OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-04

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** os nomes `dns-default` (DaemonSet e Service), o namespace `openshift-dns` e o contêiner `dns` são conhecidos da documentação de DNS do OpenShift, mas **não foram conferidos** nos módulos lidos; validar no SNO. A forma de implantação no Kubernetes upstream foi descrita de modo genérico.

</details>
