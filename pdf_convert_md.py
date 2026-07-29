from docling.document_converter import DocumentConverter

source = "./Compensation_plan_HK_CN.pdf"
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())