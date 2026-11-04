# NetworkPolicy

## Definição

Política declarativa de controle de tráfego de entrada e/ou saída de Pods selecionados. Sua aplicação depende de um plugin de rede compatível.

## Por que existe?

Restringir comunicações de rede entre workloads e destinos conforme critérios definidos.

## Relações

`Pod`, `Namespace`, `Label Selector`, `OVN-Kubernetes`.

## Como visualizar e inspecionar

```bash
oc get networkpolicies -A
oc describe networkpolicy <nome> -n <namespace>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

Uma NetworkPolicy sem efeito pode indicar plugin incompatível, seletores errados ou políticas que não abrangem o fluxo investigado.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **Classe:** Objeto API Kubernetes (namespaced)
- **Categoria:** 04-networking
- **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável

**Notas de revisão**

Versão inicial. Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.

</details>
