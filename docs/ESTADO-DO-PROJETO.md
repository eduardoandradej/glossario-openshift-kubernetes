# Estado do projeto

## Rodada 2026-11-04 — categoria 00, lote 1

- **Kit inicial importado** para a `main` sem alterações (commit próprio).
- **12 verbetes desenvolvidos** na categoria 00, mais 1 remissão (K8s): Kubernetes, OpenShift Container Platform, Cluster, API, Objeto, Recurso, Kind, Spec, Status, Estado desejado, Estado observado, Reconciliação.
- Estado de todos: 🟡 **desenvolvido**. Fontes oficiais conferidas, mas **sem validação no cluster** e com as URLs publicadas não abertas (detalhes em [TERMOS-A-VALIDAR](TERMOS-A-VALIDAR.md)). Nenhum deles é considerado "concluído".
- **Versão de referência confirmada:** o OCP 4.22 usa **Kubernetes 1.35** com CRI-O (release notes 4.22). Os fontes do Kubernetes foram lidos na branch `release-1.35`.
- **Novos índices:** [por categoria](INDICE-POR-CATEGORIA.md), [mapa de relações](MAPA-DE-RELACOES.md), [termos a validar](TERMOS-A-VALIDAR.md); [índice alfabético](INDICE-ALFABETICO.md) refeito com estados e remissões.
- **Novo diagrama:** [00 — modelo declarativo](../diagramas/00-modelo-declarativo.md).
- **Inventário:** as 13 entradas trabalhadas em `dados/inventario.json` foram classificadas (`kind_class`, `scope`, `fontes`, `slug_verbete`, `relacoes`, `verificado_em`, `validacao_cluster`).
- **HomeLab:** não acessado. Nenhum comando foi executado no cluster.

### Próximo lote recomendado (categoria 00, lote 2)

API Server, API Group, API Version, Manifest, YAML, JSON, Metadata, Controller, Control Loop (remissão para Reconciliação), Resource Name, UID e revisão do Namespace (semente → desenvolvido). Lote 3: Project, Label, Annotation, Selector, OwnerReference, Finalizer, Garbage Collection, ResourceVersion, Generation, ObservedGeneration, Conditions, Events.

## Estado inicial — 2026-11-03

- Criadas 18 categorias e 680 entradas candidatas brutas (incluindo sinônimos e remissões).
- Geradas 24 páginas-semente, ainda **não concluídas** sob o modelo editorial completo.
- Criados cinco diagramas Mermaid, prompt mestre, prompt de continuação, prompt de revisão e critérios de qualidade.
- Verificação de suporte real via `oc api-resources` no HomeLab: **não realizada**; este artefato não acessou o cluster.
- Publicação no GitHub: **não realizada** na época; o kit foi publicado na `main` em 2026-11-04.
