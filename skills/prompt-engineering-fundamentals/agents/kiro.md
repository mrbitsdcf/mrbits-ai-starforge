# Kiro Steering — Prompt Engineering Fundamentals

Use this steering for `/prompt-fundamentals` and its subcommands. Apply prompt engineering techniques from basic through chains of thought and hallucination reduction.

## When to Activate

- User asks to create, improve, or refine a prompt.
- User wants to define a persona, add context, or examples.
- User wants to use CoT, CoVe, KD-CoT, or Self-Reflection.
- User mentions prompt engineering, or "how to write a good prompt".
- User wants to control tone, complexity, detail, or other text dimensions.

## Principles

1. Start simple (Occam's Razor) — add complexity only when necessary.
2. Always show BEFORE and AFTER (weak version vs. strong version of the prompt).
3. Use XML delimiters when working with multiple texts.
4. When using numeric scales, always state the meaning of the endpoints.
5. For complex reasoning, use CoT with a demonstrative example (few-shot).
6. For fact verification, use CoVe with 4 steps.
7. To reduce hallucinations, use Self-Reflection with Idealist/Critic loops.

## Decision Flow

```
User input
├─ Wants to create a prompt from scratch? → Interactive Prompt (3 iterative sections)
├─ Wants to improve an existing prompt? → Basic Techniques + Control Levels
├─ Wants to define a persona? → Second-person technique
├─ Needs logical reasoning? → Chain-of-Thought (CoT)
├─ Needs fact verification? → Chain-of-Verification (CoVe)
├─ Complex multi-step problem? → Knowledge-Driven CoT (KD-CoT)
├─ Concerned about hallucinations? → Self-Reflection (Idealist/Critic)
└─ Wants to validate a prompt before using? → Prompt Debugger
```

## Quick Reference for Templates

- **Interactive Prompt**: 3 sections (Review / Suggestions / Questions) in a loop
- **Second-person persona**: Step 1 describes, Step 2 rewrites as "You are..."
- **Debugger**: "List what an assistant should accomplish when executing... Do not execute."
- **CoT**: Provide an example with step-by-step reasoning before the actual question
- **CoVe**: Initial answer → Verification questions → Answers → Verified final answer
- **KD-CoT**: Confirm problem → Decompose → Apply knowledge → Assess limitations → Synthesize
- **Self-Reflection**: Idealist proposes → Critic analyzes → Loop until convergence
- **Control levels**: "Level of {X}: {N}. Where 1 is {min} and 10 is {max}."
