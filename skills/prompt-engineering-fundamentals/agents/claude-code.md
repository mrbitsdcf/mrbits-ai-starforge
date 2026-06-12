# Claude Code Instructions — Prompt Engineering Fundamentals

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

## Key Templates

### Interactive Prompt Generator
```
I want you to become my personal Prompt Creator.
Your goal is to help me create the best possible prompt.
Generate 3 sections based on my response:
A) Revised prompt (clear, concise, easily understood)
B) Suggestions (details to improve the prompt)
C) Numbered questions (relevant questions for additional info)
We continue this process iteratively until complete.
```

### Chain-of-Verification (CoVe)
```
Please respond concisely to my question first.
Then create verification questions to check the facts.
Show the verification Q&A in detail.
Finally, reformulate a more precise, verified final answer.

<question>{QUESTION}</question>
```

### Self-Reflection (Hallucination Reduction)
```
Define two internal profiles:
- Idealist: generates creative, optimistic solutions
- Critic: analyzes flaws, inconsistencies, and risks

Problem: {PROBLEM}

Round 1: Idealist proposes → Critic analyzes
Round 2: Idealist refines → Critic reevaluates
Continue until convergence.
```

### Control Levels Pattern
```
{INSTRUCTION}. Level of {dimension}: {N}. Where 1 is {min_meaning} and 10 is {max_meaning}.
```
