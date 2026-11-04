# Events

> **ID:** 00-fundamentos-e-linguagem/events | **Termo original:** Event | **Tradução:** evento | **Classe ontológica:** objeto da API | **API:** `kind: Event` em `events.k8s.io/v1` e, por compatibilidade, no grupo *core* (`v1`) | **Plataforma:** Kubernetes / OpenShift | **Escopo:** namespaced (o evento fica no namespace do objeto envolvido) | **Disponibilidade:** nativo | **Versões validadas:** Kubernetes 1.35 / OCP 4.22 | **Nível:** básico → intermediário | **Atualizado em:** 2026-11-04

## Definição em uma frase

Um Event é um objeto que descreve **uma mudança de estado ou uma ocorrência notável** no cluster ("Pod agendado", "imagem baixada", "falha ao montar volume"). É emitido por controllers e pelo kubelet e serve como **histórico curto e informativo**.

## Explicação didática

As [Conditions](conditions.md) mostram **como o objeto está agora**. Os Events contam **o que aconteceu até aqui**, como um diário de bordo. Quando um Pod não sobe, é nos Events que aparecem frases como `FailedScheduling`, `Failed to pull image` ou `Back-off restarting failed container`.

Mas é um diário de **memória curta**: os Events têm tempo de retenção limitado e devem ser tratados como dados **suplementares, de melhor esforço**.

## Para que existe e qual problema resolve

Dá visibilidade às ações automáticas dos controllers sem precisar abrir os logs de cada componente. É a primeira parada de quase todo diagnóstico.

## Funcionamento técnico e ciclo de vida

Campos principais (API `events.k8s.io/v1`):

| Campo | Significado |
|---|---|
| `regarding` | O objeto sobre o qual é o evento (no core v1: `involvedObject`) |
| `related` | Objeto secundário opcional (ex.: o Pod criado por um ReplicaSet) |
| `reason` | Motivo curto (ex.: `Scheduled`, `BackOff`) |
| `note` | Texto legível (no core v1: `message`) |
| `type` | `Normal` ou `Warning` |
| `action` | Ação tomada ou que falhou |
| `reportingController` | Quem emitiu (ex.: `kubernetes.io/kubelet`) |
| `series` | Agregação de ocorrências repetidas (`count`, `lastObservedTime`) |

- **Duas representações:** a API `events.k8s.io/v1` é a mais nova; o kind `Event` do grupo *core* continua servido, e o campo `deprecatedSource` mantém a compatibilidade entre elas.
- **Retenção:** limitada. O kube-apiserver apaga eventos antigos depois de um tempo configurável (`--event-ttl`); no OpenShift, esse valor é gerido pela plataforma.
- **Estabilidade:** o momento e a mensagem associados a um `reason` podem mudar entre versões. Não construa automação crítica dependendo de eventos.
- **Auditoria é outra coisa:** os registros de auditoria (`audit.k8s.io`) também se chamam "events", mas são outro mecanismo.

## Relações e dependências

- Referenciam objetos por kind, nome e [UID](uid.md).
- Complementam [Conditions](conditions.md) e [Status](status.md).
- Emitidos por [controllers](controller.md), pelo scheduler e pelo kubelet.

## Exemplo de situação real

Um Pod está `Pending`. O `describe` mostra o Event `Warning FailedScheduling ... 0/1 nodes are available: 1 Insufficient memory`. A causa é capacidade, e não a aplicação: num SNO, o único nó não tem memória livre suficiente para os *requests* pedidos.

## Como visualizar e inspecionar (somente leitura)

```bash
# Eventos do namespace, em ordem cronológica
oc get events -n <namespace> --sort-by=.lastTimestamp

# Só avisos
oc get events -n <namespace> --field-selector type=Warning

# Eventos de um objeto específico
oc get events -n <namespace> --field-selector involvedObject.name=<nome>

# Os eventos aparecem no final do describe
oc describe pod <nome> -n <namespace>

# Todos os namespaces (pode ser volumoso)
oc get events -A --field-selector type=Warning

# Comando dedicado, se disponível no seu cliente (a verificar no oc 4.22)
oc events -n <namespace>
```

## Como interpretar a saída

Saída **ilustrativa** de `oc get events`:

```text
LAST SEEN   TYPE      REASON             OBJECT          MESSAGE
2m          Normal    Scheduled          pod/web-x2kqp   Successfully assigned <ns>/web-x2kqp to <nó>
90s         Warning   BackOff            pod/web-x2kqp   Back-off restarting failed container
```

- `TYPE=Warning` merece atenção; `Normal` documenta o fluxo esperado.
- Um `REASON` repetido com contagem crescente indica um laço que tenta e falha. A causa está no que ele tenta fazer: veja logs e configuração.
- Ausência de eventos antigos **não** significa que nada aconteceu, porque eles expiram.
- Sem `--sort-by`, a ordem da listagem não é cronológica.

## Diferenças e confusões frequentes

- **Events × Conditions:** histórico × foto atual.
- **Events × logs:** o evento é emitido pelo sistema sobre o objeto; o log é a saída do processo do contêiner (`oc logs`).
- **Events × auditoria:** propósitos e APIs diferentes.
- **`involvedObject` (core v1) × `regarding` (events.k8s.io/v1):** mesmo papel, nomes diferentes.

## No OpenShift 4.22 versus Kubernetes

Mesmo modelo. O console web do OpenShift mostra os eventos por projeto e por objeto. Componentes de plataforma e Operators emitem muitos eventos nos namespaces `openshift-*`.

## No HomeLab SNO

`oc get events` é leitura e a ferramenta número 1 de diagnóstico. Prefira filtrar por namespace e por `type=Warning`, para não sobrecarregar o terminal e a API.

## Termos relacionados

[Conditions](conditions.md) · [Status](status.md) · [Controller](controller.md) · [UID](uid.md) · [Estado observado](current-state.md) · [Pod](../../03-workloads/verbetes/pod.md)

## Fontes oficiais

- Kubernetes Glossary — Event: <https://kubernetes.io/docs/reference/glossary/?all=true#term-event> (fonte: `kubernetes/website` `release-1.35`, `reference/glossary/event.md`)
- Kubernetes API Reference — Event (`events.k8s.io/v1`): <https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/event-v1/>
- Kubernetes — Owners and Dependents (exemplo de consulta por `--field-selector=reason=...`): <https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/>

## Revisão editorial

- **Estado:** 🟡 desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** confirmar o valor padrão de `--event-ttl` no kube-apiserver 1.35 e o valor configurado pelo OCP 4.22; confirmar se o `oc` 4.22 expõe `oc events`; validar os field selectors (`type`, `involvedObject.name`) no SNO. Nada disso foi **verificado** nesta rodada.
