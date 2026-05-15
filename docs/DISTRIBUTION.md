# Distribuição e versionamento

Este repositório distribui artefatos para agentes de IA por meio de branches, tags e releases do GitHub.

## Canais

| Canal | Uso |
| --- | --- |
| `main` | Linha principal estável para consumo direto. |
| Tags | Marcos versionados, por exemplo `v0.1.0`. |
| Releases | Notas públicas de alterações e artefatos destacados. |

## Versionamento

Use versionamento semântico para releases do repositório:

- `MAJOR`: mudanças incompatíveis em estrutura, instalação ou contrato de artefatos.
- `MINOR`: novos artefatos ou funcionalidades compatíveis.
- `PATCH`: correções, documentação e melhorias compatíveis.

Artefatos individuais podem ter versionamento próprio no README quando necessário.

## Empacotamento

### Skills

Skills devem ficar em:

```text
skills/<nome-da-skill>/
```

Estrutura mínima:

```text
SKILL.md
README.md
```

Estrutura opcional:

```text
agents/
assets/
examples/
scripts/
tests/
```

### Prompts

Prompts simples podem ser arquivos Markdown:

```text
prompts/<nome-do-prompt>.md
```

Prompts com exemplos, assets ou testes devem usar diretório próprio:

```text
prompts/<nome-do-prompt>/
```

### MCPs

MCPs devem ficar em:

```text
mcps/<nome-do-mcp>/
```

Cada MCP deve documentar instalação, execução, configuração, permissões, variáveis de ambiente e validação local.

## Checklist de release

Antes de publicar uma release:

1. Confirme que o README raiz lista os artefatos novos ou removidos.
2. Confirme que cada artefato alterado tem documentação própria.
3. Rode as validações aplicáveis.
4. Verifique que não há segredos, tokens ou arquivos locais.
5. Escreva release notes com artefatos alterados e impacto para usuários.

## Instalação por consumidores

Consumidores podem usar o repositório de três formas:

- Clonar o repositório e referenciar os artefatos localmente.
- Copiar um diretório de artefato para a ferramenta desejada.
- Instalar diretamente a partir de um caminho GitHub quando a ferramenta suportar esse formato.
