import os
import zipfile

import pytest

from repack_docx import patch_content_type, rebuild


TEMPLATE_CONTENT_TYPES = (
    '<?xml version="1.0"?>'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Override PartName="/word/document.xml" '
    'ContentType="application/vnd.openxmlformats-officedocument'
    '.wordprocessingml.template.main+xml"/>'
    '</Types>'
)

DOCUMENT_CONTENT_TYPES = (
    '<?xml version="1.0"?>'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Override PartName="/word/document.xml" '
    'ContentType="application/vnd.openxmlformats-officedocument'
    '.wordprocessingml.document.main+xml"/>'
    '</Types>'
)


def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def make_office_style_zip(path, entries):
    """Write a zip containing only file entries (no directory entries),
    matching how real Office-generated .docx/.dotx files are structured."""
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        for name, content in entries:
            zf.writestr(name, content)


def test_patch_content_type_rewrites_template_to_document(tmp_path):
    write_file(str(tmp_path / "[Content_Types].xml"), TEMPLATE_CONTENT_TYPES)

    patched = patch_content_type(str(tmp_path))

    assert patched is True
    with open(tmp_path / "[Content_Types].xml", encoding="utf-8") as f:
        result = f.read()
    assert "wordprocessingml.document.main+xml" in result
    assert "wordprocessingml.template.main+xml" not in result


def test_patch_content_type_leaves_document_type_unchanged(tmp_path):
    write_file(str(tmp_path / "[Content_Types].xml"), DOCUMENT_CONTENT_TYPES)

    patched = patch_content_type(str(tmp_path))

    assert patched is False
    with open(tmp_path / "[Content_Types].xml", encoding="utf-8") as f:
        result = f.read()
    assert result == DOCUMENT_CONTENT_TYPES


def test_rebuild_produces_no_directory_entries_in_original_order(tmp_path):
    original = tmp_path / "original.dotx"
    entries = [
        ("[Content_Types].xml", TEMPLATE_CONTENT_TYPES),
        ("_rels/.rels", "<rels/>"),
        ("word/document.xml", "<document>original</document>"),
    ]
    make_office_style_zip(str(original), entries)

    edited_dir = tmp_path / "edited"
    write_file(str(edited_dir / "[Content_Types].xml"), TEMPLATE_CONTENT_TYPES)
    write_file(str(edited_dir / "_rels" / ".rels"), "<rels/>")
    write_file(str(edited_dir / "word" / "document.xml"), "<document>changed</document>")

    output = tmp_path / "output.docx"
    rebuild(str(original), str(edited_dir), str(output))

    result_names = [i.filename for i in zipfile.ZipFile(output).infolist()]
    assert result_names == [name for name, _ in entries]
    assert not any(name.endswith("/") for name in result_names)


def test_rebuild_patches_content_type_from_dotx_source(tmp_path):
    original = tmp_path / "original.dotx"
    entries = [
        ("[Content_Types].xml", TEMPLATE_CONTENT_TYPES),
        ("word/document.xml", "<document>original</document>"),
    ]
    make_office_style_zip(str(original), entries)

    edited_dir = tmp_path / "edited"
    write_file(str(edited_dir / "[Content_Types].xml"), TEMPLATE_CONTENT_TYPES)
    write_file(str(edited_dir / "word" / "document.xml"), "<document>changed</document>")

    output = tmp_path / "output.docx"
    patched = rebuild(str(original), str(edited_dir), str(output))

    assert patched is True
    with zipfile.ZipFile(output) as zf:
        content_types = zf.read("[Content_Types].xml").decode("utf-8")
    assert "wordprocessingml.document.main+xml" in content_types


def test_rebuild_raises_if_directory_entry_leaks_into_output(tmp_path):
    original = tmp_path / "original.docx"
    entries = [
        ("[Content_Types].xml", DOCUMENT_CONTENT_TYPES),
        ("word/document.xml", "<document>original</document>"),
    ]
    make_office_style_zip(str(original), entries)

    edited_dir = tmp_path / "edited"
    write_file(str(edited_dir / "[Content_Types].xml"), DOCUMENT_CONTENT_TYPES)
    write_file(str(edited_dir / "word" / "document.xml"), "<document>changed</document>")

    # Simulate a corrupted "original" whose own archive order contains a
    # directory entry -- rebuild must still refuse to ship it.
    with zipfile.ZipFile(original, "a") as zf:
        zf.writestr("word/", "")

    output = tmp_path / "output.docx"
    with pytest.raises(RuntimeError):
        rebuild(str(original), str(edited_dir), str(output))
