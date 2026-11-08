# Pod Template

## Definição em uma frase

O Pod Template (`spec.template`) é o **molde de Pod** embutido num workload (Deployment, StatefulSet, DaemonSet, Job...), a partir do qual o controller cria os Pods reais.

## Explicação didática

Um Deployment não guarda Pods: guarda a **receita** de como cada Pod deve ser. O controller lê essa receita e cria quantos Pods forem pedidos. O template faz parte do [Desired State](../../00-fundamentos-e-linguagem/verbetes/desired-state.md) do workload.

```yaml
# Trecho didático de um Job
spec:
  template:            # <- começa o Pod Template
    spec:
      containers:
      - name: hello
        image: <imagem>
      restartPolicy: OnFailure
                       # <- termina o Pod Template
```

## Para que existe e qual problema resolve

Separa "como deve ser cada Pod" de "quantos e de que forma manter", permitindo que vários controllers compartilhem o mesmo formato de Pod.

## Funcionamento técnico e ciclo de vida

- **Mudar o template não altera os Pods existentes.** O workload cria Pods **novos** com o template atualizado e substitui os antigos, segundo as suas próprias regras (rollout no Deployment, atualização ordenada no StatefulSet...).
- No [Deployment](deployment.md), **só** mudanças no template disparam um rollout; mudar apenas `replicas` não cria uma nova revisão.
- O kubelet não sabe nada de templates: só recebe Pods prontos.
- Existe também o objeto `PodTemplate` na API (grupo *core*), pouco usado diretamente; o uso comum é o campo `spec.template` dos workloads.

## Relações e dependências

- Faz parte de [Deployment](deployment.md), [ReplicaSet](replicaset.md), [StatefulSet](statefulset.md), [DaemonSet](daemonset.md) e [Job](job.md).
- Gera [Pods](pod.md); suas labels precisam casar com o seletor do workload ([Selector](../../00-fundamentos-e-linguagem/verbetes/selector.md)).

## Exemplo de situação real

Alguém edita a imagem diretamente num Pod de um Deployment. Na próxima recriação, a imagem antiga volta. A mudança precisava ser feita no **template** do Deployment.

## Como visualizar e inspecionar (somente leitura)

```bash
# O template de um Deployment
oc get deployment <nome> -n <namespace> -o jsonpath='{.spec.template}' ; echo

# Imagens definidas no template
oc get deployment <nome> -n <namespace> -o jsonpath='{range .spec.template.spec.containers[*]}{.name}: {.image}{"\n"}{end}'

# Esquema do campo
oc explain deployment.spec.template
```

## Como interpretar a saída

- O template tem a forma de um Pod (com `metadata.labels` e `spec`), mas sem `status`.
- A label `pod-template-hash` nos Pods e ReplicaSets de um Deployment identifica de qual versão do template eles vieram.

## Diferenças e confusões frequentes

- **Pod Template × Pod:** molde × instância.
- **Template × Helm/OpenShift Template:** "template" aqui é um campo do workload; Helm e o objeto `Template` do OpenShift são ferramentas de empacotamento (categoria 15).

## No OpenShift 4.22 versus Kubernetes

Igual ao Kubernetes.

## No HomeLab SNO

Estude templates com `oc explain` e `-o jsonpath`; altere apenas workloads de projetos de estudo.

## Termos relacionados

[Pod](pod.md) · [Deployment](deployment.md) · [ReplicaSet](replicaset.md) · [Spec](../../00-fundamentos-e-linguagem/verbetes/spec.md) · [Selector](../../00-fundamentos-e-linguagem/verbetes/selector.md)

## Fontes oficiais

- Kubernetes — Pods, "Pod templates" e "Pod update and replacement": <https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates> (fonte: `kubernetes/website` `release-1.35`)
- Kubernetes — Deployments (rollout só com mudança no template): <https://kubernetes.io/docs/concepts/workloads/controllers/deployment/>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/pod-template
- **Termo original:** Pod template (`spec.template`)
- **Remissões:** PodTemplate (objeto)
- **Tradução:** modelo de Pod (só como apoio)
- **Classe ontológica:** conceito (campo dos workloads)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-08.
- **Pendências:** a existência do objeto `PodTemplate` no grupo *core* deve ser confirmada com `oc api-resources | grep podtemplates`.

</details>
