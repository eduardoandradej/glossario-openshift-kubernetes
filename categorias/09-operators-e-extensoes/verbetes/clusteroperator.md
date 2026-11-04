# ClusterOperator

> **Classe:** Objeto API específico de OpenShift (cluster-scoped)  
> **Categoria:** 09-operators-e-extensoes  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável  
> **Estado editorial:** base revisada; aprofundamento ainda previsto

## Definição

Recurso de status que reporta a saúde e condições de componentes operacionais fundamentais do OpenShift, como Available, Progressing e Degraded.

## Por que existe?

Expor o estado de componentes gerenciados da plataforma e apoiar o diagnóstico do cluster.

## Relações

`CVO`, `Operator`, `Conditions`, `ClusterVersion`.

## Como visualizar e inspecionar

```bash
oc get clusteroperators
oc describe clusteroperator <nome>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Um ClusterOperator não é equivalente a qualquer Operator instalado via OLM: representa o estado de um componente da plataforma.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)

> Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.
