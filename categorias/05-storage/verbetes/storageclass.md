# StorageClass

> **Classe:** Objeto API (cluster-scoped)  
> **Categoria:** 05-storage  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável  
> **Estado editorial:** base revisada; aprofundamento ainda previsto

## Definição

Define a classe de provisionamento de volumes, incluindo provisionador, parâmetros, política de recuperação e modo de vínculo.

## Por que existe?

Oferecer perfis reutilizáveis de armazenamento para PVCs.

## Relações

`PVC`, `PV`, `CSI`, `Dynamic Provisioning`.

## Como visualizar e inspecionar

```bash
oc get storageclasses
oc describe storageclass <nome>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Uma instalação SNO pode não ter classe padrão provisionadora disponível; não assumir que criar um PVC resultará em PV.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)

> Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.
