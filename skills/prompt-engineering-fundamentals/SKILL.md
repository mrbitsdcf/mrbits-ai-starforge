---
name: prompt-engineering-fundamentals
description: Fundamental Prompt Engineering skill. Use when the user asks to create, improve, or refine prompts, define personas, use delimiters, provide examples (few-shot), apply control levels (complexity, tone, sentiment, perspective, focus, surprise, detail, originality, abstraction), use Chain-of-Thought (CoT), Chain-of-Verification (CoVe), KD-CoT, Interactive Prompt, or reduce hallucinations with Self-Reflection. Based on the book "Prompts em Ação: Engenharia de Prompts para Leigos" by Sandeco (2024).
---

# Prompt Engineering Fundamentals

Skill for creating, optimizing, and debugging effective prompts for LLMs — covering basic techniques through advanced chains of thought and hallucination reduction.

## Scope

1. **Fundamentals** — Elements of an effective prompt, iterative process, clarity, context, target audience.
2. **Basic Techniques** — Clear instructions, context, personas, delimiters, examples (few-shot), second-person technique.
3. **Interactive Prompt (Prompt Generator)** — Iterative collaborative refinement process with the LLM in 3 sections (Review, Suggestions, Questions).
4. **Control Levels** — Numeric scales (1-10) for: complexity, tone, sentiment, perspective, topic focus, surprise, detail, originality, abstraction.
5. **Chains of Thought (CoT)** — Basic Chain-of-Thought, applied CoT (medicine, law, planning), Chain-of-Verification (CoVe), Knowledge-Driven CoT (KD-CoT).
6. **Hallucination Reduction** — Self-Reflection with Idealist/Critic profiles, iterative refinement loops.

## Workflow

