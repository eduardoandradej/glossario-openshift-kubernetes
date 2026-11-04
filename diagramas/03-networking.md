# Tráfego e publicação de aplicações

```mermaid
flowchart LR
    X[Cliente externo] --> EDGE[Load balancer ou endpoint de entrada]
    EDGE --> ROUTER[OpenShift Router / ingresso]
    RT[Route] -. configura .-> ROUTER
    ING[Ingress] -. regras interpretadas pelo controlador .-> ROUTER
    ROUTER --> SVC[Service]
    SVC --> ES[EndpointSlices]
    ES --> POD[Pods]
    NP[NetworkPolicy] -. restringe fluxos quando aplicável .-> POD
```

`Ingress` (objeto), `Route` (objeto OpenShift) e `IngressController` (recurso do operador) não são a mesma coisa. O desenho representa um cenário típico, não topologia obrigatória de todos os clusters.
