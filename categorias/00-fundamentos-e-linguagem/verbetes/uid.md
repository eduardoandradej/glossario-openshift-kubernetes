# UID (metadata.uid)

> **ID:** 00-fundamentos-e-linguagem/uid | **Termo original:** UID (unique identifier) | **Tradução:** identificador único | **Classe ontológica:** conceito (campo de identidade) | **Plataforma:** Kubernetes / OpenShift | **Escopo:** único em todo o cluster, por toda a sua vida | **Disponibilidade:** nativo | **Versões validadas:** Kubernetes 1.35 / OCP 4.22 | **Nível:** básico | **Atualizado em:** 2026-11-04

## Definição em uma frase

O UID é uma string **gerada pelo sistema** que identifica um objeto de forma única em todo o cluster e ao longo de toda a vida do cluster. Nenhum outro objeto, nem antes nem depois, terá o mesmo UID.

## Explicação didática

O [nome](resource-name.md) é como um nome próprio, que pode ser reutilizado. O UID é como uma **impressão digital**: se você apaga o Pod `web-1` e cria outro `web-1`, os dois terão nomes iguais e UIDs diferentes. É assim que o sistema distingue "ocorrências históricas" de entidades parecidas.

Os UIDs do Kubernetes são **UUIDs** (identificadores universalmente únicos, padronizados em ISO/IEC 9834-8 e ITU-T X.667).

## Para que existe e qual problema resolve

Evita confusão entre um objeto apagado e um recriado com o mesmo nome. Isso é essencial para:

- **Relações de dono:** `ownerReferences` guarda o `uid` do dono. Um Pod órfão não é "adotado" por engano por um ReplicaSet recriado com o mesmo nome, a menos que os seletores e as regras de adoção permitam.
- **Coleta de lixo:** dependentes cujo dono (pelo UID) não existe mais podem ser removidos.
- **Auditoria e eventos:** os Events referenciam o `uid` do objeto envolvido.

## Funcionamento técnico e ciclo de vida

- Atribuído pelo API server na **criação**; o cliente não o define.
- **Imutável** enquanto o objeto existir.
- Some com o objeto; um objeto recriado recebe outro UID.

## Relações e dependências

- Parte do [metadata](metadata.md); complementa o [nome](resource-name.md).
- Referenciado em `ownerReferences` (próximo lote: *OwnerReference*) e nos Events.

## Exemplo de situação real

Um Deployment é apagado com `--cascade=orphan` (os Pods ficam) e depois recriado com o mesmo nome. Os ReplicaSets antigos continuam apontando, em `ownerReferences`, para o **UID antigo**. O comportamento de adoção depende das regras do controller; o UID é o que permite perceber que o dono "é outro".

## Como visualizar e inspecionar (somente leitura)

```bash
# UID de um objeto
oc get deployment <nome> -n <namespace> -o jsonpath='{.metadata.uid}{"\n"}'

# UID do dono, registrado no dependente
oc get pod <nome> -n <namespace> \
  -o jsonpath='{range .metadata.ownerReferences[*]}{.kind}/{.name} uid={.uid}{"\n"}{end}'

# Eventos citam o UID do objeto envolvido
oc get events -n <namespace> -o jsonpath='{range .items[*]}{.involvedObject.kind}/{.involvedObject.name} {.involvedObject.uid}{"\n"}{end}' | head
```

## Como interpretar a saída

- O formato é o de UUID: 32 dígitos hexadecimais em 5 grupos (`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`).
- Se o `uid` em `ownerReferences` de um Pod **não** coincide com o `uid` atual do ReplicaSet de mesmo nome, o dono registrado não existe mais: é um sinal de órfão ou de recriação.
- Nos Events, `involvedObject.uid` diz a qual "encarnação" do objeto o evento se refere, o que é útil quando o nome foi reutilizado.

## Diferenças e confusões frequentes

- **UID (do objeto) ≠ UID de usuário Linux:** o `runAsUser` de um contêiner e as faixas de UID do OpenShift (`openshift.io/sa.scc.uid-range`) são identificadores de **processo**, da categoria 08. Mesma sigla, conceitos diferentes.
- **UID ≠ `resourceVersion`:** o UID identifica o objeto; o `resourceVersion` identifica uma **versão** dele.

## No OpenShift 4.22 versus Kubernetes

Igual ao Kubernetes. Cuidado com a ambiguidade da sigla no OpenShift: em namespaces e SCCs, "UID" quase sempre significa o **UID de usuário do processo**.

## No HomeLab SNO

Leitura segura com `-o jsonpath`. Os UIDs não são segredos, mas também não há motivo para publicá-los em material de estudo.

## Termos relacionados

[Resource Name](resource-name.md) · [Metadata](metadata.md) · [Objeto](object.md) · [Namespace](namespace.md) · [ReplicaSet](../../03-workloads/verbetes/replicaset.md)

## Fontes oficiais

- Kubernetes — Object Names and IDs, "UIDs": <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/> (fonte: `kubernetes/website` `release-1.35`)
- Kubernetes Glossary — UID: <https://kubernetes.io/docs/reference/glossary/?all=true#term-uid>
- Kubernetes API Conventions — "Metadata" (`uid`): <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md>

## Revisão editorial

- **Estado:** 🟡 desenvolvido. Fontes conferidas em 2026-11-04.
- **Pendências:** o comportamento de adoção depois de `--cascade=orphan` deve ser aprofundado e conferido nos verbetes *OwnerReference* e *Garbage Collection* (lote 3). Exemplos **não executados** no SNO.
