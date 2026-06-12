# MrBiTs AI Starforge

Repositório público para desenvolvimento, curadoria e distribuição de artefatos para agentes de IA mantidos pelo MrBiTs.

O objetivo deste projeto é reunir componentes reutilizáveis que acelerem a criação de agentes, automações e fluxos assistidos por IA. Aqui ficam skills, prompts, MCPs, templates e materiais de suporte com documentação suficiente para uso direto, revisão pública e contribuição da comunidade.

## Sumário

- [Artefatos](#artefatos)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Como usar](#como-usar)
- [Como contribuir](#como-contribuir)
- [Padrões de qualidade](#padrões-de-qualidade)
- [Branches](#branches)
- [Distribuição](#distribuição)
- [Licença](#licença)

## Artefatos

| Artefato | Tipo | Caminho | Descrição |
| --- | --- | --- | --- |
| AWS Terraform Template | Skill | [`skills/aws-terraform-template`](skills/aws-terraform-template/) | Skill para criar um repositório Terraform AWS mínimo, opinativo e pronto para agentes como Codex, Claude Code, Kiro e Antigravity. |
| Prompt Guardrails | Skill | [`skills/prompt-guardrails`](skills/prompt-guardrails/) | Guardrails para LLMs — proteção contra injection, design patterns de prompts, debate multiagente, RaR e validação programática com Guardrails AI. Baseada no livro "Engenharia de Prompts II" (Sandeco, 2025). |
| Prompt Engineering Fundamentals | Skill | [`skills/prompt-engineering-fundamentals`](skills/prompt-engineering-fundamentals/) | Engenharia de Prompts fundamentais — técnicas básicas, prompt interativo, níveis de controle, CoT, CoVe, KD-CoT e redução de alucinações com autorreflexão. Baseada no livro "Prompts em Ação" (Sandeco, 2024). |
| Skills | Coleção | [`skills/`](skills/) | Diretório para skills reutilizáveis com instruções, scripts, assets e documentação própria. |
| Prompts | Coleção | [`prompts/`](prompts/) | Diretório para prompts versionados, templates de instrução e superfícies especializadas para agentes. |
| MCPs | Coleção | [`mcps/`](mcps/) | Diretório para servidores MCP, configurações, exemplos e documentação de integração. |

## Estrutura do repositório

```text
.
+-- .github/
|   +-- ISSUE_TEMPLATE/
|   +-- PULL_REQUEST_TEMPLATE.md
+-- docs/
|   +-- DISTRIBUTION.md
+-- mcps/
+-- prompts/
+-- skills/
|   +-- aws-terraform-template/
|   +-- prompt-engineering-fundamentals/
|   +-- prompt-guardrails/
+-- CODE_OF_CONDUCT.md
+-- CONTRIBUTING.md
+-- LICENSE
+-- README.md
+-- SECURITY.md
+-- SUPPORT.md
```

## Como usar

Clone o repositório:

```bash
git clone https://github.com/mrbitsdcf/mrbits-ai-starforge.git
cd mrbits-ai-starforge
```

Para usar uma skill localmente no Codex, copie ou faça link simbólico do diretório desejado para o diretório de skills do Codex:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -sfn "$PWD/skills/aws-terraform-template" "${CODEX_HOME:-$HOME/.codex}/skills/aws-terraform-template"
```

Reinicie o Codex após instalar ou atualizar uma skill.

Cada artefato deve ter documentação própria com instalação, uso, parâmetros, exemplos e validação. Consulte o README do artefato antes de executar scripts ou aplicar templates.

## Como contribuir

Contribuições são bem-vindas. Antes de abrir um pull request:

1. Leia [`CONTRIBUTING.md`](CONTRIBUTING.md).
2. Use uma branch curta e descritiva.
3. Documente o artefato criado ou alterado.
4. Inclua exemplos de uso e validação.
5. Preencha o template de pull request.

Novos artefatos devem ser pequenos, revisáveis e independentes. Evite adicionar dependências ou automações globais sem uma justificativa clara.

## Branches

Este repositório usa `main` como branch estável e `develop` como branch de integração.

- `main` é protegido e não aceita pushes diretos.
- Mudanças para `main` devem passar por pull request.
- `develop` recebe trabalho integrado antes de uma release.
- Branches de contribuição devem partir de `develop`, salvo correções emergenciais.

## Padrões de qualidade

Todo artefato deve:

- Explicar para que serve e quando deve ser usado.
- Declarar pré-requisitos e limitações.
- Ter exemplos reproduzíveis.
- Evitar segredos, tokens, dados privados ou identificadores de clientes.
- Preferir formatos simples, portáveis e fáceis de revisar.
- Ter validação manual ou automatizada proporcional ao risco.

## Distribuição

As instruções de publicação, versionamento e empacotamento estão em [`docs/DISTRIBUTION.md`](docs/DISTRIBUTION.md).

Resumo:

- Skills ficam em `skills/<nome-da-skill>/`.
- Prompts ficam em `prompts/<nome-do-prompt>/` ou `prompts/<nome>.md`.
- MCPs ficam em `mcps/<nome-do-mcp>/`.
- Mudanças incompatíveis devem ser documentadas em release notes.
- Releases públicas devem apontar quais artefatos foram alterados.

## Segurança

Para relatar vulnerabilidades, exposição de segredo ou comportamento perigoso, siga [`SECURITY.md`](SECURITY.md).

## Licença

Este repositório é distribuído sob a licença MIT. Consulte [`LICENSE`](LICENSE).
