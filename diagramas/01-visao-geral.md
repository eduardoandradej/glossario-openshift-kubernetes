# Mapa mental — Kubernetes e OpenShift

```mermaid
flowchart TB
    U[Usuário / oc / kubectl] --> A[API Server]
    A <--> E[(etcd)]
    A --> C[Controllers]
    A --> S[Scheduler]
    S --> N[Node]
    N --> K[kubelet + CRI-O]
    K --> P[Pods e contêineres]
    P --> SV[Services / EndpointSlices]
    SV --> R[Routes / Ingress]
    P --> PVC[PVC]
    PVC --> PV[PV / CSI / Storage]
    O[Operators] --> A
```

As setas simplificam relações e não representam todos os fluxos físicos de tráfego. A publicação Route/Ingress é operacionalizada por controladores próprios.
