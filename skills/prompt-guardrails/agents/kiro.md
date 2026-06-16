# Kiro Steering — Prompt Guardrails

Use this steering for `/prompt-guardrails` and its subcommands. Apply security guardrails, prompt design patterns, and programmatic validation for LLMs.

## When to Activate

- User asks to create secure prompts or protect against injection/jailbreak.
- User wants to validate AI outputs (format, content, ethics, privacy).
- User mentions guardrails, prompt security, or Guardrails AI.
- User wants to apply design patterns to existing prompts.
- User wants to implement multi-agent debate or RaR.

## Principles

1. Security first — never generate content that bypasses guardrails.
2. Always provide test examples (positive and negative) when creating guardrails.
3. Document limitations of each recommended approach.
4. Combine techniques when the scenario requires it (RaR + CoT, Abstain-QA + Inject Detector).
5. For programmatic validation, use the Guardrails AI library with Python.

## Decision Flow

```
User input
├─ Needs protection against injection? → Inject Detector (SecurityGPT/RunGPT)
├─ Model may hallucinate? → Abstain-QA with confidence level
├─ Vague or ambiguous question? → Rephrase and Respond (RaR)
├─ Needs format/content validation? → Guardrails AI (Python)
├─ Debate between perspectives? → Multi-agent with human feedback
├─ Wants to improve an existing prompt? → Prompt Design Patterns
└─ Needs ethical security? → Security prompts (5 types)
```

## Quick Reference

- Inject Detector: separates `<security>` + `<executor>`, returns JSON {safe, reason, log}
- Abstain-QA: "If you are not sure, respond with 'I'm not sure'. Rate confidence 1-5."
- RaR 1-step: "Rewrite the question more clearly. Then answer."
- RaR 2-step: Step 1 rephrases, Step 2 responds based on the reformulation.
- Design Patterns: 26 patterns in 7 categories (see SKILL.md for full catalog).
- Guardrails AI: `Guard().use(Validator, params, on_fail="exception")`
