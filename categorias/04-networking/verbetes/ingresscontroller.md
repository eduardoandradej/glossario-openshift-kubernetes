# IngressController

> **Classe:** Objeto API específico de OpenShift (namespaced na namespace do operador)  
> **Categoria:** 04-networking  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável

## Definição

Recurso de configuração do operador de ingresso OpenShift que gerencia uma implantação de controladores/routers para receber tráfego.

## Por que existe?

Configurar e operar o componente de entrada de tráfego da plataforma.

## Relações

`Route`, `Router`, `Ingress`, `Ingress Operator`.

## Como visualizar e inspecionar

```bash
oc get ingresscontrollers -n openshift-ingress-operator
oc describe ingresscontroller default -n openshift-ingress-operator
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Não confundir com o objeto Ingress Kubernetes; em OpenShift o recurso de configuração usa o grupo operator.openshift.io.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)


<details>
<summary>Notas de revisão</summary>

Versão inicial. Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.

</details>
