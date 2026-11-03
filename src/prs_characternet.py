"""
PRS CharacterNet — Loader, Validator, and Scene Integrity Tester.
Framework: PRS — Picture, Retrieve, Story.
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
    """A single PRS character record."""

    REQUIRED_CONNECTIONS = [
        "component_to_action",
        "identity_link",
        "causal_order",
        "sound_in_action",
        "tone_in_word",
        "meaning_as_payoff",
    ]
    REQUIRED_BEAMS = ["remove_shape", "remove_form", "remove_pinyin", "remove_tone", "remove_meaning"]
    TONE_CONTOURS = {
        1: "flat (ˉ)",
        2: "rising (´)",
        3: "dip-rise (ˇ)",
        4: "falling (ˋ)",
    }

    def __init__(self, data: dict):
        self.data = data

    # ---- Accessors ----
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
    @property
    def leading_question(self) -> Optional[str]: return self.data.get("leading_question")
    @property
    def scene_example(self) -> Optional[str]: return self.data.get("scene_example")

    # ---- Validation ----
    def validate(self) -> list:
        """Return a list of problems (empty = valid)."""
        problems = []

        if not re.match(r"^PRS-[0-9]{4}$", self.data.get("id", "")):
            problems.append("id must match 'PRS-NNNN'")

        if not (1 <= self.tone <= 4):
            problems.append("tone must be 1–4")

        expected = self.TONE_CONTOURS.get(self.tone)
        if expected and self.data.get("tone_contour") != expected:
            problems.append(
                f"tone_contour '{self.data.get('tone_contour')}' "
                f"does not match tone {self.tone} ('{expected}')"
            )

        if not self.visual_pieces:
            problems.append("visual_pieces must not be empty")

        if len(self.binding_constraint) < 10:
            problems.append("binding_constraint too short")

        # connections must all be True
        conn = self.data.get("connections", {})
        for key in self.REQUIRED_CONNECTIONS:
            if conn.get(key) is not True:
                problems.append(f"connection '{key}' must be true")

        # integrity_test must all be 'collapses'
        integ = self.data.get("integrity_test", {})
        for key in self.REQUIRED_BEAMS:
            if integ.get(key) != "collapses":
                problems.append(f"integrity_test '{key}' must be 'collapses'")

        return problems

    # ---- Integrity test ----
    def run_integrity_test(self) -> dict:
        """
        Simulate removing each beam / connection and report whether recall collapses.
        This is a static check: it reads the declared integrity_test block
        and checks that every beam is marked 'collapses'.
        """
        integ = self.data.get("integrity_test", {})
        results = {}
        for beam in self.REQUIRED_BEAMS:
            results[beam] = integ.get(beam, "missing")
        return results

    # ---- Scene generation (template) ----
    def describe(self) -> str:
        """Human-readable summary."""
        lines = [
            f"{self.character} ({self.pinyin}) — tone {self.tone} — {self.meaning}",
            f"  Visual pieces: {' + '.join(self.visual_pieces)}",
            f"  Leading question: {self.leading_question or '(none)'}",
            f"  Binding: {self.binding_constraint}",
        ]
        if self.scene_example:
            lines.append(f"  Scene: {self.scene_example}")
        return "\n".join(lines)


class CharacterNet:
    """Loader for a CharacterNet JSON file."""

    def __init__(self, path: str, schema_path: Optional[str] = None):
        self.path = Path(path)
        self.schema_path = Path(schema_path) if schema_path else None
        self.raw = json.loads(self.path.read_text(encoding="utf-8"))
        self._load()

    def _load(self):
        root = self.raw.get("characternet", {})
        self.version = root.get("version", "?")
        self.last_updated = root.get("last_updated")
        self.framework = root.get("framework")
        self.architecture = root.get("architecture")
        self.characters: list[PRSCharacter] = [
            PRSCharacter(c) for c in root.get("characters", [])
        ]
        self._index = {c.character: c for c in self.characters}

    # ---- Lookup ----
    def lookup(self, char: str) -> Optional[PRSCharacter]:
        return self._index.get(char)

    def by_tone(self, tone: int) -> list[PRSCharacter]:
        return [c for c in self.characters if c.tone == tone]

    def by_family(self, family: str) -> list[PRSCharacter]:
        return [c for c in self.characters if c.data.get("family") == family]

    def by_tag(self, tag: str) -> list[PRSCharacter]:
        return [c for c in self.characters if tag in c.data.get("tags", [])]

    # ---- Validation ----
    def validate_all(self) -> dict:
        report = {}
        for c in self.characters:
            probs = c.validate()
            report[c.character] = probs
        return report

    def validate_against_schema(self) -> dict:
        """Validate the whole document against the JSON Schema."""
        if jsonschema is None:
            return {"error": "jsonschema not installed (pip install jsonschema)"}
        if self.schema_path is None:
            return {"error": "no schema_path provided"}
        schema = json.loads(self.schema_path.read_text(encoding="utf-8"))
        try:
            jsonschema.validate(self.raw, schema)
            return {"valid": True}
        except jsonschema.ValidationError as e:
            return {"valid": False, "error": str(e)}

    # ---- Reporting ----
    def report(self) -> str:
        lines = [
            f"CharacterNet v{self.version} — {len(self.characters)} characters",
            f"  framework: {self.framework}",
            f"  architecture: {self.architecture}",
            "",
        ]
        for c in self.characters:
            probs = c.validate()
            status = "OK" if not probs else f"{len(probs)} problem(s)"
            lines.append(f"  [{c.data.get('id')}] {c.character} ({c.pinyin}) — {status}")
        return "\n".join(lines)


# ---- CLI ----
def main():
    import argparse
    parser = argparse.ArgumentParser(description="PRS CharacterNet loader")
    parser.add_argument("json", help="Path to characternet.json")
    parser.add_argument("--schema", help="Path to characternet.schema.json")
    parser.add_argument("--lookup", help="Look up a character, e.g. 我")
    parser.add_argument("--validate", action="store_true", help="Validate all characters")
    parser.add_argument("--integrity", action="store_true", help="Run integrity tests")
    parser.add_argument("--report", action="store_true", help="Print full report")
    args = parser.parse_args()

    net = CharacterNet(args.json, args.schema)

    if args.lookup:
        c = net.lookup(args.lookup)
        print(c.describe() if c else f"Character '{args.lookup}' not found.")
        return

    if args.validate:
        report = net.validate_all()
        for char, probs in report.items():
            print(f"{char}: {'OK' if not probs else probs}")
        if args.schema:
            print("Schema:", net.validate_against_schema())
        return

    if args.integrity:
        for c in net.characters:
            print(f"{c.character} ({c.pinyin}): {c.run_integrity_test()}")
        return

    if args.report:
        print(net.report())
        return

    # default: report
    print(net.report())


if __name__ == "__main__":
    main()
