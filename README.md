# Glossário OpenShift & Kubernetes

**Enciclopédia conceitual, visual e operacional em português brasileiro**, focada no ecossistema Kubernetes e no OpenShift Container Platform 4.22.

> Objetivo: compreender **o que é**, **por que existe**, **como funciona**, **com o que se relaciona** e **como inspecionar com segurança** cada termo, sem transformar este projeto em uma lista de comandos.

## Como navegar

- [Mapa de categorias](docs/MAPA-DE-CATEGORIAS.md)
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
- **24 verbetes-semente**, com definições e comandos, **ainda pendentes de aprofundamento editorial**.
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

Este é um novo projeto, independente, e foi entregue como **estrutura inicial pronta para ser expandida**. Não foi publicado no GitHub automaticamente.
