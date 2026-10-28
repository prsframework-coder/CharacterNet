# Dataset Card for CharacterNet

## Dataset Summary
CharacterNet is an open-source dataset for the visual decomposition of Chinese characters. It is designed to provide AI researchers and developers with the visual "ground truth" of how the human eye perceives and breaks down Chinese characters, moving away from academic etymology and toward perceptual memory.

This dataset is released under **CC BY 4.0**.

## Supported Tasks
- **Visual Decomposition:** Extracting the visual sub-components (radicals/shapes) of Chinese characters.
- **Phonetic and Semantic Mapping:** Linking visual pieces to pinyin, tone, and meaning.
- **Mnemonic Generation (Input):** Providing the "binding constraints" required to train an AI to generate mnemonic stories.

## Languages
- Chinese (Simplified / Hanzi)
- English (Metadata and Constraints)

## Dataset Structure
### Data Fields
- `character`: The Chinese character (e.g., 兔).
- `pinyin`: The romanized pronunciation (e.g., tù).
- `tone`: The tone number (1-4).
- `meaning`: The primary English meaning (e.g., rabbit).
- `visual_pieces`: An array of the visual components the eye perceives (e.g., ["子", "儿", "口"]).
- `binding_constraint`: An instruction template for story generation (e.g., "Bind the pieces... with the sound and tone...").

## What is NOT Included (The Boundary)
To protect the commercial application of this data, CharacterNet explicitly **does not include**:
- Finished, absurd mnemonic stories (Semantic Multiplexing).
- The commercial PRS Engine.
- Curriculum sequencing.

For finished stories, commercial licensing, or educational tools, visit [PRS Chinese](https://www.prschinese.sg).

## Source Data
The data is manually curated by Abraham Praise, Creator of the PRS Framework, and expanded through the PRS Chinese platform.

## Citation
If you use CharacterNet in your research, please cite:
@misc{praise2026characternet,
title={CharacterNet: A Visual Decomposition Dataset for Chinese Character Learning},
author={Praise, Abraham},
year={2026},
url={https://github.com/prsframework-coder/CharacterNet}
}

