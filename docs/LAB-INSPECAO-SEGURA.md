# Inspeção inicial segura (somente leitura)

```bash
oc whoami
oc version
oc get nodes -o wide
oc get clusteroperators
oc get projects
oc api-resources -o wide
oc api-resources --namespaced=false
oc api-resources --namespaced=true
oc explain deployment
oc explain deployment.spec
oc get pods -A
oc get services -A
oc get routes -A
oc get storageclasses
oc get crds
oc get clusterextensions  # somente se o recurso for suportado e a permissão permitir
```

Comandos podem retornar `Forbidden` por RBAC, `the server doesn't have a resource type` por API ausente ou lista vazia por falta de instâncias. **Esses casos não são equivalentes.** Em SNO não instalar nem remover Operators, criar PVCs, apagar workloads ou mudar capacidades para testar um conceito.
