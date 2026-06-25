from pdf_loader import load_pdf
from text_splitter import split_documents
from embeddings import create_embeddings
from vector_store import create_vector_store


pdf = "documents/notes.pdf"


documents = load_pdf(pdf)

chunks = split_documents(documents)

embeddings = create_embeddings()


db = create_vector_store(
    chunks,
    embeddings
)


query = "What is a production system?"


results = db.similarity_search(query, k=2)


print("Results found:", len(results))


for result in results:
    print("----------------")
    print(result.page_content[:300])