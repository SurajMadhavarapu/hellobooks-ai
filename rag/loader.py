import os

def load_documents(knowledge_base_dir: str) -> list[dict]:
    """
    Load all .md files from the knowledge base directory.
    Returns a list of dicts with 'filename' and 'content'.
    """
    documents = []
    for filename in sorted(os.listdir(knowledge_base_dir)):
        if filename.endswith(".md"):
            filepath = os.path.join(knowledge_base_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            documents.append({
                "filename": filename,
                "content": content
            })
    print(f"✅ Loaded {len(documents)} documents from knowledge base.")
    return documents


def chunk_documents(documents: list[dict], chunk_size: int = 500, overlap: int = 50) -> list[dict]:
    """
    Split documents into smaller overlapping chunks for better retrieval.
    """
    chunks = []
    for doc in documents:
        content = doc["content"]
        words = content.split()
        start = 0
        chunk_index = 0

        while start < len(words):
            end = start + chunk_size
            chunk_text = " ".join(words[start:end])
            chunks.append({
                "chunk_id": f"{doc['filename']}_chunk_{chunk_index}",
                "filename": doc["filename"],
                "content": chunk_text
            })
            start += chunk_size - overlap
            chunk_index += 1

    print(f"✅ Created {len(chunks)} chunks from {len(documents)} documents.")
    return chunks