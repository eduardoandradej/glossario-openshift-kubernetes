# Node

> **Classe:** Objeto API (cluster-scoped)  
> **Categoria:** 02-compute-e-nodes  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável

## Definição

Representa uma máquina física ou virtual habilitada a executar Pods; contém capacidade, condições e informações do kubelet. O scheduler considera restrições e recursos disponíveis ao posicionar novos Pods.

## Por que existe?

Disponibilizar capacidade de CPU, memória e execução para os workloads do cluster.

## Relações

`Pod`, `kubelet`, `Machine`, `Node Condition`, `Scheduler`.

## Como visualizar e inspecionar

```bash
oc get nodes -o wide
oc describe node <nome>
oc get nodes -o json
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Em um Single Node OpenShift, o mesmo nó desempenha funções de control plane e worker; a simples presença de um nó não significa que ele esteja Ready.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)


<details>
<summary>Notas de revisão</summary>

Versão inicial. Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.

</details>
