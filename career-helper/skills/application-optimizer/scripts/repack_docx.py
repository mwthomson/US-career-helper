#!/usr/bin/env python3
"""Safely repack an edited .docx (or .dotx-derived) directory into a
document Word will open without complaint.

Fixes the two silent corruption causes LibreOffice tolerates but Word
rejects (see ../references/docx-template-output.md for the full writeup):

1. Directory entries in the zip, which `zip -r`-style repacking introduces
   and real Office-generated files never contain.
2. A .dotx template content-type left in [Content_Types].xml when the
   output is being saved as .docx.

Usage:
    python3 repack_docx.py <original_template> <edited_dir> <output_path>
"""
import os
import sys
import zipfile


def patch_content_type(unpacked_dir):
    """Rewrite a leaked .dotx template content-type to .docx document type.

    Returns True if a patch was made, False if none was needed.
    """
    path = os.path.join(unpacked_dir, "[Content_Types].xml")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    patched = content.replace(
        "wordprocessingml.template.main+xml",
        "wordprocessingml.document.main+xml",
    )

    if patched == content:
        return False

    with open(path, "w", encoding="utf-8") as f:
        f.write(patched)
    return True


def rebuild(original_template, edited_dir, output_path):
    """Repack edited_dir into output_path using original_template's own
    archive order, writing file entries only. Returns whatever
    patch_content_type returned.
    """
    orig = zipfile.ZipFile(original_template)
    # Some retained templates were produced by older tooling and already contain
    # explicit directory entries. Preserve the original file order while
    # deliberately excluding those entries from the rebuilt Office package.
    order = [i.filename for i in orig.infolist() if not i.is_dir()]
    orig.close()

    patched = patch_content_type(edited_dir)

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for rel in order:
            full = os.path.join(edited_dir, rel)
            zf.write(full, rel)

    bad = [
        i.filename
        for i in zipfile.ZipFile(output_path).infolist()
        if i.filename.endswith("/")
    ]
    if bad:
        raise RuntimeError(f"Directory entries leaked into output zip: {bad}")

    return patched


def main():
    if len(sys.argv) != 4:
        print(
            "Usage: repack_docx.py <original_template> <edited_dir> <output_path>",
            file=sys.stderr,
        )
        sys.exit(1)

    original_template, edited_dir, output_path = sys.argv[1:4]
    patched = rebuild(original_template, edited_dir, output_path)

    print(f"Wrote {output_path}")
    print("No directory entries in output zip.")
    if patched:
        print("Patched template content-type (.dotx source) to document.main+xml.")
    else:
        print("No content-type patch needed.")


if __name__ == "__main__":
    main()
