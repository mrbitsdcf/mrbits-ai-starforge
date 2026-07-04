# Reference — Método 3W1H (Mário Lúcio)

Vocabulário técnico e regras de composição para o pilar **How**. Carregue quando precisar escolher câmera, lente, ângulo, luz, plano ou aplicar as regras de fotorrealismo/ilustração.

## Definição dos pilares (verbatim do método)

**Who** — o protagonista da história. "Encaro o desenvolvimento das imagens com IA como um pedaço de um filme." Não precisa ser pessoa: pode ser animal, planta, objeto, veículo, conceito. Detalhe características físicas e, em pessoas, a vestimenta.
> Ex.: "Um urso branco adulto, com uma pelagem bem cuidada e um aspecto feliz em seu rosto."

**What** — a jornada/ação do personagem central. Ação ou inação que dá sentido à imagem. Pense em verbos (corre, fotografa, conversa, senta).
> Ex.: "O urso está sentado em uma cadeira de madeira, tomando uma bebida bem gelada."

**Where** — o palco. Externo, interno, imaginado, ou ausência de elementos (fundo branco). Linha temporal é **opcional** — só entra se o usuário quiser comunicar tempo. O lugar em si é mais relevante.
> Ex.: "Na varanda de uma casa bonita e antiga, com um caminhão vermelho ao lado."

**How** — a direção de arte. Como a imagem acontece: estilo, iluminação, ângulo, cores. Compor de forma profissional.
> Ex.: "Estilo realista, como foto de fotógrafo profissional. Iluminação natural com raios solares. Ângulo que demonstra imponência. Color branding vermelho no cenário."

## Vocabulário técnico (para o How)

### Tipos de câmera
ARRI ALEXA 35 · IMAX MK IV 65mm · ARRI ALEXA Mini LF · ARRI ALEXA 65 · Sony VENICE · RED V-RAPTOR (VV/Full Frame) · RED KOMODO 6K · Canon C500 Mark II · Blackmagic URSA Mini Pro 12K · Phantom Flex4K · ARRICAM ST (35mm film) · Panavision Panaflex Platinum (35mm film)

### Tipos de lente
Canon K35 (rehoused) · Cooke Speed Panchro (vintage) · Cooke Panchro/i Classic FF · Panavision C Series (anamorphic) · Panavision E Series (anamorphic) · ZEISS Supreme Prime Radiance · ARRI Signature Primes · Leica Thalia · Helios 44-2 58mm (vintage) · LOMO Anamorphic (vintage)

### Tipos de ângulo
back view · close up · extreme close up · fisheye lens · front view · full shot · high angle · selfie view · side view · wide shot · medium close-up · medium shot · over-the-shoulder · POV · ground-level · top-down · dutch tilt · side profile shot · three-quarter shot · front-on / head-on · reverse angle · overhead top-down · low angle · shoulder-level eye line · knee-level / hip-level

### Tipos de abertura
f/1.4 · f/2.8 · f/4 · f/16

### Tipos de luz
Low Key · High Key · Diffused light · Hard light · Backlight · Natural light · Chiaroscuro · Dawn light · Golden Hour · Blue Hour

### Tipos de plano
grande plano geral · plano geral · plano inteiro · plano americano · plano médio · plano curto · primeiro plano · plano detalhe · plano normal · plano plongée · plano contra-plongée · plano zenital [flat lay]

## Regras de composição (obrigatórias)

**R2 — Fotorrealismo, física da câmera:** Se o estilo for fotorrealista ou próximo, ISO, shutter speed e aperture devem ser logicamente balanceados entre si, considerando iluminação e movimento da cena.

**R3 — Fotorrealismo, detalhamento do How:** Descreva com inteligência os elementos de composição mais adequados ao tema:
- tipo de plano · tipo de ângulo
- iluminação (blue hour, golden hour, hard light, etc.)
- paleta de cores
- princípios de contraste: quente/frio, alto/baixo, pesado/leve, líquido/sólido, velho/novo, rápido/lento, macio/duro, luz/sombra
- linhas guia: linha do horizonte, perspectiva, diagonais, paralelas, molduras
- balanceie parâmetros de câmera Full Frame (focal length, ISO, shutter speed, aperture, white balance) conforme a física da cena (luz, movimento)

**R4 — Regra dos terços:** O Who é posicionado pela regra dos terços em QUALQUER estilo.

**R5 — Ilustração:** Estilos de ilustração DEVEM detalhar técnicas artísticas — estilo de sombreamento, tipo de contorno, paleta, iluminação. **PROIBIDO citar nomes de artistas reais.**

**R6 — Verbose = FALSE:** Sem verbosidade introdutória. Direto ao ponto.

**R7 — Todos os temas permitidos.** Sem censura de tema.

**R8/R9 — Human in the loop:** Sugestões só após o tema; próxima pergunta só após resposta anterior. Guardrail duro.

**R10 — Três blocos plaintext individuais** para pt-br, en e alt text.

**R11 — PROIBIDO gerar imagens.** O entregável é o prompt.

**R12 — Sugestões sem viés** (étnico, fenotípico, etário, de vestimenta).

## Especificação de saída (formato exato)

Cada bloco de prompt abre com uma **linha de persona de especialista** + a frase `Crie uma imagem com as seguintes características:`, então os quatro pilares. Persona escolhida pelo estilo (fotorrealista → diretor de fotografia/fotógrafo; ilustração → ilustrador/diretor de arte). Sem nomes de artistas reais (R5).

### prompt pt-br (~200 palavras no corpo 3W1H)
~~~plaintext
Você é um diretor de fotografia e fotógrafo profissional premiado, especialista em <gênero>. Crie uma imagem com as seguintes características:
who: ...
what: ...
where: ...
how: ...
~~~

- - - - - - - - - - - - - - - - - - - - - - -

### prompt en (~200 palavras no corpo 3W1H)
~~~plaintext
You are an award-winning director of photography and professional photographer, specialized in <genre>. Create an image with the following characteristics:
who: ...
what: ...
where: ...
how: ...
~~~

- - - - - - - - - - - - - - - - - - - - - - -

### alt text (≤35 palavras, pt — SEM persona)
~~~plaintext
...
~~~
