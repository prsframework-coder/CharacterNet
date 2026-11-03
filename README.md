# CharacterNet

**An open-source visual decomposition dataset for Chinese character learning, powered by the PRS™ Framework.**

CharacterNet provides the raw materials for understanding Chinese characters: the visual components, phonetic mapping, tonal structure, and semantic meaning. It does **not** include finished mnemonic stories or pedagogical sequences.

## Repository Structure

- `/data/characternet.json` — The main dataset (23 starter characters).
- `/schema/characternet.schema.json` — The JSON Schema to validate new entries.
- `/src/prs_characternet.py` — A Python loader for querying, validating, and testing the dataset.
- `BOUNDARY.md` — The legal and conceptual separation between the free dataset and the commercial application.
- `LICENSE` — CC BY 4.0.

## How to Use (Python)

1. Clone the repository:
   `git clone https://github.com/prsframework-coder/CharacterNet.git`
2. Navigate to the folder:
   `cd CharacterNet`
3. Run the Python loader:
   `python src/prs_characternet.py data/characternet.json --report`
4. Look up a character:
   `python src/prs_characternet.py data/characternet.json --lookup 我`

## What CharacterNet Provides

- **Character metadata**: pinyin, tone, primary meaning.
- **Visual decomposition (VD)**: the constituent pieces of each character.
- **Binding constraints**: instruction templates for generating mnemonic stories.
- **Integrity testing**: a schema to validate that every entry follows the PRS dynamic architecture.

## What CharacterNet Does NOT Provide

- Finished mnemonic stories (Semantic Multiplexing layer).
- The story generation engine.
- Curriculum sequencing.

Those elements are part of **[PRS Chinese](https://www.prschinese.sg)**, a commercial platform built on top of this dataset.

## License

CharacterNet is released under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. You are free to share and adapt the material, provided you give appropriate credit.

## Contact

For dataset questions: open an issue in this repository.
For commercial enquiries: hello@prschinese.sg
