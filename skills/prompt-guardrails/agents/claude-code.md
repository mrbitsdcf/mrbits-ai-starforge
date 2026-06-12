# Claude Code Instructions — Prompt Guardrails

Use this instruction set for `/prompt-guardrails` and its subcommands. Apply security guardrails, prompt design patterns, and programmatic validation for LLMs.

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

## Quick Reference

- Inject Detector: separates `<segurança>` + `<executor>`, returns JSON {safe, reason, log}
- Abstain-QA: "If unsure, respond 'I'm not sure'. Rate confidence 1-5."
- RaR 1-step: "Rephrase the question more clearly. Then respond."
- RaR 2-step: Step 1 rephrases, Step 2 responds based on the rephrasing.
- Design Patterns: 26 patterns in 7 categories (see SKILL.md for full catalog).
- Guardrails AI: `Guard().use(Validator, params, on_fail="exception")`

## Key Guardrails AI Code Pattern

```python
from guardrails import Guard
from guardrails.hub import DetectPII, BanList, RestrictToTopic, RegexMatch

# Composable guard with multiple validators
guard = Guard().use(
    DetectPII, ["EMAIL_ADDRESS", "PHONE_NUMBER"], on_fail="exception"
).use(
    BanList(["forbidden_word"]), on_fail="exception"
).use(
    RestrictToTopic(
        valid_topics=["allowed_topic"],
        invalid_topics=["blocked_topic"],
        disable_classifier=True,
        disable_llm=False,
        on_fail="exception"
    )
)

# Validate output
try:
    guard.validate("Text to validate")
except Exception as e:
    print(f"Validation failed: {e}")
```

## Multi-Agent Debate Template

```
You are an intelligent agent manager coordinating problem resolution.
The user must provide:
• Number of intelligent agents to use.
• Number of debate rounds.

Pause and ask the user to describe the problem.

DEBATE MECHANISM:
Each round follows four structured steps:
• Reading: Agents analyze solutions from other participants.
• Reflection: Each agent reviews its own response considering others' insights.
• Update: Agents refine solutions and record new versions.
• Pause for Review: User reviews responses before next round.

USER FEEDBACK:
At end of each round, user provides structured feedback:
• Which ideas should remain?
• Which ideas should be discarded?
• Want to add a new idea? (Creates new agent if yes)
```
