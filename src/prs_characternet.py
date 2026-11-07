"""
PRS CharacterNet -- Loader & Validator (v2.0)
Framework: PRS -- Picture, Retrieve, Story (Flat Pack & ZIP Edition)
"""

import json
import re
from pathlib import Path
from typing import Optional

try:
    import jsonschema
except ImportError:
    jsonschema = None

class PRSCharacter:
    REQUIRED_CONNECTIONS = [
        "component_to_action", "identity_link", "causal_order", 
        "sound_in_action", "tone_in_word", "meaning_as_payoff"
    ]
    TONE_CONTOURS = {
        1: "flat (ˉ)", 2: "rising (')", 3: "dip-rise (ˇ)", 4: "falling (ˋ)"
    }

    def __init__(self, data: dict):
        self.data = data

    @property
    def character(self) -> str: return self.data["character"]
    @property
    def pinyin(self) -> str: return self.data["pinyin"]
    @property
    def tone(self) -> int: return self.data["tone"]
    @property
    def meaning(self) -> str: return self.data["meaning"]
    @property
    def visual_pieces(self) -> list: return self.data["visual_pieces"]
    @property
    def binding_constraint(self) -> str: return self.data["binding_constraint"]

    def validate(self) -> list:
        problems = []
        if not re.match(r"^ATOM-[0-9]{4}$", self.data.get("id", "")):
            problems.append("id must match 'ATOM-NNNN'")
        
        expected_contour = self.TONE_CONTOURS.get(self.tone)
        if expected_contour and self.data.get("tone_contour") != expected_contour:
            problems.append(f"tone_contour '{self.data.get('tone_contour')}' does not match tone {self.tone} ('{expected_contour}')")

        if not self.visual_pieces:
            problems.append("visual_pieces must not be empty")

        conn = self.data.get("connections", {})
        for key in self.REQUIRED_CONNECTIONS:
            if conn.get(key) is not True:
                problems.append(f"connection '{key}' must be true")
                
        return problems

    def describe(self) -> str:
        lines = [
            f"{self.character} ({self.pinyin}) -- {self.meaning}",
            f"  Pieces: {' + '.join(self.visual_pieces)}",
            f"  Binding: {self.binding_constraint}",
        ]
        return "\n".join(lines)

class CharacterNet:
    def __init__(self, path: str, schema_path: Optional[str] = None):
        self.path = Path(path)
        self.schema_path = Path(schema_path) if schema_path else None
        self.raw = json.loads(self.path.read_text(encoding="utf-8"))
        self._load()

    def _load(self):
        root = self.raw.get("characternet", {})
        self.version = root.get("version", "?")
        self.characters: list[PRSCharacter] = [PRSCharacter(c) for c in root.get("characters", [])]
        self._index = {c.character: c for c in self.characters}

    def lookup(self, char: str) -> Optional[PRSCharacter]:
        return self._index.get(char)

    def validate_all(self) -> dict:
        return {c.character: c.validate() for c in self.characters}

    def report(self) -> str:
        lines = [
            f"CharacterNet v{self.version} -- {len(self.characters)} characters",
            f"  framework: {self.raw.get('characternet', {}).get('framework')}",
            ""
        ]
        for c in self.characters:
            probs = c.validate()
            status = "OK" if not probs else f"{len(probs)} problem(s)"
            lines.append(f"  [{c.data.get('id')}] {c.character} ({c.pinyin}) -- {status}")
        return "\n".join(lines)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="PRS CharacterNet loader v2.0")
    parser.add_argument("json", help="Path to characternet_atoms.json")
    parser.add_argument("--lookup", help="Look up a character, e.g. 日")
    parser.add_argument("--validate", action="store_true", help="Validate all characters")
    parser.add_argument("--report", action="store_true", help="Print full report")
    args = parser.parse_args()

    net = CharacterNet(args.json)

    if args.lookup:
        c = net.lookup(args.lookup)
        print(c.describe() if c else f"Character '{args.lookup}' not found.")
        return
    if args.validate:
        report = net.validate_all()
        for char, probs in report.items():
            print(f"{char}: {'OK' if not probs else probs}")
        return

    print(net.report())

if __name__ == "__main__":
    main()