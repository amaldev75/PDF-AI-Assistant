from pdf_loader import load_pdf
from text_splitter import split_documents
from embeddings import create_embeddings
from vector_store import create_vector_store
from chatbot import create_qa_chain



pdf = "documents/notes.pdf"


documents = load_pdf(pdf)


chunks = split_documents(documents)


embeddings = create_embeddings()


db = create_vector_store(
    chunks,
    embeddings
)


qa = create_qa_chain(db)



question = "What are production rules?"


answer = qa.invoke(
    question
)


print(answer["result"])