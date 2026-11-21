CharacterNet
 
256 独体字 — the Periodic Table of Chinese.
 
Small fixed set. Officially published. Everything else is built from them.
Learn the table, unlock the language.
 
An open-source visual decomposition dataset for Chinese character learning, powered by the PRS™ Framework.
 
CharacterNet v2.0 is built on China’s Ministry of Education (MoE) 2009 Standard for Modern Commonly Used Independent Characters (the 256 “atoms” of Chinese characters, forming a periodic table that can be referred to as the alphabet of the Chinese language)[span_0](start_span)[span_0](end_span). It provides the raw perceptual materials for understanding Chinese characters: the visual components the human eye actually sees, phonetic mapping, tonal structure, and semantic constraints[span_1](start_span)[span_1](end_span).

CharacterNet is an open-source visual decomposition dataset covering China’s 256 foundational Chinese character components—the building-block “ABC” of the written language—broken down into eye-identifiable, Lego-like visual pieces rather than handwriting strokes[span_2](start_span)[span_2](end_span). Each entry follows a clean, seven-field JSON structure (`character`, `pinyin`, `tone`, `meaning`, `visual_pieces`, `component_pinyin`, and `component_meanings`) designed for easy reuse across apps and learning tools[span_3](start_span)[span_3](end_span). Rather than handing out pre-made explanations for passive memorization, the framework follows a simple **sticky-story rule**—demonstrated live on [PRS Chinese](https://www.prschinese.sg/)—where learners actively combine the labeled visual pieces, Pinyin sound, and tone to invent their own memorable story leading to the character’s meaning[span_4](start_span)[span_4](end_span).
 
It does not include finished mnemonic stories or pedagogical sequences[span_5](start_span)[span_5](end_span). 
 
🎉 CharacterNet Is the Open Substrate; PRS Chinese Is the Free Interactive Story Workbench
 
CharacterNet is the free, open dataset[span_6](start_span)[span_6](end_span). PRS Chinese ([https://www.prschinese.sg/](https://www.prschinese.sg/)) is the free web platform built on top of it, officially launched on October 1st, 2026 — China’s National Day[span_7](start_span)[span_7](end_span).
 
The date was chosen purposefully to celebrate the Chinese language from its motherland[span_8](start_span)[span_8](end_span). The PRS framework was built to honor the visual genius of Hanzi, and it is fitting that the platform took its first breath on the very day the world celebrates the language’s home[span_9](start_span)[span_9](end_span).

On [https://www.prschinese.sg/](https://www.prschinese.sg/), learners craft and save their own sticky stories completely free of charge—with no sign-up, no login, and no data collection. Saved stories live locally inside your browser page and can be exported for safekeeping and imported back anytime. The commercial side of PRS Chinese covers physical books, merchandise, and custom partnerships, as documented in `BOUNDARY.md`.
 
Repository Structure
• `/data/characternet_atoms.json` — The main dataset (the 256 Periodic Table Atoms)[span_10](start_span)[span_10](end_span).
• `/schema/characternet.schema.json` — The JSON Schema to validate new entries[span_11](start_span)[span_11](end_span).
• `/src/prs_characternet.py` — A Python loader for querying and validating the dataset[span_12](start_span)[span_12](end_span).
• `BOUNDARY.md` — The legal and conceptual separation between the free dataset/web app and commercial products[span_13](start_span)[span_13](end_span).
• `LICENSE` — CC BY 4.0[span_14](start_span)[span_14](end_span). 
 
How to Use (Python)
1. Clone the repository:
`git clone https://github.com/prsframework-coder/CharacterNet.git`[span_15](start_span)[span_15](end_span)
2. Navigate to the folder:
`cd CharacterNet`[span_16](start_span)[span_16](end_span)
3. Run the Python loader:
`python src/prs_characternet.py data/characternet_atoms.json —report`
4. Look up a character:
`python src/prs_characternet.py data/characternet_atoms.json —lookup 白`
 
 
What CharacterNet Provides
• Perceptual Decomposition (VD): The visual “flat-pack” pieces of each character as seen by the human eye, not by historical etymology[span_17](start_span)[span_17](end_span). (e.g., 白 is seen as 日 + a waving hand[span_18](start_span)[span_18](end_span).)
• Character metadata: Pinyin, tone, primary meaning, and squeezed forms[span_19](start_span)[span_19](end_span).
• Binding constraints: The structural rules that guide learners (or AI helpers) to weave the shape, sound, tone, and meaning into a single sticky story[span_20](start_span)[span_20](end_span). 
 
What CharacterNet Does NOT Provide
• Pre-written mnemonic stories (learners craft and export their own stories free on [https://www.prschinese.sg/](https://www.prschinese.sg/)).
• Curriculum sequencing or classroom pacing[span_21](start_span)[span_21](end_span).
• Physical books, printed card decks, or branded merchandise (offered through the commercial arm of PRS Chinese).
 
License
 
CharacterNet is released under the Creative Commons Attribution 4.0 International (CC BY 4.0) license[span_22](start_span)[span_22](end_span). You are free to share, adapt, and build on the material — including commercially — provided you give appropriate credit[span_23](start_span)[span_23](end_span).
 
CharacterNet is provided “as is,” with no warranty of accuracy for pedagogical use[span_24](start_span)[span_24](end_span). Verify before deploying in a classroom[span_25](start_span)[span_25](end_span). 
 
Contact
• Dataset questions: Open an issue in this repository[span_26](start_span)[span_26](end_span).
• Books, merchandise, or commercial enquiries: hello@prschinese.sg
