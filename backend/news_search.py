from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

news_articles = [
    "The government has introduced new AI regulations to ensure safety and transparency.",
    "Scientists discover a new method to slow down climate change effects.",
    "Tech companies are investing heavily in artificial intelligence and machine learning.",
    "A new space mission aims to explore Mars and search for signs of life.",
    "Healthcare advances using AI are improving early disease detection."
]

news_embeddings = model.encode(news_articles)

query = input("Enter your news topic: ")
query_embedding = model.encode([query])

similarities = cosine_similarity(query_embedding, news_embeddings)[0]

top_indices = np.argsort(similarities)[::-1][:3]

print("\nTop News Results:\n")

for idx in top_indices:
    print(f"{news_articles[idx]} (score: {similarities[idx]:.3f})")