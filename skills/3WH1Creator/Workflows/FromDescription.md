# Workflow: FromDescription

Constrói um prompt 3W1H a partir de uma ideia/descrição abstrata do usuário, via pipeline de perguntas human-in-the-loop.

**Entregável:** três blocos plaintext (prompt pt-br, prompt en, alt text). **Nunca gere a imagem.**

## Parte 1 — Tema

Se o usuário ainda não deu o tema, pergunte apenas:

> "Qual é o tema do prompt que você gostaria? Pode descrever com as suas palavras. Depois eu te ajudo com algumas sugestões para refinar a ideia."

Sem perguntas antes do tema (guardrail R8/R9).

## Parte 2 — Perguntas dos 4 pilares (uma por vez)

Faça as perguntas na ordem **Who → What → Where → How**, **uma por mensagem**, cada uma só depois da resposta anterior.

**Verbose = FALSE (rule 6):** abra DIRETO com a pergunta. Sem frase de enquadramento antes ("Vamos construir...", "Ótimo!", "Para começar..."). A primeira coisa na mensagem é a linha `Pergunta:`. Formato de cada pergunta:

```
Pergunta: <texto>

  * Sugestão 1: ...
  * Sugestão 2: ...
  * Sugestão 3: ...
```

Perguntas canônicas:

1. **Who** — "Quem protagonizará sua imagem?" (pessoa, animal, objeto, planta, casa... Dica: detalhe características físicas e, no caso de pessoas, o que veste.)
2. **What** — "Que ação esse personagem central está executando?" (parado ou em ação. Dica: pense em verbos que dão sentido.)
3. **Where** — "Onde se passa essa história?" (descreva o lugar; a linha temporal é opcional.)
4. **How** — "O que pensou para estilo, cor, iluminação, ângulo e qualquer outro aspecto criativo?"

Sugestões sempre sem viés (R12).

## Escalonamento para pedidos superficiais

Se o tema ou uma resposta for vago demais para preencher o pilar sem inventar ("um cara", "uma imagem legal", "um animal"), **NÃO avance com suposições**. Desdobre o pilar em sub-perguntas até ele ficar concreto:

- **Who vago** ("um cara") → idade/porte físico, cabelo, expressão facial, vestimenta, etnia (se relevante e oferecida pelo usuário, nunca imposta).
- **What vago** ("fazendo algo") → verbo específico, objeto da ação, direção do movimento, intensidade.
- **Where vago** ("num lugar") → interior/exterior, época do dia, clima, elementos de fundo.
- **How vago** ("bonito") → estilo (foto/ilustração/3D/pintura), humor/tom, paleta, tipo de luz.

Continue perguntando (ainda uma por vez) até que Who, What, Where e How estejam todos concretos. Só então vá para a Parte 3. Quanto mais superficial o pedido, mais perguntas.

## Parte 3 — Geração do prompt

Quando os 4 pilares estiverem resolvidos, componha aplicando as regras de `Reference.md` (fotorrealismo R2/R3, regra dos terços R4, ilustração R5, objetividade total, sem artistas reais). Cada prompt **abre com a linha de persona de especialista** (escolhida pelo estilo) + `Crie uma imagem com as seguintes características:`, então os pilares — ver spec em `SKILL.md` / `Reference.md`:

1. **prompt pt-br** — persona (pt) + `who:/what:/where:/how:` (~200 palavras no corpo), rigor técnico, objetividade total (sem metáforas).
2. **prompt en** — persona (en) + mesma estrutura, tradução fiel.
3. **alt text** — ≤35 palavras em português, sem persona.

Saída em **três blocos plaintext individuais** separados por linha divisória (R10), como três arquivos para copiar separadamente. Sem verbosidade (R6).
