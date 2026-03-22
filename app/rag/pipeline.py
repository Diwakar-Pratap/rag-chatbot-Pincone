from app.rag.retriever import retrieve_docs
from app.llm.nvidia_client import generate_response

def rag_chat(query):

    docs = retrieve_docs(query)

    context = "\n".join(docs)

    messages = [
        {
            "role": "system",
            "content": "Answer based on the provided context."
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion:{query}"
        }
    ]

    return generate_response(messages)