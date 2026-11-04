# Cluster DNS

## Definição em uma frase

Cluster DNS é o **servidor DNS interno do cluster**, que publica registros para Services e Pods e permite que as aplicações se encontrem **pelo nome**, e não pelo IP.

## Explicação didática

IPs de Pods mudam o tempo todo, e os de Services são difíceis de memorizar. Com o Cluster DNS, um Pod alcança o Service `banco` do próprio namespace só pelo nome `banco`, ou outro namespace por `banco.dados.svc.cluster.local`. O kubelet configura o DNS de cada Pod para usar esse servidor automaticamente.

## Para que existe e qual problema resolve

Dá **descoberta de serviços** por nome, de forma estável e independente de IPs. Muitos exemplos e aplicações dependem dele; por isso a documentação diz que todo cluster Kubernetes deveria ter Cluster DNS.

## Funcionamento técnico e ciclo de vida

- Services recebem nomes DNS no formato `<serviço>.<namespace>.svc.<domínio-do-cluster>`. O domínio padrão é `cluster.local`.
- A lista de busca do DNS de um Pod inclui o namespace do Pod e o domínio do cluster. Uma consulta sem namespace resolve **no namespace do próprio Pod**.
- O nome do namespace entra no DNS, e é por isso que nomes de namespace precisam ser labels DNS válidos. Ver [Namespace](../../00-fundamentos-e-linguagem/verbetes/namespace.md).
- **No OpenShift:** o Cluster DNS é provido por **[CoreDNS](coredns.md)**, implantado e gerenciado pelo **[DNS Operator](dns-operator.md)**. O IP do serviço de DNS é o **10º endereço** da faixa de Services do cluster (ex.: `172.30.0.10` numa rede `172.30.0.0/16`).

## Relações e dependências

- Implementado pelo [CoreDNS](coredns.md), gerenciado pelo [DNS Operator](dns-operator.md).
- Configurado nos Pods pelo [kubelet](kubelet.md).
- Resolve nomes de [Services](../../04-networking/verbetes/service.md).

## Exemplo de situação real

Uma aplicação no namespace `loja` tenta acessar `banco`, que está no namespace `dados`, e recebe "host not found". O nome curto resolve só no próprio namespace; a correção é usar `banco.dados` ou o FQDN `banco.dados.svc.cluster.local`.

## Como visualizar e inspecionar (somente leitura)

```bash
# Domínio do cluster e IP do serviço de DNS
oc get dns.operator.openshift.io default -o jsonpath='{.status.clusterDomain}{"  "}{.status.clusterIP}{"\n"}'

# Faixa de Services (o IP do DNS é o 10º endereço dela)
oc get network.config.openshift.io cluster -o jsonpath='{.status.serviceNetwork}{"\n"}'

# Configuração de DNS que um Pod recebeu (só leitura dentro do contêiner, se ele tiver o arquivo)
oc exec <pod> -n <namespace> -- cat /etc/resolv.conf
```

## Como interpretar a saída

- `clusterDomain` costuma ser `cluster.local`; `clusterIP` é o endereço que os Pods consultam.
- No `resolv.conf` de um Pod, espere `nameserver <clusterIP do DNS>` e uma linha `search <ns>.svc.cluster.local svc.cluster.local cluster.local ...`. Isso explica por que nomes curtos funcionam dentro do namespace.
- Se o `nameserver` não for o IP do Cluster DNS, o Pod pode estar com política de DNS especial (`dnsPolicy`, categoria 03).

## Diferenças e confusões frequentes

- **Cluster DNS × DNS externo:** o Cluster DNS responde pelos nomes internos e encaminha o resto para os servidores externos.
- **Cluster DNS × Route/hostname:** os nomes de Route (ex.: `app.apps.<domínio>`) são resolvidos pelo DNS **externo**, e não pelo Cluster DNS.
- **`cluster.local` não é alcançável de fora do cluster.**

## No OpenShift 4.22 versus Kubernetes

No Kubernetes, o Cluster DNS é um *addon* (normalmente CoreDNS). No OpenShift, ele é parte da plataforma, mantido pelo DNS Operator.

## No HomeLab SNO

Os nomes internos (`*.svc.cluster.local`) resolvem dentro do cluster. Os nomes da API e das Routes dependem do DNS externo do seu HomeLab, que é outro servidor e fica fora do cluster.

## Termos relacionados

[CoreDNS](coredns.md) · [DNS Operator](dns-operator.md) · [kubelet](kubelet.md) · [Namespace](../../00-fundamentos-e-linguagem/verbetes/namespace.md) · [Service](../../04-networking/verbetes/service.md)

## Fontes oficiais

- Kubernetes — DNS for Services and Pods: <https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/> (fonte: `kubernetes/website` `release-1.35`)
- Kubernetes — Cluster Architecture, "DNS": <https://kubernetes.io/docs/concepts/architecture/#dns>
- OCP 4.22 — DNS Operator, "View the default DNS" (domínio, IP no 10º endereço; fontes: `networking/networking_operators/dns-operator.adoc`, `modules/nw-dns-view.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 01-arquitetura-e-control-plane/cluster-dns
- **Termo original:** cluster DNS
- **Remissões:** DNS for Services and Pods, `cluster.local`
- **Tradução:** DNS do cluster (só como apoio)
- **Classe ontológica:** conceito / serviço do cluster
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** addon recomendado no Kubernetes; nativo no OpenShift (via DNS Operator)
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico → intermediário
- **Atualizado em:** 2026-11-04

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** a linha `search` do `resolv.conf` é ilustrativa; validar no SNO. `oc exec` exige permissão e só funciona se o contêiner tiver `cat`; pode ser trocado por uma inspeção via `oc debug` em ambiente de estudo.

</details>
