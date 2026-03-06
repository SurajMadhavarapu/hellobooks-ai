from groq import Groq


def generate_answer(query: str, retrieved_chunks: list[dict], groq_client: Groq) -> str:
    """
    Send the query + retrieved context to Groq LLM and return the answer.
    """
    # Build context from retrieved chunks
    context_parts = []
    for i, chunk in enumerate(retrieved_chunks, 1):
        source = chunk["filename"].replace(".md", "").replace("_", " ").title()
        context_parts.append(f"[Source {i} - {source}]\n{chunk['content']}")

    context = "\n\n".join(context_parts)

    system_prompt = """You are Hellobooks AI, a helpful accounting assistant for small businesses.
You answer questions based only on the provided context from the Hellobooks knowledge base.
Be concise, clear, and friendly. If the context doesn't contain enough information, say so honestly.
Always structure your answers with clear points when explaining accounting concepts."""

    user_message = f"""Context from knowledge base:
{context}

User Question: {query}

Please answer the question based on the context above."""

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Fast and free on Groq
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.3,
        max_tokens=1024
    )

    return response.choices[0].message.content