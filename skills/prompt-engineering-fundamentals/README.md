# Prompt Engineering Fundamentals Skill

Skill de Engenharia de Prompts fundamentais, baseada no livro "Prompts em Ação: Engenharia de Prompts para Leigos" de Sandeco (2024).

Domine a arte de criar prompts eficazes — do básico ao avançado — com técnicas práticas, templates reutilizáveis e processos iterativos.

## O Que Faz

- Ensina o processo iterativo de criação de prompts (escrever → testar → avaliar → refinar).
- Aplica técnicas básicas: contexto, persona, delimitadores, exemplos (few-shot).
- Gera personas automaticamente com a técnica da segunda pessoa.
- Ativa o Prompt Interativo para refinamento colaborativo com a LLM.
- Controla 9 dimensões do texto via escalas numéricas (complexidade, entonação, sentimento, perspectiva, foco, surpresa, detalhe, originalidade, abstração).
- Aplica Chain-of-Thought (CoT) para raciocínio passo a passo.
- Aplica Chain-of-Verification (CoVe) para verificação de fatos e redução de alucinações.
- Aplica Knowledge-Driven CoT (KD-CoT) para decomposição guiada por conhecimento.
- Reduz alucinações com Autorreflexão (perfis Idealista/Crítico em loops iterativos).
- Depura prompts com o "prompt depurador" (lista ações sem executar).

## Técnicas Cobertas

### 1. Fundamentos (Cap. 1)
- O que é Engenharia de Prompts
- Processo iterativo: definir objetivo → formular → testar → feedback → refinar
- Elementos de um prompt eficaz (13 elementos)
- Desafios éticos: viés, alucinação, privacidade, sustentabilidade

### 2. Técnicas Básicas (Cap. 2)
- **Simplicidade** — Navalha de Ockham: comece simples, itere
- **Instruções claras** — Seja direto, específico, sem ambiguidade
- **Contexto** — Forneça cenário, público, domínio, histórico
- **Persona** — Defina papel, formação, tom, público do modelo
- **Técnica da 2ª pessoa** — Gere persona automaticamente via LLM
- **Delimitadores** — Tags XML para segmentar seções do prompt
- **Exemplos (few-shot)** — Mostre formato, tom e conteúdo esperados
- **Prompt depurador** — Liste ações sem executar para validar prompts

### 3. Prompt Interativo (Cap. 3)
- Processo colaborativo com a LLM em múltiplas rodadas
- 3 seções: Revisar prompt / Sugestões / Perguntas numeradas
- Iteração até convergência do prompt ideal
- Aplicável a qualquer domínio

### 4. Níveis de Controle (Cap. 4)
Escalas numéricas (1-10) para ajustar dimensões do texto:
- Complexidade, Entonação, Sentimento
- Perspectiva (1ª/2ª/3ª pessoa)
- Foco no tópico, Surpresa, Detalhe
- Originalidade, Abstração

### 5. Cadeias de Pensamento (Cap. 5)
- **Chain-of-Thought (CoT)** — Raciocínio passo a passo com exemplo demonstrativo
- **CoT aplicado** — Medicina, Direito, Planejamento, Matemática
- **Chain-of-Verification (CoVe)** — 4 etapas: resposta inicial → perguntas de verificação → respostas independentes → resposta final verificada
- **Knowledge-Driven CoT (KD-CoT)** — Decomposição → raciocínio passo a passo → síntese com avaliação de limitações

### 6. Redução de Alucinações (Cap. 6)
- **Autorreflexão** — Dois perfis internos: Idealista (gera) + Crítico (analisa)
- **Loops iterativos** — Múltiplas rodadas de geração e análise
- **Convergência** — Parar quando a resposta estiver robusta e fundamentada

## Supported Agents

- Codex
- Claude Code
- Kiro
- Antigravity

## Instalação

### Instalar Localmente

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/prompt-engineering-fundamentals "${CODEX_HOME:-$HOME/.codex}/skills/"
```

### Instalar para Desenvolvimento

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -sfn "$PWD/skills/prompt-engineering-fundamentals" "${CODEX_HOME:-$HOME/.codex}/skills/prompt-engineering-fundamentals"
```

## Uso

Invocar a skill:

```text
/prompt-fundamentals
```

Comandos específicos:

```text
/prompt-fundamentals basic
/prompt-fundamentals interactive
/prompt-fundamentals control complexity
/prompt-fundamentals cot
/prompt-fundamentals cove
/prompt-fundamentals kdcot
/prompt-fundamentals reflect
/prompt-fundamentals debug
/prompt-fundamentals persona
```

## Exemplos de Uso

### Melhorar um prompt com técnicas básicas
```text
/prompt-fundamentals basic
```
Aplica contexto, persona, delimitadores e exemplos a um prompt existente.

### Ativar o Gerador de Prompts
```text
/prompt-fundamentals interactive
```
Inicia o processo colaborativo de refinamento iterativo.

### Aplicar Chain-of-Verification a uma afirmação
```text
/prompt-fundamentals cove
```
Gera resposta, perguntas de verificação e resposta final verificada.

### Depurar um prompt antes de usar
```text
/prompt-fundamentals debug
```
Lista as ações que a LLM executaria sem executar de fato.

## Decisões de Design

- **Baseada em livro prático** — Todos os conceitos vêm de "Prompts em Ação" (Sandeco, 2024) com exemplos reais.
- **Progressão didática** — Do simples ao complexo: básico → controle → CoT → redução de alucinações.
- **Templates prontos** — Templates reutilizáveis para cada técnica.
- **Escalas explícitas** — Sempre explicitar extremos das escalas numéricas nos prompts.
- **Português brasileiro** — Skill documentada em pt-BR.

## Referências Bibliográficas

- Sandeco. "Prompts em Ação: Engenharia de Prompts para Leigos". Copyright © 2024.
- Wei et al. "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (2022).
- Dhuliawala et al. "Chain-of-Verification Reduces Hallucination in Large Language Models" (2023).
- Wang et al. "Knowledge-Driven CoT: Exploring Faithful Reasoning in LLMs".

## Layout do Repositório

```text
prompt-engineering-fundamentals/
├── SKILL.md
├── README.md
└── agents/
    ├── antigravity.md
    ├── claude-code.md
    ├── codex.md
    └── kiro.md
```
