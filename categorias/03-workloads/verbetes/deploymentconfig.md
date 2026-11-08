# DeploymentConfig

## Definição em uma frase

O DeploymentConfig é o **recurso de implantação próprio e legado do OpenShift**, **deprecated desde o OCP 4.14**: ainda é suportado, mas não é recomendado para novas instalações, e a alternativa indicada é o [Deployment](deployment.md).

## Explicação didática

Antes de o Deployment do Kubernetes amadurecer, o OpenShift oferecia o DeploymentConfig, com recursos próprios, como *triggers* que reimplantavam a aplicação quando uma imagem nova chegava a um ImageStream. Hoje o Deployment cobre esse papel, e a Red Hat descontinuou o DeploymentConfig.

| | Deployment | DeploymentConfig |
|---|---|---|
| Origem | Kubernetes (`apps/v1`) | OpenShift (`apps.openshift.io/v1`) |
| Controla | ReplicaSets | ReplicationControllers |
| Situação no OCP 4.22 | **Recomendado** | **Deprecated** desde o 4.14 |

## Para que existe e qual problema resolve

Historicamente, implantação e atualização de aplicações no OpenShift. Hoje, o que importa é **reconhecê-lo** e **migrar** para Deployment.

## Funcionamento técnico e ciclo de vida

- Cria um [ReplicationController](replicationcontroller.md) por versão implantada (`<nome>-1`, `<nome>-2`...).
- Usa Pods "deployer" para executar cada implantação.
- Tem *triggers* (como `ImageChange` e `ConfigChange`) e *hooks* de ciclo de vida próprios.
- **Situação:** as release notes do OCP 4.14 anunciam a deprecação. O recurso continua suportado, mas só correções de segurança e críticas são feitas, e a recomendação é usar objetos `Deployment` ou outra alternativa. A tabela de recursos deprecated do 4.22 mantém o estado **Deprecated**.

## Relações e dependências

- Usa [ReplicationController](replicationcontroller.md) (legado).
- Substituto: [Deployment](deployment.md). Para reimplantar por mudança de imagem, há alternativas com ImageStreams e *triggers* em Deployments (categoria 10).

## Exemplo de situação real

Uma auditoria encontra DeploymentConfigs em projetos antigos. O plano de migração recria cada aplicação como Deployment (`apps/v1`), ajusta os campos equivalentes e remove os DeploymentConfigs, antes que o recurso seja removido numa versão futura.

## Como visualizar e inspecionar (somente leitura)

```bash
# Ainda há DeploymentConfigs no cluster?
oc get deploymentconfigs -A

# A API continua servida neste cluster?
oc api-resources --api-group=apps.openshift.io
```

## Como interpretar a saída

- `No resources found`: nenhum uso legado.
- O cliente pode exibir avisos de uso de recurso deprecated ao acessar o tipo. Isso é esperado.
- Se a API não for servida (por exemplo, com a *capability* correspondente desabilitada), o comando informa que o tipo não existe. Isso **não** é erro de permissão.

## Diferenças e confusões frequentes

- **DeploymentConfig não é "o Deployment do OpenShift":** é um recurso diferente, legado.
- **Deprecated ≠ removido:** ainda funciona e é suportado no 4.22, mas não deve ser usado em aplicações novas.

## No OpenShift 4.22 versus Kubernetes

Exclusivo do OpenShift, sem equivalente no Kubernetes upstream. Deprecated desde o 4.14 e assim mantido no 4.22.

## No HomeLab SNO

Não crie DeploymentConfigs nas aplicações de estudo. Use Deployment e trate o DeploymentConfig só como conceito histórico.

## Termos relacionados

[Deployment](deployment.md) · [ReplicationController](replicationcontroller.md) · [ReplicaSet](replicaset.md) · [Kind](../../00-fundamentos-e-linguagem/verbetes/kind.md)

## Fontes oficiais

- OCP 4.14 — Release notes, "DeploymentConfig resources are now deprecated" (fonte: `openshift-docs` `enterprise-4.14`, `release_notes/ocp-4-14-release-notes.adoc`)
- OCP 4.22 — Release notes, tabela de recursos deprecated e removidos: <https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/release_notes/ocp-4-22-release-notes> (fonte: `modules/rn-ocp-release-notes-deprecated-removed-tables.adoc`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/deploymentconfig
- **Termo original:** DeploymentConfig (DC)
- **Remissões:** deployer Pod, ImageChange trigger
- **Tradução:** não se traduz
- **Classe ontológica:** legado / deprecated (objeto da API do OpenShift)
- **API:** `apiVersion: apps.openshift.io/v1`, `kind: DeploymentConfig`
- **Plataforma:** OpenShift
- **Escopo:** namespaced
- **Disponibilidade:** deprecated desde o OCP 4.14; ainda suportado no 4.22
- **Versões validadas:** OCP 4.14 (deprecação) e OCP 4.22 (estado atual)
- **Nível:** básico
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-08.
- **Pendências:** os detalhes de *triggers*, *hooks* e Pods deployer são conhecidos da documentação de versões anteriores e **não foram conferidos** no 4.22. Verificar se o DeploymentConfig depende de uma *capability* opcional no 4.22.

</details>
