# 3WH1Creator

Skill de **engenharia de prompts para IAs de imagem** baseada no método **3W1H** de Mário Lúcio. Decompõe qualquer ideia visual em quatro componentes acionáveis — **Who** (protagonista), **What** (ação), **Where** (cenário), **How** (direção de arte) — e entrega prompts técnicos, objetivos e de alta fidelidade, prontos para colar em Midjourney, DALL-E, Flux, nano-banana, Gemini e afins.

> **A skill produz apenas o prompt. Ela NÃO gera imagens.** (Fiel à regra 11 do método original — a pessoa usuária quer o prompt, não a imagem.)

---

## O que é o método 3W1H

Criado por Mário Lúcio no início de 2023, o 3W1H adapta o **5W2H** do Sistema Toyota de Produção para prompts de imagem. Em vez de uma lista de palavras-chave separadas por vírgula, o prompt é estruturado em uma narrativa modular — "encaro a imagem como um pedaço de um filme". São quatro pilares:

| Pilar | Pergunta | O que define |
|-------|----------|--------------|
| **Who** | Quem protagoniza? | Sujeito central: pessoa, animal, planta, objeto, veículo, conceito. Características físicas + vestimenta. |
| **What** | Que ação executa? | Ação ou inação que dá sentido à cena. Pense em verbos. |
| **Where** | Onde se passa? | Cenário/ambiente (externo, interno, imaginado, fundo neutro). Linha temporal é opcional. |
| **How** | Como acontece? | Direção de arte: estilo, iluminação, ângulo, cores, plano, câmera/lente, composição. |

**Fontes:** [Método 3W1H (LinkedIn de Mário Lúcio)](https://www.linkedin.com/pulse/método-3w1h-o-que-é-e-como-funciona-na-prática-mário-lúcio-w8n0f/) · [Slides](https://slides-3w1h.vercel.app/) · [Prompt-fonte no GitHub](https://github.com/marioluciofjr/prompts/blob/main/IAs_de_Imagem/metodo_3w1h.md)

---

## Dois modos de uso

A skill roteia automaticamente para um de dois workflows conforme o pedido:

### 1. `FromDescription` — ideia abstrata → prompt

Para quando você tem uma ideia na cabeça e quer transformá-la em prompt. A skill conduz um pipeline **human-in-the-loop**: pergunta o tema, depois faz uma pergunta por pilar (uma de cada vez), oferecendo 3 sugestões sem viés a cada passo. Ao final, monta os prompts.

**Gatilhos:** "crie um prompt de imagem de...", "quero uma imagem de...", uma descrição em texto.

**Escalonamento para pedidos vagos:** se o pedido for superficial ("crie uma imagem", "faz um cara"), a skill **não inventa** — ela aumenta o número de perguntas, desdobrando cada pilar em sub-perguntas (idade, porte, vestimenta, expressão...) até Who/What/Where/How ficarem concretos. Quanto mais vago o pedido, mais perguntas.

### 2. `FromImage` — engenharia reversa de uma imagem → prompt

Para quando você tem uma imagem e quer o prompt que a recria. A skill lê o arquivo com a tool `Read`, decompõe a imagem nos quatro pilares e gera os prompts.

**Gatilhos:** "gere o prompt desta imagem", um caminho de arquivo de imagem, "engenharia reversa".

**Decomposição física exaustiva:** o princípio deste modo é *quanto mais específica a descrição física, mais fiel a recriação*. Para sujeitos humanos, a skill percorre um checklist granular — rosto (olhos, nariz, lábios, sobrancelhas), cabelo, corpo mensurável (proporções, busto, cintura, quadris, pernas), pele, cada peça de roupa (caimento, tecido, transparência), pose e enquadramento. Sujeitos não humanos recebem a mesma exaustividade. Neste modo, o detalhe **vence** o limite de palavras.

---

## Formato de saída (sempre)

Três blocos `plaintext` **individuais e separados**, para cópia independente:

1. **prompt pt-br** — persona + estrutura `who: / what: / where: / how:`
2. **prompt en** — persona + mesma estrutura, tradução fiel
3. **alt text** — ≤ 35 palavras em português (sem persona — é legenda)

Cada prompt abre com uma **linha de persona de especialista** + a instrução, seguida dos quatro pilares:

```plaintext
Você é um diretor de fotografia e fotógrafo profissional premiado, especialista em <gênero>. Crie uma imagem com as seguintes características:
who: ...
what: ...
where: ...
how: ...
```

A persona é **adaptativa ao estilo**: fotorrealista → *diretor de fotografia / fotógrafo premiado*; ilustração/pintura/3D → *ilustrador digital / diretor de arte*. Ela nunca cita nomes de artistas reais.

---

## Regras-chave (guardrails)

- **Human-in-the-loop:** uma pergunta por vez; a próxima só aparece após a resposta anterior. Nunca gera o prompt antes de ter todos os pilares.
- **Nunca gera a imagem** — só o prompt.
- **Regra dos terços** aplicada ao sujeito em qualquer estilo.
- **Fotorrealismo exige física de câmera balanceada:** ISO + shutter + aperture + focal length + white balance de sensor Full Frame, coerentes com luz e movimento.
- **Ilustração exige técnica explícita:** sombreamento, contorno, paleta, iluminação — nunca nomes de artistas reais.
- **Objetividade total:** sem metáforas nem subjetividade no prompt final.
- **Sugestões sem viés** (étnico, fenotípico, etário, de vestimenta).
- **Todos os temas são permitidos** — sem censura de conteúdo.
- **Verbose = FALSE:** vai direto ao ponto, inclusive nas perguntas.

---

## Estrutura de arquivos

```
3WH1Creator/
├── SKILL.md                       # Roteamento, formato de saída, persona, gotchas
├── README.md                      # Este arquivo
├── Reference.md                   # Vocabulário técnico + 12 regras + spec de saída
└── Workflows/
    ├── FromDescription.md         # Ideia abstrata → perguntas 3W+H1 → prompt
    └── FromImage.md               # Arquivo de imagem → engenharia reversa → prompt
```

O `Reference.md` contém o vocabulário técnico completo para o pilar **How**: tipos de câmera (ARRI, RED, Sony...), lentes (Cooke, ZEISS, Panavision...), ângulos, aberturas (f/1.4–f/16), tipos de luz (golden hour, chiaroscuro...) e tipos de plano (plano geral, primeiro plano, plano zenital...).

---

## Exemplos de invocação

```
/3WH1Creator quero um prompt de uma fotógrafa idosa fotografando uma poça ao amanhecer
/3WH1Creator crie uma imagem de um cara          → dispara escalonamento de perguntas
/3WH1Creator gere o prompt desta imagem: /caminho/para/foto.png
```

Ou em linguagem natural: *"me ajuda a criar um prompt 3W1H para..."*, *"faz a engenharia reversa dessa imagem em prompt"*.

---

## Créditos

Método **3W1H** por **Mário Lúcio**. Skill implementada para o ecossistema PAI seguindo as convenções de skills (progressive disclosure, dynamic loading, flat folder structure).
