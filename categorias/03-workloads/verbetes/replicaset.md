# ReplicaSet

> **Classe:** Objeto API (namespaced)  
> **Categoria:** 03-workloads  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável  
> **Estado editorial:** base revisada; aprofundamento ainda previsto

## Definição

Controlador que mantém uma quantidade desejada de réplicas de Pods que correspondem a um seletor. Normalmente é gerenciado por um Deployment.

## Por que existe?

Manter o número de Pods desejado apesar de falhas e substituições.

## Relações

`Deployment`, `Pod`, `Label Selector`.

## Como visualizar e inspecionar

```bash
oc get replicasets -A
oc describe replicaset <nome> -n <namespace>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Um ReplicaSet antigo pode permanecer após um rollout para permitir histórico e rollback, respeitando o limite de revisões.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)

> Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.
