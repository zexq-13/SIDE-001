from langchain.vectorstores import Chroma
from langchain.vectorstores import FAISS

def chroma_db(docs,embeddings):
    db= Chroma.from_documents(docs, embeddings)
    return db

def faiss_db(docs,embeddings):
    db = FAISS.from_documents(docs, embeddings)
    return db



