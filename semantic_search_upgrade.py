from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Artificial intelligence is transforming the world",
    "Machine learning models learn patterns from data",
    "Deep learning uses neural networks",
    "Bananas are yellow and rich in potassium",
    "Dogs are loyal animals"
]

# create embeddings
doc_embeddings = model.encode(documents)

query = input("Enter your search query: ")

query_embedding = model.encode([query])

similarities = cosine_similarity(query_embedding, doc_embeddings)[0]

# get top 3 results
top_indices = np.argsort(similarities)[::-1][:3]

print("\nTop matches:\n")

for idx in top_indices:
    print(f"{documents[idx]}  (score: {similarities[idx]:.3f})")