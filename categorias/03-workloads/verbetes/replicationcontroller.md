# ReplicationController

## Definição em uma frase

O ReplicationController é o **controller original de réplicas do Kubernetes**, hoje **substituído** pelas APIs Deployment e [ReplicaSet](replicaset.md): mantém um número fixo de Pods idênticos, mas com recursos mais limitados.

## Explicação didática

Antes do ReplicaSet e do Deployment, era o ReplicationController que garantia "N cópias deste Pod". Ele continua na API por compatibilidade, mas a documentação é clara: um [Deployment](deployment.md) que configura um ReplicaSet é **a forma recomendada** de fazer replicação.

## Para que existe e qual problema resolve

Historicamente, manter a disponibilidade por replicação. Hoje, só faz sentido para entender manifestos e sistemas antigos.

## Funcionamento técnico e ciclo de vida

- Mantém `replicas` Pods que casam com o seletor, criando ou removendo conforme necessário.
- O seletor aceita **apenas igualdade** (mapa de labels), enquanto o ReplicaSet aceita seletores *set-based*.
- Não tem a gestão de versões e rollouts do Deployment.
- **No OpenShift legado:** era a base do [DeploymentConfig](deploymentconfig.md), que cria ReplicationControllers para cada versão.

## Relações e dependências

- Substituído por [ReplicaSet](replicaset.md) e [Deployment](deployment.md).
- Usado pelo [DeploymentConfig](deploymentconfig.md), que também é legado.

## Exemplo de situação real

Num cluster migrado de versões antigas, aparecem ReplicationControllers com nomes como `app-1`, `app-2`. São as versões de um DeploymentConfig. A migração para Deployment elimina essa camada.

## Como visualizar e inspecionar (somente leitura)

```bash
# ReplicationControllers existentes (ainda há algum?)
oc get replicationcontrollers -A

# Dono de um RC (por exemplo, um DeploymentConfig)
oc get rc <nome> -n <namespace> -o jsonpath='{range .metadata.ownerReferences[*]}{.kind}/{.name}{"\n"}{end}'
```

## Como interpretar a saída

- `No resources found`: nenhum uso legado, que é o desejável.
- RCs com dono `DeploymentConfig`: o projeto ainda usa o mecanismo de implantação legado do OpenShift.

## Diferenças e confusões frequentes

- **ReplicationController × ReplicaSet:** seletor só de igualdade × seletor expressivo; legado × atual.
- **ReplicationController × Replication (de dados):** o nome fala de réplicas de Pods, e não de replicação de banco de dados.

## No OpenShift 4.22 versus Kubernetes

Continua servido pela API (`v1`), por compatibilidade. A documentação do OCP ainda o cita no contexto de evacuação de Pods e do DeploymentConfig.

## No HomeLab SNO

Para estudo, basta reconhecer o objeto; não crie ReplicationControllers novos.

## Termos relacionados

[ReplicaSet](replicaset.md) · [Deployment](deployment.md) · [DeploymentConfig](deploymentconfig.md) · [Selector](../../00-fundamentos-e-linguagem/verbetes/selector.md)

## Fontes oficiais

- Kubernetes — ReplicationController ("Superseded by the Deployment and ReplicaSet APIs"): <https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/> (fonte: `kubernetes/website` `release-1.35`, `concepts/workloads/controllers/replicationcontroller.md`)
- Kubernetes — Labels and Selectors (seletores só de igualdade no ReplicationController): <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/replicationcontroller
- **Termo original:** ReplicationController (RC)
- **Tradução:** controlador de replicação (só como apoio)
- **Classe ontológica:** legado (objeto da API substituído)
- **API:** `apiVersion: v1` (grupo *core*), `kind: ReplicationController`
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** namespaced
- **Disponibilidade:** servido por compatibilidade; substituído por Deployment e ReplicaSet
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-08.
- **Pendências:** confirmar no SNO se há algum ReplicationController em uso. **Não executado**.

</details>
