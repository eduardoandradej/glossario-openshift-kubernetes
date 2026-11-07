# BareMetalHost

## Definição em uma frase

Um BareMetalHost é o objeto que **representa um servidor físico** para o **Bare Metal Operator** do OpenShift: endereço da BMC, estado de energia, dados de hardware e estado de provisionamento.

## Explicação didática

Na nuvem, uma [Machine](machine.md) vira uma VM criada pela API do provedor. Em bare metal, não há API de nuvem: é preciso controlar servidores reais, ligá-los, desligá-los e instalar o sistema neles. O BareMetalHost é o "cadastro" de cada servidor, com o que o Operator precisa para controlá-lo remotamente pela **BMC** (*Baseboard Management Controller*, como IPMI ou Redfish).

## Para que existe e qual problema resolve

Permite que a Machine API funcione também em bare metal: provisionar, inspecionar e reutilizar servidores físicos de forma declarativa.

## Funcionamento técnico e ciclo de vida

- **`spec`:** o estado desejado do host, como o endereço e as credenciais da BMC (por referência a um Secret), a imagem de boot, o estado de energia desejado e o modo de limpeza automática dos discos.
- **`status`:** o estado de provisionamento e os dados de hardware (CPUs, NICs com MAC, discos, energia atual). Os dados de hardware também ficam no objeto `HardwareData`.
- **Recursos relacionados do Bare Metal Operator:** `HostFirmwareSettings`, criado quando o host chega ao estado `Available`, a partir das configurações de firmware lidas pelo serviço Ironic; e ainda `FirmwareSchema`, `HostFirmwareComponents` e `HostUpdatePolicy`.
- Ficam no namespace `openshift-machine-api`.

## Relações e dependências

- Associado a uma [Machine](machine.md) em instalações bare metal com integração de plataforma.
- As credenciais da BMC ficam em Secrets (categoria 06).

## Exemplo de situação real

Para acrescentar um worker a um cluster bare metal, o administrador cria um BareMetalHost com o endereço da BMC do servidor novo. O Operator inspeciona o hardware, o host fica `Available`, e um MachineSet pode então provisioná-lo como nó.

## Como visualizar e inspecionar (somente leitura)

```bash
# Hosts físicos e estado
oc get baremetalhosts -n openshift-machine-api

# Dados de hardware de um host
oc get hardwaredata <nome> -n openshift-machine-api -o yaml

# A API existe neste cluster?
oc api-resources --api-group=metal3.io
```

## Como interpretar a saída

- A coluna de estado mostra o ciclo de provisionamento (por exemplo, `available`, `provisioned`). Confira os valores com `oc explain baremetalhost.status.provisioning.state`.
- **Não** exiba o Secret de credenciais da BMC.
- API ausente (`metal3.io`) indica um cluster sem integração de plataforma bare metal, como um SNO com `platform: none`.

## Diferenças e confusões frequentes

- **BareMetalHost × Machine × Node:** servidor físico × máquina da Machine API × nó do Kubernetes.
- **BMC × SO do servidor:** a BMC é o controlador de gerenciamento fora de banda, independente do SO.

## No OpenShift 4.22 versus Kubernetes

Recurso do ecossistema Metal3 integrado ao OpenShift, sem equivalente no Kubernetes upstream.

## No HomeLab SNO

**Provavelmente não instalado:** um SNO em KVM com `platform: none` não usa o Bare Metal Operator.

## Termos relacionados

[Machine](machine.md) · [MachineSet](machineset.md) · [Node](node.md) · [Secret](../../06-configuracao-e-api/verbetes/secret.md)

## Fontes oficiais

- OCP 4.22 — Bare Metal Operator, "About the BareMetalHost resource" e "Bare Metal Operator architecture" (fontes: `modules/bmo-about-the-baremetalhost-resource.adoc`, `modules/bmo-bare-metal-operator-architecture.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/baremetalhost
- **Termo original:** BareMetalHost
- **Remissões:** Bare Metal Operator, Metal3, HardwareData, HostFirmwareSettings, BMC
- **Tradução:** host bare metal (só como apoio)
- **Classe ontológica:** objeto da API (extensão)
- **API:** `metal3.io` (versão a confirmar), `kind: BareMetalHost`
- **Plataforma:** OpenShift (bare metal)
- **Escopo:** namespaced (`openshift-machine-api`)
- **Disponibilidade:** depende da plataforma bare metal com o Bare Metal Operator
- **Versões validadas:** OCP 4.22
- **Nível:** avançado
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** a versão do grupo `metal3.io` e os valores de estado de provisionamento devem ser conferidos num cluster bare metal, que **não está disponível** no HomeLab.

</details>
