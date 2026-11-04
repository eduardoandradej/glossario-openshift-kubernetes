# Service

## Definição

Abstração que fornece um ponto de acesso estável e descoberta para um conjunto de endpoints, tipicamente Pods selecionados por labels. Tipos diferentes controlam a forma de exposição.

## Por que existe?

Desacoplar clientes dos IPs efêmeros e mudanças dos Pods.

## Relações

`Pod`, `Label Selector`, `EndpointSlice`, `Route`, `Ingress`.

## Como visualizar e inspecionar

```bash
oc get services -A
oc describe service <nome> -n <namespace>
oc get endpointslices -A
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Um Service do tipo ClusterIP não torna a aplicação automaticamente acessível fora do cluster.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **Classe:** Objeto API (namespaced)
- **Categoria:** 04-networking
- **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável

**Notas de revisão**

Versão inicial. Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.

</details>
