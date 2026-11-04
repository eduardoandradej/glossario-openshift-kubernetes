# Critérios de qualidade e governança

1. **Conhecimento antes do comando**: definição, objetivo, funcionamento, relações e só depois inspeção.
2. **Fontes**: documentação oficial Kubernetes, Red Hat e API Discovery; URLs por verbete; registrar a versão, não inferir suporte.
3. **Ontologia**: distinguir conceitos, componentes, status, tipos de objeto, CLI, recursos externos e extensões.
4. **Classificação**: nomes reais, API Group, kind, alcance, permissões, padrão versus opcional.
5. **Não inventar**: quando não houver objeto correspondente, explicar e usar comando indireto ou declarar não aplicável.
6. **Operação segura**: comandos de consulta sempre por padrão; não ler `Secret.data`, não revelar tokens, não alterar clusters.
7. **SNO**: não presumir storage provisioner, ODF, virtualization, AI, ingress externo, OLM adicional; explicar quando depende de instalação ou infraestrutura.
8. **Compatibilidade**: destacar deprecated e migrações, por exemplo DeploymentConfig; OLM Classic versus OLM v1.
9. **Material autoral**: jamais copiar páginas longas de Red Hat/Kubernetes ou apostilas pagas; citar e produzir texto original.
10. **Diagramas**: Mermaid legível no GitHub, com legendas e sem equivalências falsas.
11. **Granularidade**: um verbete por conceito; links relacionados; categorias com índice; índice alfabético gerado e consistente.
12. **Revisão**: termos candidatos não contam como concluídos; marcar completo somente com fontes, classificação, exemplo, interpretação e diferenças revisadas.
13. **Verificação**: se houver acesso autorizado ao cluster, usar `oc api-resources` e `oc explain` para validar APIs, nunca para pressupor componentes opcionais ou inferir ausência global.
14. **Git**: não modificar outros repositórios; trabalhar na branch main deste novo repositório conforme fluxo combinado; commits pequenos, sem force-push e sem apagar conteúdo.
