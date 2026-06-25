# PDF AI Assistant

A RAG-based PDF question answering application that allows users to upload a PDF and ask questions about its content.

## Project Description

I built this project to create an AI assistant that can understand PDF documents and answer questions based only on the uploaded document context.

The application uses Retrieval Augmented Generation (RAG). It extracts text from PDFs, converts the text into embeddings, stores them in a vector database, retrieves relevant information, and generates answers using an LLM.

## Features

- Upload PDF documents
- Extract and process PDF text
- Split documents into smaller chunks
- Create text embeddings
- Store embeddings using FAISS vector database
- Ask questions about the PDF
- Generate answers using Groq LLM
- Display source pages from the PDF

## Technologies Used

- Python
- Gradio (User Interface)
- LangChain (RAG pipeline)
- FAISS (Vector Database)
- Hugging Face Embeddings
- Groq API (LLM)
- PyPDFLoader (PDF processing)

## Project Structure
