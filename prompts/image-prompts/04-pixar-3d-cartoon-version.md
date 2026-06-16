# Pixar / 3D Cartoon Version

Category: Edit image prompt

Input: A full-body or three-quarter portrait. Clear lighting on the face.

## Prompt

```text
Re-render the person in the uploaded photo as a full-body Pixar-style
3D animated character.

CHARACTER FIDELITY:
- Keep the exact same outfit, hairstyle, and accessories.
- Keep the same general face shape and skin tone, but stylize.
- Eyes: large, expressive, with catchlight highlights.
- Skin: smooth, slightly stylized subsurface scattering, no pores.
- Proportions: slightly cartoon-exaggerated (bigger head, smaller
  features) but recognizable.

POSE: Match the photo, or default to a relaxed standing pose with
weight on one leg.

LIGHTING: Three-point studio lighting. Warm key from upper-left,
cool fill from lower-right, soft rim light separating subject from
background.

BACKGROUND: Soft gradient, light pastel blue to cream, slight bokeh
suggestion. Background should never compete with the character.

RENDER: High-end CG, similar to a feature-film promotional render.
Aspect ratio: 1:1.
```

## Expected Output

A square (1:1) image of a Pixar/Disney-style 3D character rendered in high-quality CG, representing the person from the input photo. Retains original clothing, accessories, and hairstyle, with slightly caricatured proportions (larger head, expressive eyes). Soft pastel gradient background.

## Limitations

- Full-body or three-quarter photos work best; face-only photos may produce generic poses.
- Low lighting in the input photo may result in loss of facial detail in the 3D character.
- "Pixar-style" is an aesthetic reference — the result depends on the image model's capabilities and may not be identical to actual Pixar productions.
- Very small or complex accessories may be simplified or omitted by the model.

## Examples

**Input:** Three-quarter photo of a man with a short beard, wearing a denim jacket and backpack, standing with weight on one leg.

**Expected result:** A stylized 3D character with a slightly larger head, big expressive eyes, same denim jacket and backpack, relaxed pose matching the photo, three-point studio lighting over a pastel blue background.
