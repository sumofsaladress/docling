# ...existing code...
from pathlib import Path
from docling.document_converter import DocumentConverter

source = Path("./Riman-Product-Eng-PDF.pdf")
converter = DocumentConverter()
result = converter.convert(str(source))

md = result.document.export_to_markdown()
out_path = source.with_suffix(".md")
out_path.write_text(md, encoding="utf-8")

print(f"Wrote markdown to: {out_path}")
# ...existing code...