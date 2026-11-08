# StatefulSet

## Definição em uma frase

O StatefulSet é o workload para **aplicações com estado**: mantém Pods com **identidade estável** (nome e rede previsíveis), **armazenamento próprio e persistente** para cada réplica e criação, escala e atualização em **ordem**.

## Explicação didática

Num [Deployment](deployment.md), as réplicas são intercambiáveis: qualquer uma serve. Num banco de dados em cluster, cada réplica é **alguém**: `db-0` é o primário, `db-1` e `db-2` são secundários, cada um com os seus dados. O StatefulSet garante isso: os Pods se chamam `<nome>-0`, `<nome>-1`... e, se `db-1` for recriado em outro nó, volta com o **mesmo nome** e o **mesmo volume**.

## Para que existe e qual problema resolve

Segundo a documentação, ele é indicado quando a aplicação precisa de:

- identificadores de rede estáveis e únicos;
- armazenamento persistente e estável;
- implantação e escala ordenadas e graciosas;
- atualizações ordenadas e automáticas.

Se nada disso for necessário, um Deployment é mais adequado.

## Funcionamento técnico e ciclo de vida

- **Identidade:** cada Pod recebe um **ordinal** inteiro e único. O nome é `$(nome do statefulset)-$(ordinal)`.
- **Rede:** exige um **Headless Service**, que dá a cada Pod um nome DNS estável.
- **Armazenamento:** `volumeClaimTemplates` cria um PersistentVolumeClaim **por réplica**; o volume acompanha a identidade do Pod.
- **Ordem:** a política padrão é **`OrderedReady`** (cria em ordem crescente e só passa ao próximo quando o anterior está pronto). Também existe `Parallel`.
- **Limitações importantes:**
  - o armazenamento precisa ser provisionado por uma StorageClass com provisionador dinâmico, ou criado antes por um administrador;
  - apagar ou reduzir um StatefulSet **não apaga** os volumes, para proteger os dados.

## Relações e dependências

- Gerencia [Pods](pod.md) e PVCs ([PersistentVolumeClaim](../../05-storage/verbetes/persistentvolumeclaim.md)).
- Depende de um Headless [Service](../../04-networking/verbetes/service.md) e de uma [StorageClass](../../05-storage/verbetes/storageclass.md), ou de PVs criados antes.

## Exemplo de situação real

Um StatefulSet de 3 réplicas fica com `db-0` em `Running` e `db-1` em `Pending` para sempre. Com `OrderedReady`, o `db-2` nem é criado. A causa é o PVC de `db-1`, que não encontra volume porque não há StorageClass dinâmica no cluster.

## Como visualizar e inspecionar (somente leitura)

```bash
# StatefulSets e réplicas prontas
oc get statefulsets -n <namespace>

# Pods com nomes ordinais
oc get pods -n <namespace> -l <label-do-app>

# PVCs criados pelos volumeClaimTemplates
oc get pvc -n <namespace>

# Detalhes: política, estratégia de atualização, eventos
oc describe statefulset <nome> -n <namespace>
```

## Como interpretar a saída

- `READY 2/3`: nem todas as réplicas estão prontas; veja o Pod de maior ordinal criado e os Events.
- PVCs nomeados `<template>-<statefulset>-<ordinal>` continuam existindo depois de reduzir as réplicas, porque os volumes não são apagados.

## Diferenças e confusões frequentes

- **StatefulSet × Deployment:** identidade e dados por réplica × réplicas intercambiáveis.
- **StatefulSet não é "banco de dados pronto":** a lógica de replicação dos dados é da aplicação. O StatefulSet só garante identidade, ordem e volume.

## No OpenShift 4.22 versus Kubernetes

Mesmo objeto (`apps/v1`). No OpenShift, Operators de bancos de dados costumam criar e gerenciar StatefulSets por você (categoria 09).

## No HomeLab SNO

Sem StorageClass dinâmica no SNO, os PVCs do StatefulSet ficam `Pending`. Estude o conceito, ou prepare PVs manualmente num projeto de estudo.

## Termos relacionados

[Pod](pod.md) · [Deployment](deployment.md) · [PersistentVolumeClaim](../../05-storage/verbetes/persistentvolumeclaim.md) · [StorageClass](../../05-storage/verbetes/storageclass.md) · [Service](../../04-networking/verbetes/service.md)

## Fontes oficiais

- Kubernetes — StatefulSets (usos, limitações, Headless Service, ordinais, `volumeClaimTemplates`, `OrderedReady`): <https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/> (fonte: `kubernetes/website` `release-1.35`, `concepts/workloads/controllers/statefulset.md`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/statefulset
- **Termo original:** StatefulSet
- **Remissões:** ordinal, volumeClaimTemplates, OrderedReady
- **Tradução:** conjunto com estado (só como apoio)
- **Classe ontológica:** objeto da API
- **API:** `apiVersion: apps/v1`, `kind: StatefulSet`
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** namespaced
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido (antes era uma versão inicial). Fontes conferidas em 2026-11-08.
- **Pendências:** o formato do nome dos PVCs é ilustrativo; confirmar num cluster com StorageClass.

</details>