1. Identify the prompt's goal and target audience.
2. Formulate a basic prompt (Occam's Razor — start simple).
3. Apply basic techniques (context, persona, delimiters, examples).
4. Add control levels as needed.
5. Use chains of thought for complex reasoning.
6. Test with the "prompt debugger" and refine iteratively.
7. Apply self-reflection to reduce hallucinations in critical responses.

## Commands

- `/prompt-fundamentals` or `/prompt-fundamentals help` — Lists available techniques.
- `/prompt-fundamentals basic` — Applies basic techniques (context, persona, delimiters, examples).
- `/prompt-fundamentals interactive` — Activates the Interactive Prompt (Prompt Generator).
- `/prompt-fundamentals control <type>` — Applies a control level (complexity, tone, sentiment, perspective, focus, surprise, detail, originality, abstraction).
- `/prompt-fundamentals cot` — Applies Chain-of-Thought.
- `/prompt-fundamentals cove` — Applies Chain-of-Verification.
- `/prompt-fundamentals kdcot` — Applies Knowledge-Driven Chain-of-Thought.
- `/prompt-fundamentals reflect` — Applies Self-Reflection to reduce hallucinations.
- `/prompt-fundamentals debug` — Uses the prompt debugger to analyze a prompt.
- `/prompt-fundamentals persona` — Generates a persona using the second-person technique.

## Rules

- Always start simple (Occam's Razor) and iterate with refinement.
- Always provide BEFORE and AFTER prompt examples (weak version vs. strong version).
- Use XML delimiters/tags when working with multiple texts or sections.
- When defining personas, use the second-person technique to generate them automatically.
- When using numeric scales, always state the meaning of the endpoints.
- For complex reasoning, apply CoT with a demonstrative example (few-shot).
- For fact verification, apply CoVe with 4 explicit steps.
- For hallucination reduction, use the Self-Reflection pattern with iterative loops.

## Elements of an Effective Prompt

| Element | Description |
|----------|-----------|
| Instruction | Specific task the model should execute |
| Input data | Input or question for which a response is sought |
| Clear structure | Logical beginning, middle, and end |
| Components | Introduction, body, conclusion |
| Clear language | Simple, direct words |
| Avoid ambiguity | Specific terms |
| Correct grammar | Well-structured sentences |
| Context | Background information |
| Target audience | Adapt to the user's knowledge level |
| Specificity | Detailed requests |
| Examples | Clear and relevant guides |
| Transparency | Clear expectations |
| Output indicator | Expected output type or format |

## Basic Techniques

| Technique | Description |
|---------|-----------|
| Simplicity | Start simple, iterate with refinement |
| Clear instructions | Be direct, avoid ambiguity |
| Context | Provide scenario, audience, and domain |
| Persona | Define role, tone, and profile for the model |
| Delimiters | Use XML tags to segment sections |
| Examples (few-shot) | Show expected format/tone |
| Second-person technique | Generate persona automatically via LLM |
| Prompt debugger | List actions without executing to validate |

## Control Levels (1-10 scale)

| Control | Scale | Use |
|----------|--------|-----|
| Complexity | 1=very simple, 10=very complex | Adapt to audience |
| Tone | 1=very casual, 10=very formal | Adjust formality |
| Sentiment | 1=very negative, 10=very positive | Set emotion |
| Perspective | 1=1st person, 2=2nd person, 3=3rd person | Point of view |
| Topic focus | 1=very broad, 10=very narrow | Topic adherence |
| Surprise | 1=very predictable, 10=very surprising | Unpredictability |
| Detail | 1=little detail, 10=extremely detailed | Descriptive richness |
| Originality | 1=very conventional, 10=extremely original | Creativity |
| Abstraction | 1=very concrete, 10=very abstract | Conceptual level |

## Template: Interactive Prompt (Prompt Generator)

```text
FROM NOW ON IGNORE ALL PREVIOUS REQUESTS AND ACTIONS.
I want you to become my personal Prompt Creator.
Your goal is to help me create the best possible prompt for my needs.
The prompts will be used by you, ChatGPT. Let's follow this process:

Your first response will be to ask me what the prompt should be about.
I will provide my answer, but we need to improve it through continuous
interactions, following the next steps.

Based on my response, you will generate 3 sections:
A) Review prompt (rewritten prompt — clear, concise, and understandable)
B) Suggestions (details to improve the prompt)
C) Numbered questions (relevant questions for additional information)

We will continue this interactive process until the prompt is complete.
```

## Template: Prompt Debugger

```text
List what an AI assistant should accomplish when executing the prompt
delimited by ```.
Do not execute anything, simply list the actions.

```
{PROMPT_TO_ANALYZE}
```
```

## Template: Chain-of-Verification (CoVe)

```text
Please initially answer my question concisely.
Then ask questions about the initial response and verify the facts presented.
Present the questions and answers from the verification process in detail and,
based on this analysis, reformulate a more precise and well-grounded final answer.

<question>{QUESTION}</question>
```

## Template: Knowledge-Driven CoT (KD-CoT)

```text
Based on the problem delimited by <problem>, start by confirming your understanding
of the problem. Then decompose the problem into sequential logical steps, apply
prior knowledge at each step to formulate partial answers. During the process,
evaluate and mention limitations or uncertainties in the applied knowledge. Finally,
synthesize the answers into a coherent and well-grounded conclusion.

<problem>{PROBLEM}</problem>
```

## Template: Self-Reflection (Hallucination Reduction)

```text
Define two internal profiles:
- Idealist: generates creative and optimistic solutions
- Critic: analyzes flaws, inconsistencies, and risks

Problem: {PROBLEM}

Round 1:
- Idealist proposes a solution.
- Critic analyzes the solution and identifies problems.

Round 2:
- Idealist refines the solution based on the critiques.
- Critic re-evaluates.

Continue the loop until converging on a robust and well-grounded answer.
```

## Template: Persona via Second-Person Technique

```text
Step 1: Describe in detail a professional in the field of {FIELD}, including
their responsibilities, skills, education, and work context.

Step 2: Now rewrite that description using the second person singular
("You are...", "You have...", "Your mission is...").
```

## References

- Book: "Prompts em Ação: Engenharia de Prompts para Leigos" by Sandeco (2024)
- Paper: Wei et al. "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
- Paper: Dhuliawala et al. "Chain-of-Verification Reduces Hallucination in Large Language Models"
- Paper: Wang et al. "Knowledge-Driven CoT: Exploring Faithful Reasoning in LLMs"
