# HugePages (recurso `hugepages-<tamanho>`)

## Definição em uma frase

HugePages são **páginas de memória maiores que as comuns** de 4Ki (no x86_64, tipicamente 2Mi e 1Gi), **pré-alocadas** no nó e expostas ao Kubernetes como recursos agendáveis com o nome `hugepages-<tamanho>`.

## Explicação didática

A CPU traduz endereços de memória com a ajuda de um cache de hardware pequeno, o **TLB**. Com páginas de 4Ki, um processo que usa muita memória precisa de muitas entradas nesse cache e perde desempenho. Com páginas maiores, menos entradas cobrem a mesma memória. Bancos de dados, funções de rede e aplicações de alto desempenho se beneficiam, desde que sejam **escritas para usar huge pages**.

## Para que existe e qual problema resolve

Reduz a sobrecarga de tradução de memória em cargas sensíveis a desempenho.

## Funcionamento técnico e ciclo de vida

- **Pré-alocação no nó:** o nó precisa reservar as huge pages, preferencialmente **na inicialização**, quando a memória ainda não está fragmentada. Só então ele relata `hugepages-2Mi` ou `hugepages-1Gi` em [Capacity](capacity.md) e [Allocatable](allocatable.md).
- **Consumo pelo Pod:** pedidas em `resources` como os demais recursos, junto com um request de CPU ou de memória, e montadas por um `emptyDir` com `medium: HugePages` (ou `medium: HugePages-<tamanho>`, quando o Pod usa mais de um tamanho).
- **Sem overcommit:** diferente de CPU e memória, não é possível pedir mais huge pages do que o nó reservou.
- **No OpenShift:** a reserva na inicialização é feita pelo **Node Tuning Operator** (plugin de *boot loader* do TuneD, só em nós de compute RHCOS) nos nós rotulados para isso.

## Relações e dependências

- Aparece em [Capacity](capacity.md) e [Allocatable](allocatable.md); é pedida como [Resource Request](resource-request.md) e [Resource Limit](resource-limit.md).
- Relacionada a [NUMA](numa.md) em cargas de alto desempenho.

## Exemplo de situação real

Um Pod de banco de dados pede `hugepages-1Gi: 4Gi` e fica `Pending` com `Insufficient hugepages-1Gi`. Nenhum nó reservou huge pages de 1Gi. É preciso configurar a reserva nos nós dedicados, o que exige reinicializá-los.

## Como visualizar e inspecionar (somente leitura)

```bash
# Huge pages reservadas e alocáveis no nó
oc get node <nó> -o jsonpath='{.status.capacity}{"\n"}{.status.allocatable}{"\n"}' | tr ',' '\n' | grep -i hugepages

# Pedido de huge pages num Pod
oc get pod <nome> -n <namespace> -o jsonpath='{range .spec.containers[*]}{.name}: {.resources.limits}{"\n"}{end}'
```

## Como interpretar a saída

- `hugepages-2Mi: 0` e `hugepages-1Gi: 0`: o nó não reservou huge pages.
- Valores diferentes de zero: memória já separada para huge pages, que **deixa de estar disponível** como memória comum.

## Diferenças e confusões frequentes

- **HugePages × Transparent Huge Pages (THP):** as primeiras são pré-alocadas e pedidas explicitamente; as THP são uma tentativa automática do kernel, sem controle pelo Kubernetes.
- **Quantos tamanhos por nó:** a documentação do Kubernetes mostra um nó com huge pages de **vários** tamanhos; a do OCP 4.22 afirma que **um nó só pode pré-alocar huge pages de um tamanho**. Siga a do OpenShift no OpenShift.

## No OpenShift 4.22 versus Kubernetes

O conceito é o mesmo. No OpenShift, a configuração é feita pelo Node Tuning Operator, e há a restrição de tamanho citada acima.

## No HomeLab SNO

Não reserve huge pages no SNO pequeno: a memória reservada sai da memória comum do único nó, e a configuração exige reinicializá-lo.

## Termos relacionados

[Memory](memory.md) · [Capacity](capacity.md) · [Allocatable](allocatable.md) · [NUMA](numa.md) · [Resource Limit](resource-limit.md)

## Fontes oficiais

- Kubernetes — Manage HugePages: <https://kubernetes.io/docs/tasks/manage-hugepages/scheduling-hugepages/> (fonte: `kubernetes/website` `release-1.35`, `tasks/manage-hugepages/scheduling-hugepages.md`)
- OCP 4.22 — What huge pages do and how they are consumed by applications (fontes: `scalability_and_performance/what-huge-pages-do-and-how-they-are-consumed-by-apps.adoc`, `modules/what-huge-pages-do.adoc`, `modules/how-huge-pages-are-consumed-by-apps.adoc`, `modules/configuring-huge-pages.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/hugepages
- **Termo original:** huge pages (`hugepages-<size>`)
- **Remissões:** Transparent Huge Pages (THP), TLB
- **Tradução:** páginas grandes de memória (só como apoio)
- **Classe ontológica:** conceito (tipo de recurso computacional)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo; exige pré-alocação no nó
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** avançado
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Divergência registrada:** o Kubernetes mostra vários tamanhos por nó; o OCP 4.22 diz um tamanho por nó.
- **Pendências:** a configuração via Node Tuning Operator será detalhada na categoria 11.

</details>
