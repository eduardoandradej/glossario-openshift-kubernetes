# Glossário OpenShift & Kubernetes

[![OpenShift 4.22](https://img.shields.io/badge/OpenShift-4.22-EE0000?style=for-the-badge&logo=redhatopenshift&logoColor=white)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)
[![Kubernetes 1.35](https://img.shields.io/badge/Kubernetes-1.35-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/docs/concepts/)
[![Idioma pt-BR](https://img.shields.io/badge/idioma-pt--BR-009C3B?style=for-the-badge)](#)
[![Licença Apache 2.0](https://img.shields.io/badge/licen%C3%A7a-Apache%202.0-D22128?style=for-the-badge&logo=apache&logoColor=white)](LICENSE)

[![Categorias](https://img.shields.io/badge/categorias-18-6F42C1?style=flat-square)](docs/MAPA-DE-CATEGORIAS.md)
[![Verbetes desenvolvidos](https://img.shields.io/badge/verbetes%20desenvolvidos-35-F2C744?style=flat-square)](docs/INDICE-POR-CATEGORIA.md)
[![Sementes](https://img.shields.io/badge/sementes-23-8BC34A?style=flat-square)](docs/INDICE-ALFABETICO.md)
[![Candidatos](https://img.shields.io/badge/candidatos-680-9E9E9E?style=flat-square)](dados/inventario.json)
[![Lote atual](https://img.shields.io/badge/categoria%2000-coberta%20(37%2F37)-0A7EA4?style=flat-square)](categorias/00-fundamentos-e-linguagem/README.md)
[![Diagramas](https://img.shields.io/badge/diagramas-Mermaid-FF3670?style=flat-square&logo=mermaid&logoColor=white)](diagramas/00-modelo-declarativo.md)
[![Validação no cluster](https://img.shields.io/badge/valida%C3%A7%C3%A3o%20no%20cluster-pendente-orange?style=flat-square)](docs/TERMOS-A-VALIDAR.md)

## 👋 Antes de tudo: bem-vindo!

Já pensou em aprender, de verdade, a tecnologia que está mudando a forma como o mundo inteiro roda aplicações? Kubernetes e OpenShift estão por trás de bancos, operadoras, streaming, governo e de boa parte da nuvem que você usa todo dia. E, convenhamos: a primeira impressão costuma ser de uma sopa de siglas, YAML e conceitos que parecem iguais, mas não são.

Este glossário nasceu exatamente para isso: **desembaraçar essa sopa**, um conceito de cada vez, em português claro e sem perder o rigor técnico.

### Quem vos fala

<img src="assets/autor.png" alt="Foto de Eduardo Andrade" width="110" align="left" />

Sou **Eduardo Andrade**, profissional especializado em **infraestrutura Linux corporativa, cibersegurança, automação e computação em nuvem**, com longa experiência em ambientes de missão crítica baseados em **Red Hat Enterprise Linux (RHEL)**, virtualização, observabilidade e operações de alta disponibilidade. Sou **mestre em Computação Aplicada, com ênfase em Cibersegurança**.

Sou um eterno aprendiz, apaixonado por resolver problemas complexos e por aprender com os erros e com os acertos, para um dia repassar tudo isso com **leveza**. A ideia aqui é absorver o máximo dessas tecnologias complexas e traduzi-las de um jeito fácil e amigável.

Vamos nessa! 🚀

<br clear="left" />

[![Meu LinkedIn](https://img.shields.io/badge/Meu-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/eduardoandradej/)
[![Minhas credenciais](https://img.shields.io/badge/Minhas%20credenciais-Credly-FF6B00?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/users/eduardoandradej)

---

## Sobre o glossário

**Enciclopédia conceitual, visual e operacional em português brasileiro**, focada no ecossistema Kubernetes e no OpenShift Container Platform 4.22.

> Objetivo: compreender **o que é**, **por que existe**, **como funciona**, **com o que se relaciona** e **como inspecionar com segurança** cada termo, sem transformar este projeto em uma lista de comandos.

## Como navegar

- [Mapa de categorias](docs/MAPA-DE-CATEGORIAS.md)
- [Índice alfabético](docs/INDICE-ALFABETICO.md) · [Índice por categoria](docs/INDICE-POR-CATEGORIA.md) · [Mapa de relações](docs/MAPA-DE-RELACOES.md)
- [Estado do projeto](docs/ESTADO-DO-PROJETO.md) · [Termos a validar](docs/TERMOS-A-VALIDAR.md)
- [Modelo declarativo (spec → reconciliation → status)](diagramas/00-modelo-declarativo.md)
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
- **35 verbetes desenvolvidos** (categoria 00 inteira, lotes 1 a 3, 2026-11-04): fontes oficiais conferidas, **sem validação no cluster**.
- **23 verbetes-semente** herdados do kit, **ainda pendentes de aprofundamento editorial**.
- **5 diagramas** autorais em Mermaid.

## Ordem de leitura sugerida

Comece por fundamentos e arquitetura; em seguida compute/nodes e workloads; depois networking e storage; então configuração, identidade, segurança e Operators. Use os mapas de relações para conectar os conceitos.

## Filosofia e cuidados

1. Nem todo termo é um objeto da API; nem toda API existe no cluster local.
2. Uma lista retornada por `oc api-resources` não significa que existam instâncias, nem que o usuário tenha permissão de lê-las.
3. `oc get all` não lista todos os recursos Kubernetes/OpenShift.
4. Conceitos opcionais como ODF, OpenShift Virtualization, AI e Service Mesh não estão necessariamente instalados no SNO.
5. O glossário é autoral e **não reproduz material de treinamento proprietário**.

## Relação com outros materiais

Este glossário é independente. Para praticar os comandos de inspeção, use a [Academia de Comandos OpenShift](https://github.com/eduardoandradej/academia-comandos-openshift): prática, exercícios e troubleshooting de CLI.

Os roteiros de curso ficam em materiais de estudo privados do autor, que não são citados nem linkados aqui.

Este é um projeto novo e independente, publicado na branch `main` deste repositório e expandido em lotes pequenos (ver [estado do projeto](docs/ESTADO-DO-PROJETO.md)).
