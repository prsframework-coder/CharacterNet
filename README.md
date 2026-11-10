CharacterNet
 
256 独体字 -- the Periodic Table of Chinese.
 
Small fixed set. Officially published. Everything else is built from them.
Learn the table, unlock the language.
 
An open-source visual decomposition dataset for Chinese character learning, powered by the PRS™ Framework.
 
CharacterNet v2.0 is built on China’s Ministry of Education (MoE) 2009 Standard for Modern Commonly Used Independent Characters (the 256 “atoms” of Chinese characters, which can be referred to as the alphabet of the Chinese language). It provides the raw perceptual materials for understanding Chinese characters: the visual components the human eye actually sees, phonetic mapping, tonal structure, and semantic constraints.
 
It does not include finished mnemonic stories or pedagogical sequences. 
 
🎉 CharacterNet Is the Open Substrate; PRS Chinese Is the Commercial Layer
 
CharacterNet is the free, open dataset. PRS Chinese (www.prschinese.sg) is the commercial platform built on top of it. It was officially launched on October 1st, 2026 -- China's National Day.
 
The date was chosen purposefully to celebrate the Chinese language from its motherland. The PRS framework was built to honor the visual genius of Hanzi, and it is fitting that the commercial platform took its first breath on the very day the world celebrates the language's home.
 
The split is deliberate and documented in BOUNDARY.md: the visual decomposition is open; the storytelling engine is proprietary. 
 
Repository Structure
• /data/characternet_atoms.json -- The main dataset (the 256 Periodic Table Atoms).
• /schema/characternet.schema.json -- The JSON Schema to validate new entries.
• /src/prs_characternet.py -- A Python loader for querying and validating the dataset.
• BOUNDARY.md -- The legal and conceptual separation between the free dataset and the commercial application.
• LICENSE -- CC BY 4.0. 
 
How to Use (Python)
1. Clone the repository:
git clone https://github.com/prsframework-coder/CharacterNet.git
2. Navigate to the folder:
cd CharacterNet
3. Run the Python loader:
python src/prs_characternet.py data/characternet_atoms.json --report
4. Look up a character:
python src/prs_characternet.py data/characternet_atoms.json --lookup 白
 
 
What CharacterNet Provides
• Perceptual Decomposition (VD): The visual "flat-pack" pieces of each character as seen by the human eye, not by historical etymology. (e.g., 白 is seen as 日 + a waving hand.)
• Character metadata: Pinyin, tone, primary meaning, and squeezed forms.
• Binding constraints: The strict instruction template that forces an AI to weave the shape, sound, tone, and meaning into a single causal story. 
 
What CharacterNet Does NOT Provide
• Finished mnemonic stories (the "ZIP" / Semantic Multiplexing layer).
• The PRS Engine (the prompt architecture that generates stories and enforces the Immutable Story Lock).
• Curriculum sequencing. 
Those elements are part of PRS Chinese, a commercial platform built on top of this dataset. 
 
License
 
CharacterNet is released under the Creative Commons Attribution 4.0 International (CC BY 4.0) license. You are free to share, adapt, and build on the material -- including commercially -- provided you give appropriate credit.
 
CharacterNet is provided "as is," with no warranty of accuracy for pedagogical use. Verify before deploying in a classroom. 
 
Contact
• Dataset questions: Open an issue in this repository.
• Commercial enquiries: hello@prschinese.sg