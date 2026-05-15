# Política de branches

Este repositório usa um fluxo simples com duas branches permanentes:

| Branch | Uso | Política |
| --- | --- | --- |
| `main` | Linha estável e base de releases públicas. | Protegida; não aceita pushes diretos. Mudanças entram por pull request. |
| `develop` | Integração de mudanças antes de release. | Aceita branches de feature, correção e documentação. |

## Regras para `main`

- Push direto para `main` não é permitido.
- Force push não é permitido.
- Exclusão da branch não é permitida.
- Alterações devem passar por pull request.
- A proteção deve se aplicar também a administradores quando suportado pelo GitHub.

## Fluxo recomendado

1. Crie uma branch a partir de `develop`.
2. Faça commits pequenos e documentados.
3. Abra pull request para `develop`.
4. Promova `develop` para `main` por pull request de release.

## Nomes de branch

Use nomes curtos em `kebab-case`:

```text
feature/nova-skill
fix/template-terraform
docs/branch-policy
security/mcp-permissions
```
