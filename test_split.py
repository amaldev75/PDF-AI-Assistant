from pdf_loader import load_pdf
from text_splitter import split_documents


pdf = "documents/notes.pdf"

documents = load_pdf(pdf)

chunks = split_documents(documents)


print("Original pages:", len(documents))
print("Total chunks:", len(chunks))

print(chunks[0].page_content[:500])