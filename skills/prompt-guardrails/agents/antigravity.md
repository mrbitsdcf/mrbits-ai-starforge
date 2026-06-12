# Antigravity Rules — Prompt Guardrails

Use this rule set for `/prompt-guardrails` and its subcommands. Apply security guardrails, prompt design patterns, and programmatic validation for LLMs.

## Activation Triggers

- User asks to create secure prompts or protect against injection/jailbreak.
- User wants to validate AI outputs (format, content, ethics, privacy).
- User mentions guardrails, prompt security, or Guardrails AI.
- User wants to apply design patterns to existing prompts.
- User wants to implement multi-agent debate or RaR.

## Core Principles

1. Security first — never generate content that bypasses guardrails.
2. Always provide test examples (positive and negative) when creating guardrails.
3. Document limitations of each recommended approach.
4. Combine techniques when the scenario requires (RaR + CoT, Abstain-QA + Inject Detector).
5. For programmatic validation, use the Guardrails AI library with Python.

## Decision Flow

```
User input
├─ Needs injection protection? → Inject Detector (SecurityGPT/RunGPT)
├─ Model might hallucinate? → Abstain-QA with confidence level
├─ Vague or ambiguous question? → Rephrase and Respond (RaR)
├─ Needs format/content validation? → Guardrails AI (Python)
├─ Debate between perspectives? → Multi-agent with human feedback
├─ Wants to improve existing prompt? → Prompt Design Patterns
└─ Needs ethical safety? → Security prompts (5 types)
```

## Technique Summary

### Inject Detector
Separates security analysis from execution using `<segurança>` + `<executor>` tags. Returns JSON with {safe, reason, log}. If safe=false, block execution.

### Abstain-QA
Forces model to abstain when uncertain. Three variants:
- Standard clause: adds "I don't know" option
- Abstention clause: adds incentive to avoid uncertain answers
- Extreme clause: intensifies pressure to abstain in ambiguous scenarios

### Rephrase and Respond (RaR)
- 1-step: Model rephrases and responds in same prompt
- 2-step: Model 1 rephrases, Model 2 responds
- Combinable with Chain-of-Thought for maximum precision

### Prompt Design Patterns (26 patterns, 7 categories)
Conciseness, Audience, Structure, Examples, Style, Specificity, Technical Tasks.

### Security Prompts (5 types)
Content filtering, Ethics compliance, Jailbreak detection, Factuality verification, Privacy guarantee.

### Guardrails AI Library (Python)
Guards + Validators pattern. Key validators: RegexMatch, RestrictToTopic, DetectPII, BanList, ValidChoices, ValidPython, ValidSQL. Supports RAIL (XML) and Pydantic schemas.
