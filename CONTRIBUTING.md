# Guia de contribuição

Obrigado por considerar uma contribuição para o MrBiTs AI Starforge.

Este repositório aceita artefatos para agentes de IA, incluindo skills, prompts, MCPs, templates e documentação de suporte. O foco é manter tudo reutilizável, auditável e simples de instalar.

## Antes de contribuir

- Abra uma issue para mudanças grandes, incompatíveis ou que adicionem dependências.
- Para correções pequenas, documentação e novos exemplos, um pull request direto é suficiente.
- Nunca inclua segredos, tokens, chaves privadas, dados de clientes ou credenciais de teste reais.
- Prefira mudanças pequenas e coesas.

## Tipos de contribuição

| Tipo | Caminho sugerido | Requisitos |
| --- | --- | --- |
| Skill | `skills/<nome>/` | `SKILL.md`, README, exemplos e validação. |
| Prompt | `prompts/<nome>.md` ou `prompts/<nome>/` | Objetivo, contexto de uso, entradas esperadas e exemplo. |
| MCP | `mcps/<nome>/` | README, instruções de execução, configuração e segurança. |
| Documentação | `docs/` ou README do artefato | Deve refletir o estado real dos arquivos. |

## Padrão para novas skills

Uma skill deve conter, no mínimo:

```text
skills/<nome>/
+-- SKILL.md
+-- README.md
```

Use `scripts/` para automações e `assets/` para templates, exemplos ou arquivos estáticos. Scripts devem ser determinísticos e evitar dependências externas quando possível.

## Padrão para prompts

Prompts devem informar:

- Finalidade.
- Quando usar.
- Entradas esperadas.
- Saída esperada.
- Riscos ou limitações.
- Exemplo de uso.

## Padrão para MCPs

MCPs devem informar:

- Como instalar e executar.
- Variáveis de ambiente necessárias.
- Escopos de permissão.
- Dados acessados ou persistidos.
- Como testar localmente.
- Ameaças conhecidas e limites de segurança.

## Pull requests

Antes de abrir um pull request:

1. Atualize a documentação do artefato alterado.
2. Atualize o índice no `README.md` se criar ou remover artefatos.
3. Rode a validação aplicável.
4. Preencha todos os campos do template de pull request.

## Estilo

- Use português claro para documentação geral do repositório.
- Documentação interna de artefatos pode usar português ou inglês, desde que seja consistente.
- Prefira exemplos copiáveis.
- Evite dependências novas sem necessidade real.
- Mantenha nomes de diretórios em `kebab-case`.

## Licença de contribuições

Ao contribuir, você concorda que sua contribuição será licenciada sob a licença MIT deste repositório.
