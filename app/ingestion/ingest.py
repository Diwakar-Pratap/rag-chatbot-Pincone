from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from pathlib import Path
from app.config import PINECONE_API_KEY, PINECONE_INDEX

# 🔹 Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# 🔹 Create index if not exists
if PINECONE_INDEX not in pc.list_indexes().names():
    pc.create_index(
        name=PINECONE_INDEX,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(PINECONE_INDEX)

# 🔹 Correct data path
data_path = Path(__file__).resolve().parent.parent.parent / "data" / "documents"
print("DATA PATH:", data_path)
print("Exists:", data_path.exists())

# 🔹 Load TXT files
text_loader = DirectoryLoader(
    str(data_path),
    glob="**/*.txt",
    loader_cls=TextLoader
)

# 🔹 Load PDF files
pdf_loader = DirectoryLoader(
    str(data_path),
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)

documents = text_loader.load() + pdf_loader.load()

print(f"Loaded {len(documents)} documents")

# 🔹 Split documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

texts = text_splitter.split_documents(documents)

print(f"Split into {len(texts)} chunks")

# 🔹 Embeddings (LOCAL)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 🔹 Store in Pinecone
vector_store = PineconeVectorStore.from_documents(
    texts,
    embeddings,
    index_name=PINECONE_INDEX
)

print(f"✅ {len(texts)} chunks uploaded to Pinecone!")