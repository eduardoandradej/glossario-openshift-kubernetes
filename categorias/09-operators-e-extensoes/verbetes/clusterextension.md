# ClusterExtension

> **Classe:** Objeto API OLM v1 (cluster-scoped)  
> **Categoria:** 09-operators-e-extensoes  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável  
> **Estado editorial:** base revisada; aprofundamento ainda previsto

## Definição

Recurso de OLM v1 utilizado para declarar e gerenciar a instalação e o ciclo de vida de extensões no cluster.

## Por que existe?

Gerenciar extensões do cluster pelo modelo mais recente do OLM no OpenShift 4.22.

## Relações

`OLM v1`, `ClusterCatalog`, `Catalogd`, `Operator Controller`.

## Como visualizar e inspecionar

```bash
oc api-resources --api-group=olm.operatorframework.io
oc get clusterextensions
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

OLM v1 e OLM Classic coexistem no OCP 4.22; não confundir ClusterExtension com Subscription/CSV do modelo Classic.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)

> Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.
