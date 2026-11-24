# Writes the one roast to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
import os
LINE = "My phone's autocorrect has corrected me so many times, it now finishes my sentences and starts my arguments."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
