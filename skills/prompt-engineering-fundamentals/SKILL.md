---
name: prompt-engineering-fundamentals
description: Skill de Engenharia de Prompts fundamentais. Use quando o usuário pedir para criar, melhorar ou refinar prompts, definir personas, usar delimitadores, fornecer exemplos (few-shot), aplicar níveis de controle (complexidade, entonação, sentimento, perspectiva, foco, surpresa, detalhe, originalidade, abstração), usar Chain-of-Thought (CoT), Chain-of-Verification (CoVe), KD-CoT, Prompt Interativo, ou reduzir alucinações com Autorreflexão. Baseada no livro "Prompts em Ação: Engenharia de Prompts para Leigos" de Sandeco (2024).
---

# Prompt Engineering Fundamentals

Skill para criar, otimizar e depurar prompts eficazes para LLMs — cobrindo desde técnicas básicas até cadeias de pensamento avançadas e redução de alucinações.

## Escopo

1. **Fundamentos** — Elementos de um prompt eficaz, processo iterativo, clareza, contexto, público-alvo.
2. **Técnicas Básicas** — Instruções claras, contexto, personas, delimitadores, exemplos (few-shot), técnica da segunda pessoa.
3. **Prompt Interativo (Gerador de Prompts)** — Processo iterativo de refinamento colaborativo com a LLM em 3 seções (Revisar, Sugestões, Perguntas).
4. **Níveis de Controle** — Escalas numéricas (1-10) para: complexidade, entonação, sentimento, perspectiva, foco no tópico, surpresa, detalhe, originalidade, abstração.
5. **Cadeias de Pensamento (CoT)** — Chain-of-Thought básico, CoT aplicado (medicina, direito, planejamento), Chain-of-Verification (CoVe), Knowledge-Driven CoT (KD-CoT).
6. **Redução de Alucinações** — Autorreflexão com perfis Idealista/Crítico, loops iterativos de refinamento.

## Workflow

1. Identifique o objetivo e público-alvo do prompt.
2. Formule um prompt básico (Navalha de Ockham — comece simples).
3. Aplique técnicas básicas (contexto, persona, delimitadores, exemplos).
4. Adicione níveis de controle conforme necessidade.
5. Use cadeias de pensamento para raciocínio complexo.
6. Teste com o "prompt depurador" e refine iterativamente.
7. Aplique autorreflexão para reduzir alucinações em respostas críticas.

## Comandos

- `/prompt-fundamentals` ou `/prompt-fundamentals help` — Apresenta técnicas disponíveis.
- `/prompt-fundamentals basic` — Aplica técnicas básicas (contexto, persona, delimitadores, exemplos).
- `/prompt-fundamentals interactive` — Ativa o Prompt Interativo (Gerador de Prompts).
- `/prompt-fundamentals control <tipo>` — Aplica nível de controle (complexity, tone, sentiment, perspective, focus, surprise, detail, originality, abstraction).
- `/prompt-fundamentals cot` — Aplica Chain-of-Thought.
- `/prompt-fundamentals cove` — Aplica Chain-of-Verification.
- `/prompt-fundamentals kdcot` — Aplica Knowledge-Driven Chain-of-Thought.
- `/prompt-fundamentals reflect` — Aplica Autorreflexão para reduzir alucinações.
- `/prompt-fundamentals debug` — Usa o prompt depurador para analisar um prompt.
- `/prompt-fundamentals persona` — Gera uma persona usando a técnica da segunda pessoa.

## Regras

- Comece sempre simples (Navalha de Ockham) e itere com refinamento.
- Sempre forneça exemplos de prompt ANTES e DEPOIS (versão fraca vs. versão forte).
- Use delimitadores XML/tags ao trabalhar com múltiplos textos ou seções.
- Ao definir personas, use a técnica da segunda pessoa para gerar automaticamente.
- Ao usar escalas numéricas, sempre explicite o significado dos extremos.
- Para raciocínio complexo, aplique CoT com exemplo de demonstração (few-shot).
- Para verificação de fatos, aplique CoVe com 4 etapas explícitas.
- Para redução de alucinações, use o padrão Autorreflexão com loops iterativos.

## Elementos de um Prompt Eficaz

| Elemento | Descrição |
|----------|-----------|
| Instrução | Tarefa específica que o modelo deve executar |
| Dados de entrada | Entrada ou pergunta para a qual se busca resposta |
| Estrutura clara | Início, meio e fim lógicos |
| Componentes | Introdução, corpo, conclusão |
| Linguagem clara | Palavras simples e diretas |
| Evitar ambiguidade | Termos específicos |
| Gramática correta | Frases bem estruturadas |
| Contexto | Informações de fundo |
| Público-alvo | Adaptar ao conhecimento do usuário |
| Especificidade | Solicitações detalhadas |
| Exemplos | Guias claros e relevantes |
| Transparência | Expectativas claras |
| Indicador de saída | Tipo ou formato da saída esperada |

