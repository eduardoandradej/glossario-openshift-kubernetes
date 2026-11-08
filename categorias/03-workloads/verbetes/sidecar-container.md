# Sidecar Container

## Definição em uma frase

Um Sidecar Container é um **contêiner auxiliar que roda ao lado da aplicação no mesmo [Pod](pod.md)** durante toda a vida dele. No Kubernetes atual, é declarado como um [init container](init-container.md) com `restartPolicy: Always`.

## Explicação didática

O nome vem do side-car da motocicleta: vai junto, o tempo todo, com uma função de apoio. Exemplos: coletar logs, fazer proxy de rede, renovar certificados.

O Kubernetes 1.29 em diante oferece um jeito **nativo** de declará-lo:

```yaml
# Ilustrativo
spec:
  initContainers:
  - name: coletor-de-logs
    image: <imagem>
    restartPolicy: Always   # é isso que o torna sidecar
  containers:
  - name: app
    image: <imagem>
```

## Para que existe e qual problema resolve

Antes do suporte nativo, sidecars eram contêineres comuns em `containers`, sem garantia de ordem: podiam iniciar depois da aplicação ou impedir um Job de terminar. O sidecar nativo resolve isso:

- **inicia antes** dos contêineres da aplicação e segue rodando;
- **termina depois** deles, no encerramento do Pod;
- **não impede** um Job de concluir.

## Funcionamento técnico e ciclo de vida

- Inicia na ordem dos init containers; o próximo init container ou a aplicação começa assim que o sidecar **está iniciado** (e não concluído).
- É reiniciado sempre que termina, independentemente da [Restart Policy](restart-policy.md) do Pod.
- **Suporta probes** (`startupProbe`, `readinessProbe`, `livenessProbe`) e hooks de ciclo de vida, diferentemente dos init containers comuns.
- Recurso `SidecarContainers` ativo por padrão desde o Kubernetes 1.29.

## Relações e dependências

- Forma especial de [Init Container](init-container.md).
- Muito usado em *service meshes* (proxies de rede) e em coleta de logs.

## Exemplo de situação real

Um Job com um sidecar de envio de logs declarado em `containers` nunca terminava: o sidecar ficava rodando depois do fim da tarefa. Declarado como sidecar nativo, o Job conclui quando o contêiner principal termina, e o sidecar é encerrado em seguida.

## Como visualizar e inspecionar (somente leitura)

```bash
# Init containers com restartPolicy: Always (sidecars nativos)
oc get pod <nome> -n <namespace> -o jsonpath='{range .spec.initContainers[*]}{.name} restartPolicy={.restartPolicy}{"\n"}{end}'

# Logs do sidecar
oc logs <nome> -n <namespace> -c <sidecar>
```

## Como interpretar a saída

- `restartPolicy=Always`: sidecar nativo.
- Vazio: init container comum, que deve terminar.

## Diferenças e confusões frequentes

- **Sidecar nativo × contêiner extra em `containers`:** o primeiro tem ordem garantida de início e fim; o segundo não.
- **Sidecar × Ephemeral Container:** o sidecar é parte permanente do Pod; o [Ephemeral Container](ephemeral-container.md) é temporário, para depuração.

## No OpenShift 4.22 versus Kubernetes

Disponível conforme o Kubernetes 1.35. Componentes do OpenShift (como o service mesh) podem injetar sidecars automaticamente.

## No HomeLab SNO

Útil para estudar padrões de logs e proxies sem alterar a imagem da aplicação.

## Termos relacionados

[Init Container](init-container.md) · [Ephemeral Container](ephemeral-container.md) · [Restart Policy](restart-policy.md) · [Pod](pod.md) · [Job](job.md)

## Fontes oficiais

- Kubernetes — Sidecar Containers: <https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/> (fonte: `kubernetes/website` `release-1.35`, `concepts/workloads/pods/sidecar-containers.md`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/sidecar-container
- **Termo original:** sidecar container
- **Remissões:** native sidecar, SidecarContainers
- **Tradução:** contêiner auxiliar (só como apoio)
- **Classe ontológica:** padrão de uso / componente do Pod
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo (ativo por padrão desde o Kubernetes 1.29)
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** intermediário
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-08.
- **Pendências:** confirmar se o service mesh do OCP 4.22 injeta sidecars nativos ou em `containers`.

</details>
