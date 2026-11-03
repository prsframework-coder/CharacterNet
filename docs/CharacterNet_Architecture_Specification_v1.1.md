CharacterNet™ — Architecture Specification (v1.1)

The Machine-Readable Dynamic Architecture for PRS Character Encoding

Author: Abraham Praise (Creator of the PRS™ Framework)
Domain: www.characternet.org · www.prschinese.sg
License: CC BY 4.0
Status: Active

---

1. The Core Principle

The CharacterNet JSON stores the constraint, not the scene.

· visual_pieces = the given materials.
· binding_constraint = the instruction to fuse them.
· leading_question = the reasoning prompt.
· connections = the validation rules.

The scene itself is generated fresh each time—by an AI, a learner, or software. This preserves the Dynamic Architecture: different scene each time, same kind of connection.

2. The Schema (v1.1)

Every character record must strictly follow this JSON structure.

```json
{
  "id": "PRS-0001",
  "character": "我",
  "pinyin": "wǒ",
  "tone": 3,
  "tone_contour": "dip-rise (ˇ)",
  "meaning": "I, me",
  "visual_pieces": ["手", "戈"],
  "component_meanings": {
    "手": "hand",
    "戈": "halberd / spear"
  },
  "component_pinyin": {
    "手": "shǒu",
    "戈": "gē"
  },
  "binding_constraint": "Bind the visual pieces (a hand, a halberd) with the sound 'wǒ' and the 3rd falling then rising tone into a scene that means 'I, me'.",
  "leading_question": "What is the hand doing with the spear?",
  "connections": {
    "component_to_action": true,
    "identity_link": true,
    "causal_order": true,
    "sound_in_action": true,
    "tone_in_word": true,
    "meaning_as_payoff": true
  },
  "integrity_test": {
    "remove_shape": "collapses",
    "remove_form": "collapses",
    "remove_pinyin": "collapses",
    "remove_tone": "collapses",
    "remove_meaning": "collapses"
  },
  "tags": ["pronoun", "first-person", "hs1"],
  "family": "pronouns"
}
```

3. Field Definitions

Field Type Description
id String Unique identifier (PRS-XXXX).
character String The Chinese character.
pinyin String Romanization with tone mark.
tone Integer 1, 2, 3, or 4.
tone_contour String Must be exactly: flat (ˉ), rising (´), dip-rise (ˇ), or falling (ˋ).
meaning String Short English meaning.
visual_pieces Array The recognizable components the eye sees (never single strokes).
component_meanings Object Dictionary mapping each piece to its English meaning.
component_pinyin Object Dictionary mapping each piece to its pinyin.
binding_constraint String The instruction to weave the pieces, sound, and tone into a scene.
leading_question String A prompt to guide the learner to find the pieces.
connections Object Six boolean flags (see Section 4).
integrity_test Object Five flags indicating what happens if a beam is removed (see Section 5).
tags Array Searchable tags (e.g., "hs1", "pronoun").
family String The thematic group (e.g., "circus-numbers").

4. The Six Load-Bearing Connections

Every record must have all six connections set to true. If any are false, the story is static and fails the architecture.

1. component_to_action: Every shape does something.
2. identity_link: Explicit phrase fuses components (e.g., "the same hand").
3. causal_order: Each hook causes the next.
4. sound_in_action: The pinyin is the action itself.
5. tone_in_word: An English word naturally performs the tone contour.
6. meaning_as_payoff: The scene resolves into the meaning.

5. The Integrity Test

Every record must have all five beams set to collapses. If a beam can be removed without collapsing recall, the build is decorative, not architectural.

· remove_shape → No visual anchor.
· remove_form → No semantic role.
· remove_pinyin → No phonetic trigger.
· remove_tone → No prosodic contour.
· remove_meaning → No payoff.

6. How an AI Uses This

1. Retrieval: The AI looks up the character record.
2. Scene Generation: The AI reads the visual_pieces, binding_constraint, and leading_question. It generates a fresh scene that satisfies the constraint.
3. Validation: The AI checks its generated scene against the connections and integrity_test. If it misses a beam, it regenerates.

7. Python Implementation

The official Python loader and validator (prs_characternet.py) is available in the /src directory. It allows developers to:

· Load and parse the dataset.
· Validate records against the JSON Schema.
· Query by family, tone, or tag.
· Run automated integrity tests.

---

CharacterNet™ — The visual knowledge foundation for Chinese characters.
Born in Singapore. Created for the world.
The foundation is open. The possibilities are global.

---
