# CharacterNet

**An open-source visual decomposition dataset for Chinese character learning.**

CharacterNet provides the raw materials for understanding Chinese characters: the visual components, phonetic mapping, tonal structure, and semantic meaning. It does **not** include finished mnemonic stories or pedagogical sequences.

---

## What CharacterNet Provides

- **Character metadata**: pinyin, tone, primary meaning
- **Visual decomposition (VD)**: the constituent pieces (radicals, sub-components) of each character
- **Binding constraints**: instruction templates that define the parameters for generating a mnemonic story (visual pieces + sound + tone + meaning)

CharacterNet is the **input dataset**. It is not the engine.

---

## What CharacterNet Does NOT Provide

- **Finished mnemonic stories** (Semantic Multiplexing layer)
- **Story generation engine**
- **Curriculum sequencing**
- **User experience or pedagogical framework**

Those elements are part of **[PRS Chinese](https://www.prschinese.sg)**, a commercial platform built on top of this dataset.

---

## Licence

CharacterNet is released under **[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)**.

You are free to:
- **Share**: copy and redistribute the material in any medium or format
- **Adapt**: remix, transform, and build upon the material for any purpose, including commercially

**Attribution requirement**: credit CharacterNet and link to this repository.

---

## Boundary Statement

### Free (Open Source)
CharacterNet is a **dataset**. It contains:
- Visual decomposition (VD): the constituent pieces of each character
- Phonetic and tonal metadata
- Binding constraints: the raw parameters for story generation

### Paid (Commercial)
**PRS Chinese** is a **platform**. It contains:
- Semantic Multiplexing (SM): the absurd, finished mnemonic stories
- The story generation engine (proprietary)
- Curriculum design and adaptive sequencing
- Full user experience (web app, mobile, coaching)

**CharacterNet is the scaffolding. PRS Chinese is the house.**

If you are building research tools, training AI models, or creating non-commercial educational projects, CharacterNet is yours to use freely.

If you are building a commercial learning platform that generates finished stories, you are welcome to use CharacterNet as the input dataset, but the story generation layer is outside the scope of this repository.

---

## Usage

### Installation
```bash
git clone https://github.com/your-org/CharacterNet.git
cd CharacterNet
