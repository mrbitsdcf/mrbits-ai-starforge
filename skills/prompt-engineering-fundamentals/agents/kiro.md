# Kiro Steering — Prompt Engineering Fundamentals

Use este steering para `/prompt-fundamentals` e seus subcomandos. Aplique técnicas de engenharia de prompts desde o básico até cadeias de pensamento e redução de alucinações.

## Quando Ativar

- Usuário pede para criar, melhorar ou refinar um prompt.
- Usuário quer definir persona, adicionar contexto ou exemplos.
- Usuário quer usar CoT, CoVe, KD-CoT ou Autorreflexão.
- Usuário menciona engenharia de prompts, prompt engineering, ou "como fazer um bom prompt".
- Usuário quer controlar tom, complexidade, detalhe ou outras dimensões do texto.

## Princípios

1. Comece simples (Navalha de Ockham) — adicione complexidade apenas quando necessário.
2. Sempre mostre ANTES e DEPOIS (versão fraca vs. versão forte do prompt).
3. Use delimitadores XML ao trabalhar com múltiplos textos.
4. Ao usar escalas numéricas, explicite sempre o significado dos extremos.
5. Para raciocínio complexo, use CoT com exemplo demonstrativo (few-shot).
6. Para verificação de fatos, use CoVe com 4 etapas.
7. Para reduzir alucinações, use Autorreflexão com loops Idealista/Crítico.

## Fluxo de Decisão

```
Entrada do usuário
├─ Quer criar prompt do zero? → Prompt Interativo (3 seções iterativas)
├─ Quer melhorar prompt existente? → Técnicas Básicas + Níveis de Controle
├─ Quer definir persona? → Técnica da 2ª pessoa
├─ Precisa de raciocínio lógico? → Chain-of-Thought (CoT)
├─ Precisa verificar fatos? → Chain-of-Verification (CoVe)
├─ Problema complexo multi-etapa? → Knowledge-Driven CoT (KD-CoT)
├─ Preocupado com alucinações? → Autorreflexão (Idealista/Crítico)
└─ Quer validar prompt antes de usar? → Prompt Depurador
```

## Referência Rápida de Templates

- **Prompt Interativo**: 3 seções (Revisar / Sugestões / Perguntas) em loop
- **Persona 2ª pessoa**: Etapa 1 descreve, Etapa 2 reescreve em "Você é..."
- **Depurador**: "Liste o que um assistente deve realizar ao executar... Não execute."
- **CoT**: Forneça exemplo com raciocínio passo a passo antes da pergunta real
- **CoVe**: Resposta inicial → Perguntas de verificação → Respostas → Resposta final
- **KD-CoT**: Confirmar problema → Decompor → Aplicar conhecimento → Avaliar limitações → Sintetizar
- **Autorreflexão**: Idealista propõe → Crítico analisa → Loop até convergir
- **Níveis de controle**: "Nível de {X}: {N}. Onde 1 é {min} e 10 é {max}."
