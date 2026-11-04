# Namespace

> **Classe:** Objeto API (cluster-scoped)  
> **Categoria:** 00-fundamentos-e-linguagem  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável  
> **Estado editorial:** base revisada; aprofundamento ainda previsto

## Definição

Espaço lógico que organiza e delimita o escopo de vários recursos da API. Namespaces separam nomes e facilitam políticas de acesso e cotas, mas não equivalem, por si só, a isolamento físico ou de rede.

## Por que existe?

Organizar recursos de equipes, projetos e aplicações dentro de um cluster.

## Relações

`Project`, `RBAC`, `ResourceQuota`, `NetworkPolicy`.

## Como visualizar e inspecionar

```bash
oc get namespaces
oc describe namespace <nome>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Em OpenShift, Project é uma abstração de acesso e gestão construída em torno de um Namespace.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)

> Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.
