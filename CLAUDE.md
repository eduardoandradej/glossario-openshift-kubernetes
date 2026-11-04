# Instruções operacionais para Claude Code

Leia e siga integralmente [PROMPT-MESTRE.md](PROMPT-MESTRE.md) antes de editar.

Missão: enciclopédia original de conceitos Kubernetes/OpenShift 4.22; **definições e relações primeiro, comandos depois**. `dados/inventario.json` é lista de candidatos, não verbetes prontos nem lista de objetos API verificados. Não alterar os outros repositórios do autor. Os repositórios de curso são privados: não citá-los por nome nem por link. A `academia-comandos-openshift` é pública e pode ser linkada. Trabalhar na `main` deste repositório, preservando arquivos. Um lote/categoria por tarefa. Não operar HomeLab sem autorização. Sem segredos, sem exemplos que revelem tokens. Fontes oficiais e estados de verificação obrigatórios. `DeploymentConfig` legado, OLM Classic/v1 e Ingress/Route/IngressController merecem revisão crítica.

Leia também: `docs/CRITERIOS-DE-QUALIDADE.md`, `modelos/MODELO-VERBETE.md`, `docs/MAPA-DE-CATEGORIAS.md`, `docs/FONTES-OFICIAIS.md`. Atualize índices e mapa de relações ao produzir páginas; não invente validações ou execução. No fim, relatório de arquivos, revisão e próximo lote.

**Terminologia (decisão do autor, 2026-11-04):** termos técnicos sempre no **original em inglês** (Control Plane, Worker Node, Desired State, Reconciliation, Garbage Collection, Object, Resource...), em títulos e no texto. A **explicação do conceito** é em português; a tradução aparece só como apoio (campo **Tradução** ou entre parênteses na primeira menção). Não usar "plano de controle", "coleta de lixo" e afins como termo principal.
