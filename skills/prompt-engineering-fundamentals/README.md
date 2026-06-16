# Prompt Engineering Fundamentals Skill

Fundamental prompt engineering skill, based on the book "Prompts em Ação: Engenharia de Prompts para Leigos" by Sandeco (2024).

Master the art of creating effective prompts — from basic to advanced — with practical techniques, reusable templates, and iterative processes.

## What It Does

- Teaches the iterative prompt creation process (write → test → evaluate → refine).
- Applies basic techniques: context, persona, delimiters, examples (few-shot).
- Automatically generates personas using the second-person technique.
- Activates the Interactive Prompt for collaborative refinement with the LLM.
- Controls 9 text dimensions via numeric scales (complexity, tone, sentiment, perspective, focus, surprise, detail, originality, abstraction).
- Applies Chain-of-Thought (CoT) for step-by-step reasoning.
- Applies Chain-of-Verification (CoVe) for fact-checking and hallucination reduction.
- Applies Knowledge-Driven CoT (KD-CoT) for knowledge-guided decomposition.
- Reduces hallucinations with Self-Reflection (Idealist/Critic profiles in iterative loops).
- Debugs prompts with the "prompt debugger" (lists actions without executing).

## Techniques Covered

### 1. Fundamentals (Ch. 1)
- What is Prompt Engineering
- Iterative process: define goal → formulate → test → feedback → refine
- Elements of an effective prompt (13 elements)
- Ethical challenges: bias, hallucination, privacy, sustainability

### 2. Basic Techniques (Ch. 2)
- **Simplicity** — Occam's Razor: start simple, iterate
- **Clear instructions** — Be direct, specific, unambiguous
- **Context** — Provide scenario, audience, domain, history
- **Persona** — Define role, background, tone, audience for the model
- **Second-person technique** — Automatically generate persona via LLM
- **Delimiters** — XML tags to segment prompt sections
- **Examples (few-shot)** — Show expected format, tone, and content
- **Prompt debugger** — List actions without executing to validate prompts

### 3. Interactive Prompt (Ch. 3)
- Collaborative process with the LLM over multiple rounds
- 3 sections: Review prompt / Suggestions / Numbered questions
- Iteration until the ideal prompt converges
- Applicable to any domain

### 4. Control Levels (Ch. 4)
Numeric scales (1-10) to adjust text dimensions:
- Complexity, Tone, Sentiment
- Perspective (1st/2nd/3rd person)
- Topic focus, Surprise, Detail
- Originality, Abstraction

### 5. Chains of Thought (Ch. 5)
- **Chain-of-Thought (CoT)** — Step-by-step reasoning with a demonstrative example
- **Applied CoT** — Medicine, Law, Planning, Mathematics
- **Chain-of-Verification (CoVe)** — 4 steps: initial answer → verification questions → independent answers → verified final answer
- **Knowledge-Driven CoT (KD-CoT)** — Decomposition → step-by-step reasoning → synthesis with limitation assessment

### 6. Hallucination Reduction (Ch. 6)
- **Self-Reflection** — Two internal profiles: Idealist (generates) + Critic (analyzes)
- **Iterative loops** — Multiple rounds of generation and analysis
- **Convergence** — Stop when the answer is robust and well-grounded

## Supported Agents

- Codex
- Claude Code
- Kiro
- Antigravity

## Installation

### Install Locally

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/prompt-engineering-fundamentals "${CODEX_HOME:-$HOME/.codex}/skills/"
```

### Install for Development

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -sfn "$PWD/skills/prompt-engineering-fundamentals" "${CODEX_HOME:-$HOME/.codex}/skills/prompt-engineering-fundamentals"
```

## Usage

Invoke the skill:

```text
/prompt-fundamentals
```

Specific commands:

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

## Usage Examples

### Improve a prompt with basic techniques
```text
/prompt-fundamentals basic
```
Applies context, persona, delimiters, and examples to an existing prompt.

### Activate the Prompt Generator
```text
/prompt-fundamentals interactive
```
Starts the collaborative iterative refinement process.

### Apply Chain-of-Verification to a claim
```text
/prompt-fundamentals cove
```
Generates an answer, verification questions, and a verified final answer.

### Debug a prompt before using it
```text
/prompt-fundamentals debug
```
Lists the actions the LLM would take without actually executing them.

## Design Decisions

- **Based on a practical book** — All concepts come from "Prompts em Ação" (Sandeco, 2024) with real examples.
- **Didactic progression** — From simple to complex: basic → control → CoT → hallucination reduction.
- **Ready-made templates** — Reusable templates for each technique.
- **Explicit scales** — Always state the meaning of scale endpoints in prompts.

## References

- Sandeco. "Prompts em Ação: Engenharia de Prompts para Leigos". Copyright © 2024.
- Wei et al. "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (2022).
- Dhuliawala et al. "Chain-of-Verification Reduces Hallucination in Large Language Models" (2023).
- Wang et al. "Knowledge-Driven CoT: Exploring Faithful Reasoning in LLMs".

## Repository Layout

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
