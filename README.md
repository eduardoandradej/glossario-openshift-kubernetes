# Glossário OpenShift & Kubernetes

[![OpenShift 4.22](https://img.shields.io/badge/OpenShift-4.22-EE0000?style=for-the-badge&logo=redhatopenshift&logoColor=white)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)
[![Kubernetes 1.35](https://img.shields.io/badge/Kubernetes-1.35-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/docs/concepts/)
[![Idioma pt-BR](https://img.shields.io/badge/idioma-pt--BR-009C3B?style=for-the-badge)](#)
[![Licença Apache 2.0](https://img.shields.io/badge/licen%C3%A7a-Apache%202.0-D22128?style=for-the-badge&logo=apache&logoColor=white)](LICENSE)

## Apresentação

Kubernetes e OpenShift sustentam hoje uma parte significativa da infraestrutura de aplicações em bancos, operadoras de telecomunicações, órgãos de governo e provedores de nuvem. O vocabulário dessas plataformas é extenso, e muitos termos semelhantes designam conceitos distintos.

Este glossário organiza esse vocabulário de forma sistemática. Cada termo é definido, contextualizado e relacionado aos demais, com base na documentação oficial do Kubernetes e da Red Hat.

### Quem vos fala

<img src="assets/autor.png" alt="Foto de Eduardo Andrade" width="110" align="left" />

Sou **Eduardo Andrade**, profissional especializado em infraestrutura Linux corporativa, cibersegurança, automação e computação em nuvem, com ampla experiência em ambientes de missão crítica baseados em Red Hat Enterprise Linux (RHEL), virtualização, observabilidade e operações de alta disponibilidade. Sou mestre em Computação Aplicada, com ênfase em Cibersegurança.

Sou um eterno aprendiz, movido por desafios e problemas complexos e pelo que se aprende com cada erro e cada acerto. Este glossário reúne esse estudo contínuo, com o objetivo de apresentar tecnologias complexas de forma clara e acessível, sem perda de rigor técnico.

<br clear="left" />

[![Meu LinkedIn](https://img.shields.io/badge/Meu-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/eduardoandradej/)
[![Minhas credenciais](https://img.shields.io/badge/Minhas%20credenciais-Credly-FF6B00?style=for-the-badge&logo=credly&logoColor=white)](https://www.credly.com/users/eduardoandradej)

---

## Sobre o glossário

O **Glossário OpenShift & Kubernetes** é uma referência conceitual, em português, para quem estuda, opera ou administra clusters **Kubernetes** e **Red Hat OpenShift Container Platform 4.22** (Kubernetes 1.35).

Não é uma lista de comandos nem uma apostila de laboratório. Cada verbete explica um termo segundo a mesma estrutura:

- **o que é**: a definição em uma frase e a explicação do conceito;
- **por que existe**: o problema que resolve e um cenário real;
- **como funciona**: o ciclo de vida e os componentes envolvidos;
- **com o que se relaciona**: as dependências e as confusões mais frequentes com termos próximos;
- **como observar com segurança**: comandos somente de leitura e como interpretar o resultado;
- **o que muda no OpenShift** em relação ao Kubernetes, com as fontes oficiais usadas.

Os termos técnicos são mantidos no original em inglês (Control Plane, Pod, Desired State...), forma em que aparecem na documentação oficial e nas ferramentas; as explicações são em português. O conteúdo é organizado em 18 categorias, dos fundamentos da API aos componentes opcionais da plataforma, com índices, um mapa de relações entre os termos e diagramas.

É indicado para estudantes de certificações Red Hat de OpenShift, administradores e desenvolvedores que já usam a plataforma e querem entender **por que** ela se comporta como se comporta.

## Por onde começar

1. **Fundamentos:** o vocabulário que sustenta os demais temas: [Kubernetes](categorias/00-fundamentos-e-linguagem/verbetes/kubernetes.md), [Object](categorias/00-fundamentos-e-linguagem/verbetes/object.md), [Spec](categorias/00-fundamentos-e-linguagem/verbetes/spec.md) e [Status](categorias/00-fundamentos-e-linguagem/verbetes/status.md), [Desired State](categorias/00-fundamentos-e-linguagem/verbetes/desired-state.md) e [Reconciliation](categorias/00-fundamentos-e-linguagem/verbetes/reconciliation.md).
2. **Arquitetura:** os componentes que decidem e os que executam no cluster: [Control Plane](categorias/01-arquitetura-e-control-plane/verbetes/control-plane.md), [etcd](categorias/01-arquitetura-e-control-plane/verbetes/etcd.md), [kubelet](categorias/01-arquitetura-e-control-plane/verbetes/kubelet.md) e [CRI-O](categorias/01-arquitetura-e-control-plane/verbetes/cri-o.md).
3. **Visão de conjunto:** o diagrama do [modelo declarativo](diagramas/00-modelo-declarativo.md) e o [mapa de relações](docs/MAPA-DE-RELACOES.md).

Para localizar um termo específico, use o [índice alfabético](docs/INDICE-ALFABETICO.md), que também aceita os nomes em português (por exemplo, "plano de controle" e "estado desejado"). Para navegar por assunto, use o [índice por categoria](docs/INDICE-POR-CATEGORIA.md).

## Conteúdo

| # | Categoria | Situação |
|---|---|---|
| 00 | [Fundamentos, linguagem e modelo declarativo](categorias/00-fundamentos-e-linguagem/README.md) | ✅ Concluída |
| 01 | [Arquitetura e Control Plane](categorias/01-arquitetura-e-control-plane/README.md) | ✅ Concluída |
| 02 | [Compute, Nodes e capacidade](categorias/02-compute-e-nodes/README.md) | 🚧 Em construção |
| 03 | [Workloads](categorias/03-workloads/README.md) | 📝 Primeiros termos |
| 04 | [Networking, Services e publicação](categorias/04-networking/README.md) | 📝 Primeiros termos |
| 05 | [Storage e persistência](categorias/05-storage/README.md) | 📝 Primeiros termos |
| 06 | [Configuração e extensibilidade da API](categorias/06-configuracao-e-api/README.md) | 📝 Primeiros termos |
| 07 | [Identidade, autenticação e autorização](categorias/07-identidade-e-rbac/README.md) | 📝 Primeiros termos |
| 08 | [Segurança, isolamento e políticas](categorias/08-seguranca-e-politicas/README.md) | Planejada |
| 09 | [Operators, OLM e extensões](categorias/09-operators-e-extensoes/README.md) | 📝 Primeiros termos |
| 10 | [Build, imagens e registries](categorias/10-builds-imagens-registry/README.md) | 📝 Primeiros termos |
| 11 | [Scheduling, capacidade e escalabilidade](categorias/11-agendamento-e-escalabilidade/README.md) | Planejada |
| 12 | [Observabilidade, logs e métricas](categorias/12-observabilidade/README.md) | Planejada |
| 13 | [Instalação, atualizações e manutenção](categorias/13-ciclo-de-vida-cluster/README.md) | Planejada |
| 14 | [CLI, YAML, ferramentas e inspeção](categorias/14-cli-yaml-e-api/README.md) | Planejada |
| 15 | [Empacotamento, entrega e GitOps](categorias/15-entrega-e-automacao/README.md) | Planejada |
| 16 | [Virtualização, IA e componentes opcionais](categorias/16-virtualizacao-ia-e-extensoes/README.md) | Planejada |
| 17 | [Diagnóstico, falhas e confiabilidade](categorias/17-troubleshooting-e-resiliencia/README.md) | Planejada |

📝 *Primeiros termos*: alguns verbetes já publicados, em versão inicial.

Diagramas por tema: [arquitetura](diagramas/01-visao-geral.md) · [workloads](diagramas/02-workloads.md) · [networking](diagramas/03-networking.md) · [storage](diagramas/04-storage.md) · [Operators](diagramas/05-operators.md).

## Como ler um verbete

- Cada verbete diz **que tipo de coisa** o termo é: um objeto da API (que você cria com YAML), um componente (um software que roda no cluster), um conceito, um estado ou uma ferramenta. Nem todo termo tem um `kind`.
- Os comandos da seção **Como visualizar e inspecionar** são **somente leitura**. Quando um comando altera o cluster, ele aparece separado e marcado como tal.
- Saídas de exemplo são **ilustrativas**: o seu cluster pode mostrar valores diferentes.
- Cada verbete termina com as **fontes oficiais** (Kubernetes e Red Hat) usadas para escrevê-lo.

## Observações gerais

1. Nem toda API existe em todo cluster: depende da versão, dos Operators instalados e das *capabilities* habilitadas.
2. `oc api-resources` mostra os **tipos** que o cluster conhece, e não se existem objetos nem se você tem permissão de vê-los.
3. `oc get all` **não** lista todos os recursos.
4. Componentes opcionais (como ODF, OpenShift Virtualization, OpenShift AI e Service Mesh) podem não estar instalados no seu cluster.
5. O conteúdo é autoral e **não reproduz material de treinamento proprietário**.

## Prática

Para exercitar os comandos de inspeção, consulte a [Academia de Comandos OpenShift](https://github.com/eduardoandradej/academia-comandos-openshift), com prática, exercícios e troubleshooting de CLI.

---

<details>
<summary><b>Bastidores do projeto</b> (para quem mantém ou contribui)</summary>

- [Continuar daqui (contexto de retomada)](docs/CONTINUAR-DAQUI.md)
- [Estado do projeto e próximos lotes](docs/ESTADO-DO-PROJETO.md)
- [Termos e afirmações a validar](docs/TERMOS-A-VALIDAR.md)
- [Critérios de qualidade](docs/CRITERIOS-DE-QUALIDADE.md) · [Modelo de verbete](modelos/MODELO-VERBETE.md) · [Inspeção segura no HomeLab](docs/LAB-INSPECAO-SEGURA.md)
- [Inventário de termos candidatos](dados/inventario.json)
- Prompts de trabalho: [mestre](PROMPT-MESTRE.md) · [continuação](PROMPT-CONTINUACAO.md) · [revisão](PROMPT-REVISAO.md)

</details>
