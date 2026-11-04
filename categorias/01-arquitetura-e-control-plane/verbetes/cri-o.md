# CRI-O

> **ID:** 01-arquitetura-e-control-plane/cri-o | **Termo original:** CRI-O | **Tradução:** não se traduz | **Classe ontológica:** componente (container engine / runtime de alto nível) | **Plataforma:** Kubernetes (opcional) / OpenShift (obrigatório) | **Escopo:** não aplicável (roda em cada nó) | **Disponibilidade:** nativo no OpenShift 4.x | **Versões validadas:** Kubernetes 1.35 / OCP 4.22 | **Nível:** intermediário | **Atualizado em:** 2026-11-04

## Definição em uma frase

O CRI-O é uma **implementação da [CRI](cri.md)** feita para usar runtimes compatíveis com a OCI no Kubernetes. É o **container engine do OpenShift**.

## Explicação didática

O CRI-O faz uma coisa e foca nela: atender o kubelet. Ele baixa imagens OCI de registries, prepara os contêineres e chama um runtime de baixo nível (no OpenShift, o **crun** por padrão) para criá-los. Não é uma ferramenta de linha de comando de uso geral como o Docker ou o Podman.

## Para que existe e qual problema resolve

Oferece um runtime **mínimo e alinhado às versões do Kubernetes**, sem funcionalidades que o cluster não usa. No OpenShift, a documentação descreve o CRI-O como integrado ao sistema operacional, para uma experiência Kubernetes eficiente, e diz que ele substituiu por completo o Docker Container Engine do OpenShift 3.

## Funcionamento técnico e ciclo de vida

- Roda como **serviço systemd** (`crio`) em todos os nós, de Control Plane e de compute, e precisa estar ativo antes de qualquer contêiner.
- Atende o kubelet pela CRI (gRPC): *sandboxes* de Pod, contêineres e imagens.
- Usa um runtime OCI de baixo nível: **crun** (padrão no OCP 4.22) ou **runC** (configurável por `ContainerRuntimeConfig`).
- Faz parte do RHCOS e é atualizado junto com a plataforma.

## Relações e dependências

- Implementa a [CRI](cri.md) para o [kubelet](kubelet.md); é o [Container Runtime](container-runtime.md) do OpenShift.
- Busca imagens em registries (categoria 10).

## Exemplo de situação real

Pods de um nó ficam em `ContainerCreating`, e o kubelet reporta que o runtime não responde. Os logs do CRI-O mostram disco cheio em `/var/lib/containers`. Sem espaço, o CRI-O não consegue preparar novas camadas de imagem.

## Como visualizar e inspecionar (somente leitura)

```bash
# Versão do CRI-O em cada nó
oc get nodes -o wide

# Logs do serviço crio (permissão de administrador)
oc adm node-logs <nó> -u crio --tail=50

# Configuração de runtime aplicada pela plataforma (se houver)
oc get containerruntimeconfigs
```

## Como interpretar a saída

- `CONTAINER-RUNTIME` como `cri-o://1.35.x` (ilustrativo): a versão do CRI-O acompanha a versão menor do Kubernetes.
- `oc get containerruntimeconfigs` vazio significa que o cluster usa os padrões (crun). Um item listado indica personalização feita pelo administrador.

## Diferenças e confusões frequentes

- **CRI-O ≠ Podman:** o Podman é uma ferramenta para pessoas e scripts; o CRI-O serve o kubelet. Os dois usam bibliotecas em comum e o mesmo armazenamento de imagens no nó.
- **CRI-O ≠ crun/runC:** alto nível × baixo nível.
- **CRI-O ≠ CRI:** implementação × interface.

## No OpenShift 4.22 versus Kubernetes

No Kubernetes upstream, o CRI-O é **uma** das opções de runtime; no OpenShift 4, é **a** opção, mantida pela plataforma.

## No HomeLab SNO

O CRI-O do único nó roda todos os contêineres do cluster. Monitore o espaço em disco do nó; não limpe imagens à mão, porque a coleta do kubelet cuida disso.

## Termos relacionados

[CRI](cri.md) · [Container Runtime](container-runtime.md) · [kubelet](kubelet.md) · [Worker Node](worker-node.md) · [Control Plane](control-plane.md)

## Fontes oficiais

- Kubernetes Glossary — CRI-O: <https://kubernetes.io/docs/reference/glossary/?all=true#term-cri-o> (fonte: `kubernetes/website` `release-1.35`, `reference/glossary/cri-o.md`)
- OCP 4.22 — Architecture overview, "Custom operating system" (CRI-O integrado ao RHCOS; substitui o Docker): <https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/architecture/architecture> (fonte: `modules/architecture-platform-benefits.adoc`)
- OCP 4.22 — Control plane architecture, "Machine roles" (CRI-O como systemd; crun/runC): <https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/architecture/control-plane>
- Projeto CRI-O (fonte externa): <https://cri-o.io/>

<details>
<summary>Notas de revisão</summary>

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** confirmar que a versão do CRI-O no OCP 4.22 segue a 1.35, que o recurso `containerruntimeconfigs` responde com esse nome e o caminho de armazenamento citado (`/var/lib/containers`). Nada disso foi **verificado** nesta rodada.

</details>
