# Antigravity Rules — Prompt Engineering Fundamentals

Use this rule set for `/prompt-fundamentals` and its subcommands.

## Activation Triggers

- User asks to create, improve, or refine a prompt.
- User wants to define a persona, add context, or provide examples.
- User wants to use CoT, CoVe, KD-CoT, or Self-Reflection.
- User mentions prompt engineering or "how to make a good prompt".

## Core Principles

1. Start simple (Occam's Razor) — add complexity only when needed.
2. Always show BEFORE and AFTER (weak vs. strong prompt version).
3. Use XML delimiters when working with multiple texts.
4. When using numeric scales, always state what the extremes mean.
5. For complex reasoning, use CoT with a demonstrative example (few-shot).
6. For fact verification, use CoVe with 4 explicit steps.
7. To reduce hallucinations, use Self-Reflection with Idealist/Critic loops.

## Technique Summary

### Basic Techniques
- Simplicity (Occam's Razor), Clear instructions, Context, Persona, Delimiters, Examples (few-shot), Second Person Technique, Prompt Debugger.

### Interactive Prompt (Prompt Generator)
Collaborative iterative process with LLM. 3 sections per round: Revised prompt / Suggestions / Numbered questions. Loop until convergence.

### Control Levels (9 dimensions, scale 1-10)
Complexity, Tone, Sentiment, Perspective, Topic Focus, Surprise, Detail, Originality, Abstraction. Always state extreme meanings.

### Chain-of-Thought (CoT)
Step-by-step reasoning with demonstrative example. Applicable to math, planning, medicine, law, etc.

### Chain-of-Verification (CoVe)
4 steps: Generate initial response → Plan verification questions → Answer independently → Generate verified final response.

### Knowledge-Driven CoT (KD-CoT)
Confirm understanding → Decompose into logical steps → Apply prior knowledge per step → Assess limitations → Synthesize conclusion.

### Self-Reflection (Hallucination Reduction)
Two profiles: Idealist (generates) + Critic (analyzes). Iterative loops until convergence to robust, well-founded answer.
