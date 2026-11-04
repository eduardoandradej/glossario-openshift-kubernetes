# Mapa de categorias

O glossário está organizado em 18 categorias temáticas, da base conceitual aos componentes opcionais. A ordem sugere uma progressão de estudo, mas cada categoria pode ser consultada de forma independente.

- **[00 — Fundamentos, linguagem e modelo declarativo](../categorias/00-fundamentos-e-linguagem/README.md):** O vocabulário básico do Kubernetes e do OpenShift: o que é um objeto, como a API se organiza, o que significam Spec e Status e como funciona o modelo declarativo (Desired State e Reconciliation).
- **[01 — Arquitetura e Control Plane](../categorias/01-arquitetura-e-control-plane/README.md):** Quem decide e quem executa no cluster: os componentes do Control Plane, o que roda em cada nó e como o OpenShift organiza e mantém essas peças.
- **[02 — Compute, Nodes e capacidade](../categorias/02-compute-e-nodes/README.md):** As máquinas do cluster: Nodes, recursos de CPU e memória, configuração dos nós e como a capacidade é medida e reservada.
- **[03 — Workloads e execução de aplicações](../categorias/03-workloads/README.md):** Como as aplicações rodam: Pods, contêineres e os controllers de workload (Deployment, StatefulSet, DaemonSet, Job...).
- **[04 — Networking, Services e publicação](../categorias/04-networking/README.md):** Como as aplicações se encontram e são publicadas: Services, DNS, Routes, Ingress e políticas de rede.
- **[05 — Storage e persistência](../categorias/05-storage/README.md):** Como os dados sobrevivem aos Pods: volumes, PersistentVolumes, PersistentVolumeClaims, StorageClasses e CSI.
- **[06 — Configuração, metadados e extensibilidade da API](../categorias/06-configuracao-e-api/README.md):** Como configurar aplicações e estender a API: ConfigMaps, Secrets e os mecanismos de extensão.
- **[07 — Identidade, autenticação e autorização](../categorias/07-identidade-e-rbac/README.md):** Quem é você para o cluster e o que pode fazer: usuários, ServiceAccounts, OAuth e RBAC.
- **[08 — Segurança, isolamento e políticas](../categorias/08-seguranca-e-politicas/README.md):** Como o cluster isola e protege cargas: SCCs, Pod Security, SELinux e políticas.
- **[09 — Operators, OLM e extensões](../categorias/09-operators-e-extensoes/README.md):** Como o software é operado de forma automatizada: Operators, CRDs, ClusterOperators e o OLM (Classic e v1).
- **[10 — Build, imagens e registries](../categorias/10-builds-imagens-registry/README.md):** Do código à imagem: builds, ImageStreams, imagens de contêiner e registries.
- **[11 — Scheduling, capacidade e escalabilidade](../categorias/11-agendamento-e-escalabilidade/README.md):** Onde os Pods rodam e como a aplicação cresce: requests, limits, afinidades, taints e autoscaling.
- **[12 — Observabilidade, logs e métricas](../categorias/12-observabilidade/README.md):** Como enxergar o que acontece: métricas, alertas, logs e eventos.
- **[13 — Instalação, atualizações e manutenção](../categorias/13-ciclo-de-vida-cluster/README.md):** O ciclo de vida do cluster: instalação, atualização, backup e manutenção.
- **[14 — CLI, YAML, ferramentas e inspeção](../categorias/14-cli-yaml-e-api/README.md):** As ferramentas do dia a dia: `oc`, `kubectl`, YAML, JSONPath e técnicas de inspeção.
- **[15 — Empacotamento, entrega e GitOps](../categorias/15-entrega-e-automacao/README.md):** Como empacotar e entregar aplicações: Helm, Kustomize, Templates, pipelines e GitOps.
- **[16 — Virtualização, IA e componentes opcionais](../categorias/16-virtualizacao-ia-e-extensoes/README.md):** Componentes que podem ser instalados sobre a plataforma: virtualização, IA, service mesh e outros.
- **[17 — Diagnóstico, falhas e confiabilidade](../categorias/17-troubleshooting-e-resiliencia/README.md):** Como investigar problemas e projetar para falhas: estados de erro, diagnóstico e resiliência.
