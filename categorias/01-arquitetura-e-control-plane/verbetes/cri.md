# CRI (Container Runtime Interface)

## Definição em uma frase

A CRI é a **interface de plugin**, um protocolo **gRPC**, pela qual o [kubelet](kubelet.md) conversa com o [Container Runtime](container-runtime.md). Com ela, o Kubernetes usa vários runtimes sem precisar recompilar seus componentes.

## Explicação didática

É uma "tomada padrão": qualquer runtime que implemente a CRI (CRI-O, containerd...) pode ser plugado no kubelet. O kubelet atua como **cliente** e se conecta aos serviços de *runtime* e de *imagem* expostos pelo runtime.

## Para que existe e qual problema resolve

Antes da CRI, o suporte a runtimes era embutido no próprio kubelet. A CRI desacoplou os dois: os runtimes evoluem por conta própria, e o Kubernetes só exige que eles falem o protocolo.

## Funcionamento técnico e ciclo de vida

- **Transporte:** gRPC. O endereço do runtime é configurado no kubelet (flag `--container-runtime-endpoint`).
- **Versão da API:** a partir do Kubernetes **1.26**, o kubelet exige que o runtime suporte a CRI **`v1`**; sem isso, o nó não se registra.
- **Serviços:** um para runtime (sandboxes de Pod e contêineres) e outro para imagens (pull, listagem, remoção).
- **Atualizações:** ao atualizar o Kubernetes no nó, o kubelet reinicia; se o runtime não suportar a `v1`, o kubelet falha ao registrar o nó.

## Relações e dependências

- Liga o [kubelet](kubelet.md) ao [Container Runtime](container-runtime.md), no OpenShift o [CRI-O](cri-o.md).

## Exemplo de situação real

Depois de uma atualização manual num Kubernetes genérico, um nó não volta como `Ready`, e os logs do kubelet citam incompatibilidade da API CRI. O runtime antigo não suporta a CRI `v1`. No OpenShift isso não acontece, porque o SO, o kubelet e o CRI-O são atualizados juntos, mas o conceito explica o porquê.

## Como visualizar e inspecionar (somente leitura)

A CRI não é um objeto da API; observe-a pelos componentes que a usam:

```bash
# Runtime reportado pelo kubelet via CRI
oc get nodes -o wide

# Logs do kubelet (mensagens sobre o runtime; permissão de administrador)
oc adm node-logs <nó> -u kubelet --tail=50

# Logs do CRI-O no nó
oc adm node-logs <nó> -u crio --tail=50
```

> A ferramenta `crictl` fala CRI direto com o runtime, mas exige acesso ao nó (por exemplo `oc debug node/<nó>`). Esse acesso é **administrativo**; use só com autorização e sem alterar nada.

## Como interpretar a saída

- `CONTAINER-RUNTIME` preenchido em `oc get nodes -o wide` é a prova indireta de que o kubelet está conversando com o runtime pela CRI.
- Mensagens nos logs do kubelet sobre `container runtime is down` ou `runtime not ready` indicam falha nessa conversa; veja então os logs do CRI-O.

## Diferenças e confusões frequentes

- **CRI ≠ OCI:** a CRI é o contrato kubelet ↔ runtime; a OCI (Open Container Initiative) define os formatos de imagem e de runtime de baixo nível.
- **CRI ≠ CNI ≠ CSI:** contêineres × rede (categoria 04) × armazenamento (categoria 05). São três interfaces de plugin distintas.

## No OpenShift 4.22 versus Kubernetes

O OpenShift usa a CRI com o CRI-O, e a compatibilidade é garantida pela plataforma, que entrega SO, kubelet e runtime testados juntos.

## No HomeLab SNO

Prefira `oc get nodes -o wide` e `oc adm node-logs`. `oc debug node` cria um Pod privilegiado no nó: é uma **ação administrativa**, que não deve ser feita sem necessidade.

## Termos relacionados

[Container Runtime](container-runtime.md) · [CRI-O](cri-o.md) · [kubelet](kubelet.md) · [Worker Node](worker-node.md)

## Fontes oficiais

- Kubernetes — Container Runtime Interface (CRI): <https://kubernetes.io/docs/concepts/containers/cri/> (fonte: `kubernetes/website` `release-1.35`, `concepts/containers/cri.md`)
- Kubernetes Glossary — CRI: <https://kubernetes.io/docs/reference/glossary/?all=true#term-cri>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 01-arquitetura-e-control-plane/cri
- **Termo original:** Container Runtime Interface (CRI)
- **Tradução:** interface de runtime de contêineres (só como apoio)
- **Classe ontológica:** conceito (interface / protocolo)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo (API `v1` estável desde o Kubernetes 1.23)
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-04

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** confirmar a unidade systemd `crio` em `oc adm node-logs -u crio` e as mensagens citadas, que **não foram verificadas**.

</details>
