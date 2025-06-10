# Altibbe RAG Chatbot

This is a Retrieval-Augmented Generation (RAG) based chatbot designed to answer health-tech-related questions. It uses:

- FAISS for similarity search
- Sentence Transformers for vector embeddings
- A local Hugging Face model (`flan-t5-small`) for generating responses
- n8n as a no-code orchestrator to expose the chatbot via webhook

---

## ✅ Setup Instructions

### 1. Project Folder Structure

```
rag-chatbot-project/
├── scripts/
│   └── utils.py
├── faiss_store.pkl
├── local_models/
│   └── flan-t5-small/   ← Downloaded Hugging Face model
├── rag-chatbot-workflow.json
├── requirements.txt
├── README.md
├── technical-approach.md
```

---

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

---

### 3. Setup n8n

- Open [n8n](https://n8n.io/)
- Import `rag-chatbot-workflow.json`
- Activate the workflow

---

### 4. Test the Chatbot

Send a POST request:

```bash
curl -X POST http://localhost:5678/webhook/rag-chatbot   -H "Content-Type: application/json"   -d "{"question":"What is Altibbe?"}"
```

Expected Response:

```json
{
  "answer": "Altibbe empowers ethical AI development..."
}
```

---

## 💡 Notes

- All models are loaded locally — no external API calls
- Compatible with Windows (Python 3.9+, no GPU required)
- Designed for reproducibility and offline evaluation