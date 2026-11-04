# ResourceVersion (metadata.resourceVersion)

> **ID:** 00-fundamentos-e-linguagem/resource-version | **Termo original:** resourceVersion | **Tradução:** versão do recurso | **Classe ontológica:** conceito (campo de metadata e parâmetro de consulta) | **Plataforma:** Kubernetes / OpenShift | **Escopo:** não aplicável | **Disponibilidade:** nativo | **Versões validadas:** Kubernetes 1.35 / OCP 4.22 | **Nível:** intermediário → avançado | **Atualizado em:** 2026-11-04

## Definição em uma frase

`resourceVersion` é a string que identifica a **versão interna de um objeto no servidor**. Ela muda a cada gravação e serve para detectar mudanças, para o controle de concorrência otimista e para consultas e *watches* consistentes.

## Explicação didática

Cada vez que **qualquer coisa** num objeto é gravada (`spec`, `status`, labels...), o servidor dá a ele uma nova `resourceVersion`. Com isso:

- um cliente sabe se o objeto mudou desde a última leitura;
- duas pessoas editando ao mesmo tempo não se atropelam: quem gravar com uma versão desatualizada recebe **conflito** (HTTP 409);
- um *watch* pode retomar "a partir da versão X".

## Para que existe e qual problema resolve

**Concorrência otimista:** em vez de bloquear o objeto, o sistema deixa todos lerem e verifica, na hora de gravar, se a versão lida ainda é a atual. Se não for, a escrita falha com `Conflict`, e o cliente relê e tenta de novo. É isso que você vê quando dois `oc edit` disputam o mesmo objeto.

## Funcionamento técnico e ciclo de vida

- **Muda em toda modificação** do objeto, inclusive em atualizações de `status` feitas por controllers.
- **Deve ser devolvida sem alteração** ao servidor; o cliente não fabrica valores.
- **Comparação (novidade do 1.35):** para tipos servidos pelo kube-apiserver (nativos e CRDs), as versões são **ordenáveis como inteiros crescentes dentro do mesmo tipo de recurso**. Duas versões de Deployments podem ser comparadas, mesmo em namespaces diferentes; a de um Pod com a de um Deployment, não. A partir do **Kubernetes 1.35**, essa ordenação passou a ser requisito da certificação de conformidade. Para APIs de **servidores agregados (de extensão)**, só se pode confiar na comparação se as duas strings forem números decimais; caso contrário, só vale a **igualdade**.
- **Implementação atual:** baseada na *mod_revision* do etcd, mas a documentação pede que os clientes **não** dependam desse detalhe.
- **Em consultas:** `get`, `list` e `watch` aceitam o parâmetro `resourceVersion` para expressar requisitos de consistência. Um *watch* com versão muito antiga pode receber **410 Gone**, o que obriga o cliente a listar de novo.

## Relações e dependências

- Campo de [metadata](metadata.md).
- **Não confundir** com [Generation](generation.md): a `generation` muda só com o desired state; a `resourceVersion` muda com qualquer escrita.
- Usada internamente por [controllers](controller.md) (informers e watches).

## Exemplo de situação real

Um script lê um ConfigMap, altera um valor e grava com `replace` minutos depois. Nesse meio-tempo, outro processo mudou o mesmo ConfigMap. O `replace` falha com `the object has been modified; please apply your changes to the latest version and try again`. O script precisa reler e reaplicar a mudança.

## Como visualizar e inspecionar (somente leitura)

```bash
# Versão atual de um objeto
oc get configmap <nome> -n <namespace> -o jsonpath='{.metadata.resourceVersion}{"\n"}'

# resourceVersion × generation: veja qual muda com o quê
oc get deployment <nome> -n <namespace> \
  -o jsonpath='rv={.metadata.resourceVersion} gen={.metadata.generation}{"\n"}'

# Acompanhar mudanças em tempo real (watch; Ctrl+C para sair)
oc get deployment <nome> -n <namespace> -w -o jsonpath='{.metadata.resourceVersion}{"\n"}'
```

## Como interpretar a saída

- Se a `rv` mudou e a `gen` não, houve escrita que não alterou o desired state (normalmente atualização de `status`, de labels ou de annotations).
- No `-w`, cada linha nova indica uma gravação no objeto. Rajadas frequentes num objeto estável podem indicar um controller "brigando" com outro.
- A mensagem `the object has been modified` é o **409 Conflict** da concorrência otimista. Não é corrupção.

## Diferenças e confusões frequentes

- **ResourceVersion × Generation** (ver acima).
- **ResourceVersion × API Version:** `apps/v1` é a versão do **esquema**; a `resourceVersion` é a versão de **um objeto**.
- **ResourceVersion × revisão de Deployment:** a annotation `deployment.kubernetes.io/revision` conta rollouts e é outra coisa.
- **Ordenação:** comparar versões só faz sentido dentro do mesmo tipo de recurso, e com o cuidado acima para APIs agregadas.

## No OpenShift 4.22 versus Kubernetes

O OCP 4.22 usa Kubernetes 1.35, então a regra de ordenação vale para os tipos servidos pelo kube-apiserver. Os grupos `*.openshift.io` atendidos pelo OpenShift API server são **APIs agregadas**: antes de comparar versões desses tipos, aplique a regra dos números decimais.

## No HomeLab SNO

Observar `resourceVersion` é seguro. Usar `-w` por muito tempo mantém uma conexão aberta com a API; encerre quando terminar.

## Termos relacionados

[Generation](generation.md) · [ObservedGeneration](observed-generation.md) · [Metadata](metadata.md) · [API Server](api-server.md) · [Controller](controller.md)

## Fontes oficiais

- Kubernetes — API Concepts, "Resource versions" (ordenação no 1.35, semântica de get/list/watch, 410 Gone): <https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions> (fonte: `kubernetes/website` `release-1.35`)
- Kubernetes API Conventions — "Concurrency Control and Consistency": <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md>

<details>
<summary>Notas de revisão</summary>

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-04.
- **Correção transversal:** o verbete [Metadata](metadata.md) foi ajustado para refletir a regra de ordenação do 1.35.
- **Pendências:** confirmar o texto da mensagem de conflito no cliente 4.22 e a aplicação da regra de ordenação aos grupos `*.openshift.io` servidos por agregação, que **não foram verificados**.

</details>
