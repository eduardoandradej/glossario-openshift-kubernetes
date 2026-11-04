# Job

## Definição

Recurso que gerencia Pods de execução finita até atingir a conclusão esperada, com política de tentativas e paralelismo.

## Por que existe?

Executar tarefas batch que precisam terminar, em vez de rodar continuamente.

## Relações

`Pod`, `CronJob`, `backoffLimit`, `completions`.

## Como visualizar e inspecionar

```bash
oc get jobs -A
oc describe job <nome> -n <namespace>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Um Job é orientado à conclusão; um Deployment é orientado à permanência de réplicas.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **Classe:** Objeto API (namespaced)
- **Categoria:** 03-workloads
- **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável

**Notas de revisão**

Versão inicial. Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.

</details>
