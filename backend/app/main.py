"""
Real-Time AI Semantic Search Assistant Backend

Features:
- Streaming via SSE
- Semantic search using SentenceTransformers
- Session-based memory
- FastAPI async backend
"""

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
import asyncio
import numpy as np
import logging

# Semantic search imports
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------
# App Setup
# -------------------------
app = FastAPI()
chat_memory = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Logging
# -------------------------
logging.basicConfig(
    filename="backend/logs/search_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# -------------------------
# Load AI Model (Free)
# -------------------------
search_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load precomputed embeddings and articles
news_articles = np.load("data/news_articles.npy", allow_pickle=True)
news_embeddings = np.load("data/news_embeddings.npy")

# -------------------------
# Smart AI Response (FREE AI)
# -------------------------
async def smart_stream_response(message, history):
    # Thinking effect
    yield "🤔 Thinking... "
    await asyncio.sleep(0.5)

    message_lower = message.lower()

    if "hello" in message_lower:
        response = "Hello! How can I assist you today?"

    elif "ai" in message_lower or "news" in message_lower or "what" in message_lower:
        query_embedding = search_model.encode(message)
        similarities = cosine_similarity([query_embedding], news_embeddings)[0]

        top_idx = similarities.argmax()
        context = news_articles[top_idx]

        response = f"🧠 Based on my knowledge: {context}"

    else:
        response = f"I understand you said: '{message}'. Let me help you with that."

    for word in response.split():
        yield word + " "
        await asyncio.sleep(0.05)
# -------------------------
# Streaming Endpoint (SSE)
# -------------------------
@app.get("/stream")
async def stream(message: str, session_id: str):

    history = chat_memory.get(session_id, [])

    async def event_generator():
        full_response = ""

        async for token in smart_stream_response(message, history):
            full_response += token
            yield {"data": token}

        # Save conversation
        chat_memory.setdefault(session_id, []).append({
            "role": "user",
            "content": message
        })

        chat_memory[session_id].append({
            "role": "assistant",
            "content": full_response
        })

    return EventSourceResponse(event_generator())


# -------------------------
# Health Check
# -------------------------
@app.get("/")
def root():
    return {"status": "AI Streaming Backend Running 🚀"}