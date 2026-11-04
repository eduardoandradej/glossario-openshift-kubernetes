# StatefulSet

> **Classe:** Objeto API (namespaced)  
> **Categoria:** 03-workloads  
> **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável

## Definição

Controlador de aplicações com identidade estável por réplica, ordem de implantação e, quando configurado, armazenamento persistente individual.

## Por que existe?

Administrar aplicações que exigem identidade de rede e estado persistente por instância.

## Relações

`Pod`, `Service headless`, `PVC`, `VolumeClaimTemplate`.

## Como visualizar e inspecionar

```bash
oc get statefulsets -A
oc describe statefulset <nome> -n <namespace>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

StatefulSet não cria automaticamente um banco replicado ou altamente disponível; isso depende da aplicação e do operador.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)


<details>
<summary>Notas de revisão</summary>

Versão inicial. Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.

</details>
