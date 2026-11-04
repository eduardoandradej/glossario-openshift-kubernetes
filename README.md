# Glossário OpenShift & Kubernetes

[![OpenShift 4.22](https://img.shields.io/badge/OpenShift-4.22-EE0000?style=for-the-badge&logo=redhatopenshift&logoColor=white)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)
[![Kubernetes 1.35](https://img.shields.io/badge/Kubernetes-1.35-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/docs/concepts/)
[![Idioma pt-BR](https://img.shields.io/badge/idioma-pt--BR-009C3B?style=for-the-badge)](#)
[![Licença Apache 2.0](https://img.shields.io/badge/licen%C3%A7a-Apache%202.0-D22128?style=for-the-badge&logo=apache&logoColor=white)](LICENSE)

[![Categorias](https://img.shields.io/badge/categorias-18-6F42C1?style=flat-square)](docs/MAPA-DE-CATEGORIAS.md)
[![Termos explicados](https://img.shields.io/badge/termos%20explicados-47-F2C744?style=flat-square)](docs/INDICE-ALFABETICO.md)
[![Diagramas](https://img.shields.io/badge/diagramas-Mermaid-FF3670?style=flat-square&logo=mermaid&logoColor=white)](diagramas/00-modelo-declarativo.md)
[![Fontes oficiais](https://img.shields.io/badge/fontes-oficiais-2EA44F?style=flat-square)](docs/FONTES-OFICIAIS.md)

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

Uma **enciclopédia conceitual e visual**, em português, do ecossistema **Kubernetes** e do **OpenShift Container Platform 4.22**.

Cada termo responde, nesta ordem: **o que é**, **por que existe**, **como funciona**, **com o que se relaciona** e **como observar com segurança** no seu cluster. Os termos técnicos ficam no original em inglês (Control Plane, Pod, Desired State...), porque é assim que você vai encontrá-los na documentação, no `oc` e no dia a dia. A explicação é em português.

## Por onde começar

1. **Fundamentos:** o vocabulário que sustenta todo o resto: [Kubernetes](categorias/00-fundamentos-e-linguagem/verbetes/kubernetes.md), [Object](categorias/00-fundamentos-e-linguagem/verbetes/object.md), [Spec](categorias/00-fundamentos-e-linguagem/verbetes/spec.md) e [Status](categorias/00-fundamentos-e-linguagem/verbetes/status.md), [Desired State](categorias/00-fundamentos-e-linguagem/verbetes/desired-state.md) e [Reconciliation](categorias/00-fundamentos-e-linguagem/verbetes/reconciliation.md).
2. **Arquitetura:** quem decide e quem executa no cluster: [Control Plane](categorias/01-arquitetura-e-control-plane/verbetes/control-plane.md), [etcd](categorias/01-arquitetura-e-control-plane/verbetes/etcd.md), [kubelet](categorias/01-arquitetura-e-control-plane/verbetes/kubelet.md) e [CRI-O](categorias/01-arquitetura-e-control-plane/verbetes/cri-o.md).
3. **Para ver o todo:** o diagrama do [modelo declarativo](diagramas/00-modelo-declarativo.md) e o [mapa de relações](docs/MAPA-DE-RELACOES.md).

Procurando um termo específico? Use o **[índice alfabético](docs/INDICE-ALFABETICO.md)**. Ele aceita também os nomes em português, como "plano de controle" e "estado desejado". Prefere navegar por assunto? Use o **[índice por categoria](docs/INDICE-POR-CATEGORIA.md)**.

## O que você encontra aqui

| # | Categoria | Situação |
|---|---|---|
| 00 | [Fundamentos, linguagem e modelo declarativo](categorias/00-fundamentos-e-linguagem/README.md) | ✅ Disponível |
| 01 | [Arquitetura e Control Plane](categorias/01-arquitetura-e-control-plane/README.md) | 🚧 Em construção |
| 02 | [Compute, Nodes e capacidade](categorias/02-compute-e-nodes/README.md) | 📝 Primeiros termos |
| 03 | [Workloads](categorias/03-workloads/README.md) | 📝 Primeiros termos |
| 04 | [Networking, Services e publicação](categorias/04-networking/README.md) | 📝 Primeiros termos |
| 05 | [Storage e persistência](categorias/05-storage/README.md) | 📝 Primeiros termos |
| 06 | [Configuração e extensibilidade da API](categorias/06-configuracao-e-api/README.md) | 📝 Primeiros termos |
| 07 | [Identidade, autenticação e autorização](categorias/07-identidade-e-rbac/README.md) | 📝 Primeiros termos |
| 08 | [Segurança, isolamento e políticas](categorias/08-seguranca-e-politicas/README.md) | 🔜 Em breve |
| 09 | [Operators, OLM e extensões](categorias/09-operators-e-extensoes/README.md) | 📝 Primeiros termos |
| 10 | [Build, imagens e registries](categorias/10-builds-imagens-registry/README.md) | 📝 Primeiros termos |
| 11 | [Scheduling, capacidade e escalabilidade](categorias/11-agendamento-e-escalabilidade/README.md) | 🔜 Em breve |
| 12 | [Observabilidade, logs e métricas](categorias/12-observabilidade/README.md) | 🔜 Em breve |
| 13 | [Instalação, atualizações e manutenção](categorias/13-ciclo-de-vida-cluster/README.md) | 🔜 Em breve |
| 14 | [CLI, YAML, ferramentas e inspeção](categorias/14-cli-yaml-e-api/README.md) | 🔜 Em breve |
| 15 | [Empacotamento, entrega e GitOps](categorias/15-entrega-e-automacao/README.md) | 🔜 Em breve |
| 16 | [Virtualização, IA e componentes opcionais](categorias/16-virtualizacao-ia-e-extensoes/README.md) | 🔜 Em breve |
| 17 | [Diagnóstico, falhas e confiabilidade](categorias/17-troubleshooting-e-resiliencia/README.md) | 🔜 Em breve |

**Legenda:** ✅ categoria completa · 🚧 sendo escrita agora · 📝 alguns termos já publicados, em versão inicial · 🔜 planejada.

Diagramas por tema: [arquitetura](diagramas/01-visao-geral.md) · [workloads](diagramas/02-workloads.md) · [networking](diagramas/03-networking.md) · [storage](diagramas/04-storage.md) · [Operators](diagramas/05-operators.md).

## Como ler um verbete

- Cada verbete diz **que tipo de coisa** o termo é: um objeto da API (que você cria com YAML), um componente (um software que roda no cluster), um conceito, um estado ou uma ferramenta. Nem todo termo tem um `kind`.
- Os comandos da seção **Como visualizar e inspecionar** são **somente leitura**. Quando um comando altera o cluster, ele aparece separado e marcado como tal.
- Saídas de exemplo são **ilustrativas**: o seu cluster pode mostrar valores diferentes.
- Cada verbete termina com as **fontes oficiais** (Kubernetes e Red Hat) usadas para escrevê-lo.

## Cuidados que valem para todo o glossário

1. Nem toda API existe em todo cluster: depende da versão, dos Operators instalados e das *capabilities* habilitadas.
2. `oc api-resources` mostra os **tipos** que o cluster conhece, e não se existem objetos nem se você tem permissão de vê-los.
3. `oc get all` **não** lista todos os recursos.
4. Componentes opcionais (como ODF, OpenShift Virtualization, OpenShift AI e Service Mesh) podem não estar instalados no seu cluster.
5. O conteúdo é autoral e **não reproduz material de treinamento proprietário**.

## Quer praticar?

Para exercitar os comandos de inspeção, use a [Academia de Comandos OpenShift](https://github.com/eduardoandradej/academia-comandos-openshift), com prática, exercícios e troubleshooting de CLI.

---

<details>
<summary><b>Bastidores do projeto</b> (para quem mantém ou contribui)</summary>

- [Estado do projeto e próximos lotes](docs/ESTADO-DO-PROJETO.md)
- [Termos e afirmações a validar](docs/TERMOS-A-VALIDAR.md)
- [Critérios de qualidade](docs/CRITERIOS-DE-QUALIDADE.md) · [Modelo de verbete](modelos/MODELO-VERBETE.md) · [Inspeção segura no HomeLab](docs/LAB-INSPECAO-SEGURA.md)
- [Inventário de termos candidatos](dados/inventario.json)
- Prompts de trabalho: [mestre](PROMPT-MESTRE.md) · [continuação](PROMPT-CONTINUACAO.md) · [revisão](PROMPT-REVISAO.md)

</details>
