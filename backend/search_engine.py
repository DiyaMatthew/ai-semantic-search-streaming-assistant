from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

# load saved data
news_articles = np.load("news_articles.npy", allow_pickle=True)
news_embeddings = np.load("news_embeddings.npy")

query = input("Enter your search query: ")

query_embedding = model.encode([query])

similarities = cosine_similarity(query_embedding, news_embeddings)[0]

top_indices = similarities.argsort()[::-1][:3]

print("\nTop results:\n")

for idx in top_indices:
    print(f"{news_articles[idx]} (score: {similarities[idx]:.3f})")