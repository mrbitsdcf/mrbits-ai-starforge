# Prompts

Diretório para prompts versionados, templates de instrução e superfícies especializadas para agentes.

## Prompts disponíveis

| Prompt | O que é |
| --- | --- |
| `CLAUDE-FABLE-5.md` | Prompt de sistema para uma superfície chamada Claude Fable 5. Define informações de produto a serem usadas pelo agente, regras de segurança e recusa, diretrizes de tom e formatação, orientação para temas legais/financeiros e bem-estar do usuário, além de instruções sobre cutoff de conhecimento, memória, armazenamento persistente em artifacts e sugestões de MCP Apps. |

### Uso com Claude Code

A partir do diretório que contém `mrbits-ai-starforge/`, carregue o prompt como system prompt:

```bash
claude --dangerously-skip-permissions --system-prompt-file mrbits-ai-starforge/prompts/CLAUDE-FABLE-5.md
```

## Como adicionar um prompt

Use um arquivo Markdown para prompts simples:

```text
prompts/<nome-do-prompt>.md
```

Use um diretório quando o prompt tiver exemplos, assets ou validação:

```text
prompts/<nome-do-prompt>/
+-- README.md
+-- prompt.md
+-- examples/
```

Documente finalidade, entradas esperadas, saída esperada, limitações e exemplos.
