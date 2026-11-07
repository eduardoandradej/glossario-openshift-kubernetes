# Node Debug (`oc debug node`)

## Definição em uma frase

`oc debug node/<nó>` é a forma recomendada no OpenShift de **abrir um shell de diagnóstico num nó**: o comando cria um Pod de debug privilegiado naquele nó, com o sistema de arquivos do host montado em `/host`.

## Explicação didática

Os nós do OpenShift rodam RHCOS, um sistema **imutável** gerenciado por Operators. A documentação **não recomenda** acessar os nós por SSH. Para investigar algo no host, como ver um serviço systemd ou gerar um `sosreport`, usa-se um Pod de debug:

1. `oc debug node/<nó>` cria o Pod `<nó>-debug` e abre um shell nele;
2. `chroot /host` faz do sistema de arquivos do host a raiz do shell, para usar os binários do próprio nó;
3. a partir daí, comandos como `systemctl status kubelet` ou `toolbox` (para o `sosreport`) rodam no contexto do host.

## Para que existe e qual problema resolve

Dá acesso controlado ao host sem SSH, auditado pela API e sujeito ao RBAC. A documentação admite o SSH só quando a API não está disponível ou o kubelet não funciona.

## Funcionamento técnico e ciclo de vida

- O Pod de debug é criado num namespace temporário e removido ao sair do shell.
- Ele é **privilegiado**: tem acesso amplo ao nó. Exige permissões de administrador (`cluster-admin`, na documentação de `sosreport`).
- **Nó com taint `NoExecute`:** a documentação sugere criar um namespace auxiliar com a annotation `scheduler.alpha.kubernetes.io/defaultTolerations` e iniciar o debug a partir dele.
- **`toolbox`:** contêiner auxiliar com binários de suporte, usado principalmente para gerar `sosreport` para o suporte da Red Hat.

## Relações e dependências

- Usa um Pod agendado no [Node](node.md); pode exigir [Toleration](toleration.md) se o nó tiver taints.
- Alternativa a SSH em nós RHCOS (RHCOS: lote 3 desta categoria).
- Logs de serviços do nó também podem ser lidos sem shell, com `oc adm node-logs` (ver [kubelet](../../01-arquitetura-e-control-plane/verbetes/kubelet.md)).

## Exemplo de situação real

O kubelet de um nó reinicia em ciclo. O administrador abre `oc debug node/<nó>`, faz `chroot /host` e lê o estado do serviço com `systemctl status kubelet` e `journalctl -u kubelet`. A causa é um disco cheio em `/var`.

## Como visualizar e inspecionar (somente leitura)

Antes de abrir um shell, prefira consultas sem acesso interativo:

```bash
# Logs de serviços do nó, sem abrir shell (permissão de administrador)
oc adm node-logs <nó> -u kubelet --tail=50
oc adm node-logs <nó> -u crio --tail=50
```

**Acesso administrativo ao nó (NÃO EXECUTAR AUTOMATICAMENTE; cria um Pod privilegiado):**

```bash
oc debug node/<nó>
# dentro do Pod de debug:
chroot /host
systemctl status kubelet      # leitura
journalctl -u kubelet -n 50   # leitura
exit
```

## Como interpretar a saída

- A mensagem inicial indica o nome do Pod de debug e o namespace temporário. Ao sair, ele é removido.
- Dentro do `chroot /host`, você está no host: comandos de alteração (editar arquivos, reiniciar serviços) **afetam o nó** e podem gerar *configuration drift* no MCO.

## Diferenças e confusões frequentes

- **`oc debug node` × `oc debug deployment/<x>`:** o primeiro abre um shell no **host**; o segundo cria uma cópia de um Pod da aplicação para depurá-la.
- **`oc debug node` × SSH:** suportado e auditado × desaconselhado, salvo emergência.
- **Shell no host não é "somente leitura":** o acesso é amplo; a disciplina de só ler é sua.

## No OpenShift 4.22 versus Kubernetes

O Kubernetes tem `kubectl debug node/<nó>`, com funcionamento parecido. O `oc debug node` com `chroot /host` e o `toolbox` são o procedimento documentado pelo OpenShift para nós RHCOS.

## No HomeLab SNO

No SNO, o Pod de debug roda no único nó, onde também está o Control Plane. Use-o só para leitura e encerre a sessão ao terminar. Alterações manuais no host do SNO são especialmente arriscadas.

## Termos relacionados

[Node](node.md) · [Toleration](toleration.md) · [kubelet](../../01-arquitetura-e-control-plane/verbetes/kubelet.md) · [CRI-O](../../01-arquitetura-e-control-plane/verbetes/cri-o.md) · [Machine Config Operator](../../01-arquitetura-e-control-plane/verbetes/machine-config-operator.md)

## Fontes oficiais

- OCP 4.22 — Gathering data about your cluster, "Generating a sosreport archive for an OpenShift Container Platform cluster node" (`oc debug node`, `chroot /host`, SSH não recomendado, toleration para nós `NoExecute`; fonte: `modules/support-generating-a-sosreport-archive.adoc`)
- OCP 4.22 — "About toolbox" (fonte: `modules/about-toolbox.adoc`)
- Kubernetes — Debugging Kubernetes Nodes With Kubectl (`kubectl debug node`): <https://kubernetes.io/docs/tasks/debug/debug-cluster/kubectl-node-debug/>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/node-debug
- **Termo original:** node debug (`oc debug node`)
- **Remissões:** debug pod, `chroot /host`, toolbox
- **Tradução:** depuração de nó (só como apoio)
- **Classe ontológica:** ferramenta / comando
- **Plataforma:** OpenShift (equivalente no Kubernetes: `kubectl debug node`)
- **Escopo:** não aplicável
- **Disponibilidade:** nativo; exige permissão de administrador
- **Versões validadas:** OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-07

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-07.
- **Pendências:** a página do Kubernetes sobre `kubectl debug node` foi citada pela URL conhecida e **não foi lida**. O namespace temporário criado pelo `oc debug` não foi conferido.

</details>
