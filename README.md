# Glossário OpenShift & Kubernetes

[![OpenShift 4.22](https://img.shields.io/badge/OpenShift-4.22-EE0000?style=for-the-badge&logo=redhatopenshift&logoColor=white)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)
[![Kubernetes 1.35](https://img.shields.io/badge/Kubernetes-1.35-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/docs/concepts/)
[![Idioma pt-BR](https://img.shields.io/badge/idioma-pt--BR-009C3B?style=for-the-badge)](#)
[![Licença Apache 2.0](https://img.shields.io/badge/licen%C3%A7a-Apache%202.0-D22128?style=for-the-badge&logo=apache&logoColor=white)](LICENSE)

[![Categorias](https://img.shields.io/badge/categorias-18-6F42C1?style=flat-square)](docs/MAPA-DE-CATEGORIAS.md)
[![Verbetes desenvolvidos](https://img.shields.io/badge/verbetes%20desenvolvidos-12-F2C744?style=flat-square)](docs/INDICE-POR-CATEGORIA.md)
[![Sementes](https://img.shields.io/badge/sementes-23-8BC34A?style=flat-square)](docs/INDICE-ALFABETICO.md)
[![Candidatos](https://img.shields.io/badge/candidatos-680-9E9E9E?style=flat-square)](dados/inventario.json)
[![Lote atual](https://img.shields.io/badge/lote%20atual-00%20%C2%B7%20fundamentos-0A7EA4?style=flat-square)](categorias/00-fundamentos-e-linguagem/README.md)
[![Diagramas](https://img.shields.io/badge/diagramas-Mermaid-FF3670?style=flat-square&logo=mermaid&logoColor=white)](diagramas/00-modelo-declarativo.md)
[![Validação no cluster](https://img.shields.io/badge/valida%C3%A7%C3%A3o%20no%20cluster-pendente-orange?style=flat-square)](docs/TERMOS-A-VALIDAR.md)

**Enciclopédia conceitual, visual e operacional em português brasileiro**, focada no ecossistema Kubernetes e no OpenShift Container Platform 4.22.

> Objetivo: compreender **o que é**, **por que existe**, **como funciona**, **com o que se relaciona** e **como inspecionar com segurança** cada termo, sem transformar este projeto em uma lista de comandos.

## Como navegar

- [Mapa de categorias](docs/MAPA-DE-CATEGORIAS.md)
- [Índice alfabético](docs/INDICE-ALFABETICO.md) · [Índice por categoria](docs/INDICE-POR-CATEGORIA.md) · [Mapa de relações](docs/MAPA-DE-RELACOES.md)
- [Estado do projeto](docs/ESTADO-DO-PROJETO.md) · [Termos a validar](docs/TERMOS-A-VALIDAR.md)
- [Modelo declarativo (spec → reconciliação → status)](diagramas/00-modelo-declarativo.md)
- [Diagrama de arquitetura](diagramas/01-visao-geral.md)
- [Workloads e controllers](diagramas/02-workloads.md)
- [Tráfego e networking](diagramas/03-networking.md)
- [PV, PVC, StorageClass e CSI](diagramas/04-storage.md)
- [Operators e OLM](diagramas/05-operators.md)
- [Modelo editorial do verbete](modelos/MODELO-VERBETE.md)
- [Inspeção segura no HomeLab](docs/LAB-INSPECAO-SEGURA.md)
- [Fontes oficiais](docs/FONTES-OFICIAIS.md)
- [Prompt mestre para Claude Code](PROMPT-MESTRE.md)
- [Prompt de continuação](PROMPT-CONTINUACAO.md)

## Escopo em números (não inflar progresso)

- **18 categorias** temáticas organizadas.
- **680 entradas candidatas brutas** no inventário (contém remissões e duplicações; não são verbetes prontos).
- **12 verbetes desenvolvidos** (categoria 00, lote 1, 2026-11-04): fontes oficiais conferidas, **sem validação no cluster**.
- **23 verbetes-semente** herdados do kit, **ainda pendentes de aprofundamento editorial** (o Namespace inclusive).
- **5 diagramas** autorais em Mermaid.

## Ordem de leitura sugerida

Comece por fundamentos e arquitetura; em seguida compute/nodes e workloads; depois networking e storage; então configuração, identidade, segurança e Operators. Use os mapas de relações para conectar os conceitos. Cursos DO180/DO280 e a Academia de Comandos continuam sendo a base de treinamento prático.

## Filosofia e cuidados

1. Nem todo termo é um objeto da API; nem toda API existe no cluster local.
2. Uma lista retornada por `oc api-resources` não significa que existam instâncias, nem que o usuário tenha permissão de lê-las.
3. `oc get all` não lista todos os recursos Kubernetes/OpenShift.
4. Conceitos opcionais como ODF, OpenShift Virtualization, AI e Service Mesh não estão necessariamente instalados no SNO.
5. O glossário é autoral e **não reproduz material de treinamento proprietário**.

## Relação com outros repositórios

- [Academia de Comandos OpenShift](https://github.com/eduardoandradej/academia-comandos-openshift): prática, exercícios e troubleshooting.
- [DO180 4.22](https://github.com/eduardoandradej/openshift-do180-4.22-estudos): fundamentos e operação.
- [DO280 4.22](https://github.com/eduardoandradej/openshift-do280-4.22-estudos): administração de cluster.

Este é um projeto novo e independente, publicado na branch `main` deste repositório e expandido em lotes pequenos (ver [estado do projeto](docs/ESTADO-DO-PROJETO.md)).
