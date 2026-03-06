import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Using a lightweight, fast embedding model
MODEL_NAME = "all-MiniLM-L6-v2"

def build_faiss_index(chunks: list[dict]) -> tuple[faiss.Index, list[dict], SentenceTransformer]:
    """
    Generate embeddings for all chunks and store them in a FAISS index.
    Returns the FAISS index, chunks list, and the embedding model.
    """
    print(f"⚙️  Loading embedding model: {MODEL_NAME} ...")
    model = SentenceTransformer(MODEL_NAME)

    texts = [chunk["content"] for chunk in chunks]

    print("⚙️  Generating embeddings ...")
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

    # Normalize for cosine similarity
    faiss.normalize_L2(embeddings)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)  # Inner product = cosine similarity after normalization
    index.add(embeddings)

    print(f"✅ FAISS index built with {index.ntotal} vectors (dim={dimension}).")
    return index, chunks, model