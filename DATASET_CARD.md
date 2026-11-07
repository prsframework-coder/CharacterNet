# Dataset Card for CharacterNet v2.0

## Dataset Summary
CharacterNet v2.0 is the open-source visual ground-truth layer for Chinese characters, built on the official MoE 2009 256 Single-Component Standard. It powers the PRS™ Framework by providing the exact structural materials an AI or human needs to build the PRS Engine’s “Flat Pack & ZIP” scenes. 

It explicitly **ignores historical etymology** and instead maps the character as the human eye perceives it (Visual Decomposition).

This dataset is released under **CC BY 4.0**.

## Supported Tasks
- **Visual Decomposition:** Extracting perceptual visual pieces (e.g., 兔 = ⺈ + 口 + 儿 + 丶).
- **Constraint Generation:** Providing the exact `binding_constraint` that forces an AI to weave the pieces into a causal story.

## Data Fields
- `id`: Unique ID (e.g., ATOM-0001).
- `character`: The Hanzi.
- `pinyin` / `tone` / `tone_contour`: Phonetic and tonal metadata.
- `is_moe_atom`: Boolean indicating if it is on the 256 standard list.
- `visual_pieces`: The array of flat-pack pieces the eye sees.
- `binding_constraint`: The strict instruction template for the AI.
- `connections`: The 6 load-bearing rules the generated story must satisfy.

## The Boundary (What is NOT Included)
To protect the commercial PRS Chinese platform, CharacterNet does **not** include:
- Finished mnemonic stories (the ZIP).
- The PRS Engine prompt architecture.
- Curriculum sequencing.

For the complete learning platform, visit [PRS Chinese](https://www.prschinese.sg).