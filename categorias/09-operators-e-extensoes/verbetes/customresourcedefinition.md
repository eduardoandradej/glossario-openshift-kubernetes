# CustomResourceDefinition

> **Classe:** Objeto API (cluster-scoped)  
> **Categoria:** 09-operators-e-extensoes  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável

## Definição

Objeto que estende a API do Kubernetes com um novo tipo de recurso, validado por esquema e acessível pelas ferramentas normais de API.

## Por que existe?

Permitir que operadores e extensões introduzam objetos específicos de um domínio.

## Relações

`Custom Resource`, `Operator`, `API Group`, `Controller`.

## Como visualizar e inspecionar

```bash
oc get crds
oc describe crd <nome>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Uma CRD registra um tipo, mas não garante, sozinha, a existência de um controlador que implemente sua lógica.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)


<details>
<summary>Notas de revisão</summary>

Versão inicial. Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.

</details>
