# Secret

> **Classe:** Objeto API (namespaced)  
> **Categoria:** 06-configuracao-e-api  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável

## Definição

Recurso destinado ao armazenamento de dados sensíveis como credenciais, chaves e certificados para uso por aplicações e serviços.

## Por que existe?

Separar e controlar o acesso a valores sensíveis necessários ao funcionamento de workloads.

## Relações

`ConfigMap`, `ServiceAccount`, `Volume`, `RBAC`.

## Como visualizar e inspecionar

```bash
oc get secrets -n <namespace>
oc describe secret <nome> -n <namespace>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Base64 não é criptografia. Não mostrar ou copiar os valores de Secret em exemplos de inspeção; priorizar metadados e acesso mínimo.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)


<details>
<summary>Notas de revisão</summary>

Versão inicial. Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.

</details>
