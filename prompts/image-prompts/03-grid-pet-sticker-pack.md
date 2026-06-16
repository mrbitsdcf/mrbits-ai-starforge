# Grid Pet Sticker Pack

Category: Edit image prompt

Input: 1 to 4 clear photos of the same pet/person, ideally with varied expressions (calm, mouth open, eyes closed, looking up, etc.).

## Prompt

```text
Create a 3×3 grid of 9 die-cut sticker designs of the same subject
from the uploaded photo(s). The grid should look like a printable
sticker sheet or a messaging-app sticker pack (WhatsApp / LINE /
Telegram style).

SUBJECT CONSISTENCY: Every sticker must feature the exact same
animal/person from the uploaded photo(s) - same fur color, same
markings, same eye color, same breed/face. Do NOT invent a new
subject.

EACH STICKER MUST HAVE:
- A clean white die-cut sticker border (about 6–8 px thick) hugging
  the subject's silhouette, with a soft drop shadow underneath.
- Transparent / pure white background outside the border.
- One short text label in playful rounded sans-serif with a soft
  black outline, placed in the empty space near the subject.
- One small doodle accent (sparkles, hearts, steam puff, anger
  marks, Zzz, question marks, exclamation lines - varies per
  sticker).

THE 9 STICKERS (top-left to bottom-right):
1. Looking up curiously - label "Wow~" - small yellow sparkles.
2. Sitting paws-tucked, slightly grumpy - label "Hmph!" - small
   steam-puff doodle from the head.
3. Mid-yawn, mouth wide open - label "Yawnnn~" - pink wavy lines
   near the mouth.
4. Peeking over a small ledge, both paws visible - label "Peekaboo!"
   on a small tape banner - one pink heart in the corner.
5. Wearing tiny round black sunglasses, confident pose - label
   "I'm fabulous" - yellow sparkles around the head.
6. Side-eye, mildly annoyed - label "Not Happy!" - red anger-mark
   cross on the forehead.
7. Mouth wide open as if begging - label "Feed Me!" - small yellow
   alert lines above the head.
8. Curled up sleeping, eyes closed - no label, just blue "Zzz"
   floating above.
9. Head tilted, confused expression - no label, just three small
   dark blue question marks ("???") above the head.

LAYOUT: 3 columns × 3 rows, even spacing, each sticker centered in
its cell, plain white sheet background. Same subject and same overall
style across all 9 cells.

ASPECT RATIO: 1:1 (square sheet).
```

## Expected Output

A square (1:1) image containing a 3×3 grid of 9 die-cut stickers of the same pet/person from the input photos. Each sticker has a white border, soft drop shadow, a distinct expression/pose, short text label, and a decorative accent (sparkles, hearts, etc.). Pure white sheet background.

## Limitations

- Requires clear photos with varied expressions so the model can maintain visual consistency across all 9 stickers.
- Generation models may lose appearance consistency between grid cells, especially for specific pet markings and colors.
- Short text on stickers may not be perfectly legible depending on the model used.
- The prompt defines 9 fixed expressions — to customize them, edit the "THE 9 STICKERS" list in the prompt body.

## Examples

**Input:** 3 photos of a white cat with blue eyes — one calm, one yawning, one looking up.

**Expected result:** A square sheet with 9 stickers of the same white cat in varied poses (curious, sleeping, wearing sunglasses, etc.), each with a white die-cut border, text label, and decorative doodle.
