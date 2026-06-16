# Prompts

Directory for versioned prompts, instruction templates, and specialized agent surfaces.

## Available Prompts

| Prompt | Description |
| --- | --- |
| `CLAUDE-FABLE-5.md` | System prompt for a surface called Claude Fable 5. Defines product information for the agent, safety and refusal rules, tone and formatting guidelines, legal/financial topic guidance and user well-being, plus instructions on knowledge cutoff, memory, persistent artifact storage, and MCP Apps suggestions. |
| `image-prompts/` | Collection of 10 image generation/editing prompts for multimodal models. Each file documents purpose, input, expected output, limitations, and examples. |

### Image Prompts

Prompts for image generation and editing via multimodal models (ChatGPT Images, DALL·E, Midjourney, etc.).

| # | Prompt | Category | Input |
| --- | --- | --- | --- |
| 01 | [Action Figure in Blister Pack](image-prompts/01-action-figure-blister-pack.md) | Edit image | Front-facing photo of a person |
| 02 | [Doodle Annotation Overlay](image-prompts/02-doodle-annotation-overlay.md) | Edit image | Photo with clear subject and negative space |
| 03 | [Grid Pet Sticker Pack](image-prompts/03-grid-pet-sticker-pack.md) | Edit image | 1–4 photos of the same pet/person |
| 04 | [Pixar / 3D Cartoon Version](image-prompts/04-pixar-3d-cartoon-version.md) | Edit image | Full-body or three-quarter portrait |
| 05 | [Meet Your Younger Self — Cat Edition](image-prompts/05-meet-your-younger-self-cat-edition.md) | Edit image | 2 photos of the same cat at different ages |
| 06 | [Isometric Tiny Room](image-prompts/06-isometric-tiny-room-miniature-world.md) | Generate image | No upload required |
| 07 | [Magazine Cover With Real Typography](image-prompts/07-magazine-cover-real-typography.md) | Generate image | No upload required |
| 08 | [Infographic Poster](image-prompts/08-infographic-poster-app-performance.md) | Generate image | No upload required |
| 09 | [90s Yearbook Polaroid](image-prompts/09-90s-yearbook-polaroid.md) | Generate image | No upload required |
| 10 | [Minimalist Brand Logo](image-prompts/10-minimalist-brand-logo-northern-still.md) | Generate image | No upload required |

### Usage with Claude Code

From the directory containing `mrbits-ai-starforge/`, load the prompt as a system prompt:

```bash
claude --dangerously-skip-permissions --system-prompt-file mrbits-ai-starforge/prompts/CLAUDE-FABLE-5.md
```

## How to Add a Prompt

Use a Markdown file for simple prompts:

```text
prompts/<prompt-name>.md
```

Use a directory when the prompt has examples, assets, or validation:

```text
prompts/<prompt-name>/
+-- README.md
+-- prompt.md
+-- examples/
```

Document purpose, expected inputs, expected output, limitations, and examples.
