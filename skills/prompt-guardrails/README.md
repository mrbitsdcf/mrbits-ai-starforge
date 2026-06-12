# Prompt Guardrails Skill

Skill especializada em Guardrails para LLMs, baseada no livro "Engenharia de Prompts II – Guardrails" de Sandeco (2025).

Proteja sistemas de IA controlando entradas e filtrando saídas — mantendo modelos de linguagem dentro dos limites definidos.

## O Que Faz

- Gera prompts com guardrails de segurança contra prompt injection, jailbreak e manipulação.
- Aplica Prompt Design Patterns (26 padrões) para estruturar interações eficazes.
- Implementa Abstain-QA para abstenção responsável quando há incerteza.
- Configura debates multiagente com feedback humano como guardrail.
- Aplica Rephrase and Respond (RaR) para reformulação inteligente de perguntas.
- Gera código Python com a biblioteca Guardrails AI para validação programática.
- Protege contra vazamento de dados sensíveis (PII), conteúdo ofensivo e alucinações.

## Técnicas Cobertas

### 1. Guardrails Conceituais
- **Abstain-QA** — Modelo se abstém quando não tem certeza, evitando alucinações.
- **Inject Detector** — Separa análise de segurança da execução, bloqueando manipulações.
- **Registro de Preferências** — Memória contextual para personalização adaptativa.
- **Decisão e Abstenção** — Reconhecer limites do conhecimento e agir com prudência.

### 2. Prompt Design Patterns (26 padrões)
Organizados em 7 categorias:
- Concisão e Clareza (Direct, Affirmative, Penalty, Emphasize)
- Público-Alvo e Contexto (Audience, Natural, Persona)
- Orientação e Estrutura (Task Breakdown, Clarity, Format, Step-by-Step, Primer)
- Exemplos e Incentivo (Few-Shot Example, Reward, Start Cue)
- Controle de Estilo (Style Keeper, Mimic Style, Style Guidelines)
- Especificidade (Imperative, Unbiased, Teach-and-Test, CoT Combo)
- Tarefas Técnicas (Delimiters, Detailed Output, Automated Code Generation)

### 3. Debate Multiagente com Feedback Humano
- Definição de número de agentes e rodadas.
- Ciclo iterativo: Leitura → Reflexão → Atualização → Pausa para visualização.
- Feedback estruturado: manter, descartar ou adicionar ideias.
- Convergência natural + intervenção estratégica do usuário.

### 4. Rephrase and Respond (RaR)
- **Uma etapa** — Modelo reformula e responde no mesmo prompt.
- **Duas etapas** — Modelo 1 reformula, Modelo 2 responde.
- **RaR + CoT** — Combinação para máxima precisão.

### 5. Prompts de Segurança
- Filtragem de conteúdo sensível (ódio, violência, autolesão).
- Conformidade ética (anti-viés, anti-discriminação).
- Detecção de jailbreaking (cenários fictícios, fragmentação, linguagem indireta).
- Verificação de factualidade (fontes verificáveis, correção de imprecisões).
- Garantia de privacidade (bloqueio de PII, anonimização).

### 6. Biblioteca Guardrails AI (Python)
- Guards e Validadores (RegexMatch, RestrictToTopic, DetectPII, BanList, ValidChoices).
- Validação de código (ValidPython, ValidSQL, ValidJSON).
- Esquemas com RAIL (XML) ou Pydantic.
- Mecanismo automático de re-ask.
- Guardrails Hub com validadores comunitários.

## Supported Agents

- Codex
- Claude Code
- Kiro
- Antigravity

## Instalação

### Instalar Localmente

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/prompt-guardrails "${CODEX_HOME:-$HOME/.codex}/skills/"
```

### Instalar para Desenvolvimento

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -sfn "$PWD/skills/prompt-guardrails" "${CODEX_HOME:-$HOME/.codex}/skills/prompt-guardrails"
```

## Uso

Invocar a skill:

```text
/prompt-guardrails
```

Comandos específicos:

```text
/prompt-guardrails pattern Direct
/prompt-guardrails inject-detector
/prompt-guardrails abstain-qa
/prompt-guardrails security jailbreak
/prompt-guardrails multiagent
/prompt-guardrails rar
/prompt-guardrails validate pii
```

## Exemplos de Uso

### Criar um Guardrail contra Prompt Injection
```text
/prompt-guardrails inject-detector
```
Gera o template SecurityGPT/RunGPT com validação JSON estruturada.

### Aplicar Abstain-QA a uma pergunta crítica
```text
/prompt-guardrails abstain-qa
```
Gera prompt com cláusula de abstenção e escala de confiança 1-5.

### Gerar código Python com validação de PII
```text
/prompt-guardrails validate pii
```
Gera código com Guard + DetectPII configurado.

### Configurar debate multiagente
```text
/prompt-guardrails multiagent
```
Configura gerente de agentes com ciclo iterativo e feedback humano.

## Decisões de Design

- **Baseada em livro acadêmico** — Todos os conceitos vêm do livro "Engenharia de Prompts II" (Sandeco, 2025) e artigos científicos citados.
- **Dupla abordagem** — Cobre tanto guardrails via prompts (sem código) quanto via biblioteca Python (com código).
- **Templates prontos** — Fornece templates reutilizáveis para os cenários mais comuns.
- **Combinação de técnicas** — Incentiva o uso combinado (ex: RaR + CoT + Abstain-QA).
- **Português brasileiro** — Skill documentada em pt-BR para acessibilidade.

## Referências Bibliográficas

- Sandeco. "Engenharia de Prompts II – Guardrails". Copyright © 2025.
- Bai et al. "Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4". Janeiro 2024.
- Wang et al. "Rephrase and Respond: Let Large Language Models Ask Better Questions for Themselves".
- Guardrails AI Documentation: https://docs.guardrailsai.com/
- Guardrails Hub: https://hub.guardrailsai.com/

## Layout do Repositório

```text
prompt-guardrails/
├── SKILL.md
├── README.md
└── agents/
    ├── antigravity.md
    ├── claude-code.md
    ├── codex.md
    └── kiro.md
```
