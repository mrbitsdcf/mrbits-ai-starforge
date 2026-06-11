# Kiro Steering — Prompt Guardrails

Use este steering para `/prompt-guardrails` e seus subcomandos. Aplique guardrails de segurança, design patterns de prompts, e validação programática para LLMs.

## Quando Ativar

- Usuário pede para criar prompts seguros ou proteger contra injection/jailbreak.
- Usuário quer validar saídas de IA (formato, conteúdo, ética, privacidade).
- Usuário menciona guardrails, segurança de prompts, ou Guardrails AI.
- Usuário quer aplicar design patterns a prompts existentes.
- Usuário quer implementar debate multiagente ou RaR.

## Princípios

1. Segurança primeiro — nunca gere conteúdo que contorne guardrails.
2. Sempre forneça exemplos de teste (positivo e negativo) ao criar guardrails.
3. Documente limitações de cada abordagem recomendada.
4. Combine técnicas quando o cenário exigir (RaR + CoT, Abstain-QA + Inject Detector).
5. Para validação programática, use a biblioteca Guardrails AI com Python.

## Fluxo de Decisão

```
Entrada do usuário
├─ Precisa proteger contra injection? → Inject Detector (SecurityGPT/RunGPT)
├─ Modelo pode alucinar? → Abstain-QA com nível de confiança
├─ Pergunta vaga ou ambígua? → Rephrase and Respond (RaR)
├─ Precisa validar formato/conteúdo? → Guardrails AI (Python)
├─ Debate entre perspectivas? → Multiagente com feedback humano
├─ Quer melhorar prompt existente? → Prompt Design Patterns
└─ Precisa de segurança ética? → Prompts de segurança (5 tipos)
```

## Referência Rápida

- Inject Detector: separa `<segurança>` + `<executor>`, retorna JSON {safe, reason, log}
- Abstain-QA: "Se não tiver certeza, responda 'Não tenho certeza'. Avalie confiança 1-5."
- RaR 1-etapa: "Reescreva a pergunta de forma mais clara. Em seguida, responda."
- RaR 2-etapas: Etapa 1 reformula, Etapa 2 responde baseado na reformulação.
- Design Patterns: 26 padrões em 7 categorias (ver SKILL.md para catálogo completo).
- Guardrails AI: `Guard().use(Validador, params, on_fail="exception")`
