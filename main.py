#!/usr/bin/env python3
"""Copy the bundled entry image to the output directory.

Stdlib only: no third-party packages, no network. The grader runs this
program twice and both runs must write identical bytes, which a plain
binary copy guarantees.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Confirm the copy is complete: same size as the bundled image.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise RuntimeError("entry.png copy is incomplete")
    # PNG signature check: the first 8 bytes must be the PNG magic.
    with open(dst, "rb") as fh:
        if fh.read(8) != b"\x89PNG\r\n\x1a\n":
            raise RuntimeError("entry.png is not a valid PNG")
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
