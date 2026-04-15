from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# sample documents
documents = [
    "Artificial intelligence is transforming the world",
    "Machine learning models learn patterns from data",
    "Deep learning uses neural networks",
    "Bananas are yellow and rich in potassium",
    "Dogs are loyal animals"
]

# generate embeddings for documents
doc_embeddings = model.encode(documents)

# user query
query = input("Enter your search query: ")

# convert query to embedding
query_embedding = model.encode([query])

# compute cosine similarity
similarities = cosine_similarity(query_embedding, doc_embeddings)

# find best match
best_index = np.argmax(similarities)

print("\nBest match:")
print(documents[best_index])