# DaemonSet

> **Classe:** Objeto API (namespaced)  
> **Categoria:** 03-workloads  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável  
> **Estado editorial:** base revisada; aprofundamento ainda previsto

## Definição

Controlador que procura garantir um Pod em cada nó elegível (ou subconjunto selecionado), comumente para agentes de infraestrutura.

## Por que existe?

Instalar agentes ou serviços locais aos nós sem gerenciar manualmente cada réplica.

## Relações

`Node`, `Pod`, `Toleration`, `NodeSelector`.

## Como visualizar e inspecionar

```bash
oc get daemonsets -A
oc describe daemonset <nome> -n <namespace>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Não significa que o Pod irá executar em todos os nós indiscriminadamente: seletores, tolerações e restrições importam.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)

> Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.
