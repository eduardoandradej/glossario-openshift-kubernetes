# ImagePullBackOff

## Definição em uma frase

ImagePullBackOff é o **motivo exibido quando o kubelet não consegue baixar a imagem de um contêiner e passa a esperar intervalos crescentes entre as tentativas**; o contêiner nem chega a iniciar.

## Explicação didática

Antes de rodar, o contêiner precisa da imagem. Se o download falha, o kubelet registra `ErrImagePull` e, nas tentativas seguintes, `ImagePullBackOff`, com esperas que crescem até **5 minutos**.

## Para que existe e qual problema resolve

Como no [CrashLoopBackOff](crashloopbackoff.md), o backoff evita tentativas sem pausa contra um registry que não vai responder como esperado.

## Funcionamento técnico e ciclo de vida

- O contêiner fica em `Waiting`; o Pod, em `Pending`.
- **Causas comuns:**
  - nome ou tag da imagem errados (erro de digitação, tag inexistente);
  - registry privado sem credencial (falta `imagePullSecret` no Pod ou na ServiceAccount);
  - registry inacessível pela rede do nó (proxy, DNS, firewall, certificado);
  - limite de requisições do registry.
- O `imagePullPolicy` (`Always`, `IfNotPresent`, `Never`) define quando o kubelet tenta baixar.

## Relações e dependências

- `reason` do estado `Waiting` no [Container Lifecycle](container-lifecycle.md).
- Ligado a imagens e registries (categoria de builds e imagens) e a credenciais de pull.

## Exemplo de situação real

Um Deployment novo fica em `ImagePullBackOff`. O evento diz "unauthorized": a imagem está num registry privado. Vincular o pull secret à ServiceAccount usada pelo Pod resolve sem alterar o Deployment.

## Como visualizar e inspecionar (somente leitura)

```bash
# Imagem pedida e motivo da espera
oc get pod <nome> -n <namespace> -o jsonpath='{range .status.containerStatuses[*]}{.name}: {.image} {.state.waiting.reason} {.state.waiting.message}{"\n"}{end}'

# Eventos de pull (mensagem do registry)
oc get events -n <namespace> --field-selector involvedObject.name=<nome>

# Pull secrets disponíveis para o Pod (sem mostrar conteúdo)
oc get pod <nome> -n <namespace> -o jsonpath='{.spec.imagePullSecrets}{"\n"}'
```

## Como interpretar a saída

- "not found" ou "manifest unknown": nome ou tag errados.
- "unauthorized" ou "authentication required": falta credencial.
- Timeouts, "no such host" ou erros de certificado: rede, DNS ou confiança no registry a partir do nó.

## Diferenças e confusões frequentes

- **ErrImagePull × ImagePullBackOff:** a falha em si × a espera entre tentativas.
- **ImagePullBackOff × CrashLoopBackOff:** sem imagem × imagem baixada, mas o processo falha.

## No OpenShift 4.22 versus Kubernetes

Mesmo mecanismo. No OpenShift, há um pull secret global do cluster e configurações de registries por recursos de configuração de imagens; o registry interno é acessível pelas ServiceAccounts do projeto.

## No HomeLab SNO

Em ambientes com acesso restrito à internet, confira primeiro se o nó resolve e alcança o registry.

## Termos relacionados

[CrashLoopBackOff](crashloopbackoff.md) · [Container Lifecycle](container-lifecycle.md) · [Container](container.md) · [ServiceAccount](../../07-identidade-e-rbac/verbetes/serviceaccount.md) · [Secret](../../06-configuracao-e-api/verbetes/secret.md)

## Fontes oficiais

- Kubernetes — Images, "ImagePullBackOff" e "Image pull policy": <https://kubernetes.io/docs/concepts/containers/images/> (fonte: `kubernetes/website` `release-1.35`, `concepts/containers/images.md`)

<details>
<summary>Ficha técnica e notas de revisão</summary>

**Ficha técnica**

- **ID:** 03-workloads/imagepullbackoff
- **Termo original:** ImagePullBackOff
- **Remissões:** ErrImagePull, imagePullPolicy, imagePullSecrets
- **Tradução:** não se traduz
- **Classe ontológica:** estado (motivo de `Waiting`)
- **Plataforma:** Kubernetes / OpenShift
- **Escopo:** não aplicável
- **Disponibilidade:** nativo
- **Versões validadas:** Kubernetes 1.35 / OCP 4.22
- **Nível:** básico
- **Atualizado em:** 2026-11-08

**Notas de revisão**

- **Estado:** desenvolvido. Fontes conferidas em 2026-11-08.
- **Pendências:** detalhes do pull secret global e da configuração de registries do OCP 4.22 não conferidos nesta rodada.

</details>
