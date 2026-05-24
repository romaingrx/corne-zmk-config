#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml"]
# ///
"""Strip the outer-column &none padding so a Miryoku Corne keymap renders as 3x5+3."""
import sys
import yaml

data = yaml.safe_load(sys.stdin)
for name, keys in data["layers"].items():
    rows, thumbs = [keys[i : i + 12] for i in range(0, 36, 12)], keys[36:]
    data["layers"][name] = [k for row in rows for k in row[1:-1]] + thumbs
data["layout"] = {"qmk_keyboard": "corne_rotated", "layout_name": "LAYOUT_split_3x5_3"}
yaml.safe_dump(data, sys.stdout, sort_keys=False, allow_unicode=True)
