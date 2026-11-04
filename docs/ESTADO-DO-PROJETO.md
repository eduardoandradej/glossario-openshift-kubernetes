# Estado do projeto

## Rodada 2026-11-04 (3) — categoria 00, lote 3 (categoria coberta)

- **12 verbetes novos:** Project, Label, Annotation, Selector, OwnerReference, Finalizer, Garbage Collection, ResourceVersion, Generation, ObservedGeneration, Conditions e Events.
- **Categoria 00 coberta:** os 37 candidatos viraram 34 verbetes e 3 remissões (K8s, Control Loop e o próprio API/Kubernetes API). Todos 🟡: **sem validação no cluster**.
- **Correção transversal:** no Kubernetes 1.35, `resourceVersion` passou a ser ordenável dentro do mesmo tipo de recurso (requisito de conformidade). O verbete Metadata foi ajustado.
- Remissões "verbete futuro" dos lotes anteriores agora apontam para páginas existentes.

### Próximo passo recomendado

1. **Revisão da categoria 00** com o [prompt de revisão](../PROMPT-REVISAO.md), gerando `docs/revisoes/00-fundamentos-e-linguagem.md`.
2. **Validação no SNO**, com autorização do autor, dos itens de [TERMOS-A-VALIDAR](TERMOS-A-VALIDAR.md).
3. Depois disso, a categoria **01 — Arquitetura e control plane**.

## Rodada 2026-11-04 (2) — categoria 00, lote 2

- **10 verbetes novos:** API Server, API Group, API Version, Manifest, YAML, JSON, Metadata, Controller, Resource Name e UID. **Namespace** reescrito (de 🌱 semente para 🟡 desenvolvido). **Control Loop** virou remissão para Controller e Reconciliação.
- Fontes: `kubernetes/website` `release-1.35` (names, namespaces, using-api, api-concepts, components, controller, glossário), API Conventions e `openshift-docs` `enterprise-4.22` (control plane / machine roles, working with projects, glossary).
- Todos 🟡: **sem validação no cluster**; pendências em [TERMOS-A-VALIDAR](TERMOS-A-VALIDAR.md).
- **README:** abertura com apresentação do autor, LinkedIn e Credly. Os repositórios de curso privados não são mais citados.

### Próximo lote recomendado na época (categoria 00, lote 3) — concluído

Project, Label, Annotation, Selector, OwnerReference, Finalizer, Garbage Collection, ResourceVersion, Generation, ObservedGeneration, Conditions e Events.

## Rodada 2026-11-04 — categoria 00, lote 1

- **Kit inicial importado** para a `main` sem alterações (commit próprio).
- **12 verbetes desenvolvidos** na categoria 00, mais 1 remissão (K8s): Kubernetes, OpenShift Container Platform, Cluster, API, Objeto, Recurso, Kind, Spec, Status, Estado desejado, Estado observado, Reconciliação.
- Estado de todos: 🟡 **desenvolvido**. Fontes oficiais conferidas, mas **sem validação no cluster** e com as URLs publicadas não abertas (detalhes em [TERMOS-A-VALIDAR](TERMOS-A-VALIDAR.md)). Nenhum deles é considerado "concluído".
- **Versão de referência confirmada:** o OCP 4.22 usa **Kubernetes 1.35** com CRI-O (release notes 4.22). Os fontes do Kubernetes foram lidos na branch `release-1.35`.
- **Novos índices:** [por categoria](INDICE-POR-CATEGORIA.md), [mapa de relações](MAPA-DE-RELACOES.md), [termos a validar](TERMOS-A-VALIDAR.md); [índice alfabético](INDICE-ALFABETICO.md) refeito com estados e remissões.
- **Novo diagrama:** [00 — modelo declarativo](../diagramas/00-modelo-declarativo.md).
- **Inventário:** as 13 entradas trabalhadas em `dados/inventario.json` foram classificadas (`kind_class`, `scope`, `fontes`, `slug_verbete`, `relacoes`, `verificado_em`, `validacao_cluster`).
- **HomeLab:** não acessado. Nenhum comando foi executado no cluster.

### Próximo lote recomendado na época (categoria 00, lote 2) — concluído

API Server, API Group, API Version, Manifest, YAML, JSON, Metadata, Controller, Control Loop (remissão para Reconciliação), Resource Name, UID e revisão do Namespace (semente → desenvolvido). Lote 3: Project, Label, Annotation, Selector, OwnerReference, Finalizer, Garbage Collection, ResourceVersion, Generation, ObservedGeneration, Conditions, Events.

## Estado inicial — 2026-11-03

- Criadas 18 categorias e 680 entradas candidatas brutas (incluindo sinônimos e remissões).
- Geradas 24 páginas-semente, ainda **não concluídas** sob o modelo editorial completo.
- Criados cinco diagramas Mermaid, prompt mestre, prompt de continuação, prompt de revisão e critérios de qualidade.
- Verificação de suporte real via `oc api-resources` no HomeLab: **não realizada**; este artefato não acessou o cluster.
- Publicação no GitHub: **não realizada** na época; o kit foi publicado na `main` em 2026-11-04.
