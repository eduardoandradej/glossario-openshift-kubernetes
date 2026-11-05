# HyperShift

## Definição em uma frase

HyperShift é o **projeto e o Operator** que implementam os [Hosted Control Planes](hosted-control-plane.md) do OpenShift: o HyperShift Operator roda no management cluster e cria, como Pods, os Control Planes dos hosted clusters.

## Explicação didática

"Hosted Control Planes" é o nome do modelo de implantação; "HyperShift" é o nome do software por trás dele. Na documentação do produto, o termo aparece no **HyperShift Operator** e no grupo de API **`hypershift.openshift.io`**, que define recursos como `HostedCluster` e `NodePool`.

## Para que existe e qual problema resolve

Dá ao OpenShift a capacidade de separar o Control Plane do data plane e de hospedar muitos Control Planes num só cluster de gerenciamento, com os benefícios descritos em [Hosted Control Plane](hosted-control-plane.md).

## Funcionamento técnico e ciclo de vida

- O **HyperShift Operator** é implantado no *management cluster*, normalmente por meio do multicluster engine for Kubernetes Operator.
- Ao receber um `HostedCluster`, ele cria os componentes do Control Plane daquele cluster como cargas de trabalho no management cluster.
- `NodePool` descreve e gerencia os nós de compute do hosted cluster.
- O papel de *cluster service provider* inclui monitorar e manter a disponibilidade do HyperShift Operator e dos Control Planes dos hosted clusters.

## Relações e dependências

- Implementa o [Hosted Control Plane](hosted-control-plane.md).
- É um [Operator](../../09-operators-e-extensoes/verbetes/operator.md) com API própria, entregue como componente opcional.

## Exemplo de situação real

Num management cluster, `oc get hostedclusters -A` não responde, porque a API não existe. O HyperShift Operator não foi habilitado: o recurso de HCP depende do multicluster engine estar instalado e configurado.

## Como visualizar e inspecionar (somente leitura)

```bash
# A API do HyperShift existe neste cluster?
oc api-resources --api-group=hypershift.openshift.io

# Onde o Operator roda, num management cluster (namespace a confirmar)
oc get pods -A | grep -i hypershift
```

## Como interpretar a saída

- Lista vazia em `api-resources`: o cluster não é um management cluster com HyperShift. Isso é esperado num cluster standalone.
- Pods com `hypershift` no nome indicam o Operator em execução.

## Diferenças e confusões frequentes

- **HyperShift × Hosted Control Plane:** o software × o modelo.
- **HyperShift × multicluster engine:** o MCE é o Operator de ciclo de vida de clusters que habilita e configura o HCP; o HyperShift Operator é o componente que cria os Control Planes.

## No OpenShift 4.22 versus Kubernetes

Componente do ecossistema OpenShift; não existe no Kubernetes upstream.

## No HomeLab SNO

Não instalado. Mantenha o estudo no plano conceitual.

## Termos relacionados

[Hosted Control Plane](hosted-control-plane.md) · [Operator](../../09-operators-e-extensoes/verbetes/operator.md) · [Control Plane](control-plane.md)

## Fontes oficiais

- OCP 4.22 — Hosted control planes overview, "Glossary of common concepts and personas" (management cluster com o HyperShift Operator; *cluster service provider*): <https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/index> (fonte: `modules/hosted-control-planes-concepts-personas.adoc`)
- OCP 4.22 — "Differences between hosted control planes and OpenShift Container Platform" (API `hypershift.openshift.io`, `HostedCluster`, `NodePool`; fonte: `modules/hcp-ocp-differences.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 01-arquitetura-e-control-plane/hypershift
- **Termo original:** HyperShift, HyperShift Operator
- **Tradução:** não se traduz
- **Classe ontológica:** componente (Operator) / extensão opcional
- **Plataforma:** OpenShift (ecossistema)
- **API:** `hypershift.openshift.io`
- **Escopo:** não aplicável
- **Disponibilidade:** opcional, via multicluster engine
- **Versões validadas:** OCP 4.22
- **Nível:** avançado
- **Atualizado em:** 2026-11-05

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-05.
- **Pendências:** o namespace em que o HyperShift Operator roda e o modo exato de implantá-lo pelo MCE não foram lidos nesta rodada (documentação de preparação do HCP); conferir na categoria 16.

</details>
