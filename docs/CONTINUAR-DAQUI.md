# Continuar daqui (contexto de retomada)

> Arquivo interno de continuidade. Leia junto com `CLAUDE.md`, `PROMPT-MESTRE.md` e `docs/ESTADO-DO-PROJETO.md` antes de produzir conteúdo. Última atualização: 2026-11-04.

## Onde paramos

- **Categoria 00 (Fundamentos):** concluída. Os 37 candidatos estão cobertos por 34 verbetes e 3 remissões.
- **Categoria 01 (Arquitetura e Control Plane):** em construção.
  - **Lote 1, publicado:** Control Plane, Worker Node, Master Node, etcd, kube-scheduler, kube-controller-manager, cloud-controller-manager, kubelet, Container Runtime, CRI, CRI-O e Static Pod. Remissões: kube-apiserver e Node Agent.
  - **Lote 2, publicado:** kube-proxy, OVN-Kubernetes, CoreDNS, DNS Operator, Cluster DNS, Cluster Version Operator, Machine Config Operator, MachineConfig e MachineConfigPool. Remissão: Cluster Operator → ClusterOperator (categoria 09).
  - **Próximo: lote 3, que fecha a categoria:** Bootstrap, Quorum, High Availability, SNO, HyperShift, Hosted Control Plane e Infrastructure Node.
- **Categorias 02 a 10:** têm verbetes em **versão inicial**, herdados do kit (Node, Pod, Deployment, ReplicaSet, StatefulSet, DaemonSet, Job, Service, Route, Ingress, IngressController, NetworkPolicy, PV, PVC, StorageClass, ConfigMap, Secret, ServiceAccount, Operator, ClusterOperator, CRD, ClusterExtension e BuildConfig). Eles serão aprofundados quando cada categoria for trabalhada.
- **Último commit publicado:** `04089d2` na `main`.

## Decisões do autor (obrigatórias)

1. **Termos técnicos em inglês** (Control Plane, Desired State, Reconciliation, Garbage Collection...), com a **explicação em português**. A tradução aparece só como apoio.
2. **Páginas para o leitor** (README, READMEs de categoria, índices, mapas) **sem controles internos**: nada de lotes, "sem validação", checklists ou contagem de candidatos. O controle fica em `docs/ESTADO-DO-PROJETO.md`, `docs/TERMOS-A-VALIDAR.md`, `dados/inventario.json` e neste arquivo.
3. **Verbetes:** o título é seguido direto de "Definição em uma frase". A ficha técnica (ID, classe, plataforma, escopo, versões, nível, data) e as notas de revisão ficam no bloco recolhido `<details><summary>Ficha técnica e notas de revisão</summary>` no fim. A seção de diagrama se chama apenas **"Diagrama"**.
4. **Tom sóbrio e profissional.** O mínimo de ícones: só ✅ Concluída, 🚧 Em construção e 📝 Primeiros termos, na tabela de categorias do README. **Foguete (🚀) nunca**, nem emojis decorativos.
5. **Repositórios de curso privados** (DO180, DO280): não citar por nome nem por link. A **Academia de Comandos** é pública e pode ser linkada.
6. **README:** "Apresentação" e "Quem vos fala" (em primeira pessoa; foto em `assets/autor.png`, circular, 110 px), com os botões "Meu LinkedIn" e "Minhas credenciais" (Credly). Os dados pessoais do autor estão só no README.
7. Trabalhar na **`main`**, com commits pequenos e descritivos, **sem force push**.

## Método de trabalho usado

- **Versão de referência:** OCP 4.22 = **Kubernetes 1.35** (release notes do 4.22).
- **Fontes:** a rede da sessão bloqueava `kubernetes.io` e `docs.redhat.com`. O conteúdo foi conferido nos arquivos-fonte oficiais, pelo `raw.githubusercontent.com`:
  - `kubernetes/website`, branch `release-1.35`, `content/en/docs/...`;
  - `openshift/openshift-docs`, branch `enterprise-4.22` (assemblies e `modules/*.adoc`; `_topic_maps/_topic_map.yml` ajuda a localizar os arquivos);
  - `kubernetes/community`, `contributors/devel/sig-architecture/api-conventions.md`.
  - Cada verbete cita a URL publicada e o arquivo-fonte. As URLs publicadas não abertas ficam marcadas "a verificar".
- **Lotes** de 8 a 15 verbetes por categoria, seguindo `modelos/MODELO-VERBETE.md`.
- **A cada lote, atualizar:** a página da categoria (termos publicados e "Em breve"), `docs/INDICE-ALFABETICO.md`, `docs/INDICE-POR-CATEGORIA.md`, `docs/MAPA-DE-RELACOES.md`, `docs/TERMOS-A-VALIDAR.md`, `docs/ESTADO-DO-PROJETO.md`, `dados/inventario.json` (classe, fontes, slug, `validacao_cluster`) e, quando a situação de uma categoria mudar, a tabela do README.
- **Validações antes do commit:**
  - `python3 scripts/verificar.py` (links locais);
  - JSON do inventário válido;
  - diagramas renderizados com `@mermaid-js/mermaid-cli` (instalado no scratchpad, usando o Chromium em `/opt/pw-browsers`);
  - busca no diff por dados sensíveis.
- **Nunca afirmar execução no cluster:** saídas são sempre "ilustrativas", e as pendências ficam nas notas de revisão do verbete.

## Pendências gerais

- **Validação no HomeLab SNO** (não feita; exige autorização do autor): itens por verbete em `docs/TERMOS-A-VALIDAR.md`.
- **Abrir as URLs publicadas** quando a rede permitir: liberar `kubernetes.io` e `docs.redhat.com` em Network access do ambiente.
- **Revisão da categoria 00** com o `PROMPT-REVISAO.md`, gerando `docs/revisoes/00-fundamentos-e-linguagem.md`. Ainda não foi feita.
- O histórico Git antigo (commits `7fcc020` e `8933e7d`) ainda contém links dos repositórios de curso. Removê-los exigiria reescrever o histórico, o que só deve ser feito com decisão explícita do autor.

## Como retomar (sugestão de pedido)

> "Continue o glossário a partir de `docs/CONTINUAR-DAQUI.md`: faça o lote 3 da categoria 01 (Bootstrap, Quorum, High Availability, SNO, HyperShift, Hosted Control Plane, Infrastructure Node), seguindo as decisões registradas, e publique na `main`."
