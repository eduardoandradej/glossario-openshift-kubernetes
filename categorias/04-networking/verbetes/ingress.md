# Ingress

## Definição

Objeto Kubernetes de regras de tráfego HTTP/HTTPS para alcançar serviços, que depende de um controlador de ingress para efetivar o roteamento.

## Por que existe?

Definir regras de publicação web de modo padronizado na API Kubernetes.

## Relações

`Service`, `IngressClass`, `IngressController`, `Route`.

## Como visualizar e inspecionar

```bash
oc get ingress -A
oc describe ingress <nome> -n <namespace>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

O objeto Ingress, o controlador de ingress e o IngressController do OpenShift são três conceitos relacionados, mas distintos.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **Classe:** Objeto API Kubernetes (namespaced)
- **Categoria:** 04-networking
- **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável

**Notas de revisão**

Versão inicial. Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.

</details>
