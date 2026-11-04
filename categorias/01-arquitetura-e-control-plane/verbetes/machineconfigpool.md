# MachineConfigPool (MCP)

## Definição em uma frase

Um MachineConfigPool **agrupa nós** que devem receber a mesma configuração de sistema operacional: liga um conjunto de [MachineConfigs](machineconfig.md) a um conjunto de nós e controla como as atualizações são distribuídas entre eles.

## Explicação didática

O MCP responde a duas perguntas: **quais nós** (por seletor de labels de nó) e **quais configurações** (por seletor de MachineConfigs). Todo cluster nasce com dois pools, `master` e `worker`. Para grupos especiais de workers (como nós de infraestrutura ou nós com hardware específico), criam-se **pools personalizados**.

## Para que existe e qual problema resolve

Permite aplicar mudanças a grupos inteiros de nós de forma controlada (quantos por vez, em que ordem) e acompanhar o progresso por grupo.

## Funcionamento técnico e ciclo de vida

- **Pertencimento:** um nó pertence a **um único** pool. Se tiver labels que casam com vários (ex.: `worker` e `infra`), fica no pool **personalizado** (`infra`), que tem prioridade.
- **Pools personalizados:** só para workers; **não há suporte** a pools personalizados de Control Plane. Eles **herdam** a configuração do pool `worker` e acrescentam a sua.
- **Distribuição:** o campo `maxUnavailable` define quantos nós do pool podem ficar indisponíveis ao mesmo tempo durante uma atualização. O padrão é `1`, e a documentação recomenda **não mudar** esse valor no pool de Control Plane.
- **Ordem:** os nós são atualizados por zona (label `topology.kubernetes.io/zone`) e, dentro de cada zona, primeiro os mais antigos. Sem zonas (como em bare metal), pela idade.
- **Paralelismo entre pools:** pools diferentes atualizam em paralelo.
- **Drift:** se a configuração de um nó diverge da aplicada, o MCO marca o nó, e com ele o pool, como degradado.
- **Assinatura:** a documentação observa que nós com papel `infra` rodando só cargas de infraestrutura não contam para o total de assinaturas (*subscriptions*), mas isso é independente do pool.

## Relações e dependências

- Agrupa nós e [MachineConfigs](machineconfig.md); é gerenciado pelo [Machine Config Operator](machine-config-operator.md).
- Os pools padrão correspondem aos papéis [Master Node](master-node.md) e [Worker Node](worker-node.md).

## Exemplo de situação real

Após criar um MachineConfig para workers, `oc get mcp` mostra `worker` com `UPDATING=True` e `READYMACHINECOUNT` subindo um a um. Com `maxUnavailable=1`, um worker por vez é drenado, atualizado e reiniciado.

## Como visualizar e inspecionar (somente leitura)

```bash
# Pools e estado
oc get machineconfigpools

# Detalhes de um pool: seletores, maxUnavailable, condições, contagens
oc describe machineconfigpool worker

# Seletores de nós e de MachineConfigs
oc get mcp worker -o jsonpath='{.spec.nodeSelector}{"\n"}{.spec.machineConfigSelector}{"\n"}'
```

## Como interpretar a saída

Saída **ilustrativa** de `oc get mcp`:

```text
NAME     CONFIG                 UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-<h>    True      False      False      1              1                   1                     0                      30d
worker   rendered-worker-<h>    True      False      False      0              0                   0                     0                      30d
```

- `CONFIG` é o rendered MachineConfig vigente do pool.
- `UPDATED=True`, `UPDATING=False` e `DEGRADED=False`: pool em dia.
- Num SNO, o pool `worker` pode aparecer com **0 máquinas**, porque o único nó pertence ao pool `master`. Confira no seu cluster.

## Diferenças e confusões frequentes

- **MachineConfigPool × compute machine set:** o MCP agrupa nós para **configuração**; o machine set agrupa máquinas para **criação e escala** (Machine API).
- **Pool × papel de nó:** o papel (label) define a qual pool o nó pertence, mas um nó com dois papéis pertence a um pool só.

## No OpenShift 4.22 versus Kubernetes

Recurso exclusivo do OpenShift.

## No HomeLab SNO

Observe os pools com os comandos acima. **Não** pause pools nem altere `maxUnavailable` no SNO; qualquer atualização aplicada reinicia o único nó.

## Termos relacionados

[MachineConfig](machineconfig.md) · [Machine Config Operator](machine-config-operator.md) · [Master Node](master-node.md) · [Worker Node](worker-node.md) · [Selector](../../00-fundamentos-e-linguagem/verbetes/selector.md)

## Fontes oficiais

- OCP 4.22 — "Node configuration management with machine config pools" (pools padrão, personalizados, um pool por nó, drift, infra; fonte: `modules/architecture-machine-config-pools.adoc`)
- OCP 4.22 — "About the OpenShift Update Service" (`maxUnavailable` padrão 1 e recomendação para o Control Plane; fonte: `modules/update-service-overview.adoc`)
- OCP 4.22 — "Machine config overview" (ordem por zona e por idade; fonte: `modules/machine-config-overview.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 01-arquitetura-e-control-plane/machineconfigpool
- **Termo original:** MachineConfigPool (MCP)
- **Remissões:** machine config pool, custom pool
- **Tradução:** não se traduz
- **Classe ontológica:** objeto da API (OpenShift)
- **API:** `apiVersion: machineconfiguration.openshift.io/v1`, `kind: MachineConfigPool`
- **Plataforma:** OpenShift
- **Escopo:** cluster-scoped
- **Disponibilidade:** nativo (pools `master` e `worker` criados na instalação)
- **Versões validadas:** OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-04

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** as colunas de `oc get mcp` e o comportamento do pool `worker` no SNO (0 máquinas) devem ser confirmados no cluster, porque **não foram executados**.

</details>
