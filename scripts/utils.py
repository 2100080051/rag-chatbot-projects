from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import json

pkl_path = "C:\\Users\\nabhi\\Downloads\\rag-chatbot-project\\faiss_store.pkl"

with open("C:/Users/nabhi/Downloads/rag-chatbot-project/faiss_store.pkl", "rb") as f:

    store = pickle.load(f)

# Load embedding model
model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L3-v2")

# Absolute path to the faiss_store.pkl file in project root


with open(pkl_path, "rb") as f:
    store = pickle.load(f)

index = store["index"]
documents = store["documents"]

def search(query, top_k=3):
    query_embedding = model.encode(query)
    query_embedding = np.array([query_embedding])
    distances, indices = index.search(query_embedding, top_k)
    return [documents[i] for i in indices[0]]

# Load local Hugging Face model
model_path = "C:/Users/nabhi/Downloads/rag-chatbot-project/local_models/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_path)
llm = AutoModelForSeq2SeqLM.from_pretrained(model_path)

def generate_answer(user_query):
    context_chunks = search(user_query)
    context = "\n".join(context_chunks)
    prompt = f"Answer the question using the context below:\n\nContext:\n{context}\n\nQuestion: {user_query}"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = llm.generate(**inputs, max_new_tokens=200)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer.strip()

if __name__ == "__main__":
    question = "What is Altibbe's goal?"
    answer = generate_answer(question)
    print(json.dumps({"answer": answer}))