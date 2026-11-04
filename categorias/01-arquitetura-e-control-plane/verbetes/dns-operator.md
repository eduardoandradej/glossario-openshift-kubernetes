# DNS Operator

## Definição em uma frase

O DNS Operator é o Operator do OpenShift que **implanta e gerencia o [CoreDNS](coredns.md)** para prover o [Cluster DNS](cluster-dns.md): resolução de nomes para os Pods, descoberta de Services por DNS e resolução dos nomes internos `cluster.local`.

## Explicação didática

Em vez de você instalar e configurar o servidor DNS do cluster, o DNS Operator faz isso e **mantém** o resultado: se alguém apagar o DaemonSet do CoreDNS, ele recria; se a configuração mudar no objeto `dns.operator/default`, ele aplica. É o padrão de [Reconciliation](../../00-fundamentos-e-linguagem/verbetes/reconciliation.md) aplicado ao DNS.

## Para que existe e qual problema resolve

Torna o DNS interno uma parte gerenciada da plataforma, com estado visível e atualizações automáticas junto com o cluster.

## Funcionamento técnico e ciclo de vida

- É implantado durante a instalação como um **Deployment** (`dns-operator`, no namespace `openshift-dns-operator`).
- Implementa a API **`dns`** do grupo **`operator.openshift.io`**. Toda instalação tem um objeto `dns.operator` chamado **`default`**.
- Implanta o CoreDNS como **DaemonSet**, cria o **Service** de DNS e configura o kubelet para que os Pods usem o IP desse Service.
- O `status` do objeto `default` traz o **Cluster Domain** (domínio base, como `cluster.local`) e o **Cluster IP** (o 10º endereço da faixa de Services).
- Relata a saúde no ClusterOperator **`dns`**: `AVAILABLE=True` quando ao menos um Pod do DaemonSet do CoreDNS está disponível e o Service de DNS tem ClusterIP.

## Relações e dependências

- Gerencia o [CoreDNS](coredns.md), que implementa o [Cluster DNS](cluster-dns.md).
- É um [Operator](../../09-operators-e-extensoes/verbetes/operator.md) de plataforma; o estado aparece em [ClusterOperator](../../09-operators-e-extensoes/verbetes/clusteroperator.md).

## Exemplo de situação real

`oc get clusteroperator dns` mostra `DEGRADED=True`. Em `oc describe clusteroperator dns`, a mensagem indica que nem todos os Pods do CoreDNS estão disponíveis, por exemplo porque um nó está com pressão de recursos. O ponto de partida é o Operator, e não a aplicação que reclamou do DNS.

## Como visualizar e inspecionar (somente leitura)

```bash
# Deployment do Operator e estado do ClusterOperator
oc get -n openshift-dns-operator deployment/dns-operator
oc get clusteroperator dns

# Objeto de configuração/estado do DNS do cluster
oc describe dns.operator/default

# Logs do Operator
oc logs -n openshift-dns-operator deployment/dns-operator -c dns-operator --tail=50
```

## Como interpretar a saída

- `dns-operator` com `READY 1/1`: o Operator está rodando.
- ClusterOperator `dns`: o normal é `AVAILABLE=True`, `PROGRESSING=False`, `DEGRADED=False`.
- Em `oc describe dns.operator/default`, a seção `Status` mostra `Cluster Domain` e `Cluster IP`; a seção `Spec` mostra personalizações (como *servers* para encaminhamento por domínio), quando houver.

## Diferenças e confusões frequentes

- **DNS Operator × CoreDNS:** quem gerencia × quem responde.
- **DNS Operator × External DNS Operator:** o External DNS Operator, opcional, publica registros em provedores de DNS externos; é outro produto.
- **`dns.operator.openshift.io` × `dns.config.openshift.io`:** o primeiro configura o DNS **interno**; o segundo descreve a configuração de DNS do cluster na infraestrutura, como as zonas. Confira cada um com `oc explain`.

## No OpenShift 4.22 versus Kubernetes

Não há DNS Operator no Kubernetes upstream; lá o CoreDNS é um addon instalado e mantido à parte.

## No HomeLab SNO

Leitura segura com os comandos acima. Alterar `dns.operator/default` (encaminhamentos, por exemplo) é uma mudança de plataforma: faça só com objetivo claro e com reversão planejada.

## Termos relacionados

[CoreDNS](coredns.md) · [Cluster DNS](cluster-dns.md) · [Operator](../../09-operators-e-extensoes/verbetes/operator.md) · [ClusterOperator](../../09-operators-e-extensoes/verbetes/clusteroperator.md) · [Cluster Version Operator](cluster-version-operator.md)

## Fontes oficiais

- OCP 4.22 — DNS Operator in OpenShift Container Platform (fonte: `networking/networking_operators/dns-operator.adoc`)
- OCP 4.22 — "Check the status of the DNS Operator" e "View the default DNS" (fontes: `modules/nw-dns-operator.adoc`, `modules/nw-dns-view.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 01-arquitetura-e-control-plane/dns-operator
- **Termo original:** DNS Operator
- **Remissões:** `dns.operator.openshift.io`, ClusterOperator `dns`
- **Tradução:** não se traduz
- **Classe ontológica:** componente (Operator de plataforma)
- **Plataforma:** OpenShift
- **API:** `apiVersion: operator.openshift.io/v1`, `kind: DNS` (objeto `default`, cluster-scoped)
- **Escopo:** cluster
- **Disponibilidade:** nativo, instalado com o cluster
- **Versões validadas:** OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-04

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** confirmar o nome do contêiner `dns-operator` nos logs e a diferença entre `dns.operator` e `dns.config` com `oc explain` no SNO, que **não foi executado**. A URL publicada está **a verificar**.

</details>
