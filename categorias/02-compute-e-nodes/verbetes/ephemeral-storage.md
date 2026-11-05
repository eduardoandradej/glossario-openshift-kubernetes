# Ephemeral Storage (recurso `ephemeral-storage`)

## Definição em uma frase

`ephemeral-storage` é o tipo de recurso que mede o **armazenamento local e temporário** usado por um Pod no disco do nó: camada gravável do contêiner, volumes `emptyDir` em disco e logs. Tudo isso desaparece com o Pod.

## Explicação didática

Mesmo sem PersistentVolume, um contêiner escreve em disco: arquivos temporários, caches, logs. Esse espaço vem do disco **do nó** e é dividido entre todos os Pods. Para que um Pod não encha o disco e derrube os outros, o Kubernetes permite pedir e limitar esse uso, como faz com CPU e memória.

## Para que existe e qual problema resolve

Evita que o disco do nó se esgote (`DiskPressure`), o que levaria a despejos em massa e, no limite, a um nó inoperante.

## Funcionamento técnico e ciclo de vida

Segundo a documentação, o kubelet contabiliza como armazenamento efêmero de um Pod:

- a escrita na **camada gravável** do contêiner (rootfs) e as imagens;
- a escrita em volumes **`emptyDir`** locais (em disco; os de memória contam como RAM);
- os **logs do próprio Pod** (geralmente em `/var/log/pods`);
- arquivos de sistema gerenciados pelo Kubernetes e mapeados no Pod (como `/etc/hosts`).

Com `requests.ephemeral-storage` e `limits.ephemeral-storage`, o scheduler considera o pedido, e o kubelet pode **despejar** o Pod que ultrapassar o limite.

## Relações e dependências

- Faz parte da [Capacity](capacity.md) e do [Allocatable](allocatable.md).
- Ligado à condição `DiskPressure` ([Node Condition](node-condition.md)).
- Não confundir com armazenamento persistente (PV/PVC, categoria 05).

## Exemplo de situação real

Um Pod que grava logs extensos em arquivo dentro do contêiner é despejado com uma mensagem citando `ephemeral-storage`. A solução é mandar os logs para a saída padrão, que o sistema de logs gerencia, ou usar um volume adequado, e definir um limite coerente.

## Como visualizar e inspecionar (somente leitura)

```bash
# Requests e limits de armazenamento efêmero
oc get pod <nome> -n <namespace> \
  -o jsonpath='{range .spec.containers[*]}{.name}: req={.resources.requests.ephemeral-storage} lim={.resources.limits.ephemeral-storage}{"\n"}{end}'

# Capacidade e alocável de armazenamento efêmero do nó
oc get node <nó> -o jsonpath='{.status.capacity.ephemeral-storage} / {.status.allocatable.ephemeral-storage}{"\n"}'

# Condição de disco do nó
oc get node <nó> -o jsonpath='{range .status.conditions[?(@.type=="DiskPressure")]}{.status} {.message}{"\n"}{end}'
```

## Como interpretar a saída

- Campos vazios em requests e limits significam que o Pod não declarou uso de disco efêmero. Ele pode usar o disco livremente, até haver pressão no nó.
- `DiskPressure=True` no nó antecede despejos por disco.

## Diferenças e confusões frequentes

- **Ephemeral storage × PersistentVolume:** temporário e local × persistente e independente do Pod.
- **`emptyDir` em disco × `emptyDir` em memória:** o primeiro conta como armazenamento efêmero; o segundo, como memória.

## No OpenShift 4.22 versus Kubernetes

Mesmo modelo. No OpenShift, o armazenamento efêmero dos Pods fica no disco do nó, em `/var`, que no RHCOS é compartilhado com imagens e logs.

## No HomeLab SNO

Um único disco atende o SO, as imagens, os logs e o armazenamento efêmero de todos os Pods. Acompanhe `DiskPressure` com atenção.

## Termos relacionados

[Capacity](capacity.md) · [Allocatable](allocatable.md) · [Node Condition](node-condition.md) · [Resource Request](resource-request.md) · [Resource Limit](resource-limit.md) · [PersistentVolume](../../05-storage/verbetes/persistentvolume.md)

## Fontes oficiais

- Kubernetes — Resource Management for Pods and Containers, "Local ephemeral storage" e "Resource monitoring for local ephemeral storage": <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> (fonte: `kubernetes/website` `release-1.35`)
- Kubernetes — Ephemeral Storage: <https://kubernetes.io/docs/concepts/storage/ephemeral-storage/>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 02-compute-e-nodes/ephemeral-storage
- **Termo original:** local ephemeral storage (`ephemeral-storage`)
- **Tradução:** armazenamento efêmero (só como apoio)
- **Classe ontológica:** conceito (tipo de recurso computacional)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-05

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-05.
- **Pendências:** a página "Ephemeral Storage" foi citada pelo link da página principal e **não foi lida**. A afirmação sobre `/var` no RHCOS deve ser conferida na documentação do RHCOS.

</details>
