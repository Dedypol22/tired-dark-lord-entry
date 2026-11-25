"""Write the winning monologue to $MAKEFUN_OUTPUT_DIR/entry.txt.

Standard library only. No network, no working-directory reads.
"""

import os
import sys

# The winning monologue: exactly 100 words, 538 characters, one line.
# Queen Isolde of the Glass Throne — the mirror is on its break.
LINE = "Mirror. Mirror — yes, I know, you are on your break, take it. I have waited three hundred years, oh, you are back. I am Queen Isolde of the Glass Throne, and I poisoned an apple once, a single apple, and the girl slept a hundred years and woke up married, while I got the orchard, the debts, and a mirror with opinions. The huntsman retired. The dwarves want overtime. The apple trees have stopped producing, out of spite, I assume. Ask your question, hero. Who is fairest? Anyone. Anyone but the woman who still has to ask every morning."


def main() -> int:
    text = LINE
    if not text or not text.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 600:
        print(f"entry too long: {len(text)} chars", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    words = text.split()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("written entry does not match", file=sys.stderr)
        return 1
    print(f"chars={len(text)} words={len(words)}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
