from sentence_transformers import SentenceTransformer

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I love artificial intelligence",
    "AI is amazing",
    "Bananas are yellow"
]

# create embeddings
embeddings = model.encode(sentences)

for i, sentence in enumerate(sentences):
    print("Sentence:", sentence)
    print("Embedding vector:", embeddings[i])
    print()