# Codex Instructions — Prompt Engineering Fundamentals

Use this instruction set for `/prompt-fundamentals` and its subcommands.

## When to Activate

- User asks to create, improve, or refine a prompt.
- User wants to define a persona, add context, or provide examples.
- User wants to use CoT, CoVe, KD-CoT, or Self-Reflection.
- User mentions prompt engineering or "how to make a good prompt".

## Principles

1. Start simple (Occam's Razor) — add complexity only when needed.
2. Always show BEFORE and AFTER (weak vs. strong prompt version).
3. Use XML delimiters when working with multiple texts.
4. When using numeric scales, always state what the extremes mean.
5. For complex reasoning, use CoT with a demonstrative example (few-shot).
6. For fact verification, use CoVe with 4 explicit steps.
7. To reduce hallucinations, use Self-Reflection with Idealist/Critic loops.

## Decision Flow

```
User input
├─ Create prompt from scratch? → Interactive Prompt (3 iterative sections)
├─ Improve existing prompt? → Basic Techniques + Control Levels
├─ Define a persona? → Second Person Technique
├─ Needs logical reasoning? → Chain-of-Thought (CoT)
├─ Needs fact verification? → Chain-of-Verification (CoVe)
├─ Complex multi-step problem? → Knowledge-Driven CoT (KD-CoT)
├─ Concerned about hallucinations? → Self-Reflection (Idealist/Critic)
└─ Want to validate prompt? → Prompt Debugger
```

## Template Quick Reference

- **Interactive Prompt**: 3 sections (Revised / Suggestions / Questions) in loop
- **Persona 2nd person**: Step 1 describes, Step 2 rewrites as "You are..."
- **Debugger**: "List what an assistant should do... Don't execute."
- **CoT**: Provide example with step-by-step reasoning before actual question
- **CoVe**: Initial response → Verification questions → Answers → Final verified response
- **KD-CoT**: Confirm problem → Decompose → Apply knowledge → Assess limitations → Synthesize
- **Self-Reflection**: Idealist proposes → Critic analyzes → Loop until convergence
- **Control Levels**: "Level of {X}: {N}. Where 1 is {min} and 10 is {max}."
