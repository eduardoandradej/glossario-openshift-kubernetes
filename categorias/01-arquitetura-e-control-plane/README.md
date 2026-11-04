# 01 — Arquitetura e control plane

> Inventário inicial de candidatos a verbetes. Não significa que todos sejam objetos de API, instalados por padrão ou suportados na versão 4.22. Cada termo deve ser pesquisado e classificado.

**Total inicial:** 31 termos candidatos.

## Termos desta categoria

**Legenda:** `[x] … 🟡` = verbete desenvolvido, com fontes conferidas e **sem validação no cluster** · `[ ]` = candidato.

**Lote 1 (2026-11-04):** 12 verbetes + 2 remissões (kube-apiserver, Node Agent).

- [x] [Control Plane](verbetes/control-plane.md) 🟡
- [x] [Worker Node](verbetes/worker-node.md) 🟡
- [x] [Master Node](verbetes/master-node.md) 🟡
- [x] [kube-apiserver](../00-fundamentos-e-linguagem/verbetes/api-server.md) — remissão para API Server (categoria 00) 🟡
- [x] [etcd](verbetes/etcd.md) 🟡
- [x] [kube-scheduler](verbetes/kube-scheduler.md) 🟡
- [x] [kube-controller-manager](verbetes/kube-controller-manager.md) 🟡
- [x] [cloud-controller-manager](verbetes/cloud-controller-manager.md) 🟡
- [x] [kubelet](verbetes/kubelet.md) 🟡
- [x] [Container Runtime](verbetes/container-runtime.md) 🟡
- [x] [CRI](verbetes/cri.md) 🟡
- [x] [CRI-O](verbetes/cri-o.md) 🟡
- [ ] Kube Proxy
- [ ] OVN-Kubernetes
- [ ] CoreDNS
- [ ] DNS Operator
- [ ] Cluster DNS
- [ ] Cluster Version Operator
- [ ] Cluster Operator
- [ ] Machine Config Operator
- [ ] MachineConfig
- [ ] MachineConfigPool
- [ ] Bootstrap
- [ ] Quorum
- [ ] High Availability
- [ ] SNO
- [ ] HyperShift
- [ ] Hosted Control Plane
- [x] [Node Agent](verbetes/kubelet.md) — remissão para kubelet 🟡
- [x] [Static Pod](verbetes/static-pod.md) 🟡
- [ ] Infrastructure Node

## Como expandir

Use o [modelo de verbete](../../modelos/MODELO-VERBETE.md), consultando o [prompt mestre](../../PROMPT-MESTRE.md). Antes de marcar um termo, criar verbete original, verificar fontes oficiais, incluir comandos de inspeção quando pertinentes e revisar nomenclaturas e diferenças entre as versões.
