import os
from dotenv import load_dotenv
from groq import Groq

from rag.loader import load_documents, chunk_documents
from rag.embedder import build_faiss_index
from rag.retriever import retrieve
from rag.generator import generate_answer

load_dotenv()

def main():
    print("=" * 50)
    print("   Hellobooks AI - Accounting Assistant")
    print("=" * 50)

    # 1. Load and chunk documents
    knowledge_base_dir = os.path.join(os.path.dirname(__file__), "knowledge_base")
    documents = load_documents(knowledge_base_dir)
    chunks = chunk_documents(documents, chunk_size=500, overlap=50)

    # 2. Build FAISS index
    index, chunks, embedding_model = build_faiss_index(chunks)

    # 3. Initialize Groq client
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError(" GROQ_API_KEY not found. Please set it in your .env file.")
    groq_client = Groq(api_key=api_key)

    print("\n System ready! Ask me anything about accounting.")
    print("   Type 'exit' or 'quit' to stop.\n")

    # 4. Q&A Loop
    while True:
        query = input("You: ").strip()

        if not query:
            continue
        if query.lower() in ("exit", "quit"):
            print(" Goodbye! Keep your books balanced!")
            break

        # Retrieve relevant chunks
        retrieved = retrieve(query, index, chunks, embedding_model, top_k=3)

        # Generate answer
        print("\n Hellobooks AI: ", end="", flush=True)
        answer = generate_answer(query, retrieved, groq_client)
        print(answer)

        # Show sources
        sources = list(set(c["filename"].replace(".md", "").replace("_", " ").title() for c in retrieved))
        print(f"\n Sources: {', '.join(sources)}")
        print("-" * 50)


if __name__ == "__main__":
    main()