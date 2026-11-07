# Machine

## Definição em uma frase

Uma Machine é o objeto da **Machine API do OpenShift** que descreve o **host por trás de um nó**: a máquina de infraestrutura (VM na nuvem, host bare metal) que, depois de provisionada, se torna um [Node](node.md) do cluster.

## Explicação didática

O Node é a visão do Kubernetes ("existe um nó que roda Pods"); a Machine é a visão da infraestrutura ("existe uma VM deste tipo, nesta zona, criada por este provedor"). Com a Machine API, o OpenShift consegue **criar, substituir e remover máquinas** sozinho, em vez de depender de alguém para provisionar servidores.

Cada Machine tem um `providerSpec`, que descreve os detalhes da plataforma: tipo de instância, imagem, zona, discos.

## Para que existe e qual problema resolve

Torna o provisionamento de nós **declarativo e elástico**: após a instalação, a Machine API cuida de todas as ações de provisionamento de hosts.

## Funcionamento técnico e ciclo de vida

- A Machine API combina recursos baseados no projeto upstream **Cluster API** com recursos próprios do OpenShift.
- Uma Machine passa por **fases** (como `Provisioning`, `Provisioned`, `Running`, `Deleting`, `Failed`) até virar um Node que entra no cluster.
- Normalmente, as Machines são criadas e mantidas por um [MachineSet](machineset.md), e não individualmente.
- As Machines de Control Plane são gerenciadas por *control plane machine sets*, nas plataformas suportadas, ou como recursos avulsos.
- Ficam no namespace `openshift-machine-api`.

## Relações e dependências

- Corresponde a um [Node](node.md) (o `status.nodeRef` aponta para ele).
- Gerenciada por [MachineSet](machineset.md) e remediada por [MachineHealthCheck](machinehealthcheck.md).
- Em bare metal, associa-se a um [BareMetalHost](baremetalhost.md).

## Exemplo de situação real

Um nó some do cluster. A Machine correspondente mostra a fase `Failed`. Se houver um MachineHealthCheck, ele apaga essa Machine, e o MachineSet cria uma nova, que vira um nó novo.

## Como visualizar e inspecionar (somente leitura)

```bash
# Machines e fases
oc get machines -n openshift-machine-api -o wide

# Relação Machine → Node
oc get machine <nome> -n openshift-machine-api -o jsonpath='{.status.nodeRef.name} {.status.phase}{"\n"}'

# A Machine API está disponível neste cluster?
oc api-resources --api-group=machine.openshift.io
```

## Como interpretar a saída

- `PHASE=Running` com `NODE` preenchido: a máquina está provisionada e associada a um nó.
- `Provisioning` por muito tempo: problema no provedor (cota, credenciais, imagem).
- Nenhuma Machine listada pode significar uma instalação sem integração de plataforma, como `platform: none`, em que as máquinas não são gerenciadas pela Machine API.

## Diferenças e confusões frequentes

- **Machine × Node:** infraestrutura × visão do Kubernetes.
- **Machine × MachineConfig:** a máquina × a configuração do SO dela.
- **Machine (OpenShift) × Machine (Cluster API upstream):** baseadas no mesmo projeto, mas os recursos do OpenShift ficam no grupo `machine.openshift.io`.

## No OpenShift 4.22 versus Kubernetes

O Kubernetes upstream não tem Machine API nativa (existe o projeto Cluster API, à parte). No OpenShift, ela é parte da plataforma nas instalações integradas a um provedor.

## No HomeLab SNO

Num SNO com `platform: none`, a Machine API normalmente **não gerencia** o nó: pode não haver Machines nem MachineSets. Confira com os comandos acima.

## Termos relacionados

[MachineSet](machineset.md) · [MachineHealthCheck](machinehealthcheck.md) · [BareMetalHost](baremetalhost.md) · [Node](node.md) · [MachineConfig](../../01-arquitetura-e-control-plane/verbetes/machineconfig.md)

## Fontes oficiais

- OCP 4.22 — Machine management, "Machine API overview" (Machine, `providerSpec`, base no Cluster API, control plane machine sets; fonte: `modules/machine-api-overview.adoc`): <https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/index>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/machine
- **Termo original:** Machine
- **Remissões:** Machine API, providerSpec
- **Tradução:** máquina (só como apoio)
- **Classe ontológica:** objeto da API (OpenShift)
- **API:** `machine.openshift.io/v1beta1`, `kind: Machine`
- **Plataforma:** OpenShift
- **Escopo:** namespaced (`openshift-machine-api`)
- **Disponibilidade:** nativo em instalações integradas a uma plataforma; pode não ser usado com `platform: none`
- **Versões validadas:** OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** a versão do grupo (`v1beta1`), a lista de fases (documentação "Machine phases and lifecycle", não lida) e o comportamento no SNO com `platform: none` devem ser conferidos com `oc api-resources` e `oc explain machine`. **Não executado**.

</details>
