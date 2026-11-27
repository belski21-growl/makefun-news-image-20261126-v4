#!/usr/bin/env python3
"""Shipper for the make.fun news-image-20261126 entry, fourth revision.

The front page itself is the file ``entry.png`` sitting next to this
script.  This program does exactly one thing: it carries that exact
file into the harness output directory.  Nothing is drawn here, nothing
is fetched, nothing is recomputed from the news: the picture was
rendered beforehand (full-day edition, compiled 27 Nov 2026 ~03:35 UTC)
and is pinned below by byte count and SHA-256 digest.

Before any byte is written, the source image is measured against the
v4 fingerprint: size at most 1 MiB, the pinned digest, JPEG start and
end markers, and 1024 by 1024 pixels parsed out of the JPEG headers.
After the copy the same five measurements run again on the copy, so a
short write or a swapped file is caught instead of shipped silently.

Standard library only.  Paths go through ``os.path`` and plain
``open()``; the copy streams in 32 KiB pieces and never holds the whole
file in memory.  Two guards protect the run: the output directory must
exist (or be creatable) and must not be the directory the entry lives
in, and source and destination must not be the same file.

Usage:
    python3 main.py [--output-dir DIR] [--verify-only]

The destination is ``--output-dir`` first, then the
``MAKEFUN_OUTPUT_DIR`` environment variable, then ``./output``.
``--verify-only`` runs every check on the source and writes nothing.
"""

import hashlib
import os
import struct
import sys

# ---- fingerprint of the v4 render (27 Nov 2026 ~03:35 UTC) ----
V4_BYTES = 403428
V4_SHA256 = "72e1e291a9bbf6125fba2042eb67a989cf62b64249536461eb705f69ee4e86aa"
V4_WIDTH = 1024
V4_HEIGHT = 1024
SIZE_CAP = 1048576
PIECE = 32768
SOI = b"\xff\xd8"
EOI = b"\xff\xd9"
ENTRY = "entry.png"


class CarrierError(Exception):
    """Any failed check; the run stops and reports it once."""


def abort(message):
    """Raise the single failure type this shipper uses."""
    raise CarrierError(message)


def here():
    """Directory holding this script (and therefore entry.png)."""
    return os.path.dirname(os.path.abspath(__file__))


def measure(blob):
    """Return (size, sha256, width, height) for a JPEG byte string.

    Width and height come from the first Start-Of-Frame segment
    (C0, C1 or C2).  A blob that is not a JPEG, or that hides its frame
    header, is a failure, never a guess.
    """
    if len(blob) < 4 or blob[:2] != SOI or blob[-2:] != EOI:
        abort("not a whole JPEG: SOI/EOI markers missing")
    if len(blob) > SIZE_CAP:
        abort("image over the 1 MiB cap: %d bytes" % len(blob))
    pos = 2
    while pos + 9 <= len(blob):
        if blob[pos] != 0xFF:
            abort("bad JPEG marker at offset %d" % pos)
        mark = blob[pos + 1]
        if mark in (0xD8, 0xD9) or 0xD0 <= mark <= 0xD7:
            pos += 2
            continue
        seg_len = struct.unpack(">H", blob[pos + 2:pos + 4])[0]
        if mark in (0xC0, 0xC1, 0xC2):
            height, width = struct.unpack(
                ">HH", blob[pos + 5:pos + 9])
            return len(blob), hashlib.sha256(blob).hexdigest(), width, height
        pos += 2 + seg_len
    abort("no JPEG frame header found")


def check_source(path):
    """Read the source image and check it against the v4 fingerprint."""
    try:
        with open(path, "rb") as handle:
            blob = handle.read()
    except OSError as exc:
        abort("cannot read %s: %s" % (path, exc))
    size, digest, width, height = measure(blob)
    if size != V4_BYTES:
        abort("size mismatch: got %d bytes, v4 expects %d"
              % (size, V4_BYTES))
    if digest != V4_SHA256:
        abort("sha256 mismatch: got %s" % digest)
    if (width, height) != (V4_WIDTH, V4_HEIGHT):
        abort("dimensions mismatch: got %dx%d, v4 expects %dx%d"
              % (width, height, V4_WIDTH, V4_HEIGHT))
    return blob


def pick_output(argv):
    """Resolve the output directory from flag, env, then ./output."""
    out = None
    for i, arg in enumerate(argv):
        if arg == "--output-dir" and i + 1 < len(argv):
            out = argv[i + 1]
        elif arg.startswith("--output-dir="):
            out = arg.split("=", 1)[1]
    if out is None:
        out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    return os.path.abspath(out)


def ship(source_path, out_dir):
    """Copy entry.png to out_dir/entry.png, verifying both ends."""
    src_dir = os.path.dirname(os.path.abspath(source_path))
    if os.path.abspath(out_dir) == src_dir:
        abort("output dir must not be the source dir: %s" % out_dir)
    if os.path.exists(out_dir) and not os.path.isdir(out_dir):
        abort("output path is not a directory: %s" % out_dir)
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        abort("cannot create output dir %s: %s" % (out_dir, exc))
    dest_path = os.path.join(out_dir, ENTRY)
    if os.path.abspath(dest_path) == os.path.abspath(source_path):
        abort("source and destination are the same file")
    if os.path.exists(dest_path):
        try:
            if os.path.samefile(dest_path, source_path):
                abort("destination resolves to the source file")
        except OSError:
            pass
    blob = check_source(source_path)
    try:
        with open(source_path, "rb") as src, \
                open(dest_path, "wb") as dst:
            while True:
                piece = src.read(PIECE)
                if not piece:
                    break
                dst.write(piece)
    except OSError as exc:
        abort("copy failed: %s" % exc)
    with open(dest_path, "rb") as handle:
        copied = handle.read()
    size, digest, width, height = measure(copied)
    if (size, digest, width, height) != (V4_BYTES, V4_SHA256,
                                          V4_WIDTH, V4_HEIGHT):
        abort("copied file fails the v4 fingerprint")
    print("v4 shipper: wrote %s (%d bytes, sha256 %s)"
          % (dest_path, size, digest))
    return 0


def run(argv):
    """Entry point: verify-only short-circuits before any copy."""
    source_path = os.path.join(here(), ENTRY)
    if "--verify-only" in argv:
        check_source(source_path)
        print("v4 shipper: verify-only PASS (%d bytes, sha256 %s)"
              % (V4_BYTES, V4_SHA256))
        return 0
    return ship(source_path, pick_output(argv))


if __name__ == "__main__":
    try:
        sys.exit(run(sys.argv[1:]))
    except CarrierError as exc:
        print("v4 shipper: %s" % exc, file=sys.stderr)
        sys.exit(1)
