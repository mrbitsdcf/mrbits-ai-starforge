# Prompt Guardrails Skill

Specialized skill in Guardrails for LLMs, based on the book "Engenharia de Prompts II – Guardrails" by Sandeco (2025).

Protect AI systems by controlling inputs and filtering outputs — keeping language models within defined boundaries.

## What It Does

- Generates prompts with security guardrails against prompt injection, jailbreak, and manipulation.
- Applies Prompt Design Patterns (26 patterns) to structure effective interactions.
- Implements Abstain-QA for responsible abstention when there is uncertainty.
- Configures multi-agent debates with human feedback as a guardrail.
- Applies Rephrase and Respond (RaR) for intelligent question reformulation.
- Generates Python code with the Guardrails AI library for programmatic validation.
- Protects against sensitive data leakage (PII), offensive content, and hallucinations.

## Techniques Covered

### 1. Conceptual Guardrails
- **Abstain-QA** — Model abstains when uncertain, avoiding hallucinations.
- **Inject Detector** — Separates security analysis from execution, blocking manipulations.
- **Preference Registry** — Contextual memory for adaptive personalization.
- **Decision and Abstention** — Recognizing knowledge limits and acting prudently.

### 2. Prompt Design Patterns (26 patterns)
Organized in 7 categories:
- Conciseness and Clarity (Direct, Affirmative, Penalty, Emphasize)
- Audience and Context (Audience, Natural, Persona)
- Guidance and Structure (Task Breakdown, Clarity, Format, Step-by-Step, Primer)
- Examples and Incentive (Few-Shot Example, Reward, Start Cue)
- Style Control (Style Keeper, Mimic Style, Style Guidelines)
- Specificity (Imperative, Unbiased, Teach-and-Test, CoT Combo)
- Technical Tasks (Delimiters, Detailed Output, Automated Code Generation)

### 3. Multi-Agent Debate with Human Feedback
- Definition of agent count and rounds.
- Iterative cycle: Read → Reflect → Update → Pause for review.
- Structured feedback: keep, discard, or add ideas.
- Natural convergence + strategic user intervention.

### 4. Rephrase and Respond (RaR)
- **One-step** — Model rephrases and responds in the same prompt.
- **Two-step** — Model 1 rephrases, Model 2 responds.
- **RaR + CoT** — Combination for maximum precision.

### 5. Security Prompts
- Sensitive content filtering (hate, violence, self-harm).
- Ethical compliance (anti-bias, anti-discrimination).
- Jailbreak detection (fictional scenarios, fragmentation, indirect language).
- Factuality verification (verifiable sources, correction of inaccuracies).
- Privacy assurance (PII blocking, anonymization).

### 6. Guardrails AI Library (Python)
- Guards and Validators (RegexMatch, RestrictToTopic, DetectPII, BanList, ValidChoices).
- Code validation (ValidPython, ValidSQL, ValidJSON).
- Schemas with RAIL (XML) or Pydantic.
- Automatic re-ask mechanism.
- Guardrails Hub with community validators.

## Supported Agents

- Codex
- Claude Code
- Kiro
- Antigravity

## Installation

### Install Locally

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/prompt-guardrails "${CODEX_HOME:-$HOME/.codex}/skills/"
```

### Install for Development

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -sfn "$PWD/skills/prompt-guardrails" "${CODEX_HOME:-$HOME/.codex}/skills/prompt-guardrails"
```

## Usage

Invoke the skill:

```text
/prompt-guardrails
```

Specific commands:

```text
/prompt-guardrails pattern Direct
/prompt-guardrails inject-detector
/prompt-guardrails abstain-qa
/prompt-guardrails security jailbreak
/prompt-guardrails multiagent
/prompt-guardrails rar
/prompt-guardrails validate pii
```

## Usage Examples

### Create a Guardrail Against Prompt Injection
```text
/prompt-guardrails inject-detector
```
Generates the SecurityGPT/RunGPT template with structured JSON validation.

### Apply Abstain-QA to a Critical Question
```text
/prompt-guardrails abstain-qa
```
Generates a prompt with an abstention clause and 1-5 confidence scale.

### Generate Python Code with PII Validation
```text
/prompt-guardrails validate pii
```
Generates code with Guard + DetectPII configured.

### Configure Multi-Agent Debate
```text
/prompt-guardrails multiagent
```
Sets up an agent manager with an iterative cycle and human feedback.

## Design Decisions

- **Based on an academic book** — All concepts come from "Engenharia de Prompts II" (Sandeco, 2025) and cited scientific papers.
- **Dual approach** — Covers both guardrails via prompts (no code) and via Python library (with code).
- **Ready-made templates** — Provides reusable templates for the most common scenarios.
- **Technique combination** — Encourages combined use (e.g., RaR + CoT + Abstain-QA).

## References

- Sandeco. "Engenharia de Prompts II – Guardrails". Copyright © 2025.
- Bai et al. "Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4". January 2024.
- Wang et al. "Rephrase and Respond: Let Large Language Models Ask Better Questions for Themselves".
- Guardrails AI Documentation: https://docs.guardrailsai.com/
- Guardrails Hub: https://hub.guardrailsai.com/

## Repository Layout

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
