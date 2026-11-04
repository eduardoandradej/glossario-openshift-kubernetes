# Operator

> **Classe:** Padrão arquitetural e software controlador  
> **Categoria:** 09-operators-e-extensoes  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável  
> **Estado editorial:** base revisada; aprofundamento ainda previsto

## Definição

Software que codifica conhecimento operacional de uma aplicação ou componente, reagindo ao current state de recursos e reconciliando-o com o desired state.

## Por que existe?

Automatizar instalação, manutenção, reconciliation e atualização de serviços complexos.

## Relações

`Controller`, `CRD`, `CR`, `OLM Classic`, `OLM v1`.

## Como visualizar e inspecionar

```bash
oc get operators -A
oc get clusteroperators
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Os comandos consultam recursos diferentes, não uma lista universal de todo software que implementa o padrão Operator.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)

> Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.
