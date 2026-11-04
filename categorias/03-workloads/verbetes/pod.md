# Pod

> **Classe:** Objeto API (namespaced)  
> **Categoria:** 03-workloads  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável

## Definição

Menor unidade implantável de computação no Kubernetes: agrupa um ou mais contêineres que compartilham rede, IP e volumes declarados. Geralmente é criado e substituído por um controlador de workloads, em vez de administrado isoladamente.

## Por que existe?

Uma aplicação empacotada em contêiner precisa de uma unidade executável e gerenciável dentro do cluster.

## Relações

`Node`, `Container`, `Deployment`, `ReplicaSet`, `Service`.

## Como visualizar e inspecionar

```bash
oc get pods -A
oc describe pod <nome> -n <namespace>
oc get pod <nome> -n <namespace> -o yaml
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Um Pod em Running não garante que a aplicação esteja Ready. O IP e o ciclo de vida do Pod são efêmeros.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)


<details>
<summary>Notas de revisão</summary>

Versão inicial. Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.

</details>
