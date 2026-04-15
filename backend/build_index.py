from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

news_articles = [
    "The government has introduced new AI regulations to ensure safety and transparency.",
    "Scientists discover a new method to slow down climate change effects.",
    "Tech companies are investing heavily in artificial intelligence and machine learning.",
    "A new space mission aims to explore Mars and search for signs of life.",
    "Healthcare advances using AI are improving early disease detection."
]

# generate embeddings
embeddings = model.encode(news_articles)

# save embeddings
np.save("news_embeddings.npy", embeddings)

# save articles
np.save("news_articles.npy", news_articles)

print("Embeddings saved successfully!")