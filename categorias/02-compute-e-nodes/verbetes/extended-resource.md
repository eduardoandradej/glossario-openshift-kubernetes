# Extended Resource

## Definição em uma frase

Um Extended Resource é um **recurso com nome próprio, fora do domínio `kubernetes.io`** (por exemplo `nvidia.com/gpu`), anunciado pelo nó e pedido pelos Pods como CPU e memória, para representar hardware ou capacidades que o Kubernetes não conhece nativamente.

## Explicação didática

O Kubernetes conhece CPU, memória, armazenamento efêmero e huge pages. Para todo o resto (GPUs, FPGAs, placas de rede especiais, licenças), existe o mecanismo de recursos estendidos. Primeiro alguém **anuncia** o recurso no nó, normalmente um [Device Plugin](device-plugin.md). Depois os Pods o **pedem**. O scheduler faz a contabilidade para não entregar mais do que existe.

```yaml
# Trecho didático
resources:
  limits:
    nvidia.com/gpu: 1
```

## Para que existe e qual problema resolve

Permite agendar cargas que dependem de hardware especial sem modificar o código do Kubernetes.

## Funcionamento técnico e ciclo de vida

- **Nome qualificado:** qualquer prefixo de domínio **exceto `kubernetes.io`**, que é reservado.
- **Quantidades inteiras:** a API aceita só números inteiros (`3`, `3000m` e `3Ki` são válidos; `0.5` e `1500m` não).
- **Sem overcommit:** request e limit, se ambos estiverem presentes, precisam ser **iguais**.
- **Agendamento:** o Pod só é agendado se **todos** os requests, inclusive os estendidos, forem satisfeitos; caso contrário, fica `Pending`.
- Os recursos estendidos substituem os antigos *Opaque Integer Resources*.

## Relações e dependências

- Normalmente anunciado por um [Device Plugin](device-plugin.md); aparece em [Capacity](capacity.md) e [Allocatable](allocatable.md).
- Pedido como [Resource Request](resource-request.md) e [Resource Limit](resource-limit.md).

## Exemplo de situação real

Um Pod de treinamento de modelo pede `nvidia.com/gpu: 2` e fica `Pending` com `Insufficient nvidia.com/gpu`. O nó com GPU tem só uma livre. O problema não é CPU nem memória.

## Como visualizar e inspecionar (somente leitura)

```bash
# Recursos do nó, incluindo os estendidos
oc get node <nó> -o jsonpath='{.status.allocatable}{"\n"}'

# Pedidos de recursos estendidos num Pod
oc get pod <nome> -n <namespace> -o jsonpath='{range .spec.containers[*]}{.name}: {.resources.limits}{"\n"}{end}'
```

## Como interpretar a saída

- Chaves com domínio próprio em `allocatable` (como `nvidia.com/gpu: "1"`) são recursos estendidos anunciados.
- Ausência da chave significa que nenhum plugin ou administrador anunciou esse recurso no nó.

## Diferenças e confusões frequentes

- **Extended resource × device plugin:** o recurso é o que se pede; o plugin é quem o anuncia e o entrega ao contêiner.
- **Extended resource × label:** a label diz que o nó **tem** uma característica; o recurso estendido **contabiliza** unidades.

## No OpenShift 4.22 versus Kubernetes

Mesmo mecanismo. Para GPUs, o OpenShift usa Operators de fornecedores, que implantam os device plugins (categoria 16). O OCP 4.22 também documenta a alocação de GPUs por **DRA** (*Dynamic Resource Allocation*), um mecanismo mais novo.

## No HomeLab SNO

Sem hardware especial, não haverá recursos estendidos no nó.

## Termos relacionados

[Device Plugin](device-plugin.md) · [Capacity](capacity.md) · [Allocatable](allocatable.md) · [Resource Request](resource-request.md) · [HugePages](hugepages.md)

## Fontes oficiais

- Kubernetes — Resource Management for Pods and Containers, "Extended resources": <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#extended-resources> (fonte: `kubernetes/website` `release-1.35`)
- OCP 4.22 — "Allocating GPUs to pods by using DRA" (citado no sumário; fonte: `_topic_maps/_topic_map.yml`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/extended-resource
- **Termo original:** extended resource
- **Remissões:** Opaque Integer Resources (legado)
- **Tradução:** recurso estendido (só como apoio)
- **Classe ontológica:** conceito (tipo de recurso)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo; depende de quem anuncia o recurso
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** avançado
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** a documentação de DRA no OCP 4.22 só foi vista no sumário e **não foi lida**; detalhar na categoria 16.

</details>
