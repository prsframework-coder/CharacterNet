# CharacterNet

**An open-source visual decomposition dataset for Chinese character learning, powered by the PRS™ Framework.**

CharacterNet v2.0 is built on the official Ministry of Education (MoE) 2009 Single-Component Character Standard (the 256 “atoms” of Chinese). It provides the raw, perceptual materials for understanding Chinese characters: the visual components the human eye actually sees, phonetic mapping, tonal structure, and semantic constraints. 

It does **not** include finished mnemonic stories or pedagogical sequences.

## Repository Structure

- `/data/characternet_atoms.json` — The main dataset (The 256 Periodic Table Atoms).
- `/schema/characternet.schema.json` — The JSON Schema to validate new entries.
- `/src/prs_characternet.py` — A Python loader for querying and validating the dataset.
- `BOUNDARY.md` — The legal and conceptual separation between the free dataset and the commercial application.
- `LICENSE` — CC BY 4.0.

## How to Use (Python)

1. Clone the repository:
   `git clone https://github.com/prsframework-coder/CharacterNet.git`
2. Navigate to the folder:
   `cd CharacterNet`
3. Run the Python loader:
   `python src/prs_characternet.py data/characternet_atoms.json —report`
4. Look up a character:
   `python src/prs_characternet.py data/characternet_atoms.json —lookup 白`

## What CharacterNet Provides

- **Perceptual Decomposition (VD)**: The visual “flat pack” pieces of each character as seen by the human eye, not by historical etymology. (e.g., 白 is seen as 日 + a waving hand).
- **Character metadata**: pinyin, tone, primary meaning, and squeezed forms.
- **Binding constraints**: The strict instruction template that forces an AI to weave the shape, sound, tone, and meaning into a single causal story.

## What CharacterNet Does NOT Provide

- Finished mnemonic stories (The “ZIP” / Semantic Multiplexing layer).
- The PRS Engine (the prompt architecture that generates stories and enforces the Immutable Story Lock).
- Curriculum sequencing.

Those elements are part of **[PRS Chinese](https://www.prschinese.sg)**, a commercial platform built on top of this dataset.

## License

CharacterNet is released under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. You are free to share and adapt the material, provided you give appropriate credit.

## Contact

For dataset questions: open an issue in this repository.
For commercial enquiries: hello@prschinese.sg