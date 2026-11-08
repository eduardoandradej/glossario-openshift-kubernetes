# ReplicaSet

## Definição em uma frase

O ReplicaSet **mantém um número estável de réplicas de um [Pod](pod.md)** a qualquer momento: cria Pods quando faltam e remove quando sobram, identificando os seus Pods por um seletor de labels.

## Explicação didática

É o "contador" de Pods: "quero 3". Se um morrer, cria outro; se sobrar um, apaga. Na prática, **quase nunca se usa ReplicaSet diretamente**: ele é criado e gerenciado por um [Deployment](deployment.md), que acrescenta atualizações controladas e histórico de versões.

Remissão: **Replica** (réplica) é cada uma das cópias idênticas de um Pod mantidas por um ReplicaSet ou outro workload.

## Para que existe e qual problema resolve

Garante disponibilidade pela redundância: um número declarado de cópias idênticas da aplicação sempre rodando.

## Funcionamento técnico e ciclo de vida

- **Campos principais:** `replicas` (quantas), `selector` (quais Pods são seus) e `template` (como criar Pods novos).
- **Vínculo com os Pods:** pelos [`ownerReferences`](../../00-fundamentos-e-linguagem/verbetes/owner-reference.md) dos Pods, que apontam para o ReplicaSet dono.
- **Aquisição (adoção):** se existir um Pod **sem dono** (ou cujo dono não é um controller) que case com o seletor, o ReplicaSet o **adota** imediatamente. Por isso os seletores devem ser específicos.
- Seletores de ReplicaSets diferentes **não devem se sobrepor** no mesmo namespace, ou os controllers recebem instruções conflitantes.

## Relações e dependências

- Gerenciado por [Deployment](deployment.md); gerencia [Pods](pod.md).
- Sucessor do [ReplicationController](replicationcontroller.md), que é legado.
- Analogia usada pelo OpenShift: [MachineSet](../../02-compute-e-nodes/verbetes/machineset.md) está para as Machines como o ReplicaSet está para os Pods.

## Exemplo de situação real

Alguém cria à mão um Pod com as mesmas labels de um Deployment. O ReplicaSet passa a contar esse Pod como réplica e apaga um dos seus para manter o total. Era um conflito de seletores, e não um defeito do controller.

## Como visualizar e inspecionar (somente leitura)

```bash
# ReplicaSets: desejado, atual, pronto
oc get replicasets -n <namespace>

# Dono do ReplicaSet (normalmente um Deployment)
oc get replicaset <nome> -n <namespace> -o jsonpath='{range .metadata.ownerReferences[*]}{.kind}/{.name}{"\n"}{end}'

# Pods que pertencem a ele
oc get pods -n <namespace> -l pod-template-hash=<hash>
```

## Como interpretar a saída

- `DESIRED`, `CURRENT` e `READY` iguais: estável.
- ReplicaSets com `DESIRED 0` dentro de um Deployment: revisões antigas guardadas para rollback.
- O sufixo do nome do ReplicaSet (`web-7d9c6b8f5`) é o `pod-template-hash` da revisão.

## Diferenças e confusões frequentes

- **ReplicaSet × Deployment:** número de réplicas de uma versão × versões e atualizações.
- **ReplicaSet × ReplicationController:** o ReplicaSet aceita seletores mais expressivos e é o recomendado.
- **Escalar o ReplicaSet de um Deployment não adianta:** o Deployment o reconcilia de volta. Escale o Deployment.

## No OpenShift 4.22 versus Kubernetes

Igual ao Kubernetes. No OpenShift, ReplicaSets aparecem principalmente sob Deployments.

## No HomeLab SNO

Observe os ReplicaSets dos seus Deployments; não os edite diretamente.

## Termos relacionados

[Deployment](deployment.md) · [Pod](pod.md) · [ReplicationController](replicationcontroller.md) · [Selector](../../00-fundamentos-e-linguagem/verbetes/selector.md) · [OwnerReference](../../00-fundamentos-e-linguagem/verbetes/owner-reference.md)

## Fontes oficiais

- Kubernetes — ReplicaSet (campos, `ownerReferences`, aquisição de Pods): <https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/> (fonte: `kubernetes/website` `release-1.35`, `concepts/workloads/controllers/replicaset.md`)
- Kubernetes — Labels and Selectors (seletores sobrepostos): <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/replicaset
- **Termo original:** ReplicaSet
- **Remissões:** Replica
- **Tradução:** conjunto de réplicas (só como apoio)
- **Classe ontológica:** objeto da API
- **API:** `apiVersion: apps/v1`, `kind: ReplicaSet`
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** namespaced
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido (antes era uma versão inicial). Fontes conferidas em 2026-11-08.
- **Pendências:** exemplos **não executados** no SNO.

</details>
