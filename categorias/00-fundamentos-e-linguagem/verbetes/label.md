# Label

## Definição em uma frase

Labels são **pares chave/valor** anexados a objetos para expressar atributos **identificadores e relevantes para usuários**, e servem para **organizar e selecionar** conjuntos de objetos.

## Explicação didática

Pense em etiquetas coloridas em pastas: `app=loja`, `tier=frontend`, `environment=prod`. Diferente do [nome](resource-name.md), uma label **não é única**: muitos objetos podem ter a mesma, e é justamente isso que permite agrupá-los. Um [selector](selector.md) depois "pega" todos os objetos com determinadas etiquetas.

Labels **não têm significado para o núcleo do sistema** por si só. Quem dá sentido a elas são os seletores, as pessoas e as ferramentas.

## Para que existe e qual problema resolve

Aplicações reais são multidimensionais: versão, ambiente, camada, cliente, trilha de release. Labels permitem mapear essa organização sobre os objetos **sem hierarquia rígida** e permitem consultas e *watches* eficientes. Exemplos da documentação: `release: stable|canary`, `environment: dev|qa|production`, `tier: frontend|backend|cache`.

## Funcionamento técnico e ciclo de vida

**Sintaxe da chave:** `[prefixo/]nome`.
- **nome:** obrigatório; até 63 caracteres; começa e termina com alfanumérico; pode ter `-`, `_` e `.` no meio.
- **prefixo:** opcional; um subdomínio DNS de até 253 caracteres, seguido de `/`. Sem prefixo, a chave é considerada **privada do usuário**. Componentes automáticos que rotulam objetos de usuários **devem** usar prefixo.
- Os prefixos `kubernetes.io/` e `k8s.io/` são **reservados** aos componentes do Kubernetes.

**Valor:** até 63 caracteres (pode ser vazio); se não vazio, começa e termina com alfanumérico e pode ter `-`, `_` e `.` no meio.

Labels podem ser definidas na criação e alteradas a qualquer momento. Cada chave é única **dentro** de um objeto.

## Relações e dependências

- Ficam em [`metadata.labels`](metadata.md).
- São lidas por [Selectors](selector.md): Services encontram Pods, ReplicaSets contam Pods e NetworkPolicies escolhem alvos.
- Não confundir com [Annotations](annotation.md), que guardam dados **não identificadores**.

## Exemplo de situação real

Um Deployment com `selector.matchLabels: {app: loja}` e um template de Pod com `labels: {app: loja-web}` é **rejeitado**: o seletor precisa casar com as labels do template. Já um Service com seletor errado é aceito e simplesmente fica **sem endpoints**. Esse erro silencioso é muito comum.

## Como visualizar e inspecionar (somente leitura)

```bash
# Labels de todos os Pods do namespace
oc get pods -n <namespace> --show-labels

# Uma label como coluna
oc get pods -n <namespace> -L app,tier

# Filtrar por label (selector)
oc get pods -n <namespace> -l app=<valor>

# Labels de um objeto específico
oc get deployment <nome> -n <namespace> -o jsonpath='{.metadata.labels}' ; echo

# Labels dos nós (úteis para agendamento)
oc get nodes --show-labels
```

## Como interpretar a saída

- `--show-labels` mostra `chave=valor` separados por vírgula. Labels com prefixo (ex.: `pod-template-hash`, `kubernetes.io/metadata.name`) geralmente foram colocadas por controllers ou pela plataforma.
- `-L app` cria a coluna `APP`; vazio significa que o objeto não tem essa label.
- A label `pod-template-hash` nos Pods de Deployments é colocada pelo controller para distinguir os ReplicaSets de cada revisão. Não a altere.

## Diferenças e confusões frequentes

- **Label × annotation:** label identifica e seleciona; annotation documenta e alimenta ferramentas.
- **Label × nome:** label não é única; nome é.
- **Label ≠ dono:** quem define "quem é dono de quem" é `ownerReferences`, e não as labels. Ver [OwnerReference](owner-reference.md).
- **Maiúsculas importam:** `App=Loja` ≠ `app=loja`.

## No OpenShift 4.22 versus Kubernetes

O mecanismo é o mesmo. O OpenShift e o console usam labels de convenção, como `app.kubernetes.io/name`, `app.kubernetes.io/part-of` (agrupamento na *Topology* do console) e labels de nós como `node-role.kubernetes.io/<papel>`.

## No HomeLab SNO

Ler labels é seguro. **Não** rotule nem remova labels de nós e de objetos de plataforma: elas alimentam o agendamento, as políticas e os Operators.

## Termos relacionados

[Selector](selector.md) · [Annotation](annotation.md) · [Metadata](metadata.md) · [OwnerReference](owner-reference.md) · [Resource Name](resource-name.md) · [Service](../../04-networking/verbetes/service.md)

## Fontes oficiais

- Kubernetes — Labels and Selectors: <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/> (fonte: `kubernetes/website` `release-1.35`, `concepts/overview/working-with-objects/labels.md`)
- Kubernetes — Recommended Labels: <https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/>
- Kubernetes — Well-Known Labels, Annotations and Taints: <https://kubernetes.io/docs/reference/labels-annotations-taints/>

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 00-fundamentos-e-linguagem/label
- **Termo original:** label
- **Tradução:** rótulo, etiqueta
- **Classe ontológica:** conceito (campo `metadata.labels`)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável (vale para objetos de qualquer escopo)
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-04

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** as páginas "Recommended Labels" e "Well-Known Labels" foram citadas a partir dos links da página principal, mas **não foram lidas** nesta rodada. Confirmar o uso de `app.kubernetes.io/part-of` pela Topology do console do OCP 4.22.

</details>
