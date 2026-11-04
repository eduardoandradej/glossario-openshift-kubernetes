# Deployment

> **Classe:** Objeto API (namespaced)  
> **Categoria:** 03-workloads  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável  
> **Estado editorial:** base revisada; aprofundamento ainda previsto

## Definição

Controlador declarativo utilizado para manter e atualizar aplicações, tipicamente sem estado. Um Deployment gerencia ReplicaSets, que por sua vez mantêm o conjunto de Pods.

## Por que existe?

Executar réplicas de uma aplicação e permitir atualizações e reversões gerenciadas.

## Relações

`ReplicaSet`, `Pod`, `RollingUpdate`, `Rollout`.

## Como visualizar e inspecionar

```bash
oc get deployments -A
oc describe deployment <nome> -n <namespace>
oc rollout status deployment/<nome> -n <namespace>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Deployment não é sinônimo de Pod; também não é igual ao DeploymentConfig legado do OpenShift.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)

> Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.
