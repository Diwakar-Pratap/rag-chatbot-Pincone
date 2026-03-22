from app.db.pinecone_db import index
from app.rag.embedder import embed_text

def retrieve_docs(query):

    query_vector = embed_text(query)

    results = index.query(
        vector=query_vector,
        top_k=3,
        include_metadata=True
    )

    docs = [match["metadata"]["text"] for match in results["matches"]]

    return docs