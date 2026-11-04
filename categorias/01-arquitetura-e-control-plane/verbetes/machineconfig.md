# MachineConfig

## Definição em uma frase

Um MachineConfig é o objeto que **declara uma configuração do sistema operacional** (arquivos, unidades systemd, argumentos de kernel...) a ser aplicada pelo [Machine Config Operator](machine-config-operator.md) aos nós de um [MachineConfigPool](machineconfigpool.md).

## Explicação didática

É o "manifesto do SO do nó". Em vez de editar arquivos à mão em cada máquina, você descreve o que quer num MachineConfig e indica a qual pool ele se aplica (por label, por exemplo `machineconfiguration.openshift.io/role: worker`). O MCO combina todos os MachineConfigs do pool e aplica o resultado.

## Para que existe e qual problema resolve

Torna a configuração dos nós **declarativa, versionável e reaplicável**: nós novos do pool recebem automaticamente a mesma configuração.

## Funcionamento técnico e ciclo de vida

- **Conteúdo:** segue o formato **Ignition** (v3) e permite, entre outros, criar ou sobrescrever arquivos em `/etc` ou `/var`, criar e configurar unidades systemd, e definir argumentos de kernel e outras opções do SO.
- **Combinação:** os MachineConfigs de um pool são processados em **ordem lexicográfica** pelo nome. O primeiro é a base, e os seguintes são acrescentados, formando um **rendered MachineConfig** (`rendered-<pool>-<hash>`). Por isso os nomes costumam começar com números (`99-...`).
- **Herança:** um MachineConfig para `worker` também vale para os pools personalizados derivados de `worker`. Desde o OCP 4.15, MachineConfigs que miram um pool personalizado **sobrepõem** os de `worker` quando definem os mesmos campos.
- **Aplicação:** pode exigir drenagem e reinicialização dos nós do pool, conforme o tipo de mudança e as políticas de interrupção configuradas.

## Relações e dependências

- Aplicado pelo [Machine Config Operator](machine-config-operator.md) aos nós de um [MachineConfigPool](machineconfigpool.md).
- Formas de mais alto nível que viram MachineConfig: `KubeletConfig` e `ContainerRuntimeConfig`.

## Exemplo de situação real

Uma equipe precisa de um parâmetro de kernel em todos os workers. Ela cria um MachineConfig `99-worker-<nome>` com a label do pool `worker`. O MCO gera um novo rendered MachineConfig e atualiza os workers um a um.

## Como visualizar e inspecionar (somente leitura)

```bash
# Todos os MachineConfigs (origem e rendered)
oc get machineconfigs

# A qual pool cada um se aplica (label de papel)
oc get machineconfigs -L machineconfiguration.openshift.io/role

# Rendered MachineConfig em uso por um pool
oc get machineconfigpool worker -o jsonpath='{.status.configuration.name}{"\n"}'

# Esquema do objeto
oc explain machineconfig.spec
```

## Como interpretar a saída

- Colunas de `oc get machineconfigs` (**ilustrativo**): `NAME`, `GENERATEDBYCONTROLLER`, `IGNITIONVERSION`, `AGE`. Itens com `GENERATEDBYCONTROLLER` preenchido foram gerados pela plataforma; os vazios, em geral, foram criados por administradores.
- O nome do rendered em `status.configuration.name` muda (novo hash) quando algum MachineConfig do pool muda.
- **Cuidado:** um MachineConfig pode conter arquivos com dados sensíveis (certificados, por exemplo). Prefira listar e explicar a despejar `-o yaml` completo.

## Diferenças e confusões frequentes

- **MachineConfig × ConfigMap:** o MachineConfig configura o **SO do nó**; o ConfigMap configura **aplicações**.
- **MachineConfig × Machine:** a configuração da máquina × a própria máquina (Machine API).
- **MachineConfig de origem × rendered:** o rendered é gerado pela plataforma; não o edite.

## No OpenShift 4.22 versus Kubernetes

Recurso exclusivo do OpenShift, ligado ao RHCOS e ao MCO.

## No HomeLab SNO

Criar ou alterar MachineConfig no SNO **reinicia o único nó** na maioria dos casos. Para estudo, limite-se a listar e a usar `oc explain`.

## Termos relacionados

[Machine Config Operator](machine-config-operator.md) · [MachineConfigPool](machineconfigpool.md) · [kubelet](kubelet.md) · [CRI-O](cri-o.md) · [Manifest](../../00-fundamentos-e-linguagem/verbetes/manifest.md)

## Fontes oficiais

- OCP 4.22 — "Machine config overview" (ordem lexicográfica, rendered, herança e sobreposição desde o 4.15, `/etc` e `/var`, Ignition; fonte: `modules/machine-config-overview.adoc`)
- OCP 4.22 — Machine configuration overview (fonte: `machine_configuration/index.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 01-arquitetura-e-control-plane/machineconfig
- **Termo original:** MachineConfig
- **Remissões:** machine config, rendered MachineConfig
- **Tradução:** não se traduz
- **Classe ontológica:** objeto da API (OpenShift)
- **API:** `apiVersion: machineconfiguration.openshift.io/v1`, `kind: MachineConfig`
- **Plataforma:** OpenShift
- **Escopo:** cluster-scoped
- **Disponibilidade:** nativo
- **Versões validadas:** OCP 4.22
- **Nível:** intermediário → avançado
- **Atualizado em:** 2026-11-04

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** as colunas de `oc get machineconfigs`, o caminho `status.configuration.name` e a label `machineconfiguration.openshift.io/role` são conhecidos, mas **não foram verificados** no SNO.

</details>
