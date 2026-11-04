# ConfigMap

> **Classe:** Objeto API (namespaced)  
> **Categoria:** 06-configuracao-e-api  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável

## Definição

Objeto que armazena pares chave-valor e dados de configuração não sensíveis para consumo por Pods ou ferramentas.

## Por que existe?

Separar configuração da imagem de contêiner.

## Relações

`Pod`, `Secret`, `envFrom`, `ConfigMap Volume`.

## Como visualizar e inspecionar

```bash
oc get configmaps -A
oc describe configmap <nome> -n <namespace>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

ConfigMap não deve ser usado para credenciais ou informações sensíveis.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)


<details>
<summary>Notas de revisão</summary>

Versão inicial. Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.

</details>
