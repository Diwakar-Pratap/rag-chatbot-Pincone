from pinecone import Pinecone, ServerlessSpec
from app.config import PINECONE_API_KEY, PINECONE_INDEX

pc = Pinecone(api_key=PINECONE_API_KEY)

# create index if it doesn't exist
existing_indexes = [i["name"] for i in pc.list_indexes()]

if PINECONE_INDEX not in existing_indexes:
    pc.create_index(
        name=PINECONE_INDEX,
        dimension=384,   # embedding dimension
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

index = pc.Index(PINECONE_INDEX)