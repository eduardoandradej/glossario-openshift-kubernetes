# Master Node

## Definição em uma frase

"Master" é o **termo legado** para os nós que hospedam o [Control Plane](control-plane.md). No Kubernetes atual o termo correto é *control plane node*; no OpenShift, `master` continua sendo o nome do **papel de máquina** (*machine role*) desses nós.

## Explicação didática

A documentação do Kubernetes trata "master" como sinônimo antigo de nó de Control Plane, ainda usado por algumas ferramentas, como o kubeadm, e por serviços gerenciados para rotular nós e controlar o posicionamento de Pods. A comunidade trocou o termo por **control plane**.

No OpenShift, o nome sobrevive na **infraestrutura**: as máquinas de Control Plane têm o papel `master`, e o pool de configuração delas se chama `master`. Por isso você verá os dois nomes convivendo.

## Para que existe e qual problema resolve

Como termo, não resolve nada novo: é só histórico. Saber que existe evita confusão ao ler documentação antiga, labels de nós e nomes de pools.

## Funcionamento técnico e ciclo de vida

- Labels de nós de Control Plane: `node-role.kubernetes.io/control-plane` (atual) e, no OpenShift, também `node-role.kubernetes.io/master`.
- No OpenShift, o papel `master` define máquinas que rodam os serviços Kubernetes **e** os do OpenShift (API server, controller manager, OAuth).
- O papel `bootstrap` também existe, mas só é usado durante a instalação.

## Relações e dependências

- Hospeda o [Control Plane](control-plane.md); contraparte do [Worker Node](worker-node.md).

## Exemplo de situação real

Um tutorial antigo manda rodar `kubectl get nodes -l node-role.kubernetes.io/master`. No OpenShift 4.22 isso ainda funciona, porque o papel existe. Num Kubernetes upstream recente, a label `master` pode nem existir, e o comando correto usa `control-plane`.

## Como visualizar e inspecionar (somente leitura)

```bash
# Os dois rótulos, lado a lado
oc get nodes -L node-role.kubernetes.io/control-plane,node-role.kubernetes.io/master

# OpenShift: o pool de configuração dos nós de Control Plane se chama "master"
oc get machineconfigpool master
```

## Como interpretar a saída

- Colunas com valor vazio (`""`) também significam "label presente": labels de papel geralmente não têm valor. Ausência total aparece como `<none>` ou coluna em branco, conforme o cliente.
- O pool `master` com `UPDATED=True` indica configuração aplicada em todos os nós de Control Plane.

## Diferenças e confusões frequentes

- **Master (termo) × Control Plane (função):** prefira *Control Plane* no texto; use `master` só quando for o nome literal de um papel, label ou pool.
- **"Master" não roda aplicações**, em regra. No SNO e em clusters compactos de três nós, o mesmo nó também tem o papel `worker`.

## No OpenShift 4.22 versus Kubernetes

O Kubernetes considera o termo legado. O OpenShift 4.22 ainda usa `master` como papel e pool, ao lado do rótulo `control-plane`.

## No HomeLab SNO

O nó único mostra `control-plane,master,worker` em `ROLES`.

## Termos relacionados

[Control Plane](control-plane.md) · [Worker Node](worker-node.md) · [Static Pod](static-pod.md) · [Label](../../00-fundamentos-e-linguagem/verbetes/label.md)

## Fontes oficiais

- Kubernetes Glossary — Master ("Legacy term"): <https://kubernetes.io/docs/reference/glossary/?all=true#term-master> (fonte: `kubernetes/website` `release-1.35`, `reference/glossary/master.md`)
- OCP 4.22 — Control plane architecture, "Machine roles" (papéis `master`, `worker`, `bootstrap`): <https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/architecture/control-plane> (fonte: `modules/architecture-machine-roles.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 01-arquitetura-e-control-plane/master-node
- **Termo original:** master, master node
- **Tradução:** nó mestre (só como apoio)
- **Classe ontológica:** legado (termo) / papel de máquina no OpenShift
- **Plataforma:** Kubernetes (termo legado) / OpenShift (nome do papel `master`)
- **Escopo:** não aplicável
- **Disponibilidade:** termo legado no Kubernetes; ainda usado como papel no OpenShift
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-04

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** confirmar no SNO a presença das duas labels e a forma como `-L` exibe labels de valor vazio, o que **não foi executado**.

</details>
