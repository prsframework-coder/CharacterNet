CharacterNet: A Deterministic VDSM Engine for Open-Source Visual Chinese Decomposition
 
Author: Abraham Praise
Affiliation: Founder, PRS Chinese (www.prschinese.sg)
Date: November 2026
License: CC BY 4.0 (Dataset) 
 
Abstract
 
Traditional computer-assisted language learning (CALL) for Chinese characters relies heavily on rote memorization and etymological study. While recent advances in Large Language Models (LLMs) have enabled the generation of mnemonic stories (Semantic Multiplexing, or SM), these systems suffer from “cognitive drift”—hallucinating historical radicals or generating non-deterministic outputs that confuse visual learners.
 
This paper introduces CharacterNet, an open-source, deterministic Visual Decomposition (VD) engine. By stripping the proprietary Semantic Multiplexing (SM) layer from the broader PRS (Picture, Retrieve, Story) framework, CharacterNet isolates the 256 foundational atomic building blocks of Chinese characters. We argue that the separation of the deterministic VD layer (the “hardware”) from the generative SM layer (the “software”) provides a scalable, drift-proof foundation for visual literacy in Chinese and serves as a structural parallel to historical breakthroughs in computer vision. 
 
1. Introduction: The Parallel to Computer Vision
 
In the 1990s, artificial intelligence was blind to the physical world. Computers could process data, but a photograph of a cat was merely a matrix of RGB values. This limitation was overcome by Fei-Fei Li’s ImageNet, a massive dataset of labeled visual objects that taught machines how to “see” the world.
 
Today, AI faces a similar blindness in the realm of written Chinese. AI can read entire libraries of text, return dictionary definitions, and list stroke orders. However, AI remains fundamentally blind to the visual puzzle of the Chinese character. It understands the character as a historical artifact (etymology) or a sequence of strokes, rather than the assembly of visual shapes (bricks) that the human eye actually perceives.
 
CharacterNet is designed to bridge this gap. It is a foundational dataset that maps Chinese characters the way a visual learner sees them, establishing a new paradigm for visual literacy. 
 
2. The Problem: Cognitive Drift and the Failure of Stroke-Based Learning
 
Traditional Chinese pedagogy is heavily reliant on writing characters repeatedly (rote memorization) and understanding historical radicals. For visual learners, this method often fails. A stroke is simply a pencil movement; without a recognizable picture to anchor it, the visual memory system struggles to retain the information.
 
While modern LLMs can generate mnemonic stories to aid memory (a process we define as Semantic Multiplexing, or SM), relying on an LLM to simultaneously decompose the character and generate the story introduces Cognitive Drift.
 
When prompted with a character, an LLM will frequently revert to its training data, explaining the etymological origins of a radical rather than the visual shapes the eye actually sees. This creates a conflict between the visual story and the user’s perception, rendering the mnemonic ineffective. 
 
3. The Architecture: Isolating the VDSM Engine
 
The PRS (Picture, Retrieve, Story) framework solves this by modularizing the learning process. CharacterNet represents the strict separation of the Visual Decomposition (VD) engine from the Semantic Multiplexing (SM) engine.
 
CharacterNet = VDSM Engine − SM
 
By stripping away the generative storytelling layer, CharacterNet becomes a purely deterministic dataset. It does not “think” or generate; it only displays.
 
3.1 The 256 Atomic Standard
 
CharacterNet is built upon China’s official 2009 Ministry of Education standard, identifying the 256 foundational component characters (独体字). These are the “atoms” of the Chinese language. They are not broken down into individual strokes; rather, they are treated as indivisible “Lego bricks” that build the user’s visual vocabulary.
 
3.2 The Atomic Resolver and Squeezed Forms
 
The engine features a recursive logic system. When a compound character (e.g., 森) is input, the engine does not hallucinate a story. Instead, it looks up the constituent visual components (木 + 木 + 木). It also includes a Squeezed Form Mapper, which translates compressed visual variants (like 朩 or 氵) back into their foundational atomic parent characters, ensuring accurate quantity counting. 
 
4. The User Interface: The IKEA Flat-Pack Metaphor
 
To make the visual decomposition intuitive, CharacterNet utilizes an interface modeled on an IKEA assembly manual.
 
When a character is queried, the engine displays a “Picking List”:
• Visual: The exact geometric component the eye sees.
• Qty: How many of that component are present (e.g., 2x crossbars).
• Label: A plain, non-narrative noun (e.g., “legs,” “sun,” “child”).
• Pinyin: The phonetic anchor for that component. 
The UI intentionally leaves the “Story” column blank. This is a boundary. CharacterNet provides the flat-pack pieces; it is the user’s job (or the PRS Chinese engine’s job) to assemble them. 
 
5. Conclusion: The Boundary and the Ecosystem
 
CharacterNet is released as an open-source dataset under the CC BY 4.0 license. It serves as the “hardware” layer—a public utility for visual literacy and AI training.
 
The proprietary “software” layer—PRS Chinese—operates on top of this dataset. By wrapping the Semantic Multiplexing (SM) engine around CharacterNet’s deterministic outputs, PRS Chinese can generate absurd, hilarious, and highly memorable stories without the risk of visual drift.
 
By distinguishing between the bricks (CharacterNet) and the stories (PRS Chinese), we empower a new generation of visual learners. We give them the pieces to build the language themselves, proving that strokes are meant for paper, but bricks are meant for memory. 
 
References
1. Li, F. F., et al. (2009). ImageNet: A Large-Scale Hierarchical Image Database. IEEE Conference on Computer Vision and Pattern Recognition.
2. Ministry of Education of the People’s Republic of China. (2009). Standard of Component Characters for Chinese Language Teaching.
3. Praise, A. (2026). The PRS Framework: Visual Decomposition and Semantic Multiplexing in Chinese Language Acquisition. PRS Chinese Technical Whitepaper.