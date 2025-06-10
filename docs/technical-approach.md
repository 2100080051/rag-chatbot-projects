# Technical Approach: Altibbe RAG Chatbot

## 🎯 Objective

To develop a domain-specific chatbot for the health-tech field using Retrieval-Augmented Generation (RAG) architecture with local execution (no OpenAI or external APIs).

---

## 🧠 Architecture Overview

### 1. Document Embedding & Vector Store

- Uses `sentence-transformers/paraphrase-MiniLM-L3-v2` to convert documents into dense vectors
- Stores vectors in FAISS index
- Saves vector store as `faiss_store.pkl` for fast retrieval

### 2. Retrieval + Generation Pipeline

- At runtime, a user question is embedded
- FAISS retrieves top-k most relevant document chunks
- A prompt is constructed with context + question
- The prompt is passed to a **local Hugging Face model** (`google/flan-t5-small`)
- The model generates a response using only retrieved context

### 3. Orchestration via n8n

- n8n receives question via webhook
- Runs Python script via Execute Command node
- Response is passed to Webhook Response node

---

## ⚙️ Technologies Used

| Component         | Tool                                |
|------------------|-------------------------------------|
| Embedding         | `sentence-transformers`             |
| Retrieval         | `faiss-cpu`                         |
| LLM (local)       | `transformers` (`flan-t5-small`)    |
| Workflow          | `n8n` (Webhook, Execute Command)    |
| Language          | Python                              |

---

## ✅ Benefits of This Approach

- 💻 Fully offline and local: no OpenAI key needed
- 🔐 Data privacy preserved
- 💬 Domain-specific accuracy via document-grounded answers
- ♻️ Reusable and modular pipeline

---

## 🧪 Example Flow

User sends:

```json
{ "question": "What is Altibbe?" }
```

FAISS retrieves matching chunks → prompt is built → `flan-t5-small` generates:

```
"Altibbe empowers ethical AI development..."
```

Returned via webhook.

---

## 📌 Notes for Evaluation

- No external dependencies at runtime
- Hugging Face model downloaded via `snapshot_download`
- Workflow works end-to-end via `curl`, `Postman`, or `n8n` UI