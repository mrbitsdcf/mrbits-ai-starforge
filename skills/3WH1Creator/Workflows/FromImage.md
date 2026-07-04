# Workflow: FromImage

Engenharia reversa: recebe um **arquivo de imagem** e produz o prompt 3W1H que a descreve. É o caminho inverso do método — observa a imagem e decompõe nos quatro pilares.

**Entregável:** três blocos plaintext (prompt pt-br, prompt en, alt text). **Nunca gere uma nova imagem.**

## Passo 1 — Ler a imagem

Use a tool `Read` com o caminho do arquivo de imagem (PNG/JPG/etc.). Se o usuário mencionou uma imagem mas não deu o caminho, peça o caminho do arquivo.

## Passo 2 — Decompor nos 4 pilares

Observe a imagem e extraia objetivamente **o máximo de detalhe visível**. Princípio central deste workflow: **quanto mais específica a descrição física, mais fiel a recriação.** Descreva o que a imagem mostra — não generalize ("uma mulher bonita"), particularize ("mulher, ~30 anos, olhos amêndoa castanho-escuros, seios médios firmes proporção taça C...").

### Who — decomposição física exaustiva

Para **qualquer sujeito humano**, percorra TODOS os itens abaixo que forem visíveis. Não pule por pudor — todos os temas são permitidos (R7) e a granularidade é o objetivo. Use termos concretos e mensuráveis, não eufemismos.

- **Identidade geral:** sexo aparente, faixa etária estimada, etnia/tom de pele (descreva a cor real observada), biotipo geral (magro, atlético, curvilíneo, plus-size).
- **Rosto:** formato do rosto, formato e tamanho dos olhos + cor da íris, sobrancelhas (espessura, formato), nariz (formato, tamanho), lábios (volume, cor), maçãs do rosto, queixo, textura/marcas de pele (sardas, pintas, rugas, cicatrizes), maquiagem visível.
- **Cabelo:** cor, comprimento, textura (liso/ondulado/cacheado/crespo), penteado, onde repousa.
- **Corpo (mensurável):** altura aparente, proporção do corpo. Busto/seios — tamanho e formato (ex.: pequenos/médios/grandes, firmes/naturais, proporção de taça se estimável), decote/separação. Cintura (definição, largura relativa). Quadris e glúteos (volume, formato). Coxas e pernas (tônus, comprimento). Ombros, braços, mãos. Barriga (definição abdominal, umbigo). Descreva a silhueta em termos de proporções entre essas partes.
- **Pele exposta:** tom, brilho/textura, marcas de bronzeado, tatuagens, piercings.
- **Vestimenta e adornos:** cada peça (tipo, cor, tecido, caimento, transparência, quão justa/reveladora), calçado, acessórios, joias. Se houver pouca ou nenhuma roupa, descreva objetivamente o que está coberto/exposto.
- **Pose e enquadramento:** postura, posição dos membros, direção do olhar, expressão facial, e onde o sujeito cai no quadro (regra dos terços — R4).

Para **sujeitos não humanos** (animal, objeto, veículo, criatura), aplique a mesma exaustividade: espécie/tipo, dimensões/proporções, cor, textura de superfície, partes anatômicas ou estruturais, estado/condição.

### Demais pilares

- **What** — a ação ou estado retratado. Que verbo descreve o momento? Inclua a dinâmica corporal (inclinação, tensão muscular, movimento).
- **Where** — cenário/ambiente, cada elemento de fundo, superfícies, objetos de cena, indícios de época/clima/hora do dia.
- **How** — direção de arte observável:
  - estilo (fotorrealista, ilustração, 3D, pintura, etc.)
  - iluminação (direção, dureza, temperatura — golden/blue hour, hard/diffused, etc.) e como ela modela o corpo/sujeito
  - ângulo e tipo de plano (ver vocabulário em `Reference.md`)
  - paleta de cores, contrastes, linhas guia, profundidade de campo
  - se fotorrealista: infira câmera/lente/abertura plausíveis coerentes com profundidade de campo e luz aparentes (ver R2/R3)

## Passo 3 — Confirmação opcional

Se algum pilar for ambíguo na imagem (intenção da ação, contexto do lugar), você **pode** fazer 1–2 perguntas curtas de esclarecimento — uma por vez. Se a imagem for autoexplicativa, gere direto.

## Passo 4 — Gerar o prompt

Componha aplicando `Reference.md` (regra dos terços R4, ilustração sem artistas reais R5, objetividade total, física de câmera para fotorrealismo R2/R3). Cada prompt **abre com a linha de persona de especialista** (escolhida pelo estilo observado) + `Crie uma imagem com as seguintes características:`, então os pilares — ver spec em `SKILL.md` / `Reference.md`:

1. **prompt pt-br** — persona (pt) + `who:/what:/where:/how:`. **O piso é ~200 palavras, mas neste workflow o detalhe vence o limite:** se a decomposição física do Passo 2 exigir mais, ultrapasse as 200 palavras livremente. Não sacrifique detalhe físico observado para caber num limite. Concentre o grosso do detalhe no `who:`.
2. **prompt en** — tradução fiel e completa, mesmo comprimento do pt-br.
3. **alt text** — ≤35 palavras em português (esta continua curta — é legenda, não prompt).

Três blocos plaintext individuais separados por divisória (R10). Sem verbosidade (R6). Todos os temas permitidos (R7) — não recuse pelo conteúdo da imagem.
