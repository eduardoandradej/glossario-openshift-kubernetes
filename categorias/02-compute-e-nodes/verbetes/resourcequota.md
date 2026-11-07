# ResourceQuota

## Definição em uma frase

Uma ResourceQuota limita o **consumo agregado de recursos de um namespace**: o total de CPU, memória e armazenamento pedido por todos os objetos, e a **quantidade de objetos** de cada tipo que podem ser criados ali.

## Explicação didática

Num cluster compartilhado, a quota é o "orçamento" de cada equipe. Ela soma os requests e limits de todos os Pods do namespace (e outros recursos) e recusa criações que estourariam o orçamento.

```yaml
# Exemplo didático (não aplicar)
apiVersion: v1
kind: ResourceQuota
metadata:
  name: orcamento
spec:
  hard:
    requests.cpu: "2"
    requests.memory: 4Gi
    limits.memory: 8Gi
    pods: "20"
    persistentvolumeclaims: "5"
```

## Para que existe e qual problema resolve

Evita que uma equipe consuma mais que a sua parte de um cluster com número fixo de nós.

## Funcionamento técnico e ciclo de vida

- O administrador cria quotas por namespace. A documentação recomenda **restringir** quem pode alterá-las ou apagá-las.
- O sistema de quotas acompanha o uso e rejeita criações ou atualizações que excederiam o limite (`hard`), com **`403 Forbidden`** e uma mensagem explicando a restrição.
- **Consequência importante:** se a quota limita `cpu` ou `memory`, todo Pod precisa declarar requests ou limits desses recursos, senão é rejeitado. Um [LimitRange](limitrange.md) com padrões resolve isso.
- Mudanças na quota **não afetam** objetos já criados.
- **Escopos** permitem aplicar uma quota só a alguns Pods (por exemplo, por classe de QoS ou prioridade).
- **No OpenShift:** existe também a **ClusterResourceQuota** (grupo `quota.openshift.io`), que **agrega** o consumo de **vários projetos**, escolhidos por label ou annotation (por exemplo, todos os projetos criados por um usuário), e aplica um limite comum.

## Relações e dependências

- Soma [Resource Requests](resource-request.md) e [Resource Limits](resource-limit.md) do [Namespace](../../00-fundamentos-e-linguagem/verbetes/namespace.md).
- Complementada pelo [LimitRange](limitrange.md).
- No OpenShift, costuma ser criada pelo *project template* ([Project](../../00-fundamentos-e-linguagem/verbetes/project.md)).

## Exemplo de situação real

Um Deployment escala de 3 para 6 réplicas, mas só 4 Pods existem. Os Events do ReplicaSet mostram `exceeded quota: orcamento, requested: requests.memory=512Mi, used: requests.memory=4Gi, limited: requests.memory=4Gi`. O namespace chegou ao limite da quota, e não ao limite do cluster.

## Como visualizar e inspecionar (somente leitura)

```bash
# Quotas do namespace: limite (hard) e uso atual (used)
oc get resourcequota -n <namespace>
oc describe resourcequota <nome> -n <namespace>

# OpenShift: quotas multiprojeto (permissão de cluster)
oc get clusterresourcequota
oc describe clusterresourcequota <nome>

# Quotas que se aplicam ao projeto atual (OpenShift)
oc get appliedclusterresourcequotas -n <namespace>
```

## Como interpretar a saída

- Em `oc describe resourcequota`, as colunas `Used` e `Hard` mostram o consumo e o limite de cada item. `Used` igual a `Hard` significa que não cabe mais nada daquele recurso.
- Rejeições aparecem nos Events do controller (ReplicaSet, Job...) com a mensagem `exceeded quota`.

## Diferenças e confusões frequentes

- **ResourceQuota × LimitRange:** total do namespace × por objeto.
- **Quota × capacidade do cluster:** a quota pode bloquear mesmo com o cluster ocioso.
- **ResourceQuota × ClusterResourceQuota:** um namespace × vários projetos (OpenShift).

## No OpenShift 4.22 versus Kubernetes

A ResourceQuota é do Kubernetes. O OpenShift acrescenta a **ClusterResourceQuota** e o objeto `AppliedClusterResourceQuota`, visível por projeto.

## No HomeLab SNO

Num projeto de estudo, uma quota pequena ajuda a não pressionar o nó único. Criá-la é uma alteração; ler as existentes é seguro.

## Termos relacionados

[LimitRange](limitrange.md) · [Resource Request](resource-request.md) · [Resource Limit](resource-limit.md) · [Namespace](../../00-fundamentos-e-linguagem/verbetes/namespace.md) · [Project](../../00-fundamentos-e-linguagem/verbetes/project.md)

## Fontes oficiais

- Kubernetes — Resource Quotas: <https://kubernetes.io/docs/concepts/policy/resource-quotas/> (fonte: `kubernetes/website` `release-1.35`, `concepts/policy/resource-quotas.md`)
- OCP 4.22 — Resource quotas across multiple projects (`ClusterResourceQuota`; fontes: `applications/quotas/quotas-setting-across-multiple-projects.adoc`, `modules/quotas-selecting-projects.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/resourcequota
- **Termo original:** ResourceQuota
- **Remissões:** ClusterResourceQuota, AppliedClusterResourceQuota
- **Tradução:** cota de recursos (só como apoio)
- **Classe ontológica:** objeto da API
- **API:** `apiVersion: v1` (grupo *core*), `kind: ResourceQuota`; no OpenShift, também `quota.openshift.io/v1` `ClusterResourceQuota`
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** namespaced (ResourceQuota); cluster-scoped (ClusterResourceQuota)
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** o texto da mensagem `exceeded quota` é ilustrativo. O recurso `appliedclusterresourcequotas` é conhecido da documentação de quotas multiprojeto (`quotas-viewing-clusterresourcequotas`), que **não foi lida** nesta rodada; validar no SNO.

</details>
