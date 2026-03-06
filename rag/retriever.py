import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


def retrieve(
    query: str,
    index: faiss.Index,
    chunks: list[dict],
    model: SentenceTransformer,
    top_k: int = 3
) -> list[dict]:
    """
    Embed the user query, search FAISS index, return top_k matching chunks.
    """
    query_embedding = model.encode([query], convert_to_numpy=True)
    faiss.normalize_L2(query_embedding)

    scores, indices = index.search(query_embedding, top_k)

    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx < len(chunks):
            results.append({
                "content": chunks[idx]["content"],
                "filename": chunks[idx]["filename"],
                "score": float(score)
            })

    return results