# RHCOS (Red Hat Enterprise Linux CoreOS)

## Definição em uma frase

O RHCOS é o **sistema operacional dos nós do OpenShift**: baseado em componentes do RHEL, com imutabilidade controlada, atualizações atômicas via `rpm-ostree` e gestão remota pelo próprio cluster.

## Explicação didática

Num servidor RHEL comum, o administrador instala pacotes, edita arquivos e atualiza com `dnf`. No RHCOS, o modelo é outro: o SO é tratado como **parte da plataforma**. As atualizações chegam como uma **imagem**, aplicada de uma vez pelo [Machine Config Operator](../../01-arquitetura-e-control-plane/verbetes/machine-config-operator.md) junto com a atualização do OpenShift. As configurações são declaradas em [MachineConfig](../../01-arquitetura-e-control-plane/verbetes/machineconfig.md), e não feitas à mão.

## Para que existe e qual problema resolve

Garante que todos os nós tenham exatamente o mesmo SO, testado com aquela versão do OpenShift, e que o cluster consiga atualizar a si mesmo, inclusive o sistema operacional, de forma coordenada.

## Funcionamento técnico e ciclo de vida

Características destacadas pela documentação:

- **Baseado no RHEL:** o software vem em pacotes RPM, com as mesmas medidas de qualidade e segurança do RHEL.
- **Imutabilidade controlada:** a gestão é feita remotamente pelo cluster; poucas configurações podem ser alteradas diretamente.
- **CRI-O** como engine de contêineres (com crun como padrão; runC opcional) e um conjunto de ferramentas de contêiner (como `podman`) no lugar do CLI do Docker.
- **Atualizações `rpm-ostree`:** transacionais e atômicas, entregues como imagens de contêiner dentro do processo de atualização do OpenShift; a nova versão é preparada e ativada na reinicialização.
- **`bootupd`:** atualizações de firmware e de *boot loader*, que o `rpm-ostree` não cobre.
- **Ignition** na primeira inicialização (ver [Bootstrap](../../01-arquitetura-e-control-plane/verbetes/bootstrap.md)).
- **Layout de arquivos:**
  - `/usr`: binários e bibliotecas, **somente leitura**, e alterá-lo não é suportado;
  - `/etc`, `/boot` e `/var`: graváveis, mas a intenção é que sejam alterados **apenas pelo MCO**;
  - `/var/lib/containers`: armazenamento das imagens de contêiner.
- O Control Plane **precisa** rodar RHCOS; os nós de compute podem usar RHEL, com mais manutenção manual.

## Relações e dependências

- Gerenciado pelo [Machine Config Operator](../../01-arquitetura-e-control-plane/verbetes/machine-config-operator.md) e atualizado junto com o [Cluster Version Operator](../../01-arquitetura-e-control-plane/verbetes/cluster-version-operator.md).
- Inclui o [CRI-O](../../01-arquitetura-e-control-plane/verbetes/cri-o.md) e o [kubelet](../../01-arquitetura-e-control-plane/verbetes/kubelet.md).
- Acesso para diagnóstico: [Node Debug](node-debug.md).

## Exemplo de situação real

Um administrador acostumado ao RHEL tenta instalar um pacote num nó com `dnf install` e não consegue, porque o RHCOS não funciona assim. O caminho suportado é declarar a mudança num MachineConfig ou usar os recursos de *image mode* do RHCOS, conforme a documentação.

## Como visualizar e inspecionar (somente leitura)

```bash
# SO e versão do kernel de cada nó
oc get nodes -o wide

# Labels de SO do OpenShift
oc get nodes -L node.openshift.io/os_id,node.openshift.io/os_version

# Informações do SO no status do nó
oc get node <nó> -o jsonpath='{.status.nodeInfo.osImage}{"\n"}{.status.nodeInfo.kernelVersion}{"\n"}'
```

## Como interpretar a saída

- `OS-IMAGE` contendo "Red Hat Enterprise Linux CoreOS" indica RHCOS; `os_id=rhcos` confirma.
- A versão do RHCOS acompanha a versão do OpenShift; ela não é atualizada separadamente.

## Diferenças e confusões frequentes

- **RHCOS × RHEL:** imagem imutável gerenciada pelo cluster × SO de uso geral.
- **RHCOS × Fedora CoreOS:** o FCOS é a base comunitária usada pelo OKD.
- **Editar arquivos no nó ≠ configuração:** mudanças manuais podem causar *drift* no MCO e se perdem quando o nó é substituído.

## No OpenShift 4.22 versus Kubernetes

O Kubernetes não define o SO dos nós. O RHCOS é uma escolha e uma exigência do OpenShift (obrigatório no Control Plane).

## No HomeLab SNO

O nó único roda RHCOS. Use `oc debug node` só para leitura e mantenha qualquer configuração no MCO.

## Termos relacionados

[Machine Config Operator](../../01-arquitetura-e-control-plane/verbetes/machine-config-operator.md) · [MachineConfig](../../01-arquitetura-e-control-plane/verbetes/machineconfig.md) · [CRI-O](../../01-arquitetura-e-control-plane/verbetes/cri-o.md) · [Node Debug](node-debug.md) · [Bootstrap](../../01-arquitetura-e-control-plane/verbetes/bootstrap.md)

## Fontes oficiais

- OCP 4.22 — Architecture, "Red Hat Enterprise Linux CoreOS (RHCOS)" → "Key RHCOS features" (fontes: `architecture/architecture-rhcos.adoc`, `modules/rhcos-key-features.adoc`): <https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/architecture/architecture-rhcos>
- OCP 4.22 — Architecture overview, "Custom operating system" (fonte: `modules/architecture-platform-benefits.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/rhcos
- **Termo original:** Red Hat Enterprise Linux CoreOS (RHCOS)
- **Remissões:** rpm-ostree, bootupd, Ignition
- **Tradução:** não se traduz
- **Classe ontológica:** tecnologia (sistema operacional)
- **Plataforma:** OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo; obrigatório no Control Plane
- **Versões validadas:** OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** a versão do RHEL em que o RHCOS do OCP 4.22 se baseia **não foi confirmada** nesta rodada. O *image mode* (on-cluster layering) deve ser detalhado na categoria 13.

</details>
