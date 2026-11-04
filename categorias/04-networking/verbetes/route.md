# Route

> **Classe:** Objeto API específico de OpenShift (namespaced)  
> **Categoria:** 04-networking  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável

## Definição

Recurso OpenShift que declara a publicação de um serviço por hostname e, quando configurado, TLS e regras de roteamento através da infraestrutura de ingresso da plataforma.

## Por que existe?

Expor aplicações, principalmente HTTP/HTTPS, ao exterior de maneira integrada ao OpenShift.

## Relações

`Service`, `Router`, `IngressController`, `TLS`.

## Como visualizar e inspecionar

```bash
oc get routes -A
oc describe route <nome> -n <namespace>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Route não é o mesmo objeto que Ingress. A compatibilidade e opções de TLS podem variar conforme o tipo de tráfego e implementação.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)


<details>
<summary>Notas de revisão</summary>

Versão inicial. Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.

</details>
