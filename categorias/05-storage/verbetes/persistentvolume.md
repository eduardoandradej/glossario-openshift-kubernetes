# PersistentVolume

## Definição

Representação de uma capacidade de armazenamento disponibilizada no cluster; pode ser provisionada previamente ou dinamicamente para atender a um PVC.

## Por que existe?

Oferecer um recurso persistente desacoplado do ciclo de vida de um Pod.

## Relações

`PersistentVolumeClaim`, `StorageClass`, `CSI`.

## Como visualizar e inspecionar

```bash
oc get pv
oc describe pv <nome>
```

**Leitura da saída:** observe nome, namespace ou escopo global, status/condições, seletor ou vínculo, seção `Events` e campos relevantes do recurso. A interpretação exata depende do tipo. Não execute alterações para consultar um objeto.

## Atenção às diferenças

PV não é sinônimo de disco físico. Sua implementação e ciclo de vida variam conforme backend e política de recuperação.

## Fontes para aprofundamento

- [Conceitos Kubernetes](https://kubernetes.io/docs/concepts/)
- [Documentação OpenShift 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **Classe:** Objeto API (cluster-scoped)
- **Categoria:** 05-storage
- **Plataforma:** OpenShift 4.22 / Kubernetes, conforme aplicável

**Notas de revisão**

Versão inicial. Próxima revisão: completar diagrama, exemplo real, correspondências entre API Groups, interpretação detalhada de campos, comparação e links cruzados. Nunca declarar o verbete "completo" antes desses itens.

</details>
