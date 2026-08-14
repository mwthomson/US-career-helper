# Producing a Valid .docx Every Time

Editing and repacking a `.docx` or `.dotx` file can produce output that LibreOffice
renders to PDF just fine, but that Microsoft Word reports as corrupt. Both root
causes below are silent — PDF conversion and most validation scripts do not catch
them. Follow this file exactly whenever unpacking, editing, and repacking a `.docx`
or `.dotx`, whether for a resume, cover letter, or any other document.

## Cause 1: rebuilding the zip with directory entries

Running `zip -Xr out.docx .` from inside an unpacked folder writes explicit directory
entries (`word/`, `word/_rels/`, `docProps/`, `word/theme/`, etc.) into the archive.
Real Office-generated `.docx`/`.dotx` files never contain directory entries — only
file entries. Word's parser is far stricter about this than LibreOffice and will
refuse to open a file that has them, even though `unzip -t` and LibreOffice report it
as fine.

**Never use the shell `zip` command to repack, and never hand-write the rebuild
logic.** Use `career-helper-us-localized/skills/application-optimizer/scripts/repack_docx.py`,
which rebuilds the zip with file entries only (in the original archive's order) and
raises an error itself if any directory entry would leak into the output -- this is
the same logic previously spelled out here as prose, now run as a script instead of
re-derived by hand every time:

```bash
python3 career-helper-us-localized/skills/application-optimizer/scripts/repack_docx.py original.docx unpacked/ output.docx
```

If it exits without error, no directory entries leaked into `output.docx` -- the
script already verified this before returning.

## Cause 2: template content-type leaking into a .docx

A `.dotx` is a Word **template**. Its `[Content_Types].xml` declares
`/word/document.xml` with
`ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml"`
(note `.template.main+xml`, not `.document.main+xml`). If you unpack a `.dotx`, edit
`document.xml`, and repack it with a `.docx` extension, that content-type declaration
carries over unchanged. The file extension then says "document" while the internal
content-type says "template" — Word treats that mismatch as corruption, even though
LibreOffice silently tolerates it and renders a perfectly fine-looking PDF.

`career-helper-us-localized/skills/application-optimizer/scripts/repack_docx.py`
(see Cause 1 above) already checks for this and patches it automatically before
repacking, whenever it finds a leaked template content-type -- no separate step
needed. It prints "Patched template content-type" when it did so, or "No
content-type patch needed" when the source was already a `.docx`.

As of the 2026-08 template conversion, Marc's cover letter template
(`Cover Letter - Template.docx`) is a `.docx`, not a `.dotx`, so this cause no
longer applies to normal cover letter generation -- it's retained here, and in
the script, for any future `.dotx` source.

## Mandatory verification before delivering any docx

Do all of the following before presenting a generated or edited `.docx` to the user.
Do not skip this because LibreOffice conversion succeeded — that alone does not prove
Word can open the file.

1. Repack with `career-helper-us-localized/skills/application-optimizer/scripts/repack_docx.py`
   (see Cause 1 above) -- this covers the directory-entry check and the
   content-type patch/check in one step, and fails loudly if either is wrong.
2. Run the `docx` skill's validation script (if available) against the output,
   comparing it to the original template — must pass with no warnings.
3. Render to PDF and visually inspect: page breaks fall at natural boundaries, no
   orphaned headings, header/contact-info block unchanged, formatting consistent
   throughout. This catches formatting problems but NOT the zip/content-type
   issues above, so it is an addition to, not a replacement for, steps 1-2.

If the user reports that a delivered docx won't open in Word, re-check both causes
above first before assuming it's a formatting or content issue.
