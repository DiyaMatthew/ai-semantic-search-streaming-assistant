import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

# load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# load dataset
df = pd.read_csv("news_data.csv")

# clean text
df["title"] = df["title"].str.strip()

# remove empty rows
df = df.dropna()

# get text data
documents = df["title"].tolist()

# generate embeddings
embeddings = model.encode(documents)

# save
np.save("news_embeddings.npy", embeddings)
np.save("news_articles.npy", documents)

print("Embeddings built from CSV successfully!")