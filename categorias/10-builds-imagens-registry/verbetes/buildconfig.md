# BuildConfig

> **Classe:** Objeto API específico de OpenShift (namespaced)  
> **Categoria:** 10-builds-imagens-registry  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável

## Definição

Recurso histórico do subsistema de builds do OpenShift que define fontes, estratégia, gatilhos e destino de imagem para executar builds gerenciados.

## Por que existe?

Automatizar a construção de imagens a partir de código e estratégias suportadas pelo cluster.

## Relações

`Build`, `ImageStream`, `S2I`, `Registry`, `Tekton`.

## Como visualizar e inspecionar

```bash
oc api-resources | grep -i build
oc get buildconfigs -A
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Verificar disponibilidade e suporte na versão alvo; não confundir builds da plataforma com pipelines Tekton.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)


<details>
<summary>Notas de revisão</summary>

Versão inicial. Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.

</details>
