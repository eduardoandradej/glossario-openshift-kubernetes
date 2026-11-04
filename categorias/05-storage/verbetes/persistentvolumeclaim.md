# PersistentVolumeClaim

> **Classe:** Objeto API (namespaced)  
> **Categoria:** 05-storage  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável  
> **Estado editorial:** base revisada; aprofundamento ainda previsto

## Definição

Pedido de armazenamento realizado por uma aplicação ou usuário que solicita capacidade, modo de acesso e, opcionalmente, uma StorageClass.

## Por que existe?

Permitir que workloads solicitem armazenamento sem conhecer os detalhes físicos de sua provisão.

## Relações

`PersistentVolume`, `StorageClass`, `Pod`, `CSI`.

## Como visualizar e inspecionar

```bash
oc get pvc -A
oc describe pvc <nome> -n <namespace>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

PVC Pending pode ser normal com WaitForFirstConsumer; antes de concluir falha, examine StorageClass e eventos.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)

> Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.
