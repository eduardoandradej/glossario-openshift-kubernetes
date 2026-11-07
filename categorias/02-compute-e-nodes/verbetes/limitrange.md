# LimitRange

## Definição em uma frase

Um LimitRange é uma política, **por namespace**, que define **mínimos, máximos, proporções e valores padrão** de requests e limits para cada Pod, contêiner ou PersistentVolumeClaim criado ali.

## Explicação didática

A [ResourceQuota](resourcequota.md) limita o **total** de um namespace; o LimitRange limita **cada objeto**. Ele evita que um único Pod monopolize os recursos do namespace e preenche requests e limits padrão para quem não os declarou.

```yaml
# Exemplo didático (não aplicar)
apiVersion: v1
kind: LimitRange
metadata:
  name: padroes
spec:
  limits:
  - type: Container
    default:          # limit padrão
      cpu: 500m
      memory: 512Mi
    defaultRequest:   # request padrão
      cpu: 100m
      memory: 128Mi
    max:
      memory: 1Gi
```

## Para que existe e qual problema resolve

Garante que todo contêiner tenha requests e limits razoáveis, sem depender da disciplina de cada desenvolvedor, e impede pedidos exagerados.

## Funcionamento técnico e ciclo de vida

- Vale para o namespace **sempre que houver ao menos um** LimitRange nele.
- Na criação de um objeto:
  1. o **admission controller** de LimitRange aplica os **padrões** de request e limit aos contêineres que não os declararam;
  2. em seguida, verifica mínimos, máximos e proporções;
  3. se houver violação, a API rejeita a criação com **`403 Forbidden`** e uma mensagem explicando a restrição.
- Pode limitar também o tamanho de **PersistentVolumeClaims** e a **proporção** entre limit e request.
- Atua **na admissão**: não altera Pods que já existem.

## Relações e dependências

- Preenche e restringe [Resource Request](resource-request.md) e [Resource Limit](resource-limit.md); afeta a [QoS Class](qos-class.md) resultante.
- Complementa a [ResourceQuota](resourcequota.md).
- Objeto de [Namespace](../../00-fundamentos-e-linguagem/verbetes/namespace.md); no OpenShift, frequentemente criado pelo *project template*.

## Exemplo de situação real

Um desenvolvedor cria um Pod sem `resources`, e ele aparece com `requests.cpu: 100m` e `limits.memory: 512Mi`. Quem preencheu foi o LimitRange do projeto. Outro Pod, que pedia 2Gi, foi rejeitado com `403`, porque o máximo é 1Gi.

## Como visualizar e inspecionar (somente leitura)

```bash
# LimitRanges do namespace e seus valores
oc get limitrange -n <namespace>
oc describe limitrange <nome> -n <namespace>

# O describe do namespace também mostra os limites
oc describe namespace <namespace>
```

## Como interpretar a saída

Em `oc describe limitrange`, cada linha mostra `Type`, `Resource`, `Min`, `Max`, `Default Request`, `Default Limit` e `Max Limit/Request Ratio`. Um traço (`-`) indica ausência de restrição naquele campo.

## Diferenças e confusões frequentes

- **LimitRange × ResourceQuota:** por objeto × total do namespace.
- **LimitRange × limits do contêiner:** o LimitRange define regras e padrões; os limits efetivos ficam no Pod.
- **Padrão aplicado ≠ declarado:** o Pod armazenado mostra os valores injetados, que não estavam no manifesto.

## No OpenShift 4.22 versus Kubernetes

Objeto padrão do Kubernetes (`v1`). No OpenShift, administradores costumam incluí-lo no *project template*, para que todo projeto novo nasça com padrões de recursos.

## No HomeLab SNO

Num projeto de estudo, um LimitRange com padrões modestos protege o nó único de Pods sem limites. Criá-lo é uma alteração no projeto; ler os existentes é seguro.

## Termos relacionados

[ResourceQuota](resourcequota.md) · [Resource Request](resource-request.md) · [Resource Limit](resource-limit.md) · [QoS Class](qos-class.md) · [Project](../../00-fundamentos-e-linguagem/verbetes/project.md)

## Fontes oficiais

- Kubernetes — Limit Ranges: <https://kubernetes.io/docs/concepts/policy/limit-range/> (fonte: `kubernetes/website` `release-1.35`, `concepts/policy/limit-range.md`)
- OCP 4.22 — Restrict resource consumption with limit ranges (fonte: `nodes/clusters/nodes-cluster-limit-ranges.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/limitrange
- **Termo original:** LimitRange
- **Tradução:** faixa de limites (só como apoio)
- **Classe ontológica:** objeto da API
- **API:** `apiVersion: v1` (grupo *core*), `kind: LimitRange`
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** namespaced
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico → intermediário
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** a assembly do OCP sobre limit ranges foi baixada, mas seus módulos **não foram lidos**; os tipos adicionais do OpenShift (como `openshift.io/Image`) ficam para verificação.

</details>
