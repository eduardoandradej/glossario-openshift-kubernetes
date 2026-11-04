# ServiceAccount

## Definição

Identidade não humana atribuída a processos ou Pods quando precisam interagir com a API do Kubernetes. As permissões são concedidas com RBAC.

## Por que existe?

Fornecer identidade apropriada a aplicações e automações.

## Relações

`Pod`, `Token`, `RoleBinding`, `ClusterRoleBinding`.

## Como visualizar e inspecionar

```bash
oc get serviceaccounts -A
oc describe serviceaccount <nome> -n <namespace>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Não pressupor que toda ServiceAccount tenha token Secret de longa duração criado automaticamente.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **Classe:** Objeto API (namespaced)
- **Categoria:** 07-identidade-e-rbac
- **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável

**Notas de revisão**

Versão inicial. Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.

</details>
