from sentence_transformers import SentenceTransformer
import faiss
import os
import numpy as np
import pickle


model = SentenceTransformer("all-MiniLM-L6-v2")
docs_path = "C:\\Users\\nabhi\\Downloads\\rag-chatbot-project\\data\\sample-documents"
documents = []
embeddings = []

for file_name in os.listdir(docs_path):
    with open(os.path.join(docs_path, file_name), 'r', encoding='utf-8') as f:
        content = f.read()
        chunks = content.split(". ")
        for chunk in chunks:
            chunk = chunk.strip()
            if chunk:
                documents.append(chunk)
                embedding = model.encode(chunk)
                embeddings.append(embedding)
dimension = len(embeddings[0])
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))
with open(os.path.join(os.path.dirname(__file__), "faiss_store.pkl"), "wb") as f:
    pickle.dump({"index": index, "documents": documents, "embeddings": embeddings}, f)

print("✅ FAISS index created and saved.")
