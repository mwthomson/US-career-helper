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

**Never use the shell `zip` command to repack.** Always rebuild with Python's
`zipfile`, writing only files, in the same filename order as the original archive:

```python
import zipfile, os

def rebuild(src_dir, orig_docx, out_path):
    orig = zipfile.ZipFile(orig_docx)
    order = [i.filename for i in orig.infolist()]
    with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for rel in order:
            full = os.path.join(src_dir, rel)
            zf.write(full, rel)   # file entries only, no directories

rebuild('unpacked/', 'original.docx', 'output.docx')
```

Verify afterward that no entry ends in `/`:
`python3 -c "import zipfile; print([i.filename for i in zipfile.ZipFile('output.docx').infolist() if i.filename.endswith('/')])"`
should print `[]`.

## Cause 2: template content-type leaking into a .docx

A `.dotx` is a Word **template**. Its `[Content_Types].xml` declares
`/word/document.xml` with
`ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml"`
(note `.template.main+xml`, not `.document.main+xml`). If you unpack a `.dotx`, edit
`document.xml`, and repack it with a `.docx` extension, that content-type declaration
carries over unchanged. The file extension then says "document" while the internal
content-type says "template" — Word treats that mismatch as corruption, even though
LibreOffice silently tolerates it and renders a perfectly fine-looking PDF.

**Whenever the structural source for an edit is a `.dotx` and the output is being
saved as `.docx`, patch `[Content_Types].xml` before repacking:**

```python
python3 -c "
path = 'unpacked/[Content_Types].xml'
with open(path) as f:
    content = f.read()
content = content.replace('wordprocessingml.template.main+xml', 'wordprocessingml.document.main+xml')
with open(path, 'w') as f:
    f.write(content)
"
```

Then confirm the fix:
`grep -o 'PartName="/word/document.xml" ContentType="[^"]*"' "unpacked/[Content_Types].xml"`
must show `...wordprocessingml.document.main+xml`, never `...template.main+xml`.

This step is **not needed** when the structural source is already a `.docx` — only
when starting from a `.dotx`.

## Mandatory verification before delivering any docx

Do all of the following before presenting a generated or edited `.docx` to the user.
Do not skip this because LibreOffice conversion succeeded — that alone does not prove
Word can open the file.

1. Run the `docx` skill's validation script (if available) against the output,
   comparing it to the original template — must pass with no warnings.
2. Confirm no directory entries in the zip (see Cause 1 check above).
3. If the structural source was a `.dotx`, confirm `[Content_Types].xml` declares
   `document.main+xml`, not `template.main+xml` (see Cause 2 check above).
4. Render to PDF and visually inspect: page breaks fall at natural boundaries, no
   orphaned headings, header/contact-info block unchanged, formatting consistent
   throughout. This catches formatting problems but NOT the two issues above, so it
   is an addition to, not a replacement for, steps 1-3.

If the user reports that a delivered docx won't open in Word, re-check both causes
above first before assuming it's a formatting or content issue.
