# 🚀 Real-Time AI Semantic Search Assistant

## ❗ Problem Statement

Traditional chatbots struggle with real-time responses and contextual understanding when working with custom datasets.

This project solves that by building a lightweight Retrieval-Augmented AI system that:

* Retrieves relevant context using semantic search
* Streams responses in real-time (like ChatGPT)
* Maintains session-based conversational memory

## 🧠 What This Project Demonstrates

This project simulates a production-style AI system:

* Retrieval-based AI (RAG prototype)
* Real-time streaming responses (SSE)
* Session-based conversational memory
* Async backend architecture

Note: Uses a small curated dataset to demonstrate system design rather than scale.

## 💡 Overview

This project is a real-time AI system that simulates a production-ready assistant using:

* Semantic Search (SentenceTransformers)
* Streaming responses (Server-Sent Events)
* Session-based memory
* FastAPI backend + JS frontend

---

## ⚡ Key Features

* 🔄 Real-time streaming (SSE)
* 🧠 Context-aware responses (semantic search)
* 💾 Session memory using session_id
* ⚙️ Async FastAPI backend
* 💬 ChatGPT-style UI

---

## 🏗️ Architecture

Frontend (JS)
→ EventSource (SSE)
→ FastAPI Backend
→ Semantic Search
→ Stream response back

---
Designed with scalability in mind (can be extended with vector DBs like FAISS or Pinecone).

## 🧪 Tech Stack

* FastAPI
* JavaScript
* SentenceTransformers
* NumPy
* SSE (EventSource)

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open frontend:

```
frontend/index.html
```

---

## 📸 Demo

<img width="1683" height="682" alt="Screenshot 2026-04-15 at 09 56 58" src="https://github.com/user-attachments/assets/9bbbd9c3-7a8d-4a97-a7fe-7815771176f2" />
<img width="1686" height="683" alt="Screenshot 2026-04-15 at 09 57 13" src="https://github.com/user-attachments/assets/4bbb04af-06d0-48eb-9805-7aaae457c0df" />



---

## 📈 Future Improvements

* OpenAI integration
* Redis memory
* Authentication
* Multi-user scaling

---
## 💡 Why This Project Stands Out

* Built without relying on paid APIs (fully local AI pipeline)
* Implements real-time streaming using Server-Sent Events (SSE)
* Demonstrates core concepts of production AI systems (RAG, memory, async backend)
* Designed to be easily extended with vector databases like FAISS or Pinecone

## 👨‍💻 Author

Diya Mathew