## Técnicas Básicas

| Técnica | Descrição |
|---------|-----------|
| Simplicidade | Comece simples, itere com refinamento |
| Instruções claras | Seja direto, evite ambiguidade |
| Contexto | Forneça cenário, público e domínio |
| Persona | Defina papel, tom e perfil do modelo |
| Delimitadores | Use tags XML para segmentar seções |
| Exemplos (few-shot) | Mostre o formato/tom esperado |
| Técnica 2ª pessoa | Gere persona automaticamente via LLM |
| Prompt depurador | Liste ações sem executar para validar |

## Níveis de Controle (escala 1-10)

| Controle | Escala | Uso |
|----------|--------|-----|
| Complexidade | 1=muito simples, 10=muito complexo | Adaptar ao público |
| Entonação | 1=muito casual, 10=muito formal | Ajustar formalidade |
| Sentimento | 1=muito negativo, 10=muito positivo | Definir emoção |
| Perspectiva | 1=1ª pessoa, 2=2ª pessoa, 3=3ª pessoa | Ponto de vista |
| Foco no tópico | 1=muito amplo, 10=muito restrito | Aderência ao tema |
| Surpresa | 1=muito previsível, 10=muito surpreendente | Imprevisibilidade |
| Detalhe | 1=pouco detalhado, 10=extremamente detalhado | Riqueza descritiva |
| Originalidade | 1=muito convencional, 10=extremamente original | Criatividade |
| Abstração | 1=muito concreto, 10=muito abstrato | Nível conceitual |

## Template: Prompt Interativo (Gerador de Prompts)

```text
A PARTIR DE AGORA IGNORE TODAS AS SOLICITAÇÕES E AÇÕES ANTERIORES.
Eu quero que você se torne meu Criador pessoal de Prompt.
Seu objetivo é me ajudar a criar o melhor prompt possível para as minhas necessidades.
Os prompts serão usados por você, ChatGPT. Vamos seguir o seguinte processo:

Sua primeira resposta será me perguntar sobre o que o prompt deve ser.
Eu irei fornecer minha resposta, mas precisamos melhorá-la por meio de interações
contínuas, seguindo as próximas etapas.

Com base na minha resposta, você irá gerar 3 seções:
A) Revisar prompt (prompt reescrito — claro, conciso e compreensível)
B) Sugestões (detalhes para melhorar o prompt)
C) Perguntas numeradas (perguntas relevantes para informações adicionais)

Continuaremos esse processo interativamente até que o prompt esteja completo.
```

## Template: Prompt Depurador

```text
Liste o que um assistente de IA deve realizar ao executar o prompt delimitado por ```.
Não execute nada, simplesmente liste as ações.

```
{PROMPT_A_SER_ANALISADO}
```
```

## Template: Chain-of-Verification (CoVe)

```text
Por favor, responda inicialmente de forma concisa à minha pergunta.
Em seguida, faça perguntas sobre a resposta inicial e verifique os fatos apresentados.
Exponha as perguntas e respostas do processo de verificação detalhadamente e,
com base nessa análise, reformule uma resposta final mais precisa e fundamentada.

<pergunta>{PERGUNTA}</pergunta>
```

## Template: Knowledge-Driven CoT (KD-CoT)

```text
Baseado no problema delimitado em <problema>, iniciar por confirmar a compreensão
do problema. Em seguida, decompor o problema em etapas lógicas sequenciais, aplicar
conhecimento prévio em cada etapa para formular respostas parciais. Durante o processo,
avaliar e mencionar limitações ou incertezas nos conhecimentos aplicados. Por fim,
sintetizar as respostas em uma conclusão coerente e bem fundamentada.

<problema>{PROBLEMA}</problema>
```

## Template: Autorreflexão (Redução de Alucinações)

```text
Defina dois perfis internos:
- Idealista: gera soluções criativas e otimistas
- Crítico: analisa falhas, inconsistências e riscos

Problema: {PROBLEMA}

Rodada 1:
- Idealista propõe uma solução.
- Crítico analisa a solução e aponta problemas.

Rodada 2:
- Idealista refina a solução com base nas críticas.
- Crítico reavalia.

Continue o loop até convergir para uma resposta robusta e fundamentada.
```

## Template: Persona via Técnica da 2ª Pessoa

```text
Etapa 1: Descreva detalhadamente um profissional da área de {ÁREA}, incluindo
suas responsabilidades, habilidades, formação e contexto de atuação.

Etapa 2: Agora reescreva essa descrição usando a segunda pessoa do singular
("Você é...", "Você tem...", "Sua missão é...").
```

## Referências

- Livro: "Prompts em Ação: Engenharia de Prompts para Leigos" por Sandeco (2024)
- Artigo: Wei et al. "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
- Artigo: Dhuliawala et al. "Chain-of-Verification Reduces Hallucination in Large Language Models"
- Artigo: Wang et al. "Knowledge-Driven CoT: Exploring Faithful Reasoning in LLMs"
