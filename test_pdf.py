from pdf_loader import load_pdf


pdf = "documents/notes.pdf"

documents = load_pdf(pdf)

print("Pages:", len(documents))

print(documents[0].page_content[:500])