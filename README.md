# 🤖 RAG Chatbot with FastAPI + Pinecone

A **Retrieval-Augmented Generation (RAG)** based AI chatbot that answers questions using custom documents (PDF/TXT) by combining:

* Vector embeddings
* Pinecone vector database
* FastAPI backend
* Lightweight frontend UI

---

## 🚀 Features

* 📂 **Multi-document ingestion** (PDF + TXT)
* 🧠 **Semantic search using embeddings**
* ⚡ **FastAPI backend for chat API**
* 🌐 **Simple frontend UI (HTML + JS)**
* ☁️ **Pinecone vector database integration**
* 🆓 **Local embeddings (Sentence Transformers)**
* 🔁 **Scalable RAG pipeline**

---

## 🏗️ Architecture

```
Documents (PDF/TXT)
        ↓
Text Chunking
        ↓
Embeddings (MiniLM)
        ↓
Pinecone Vector DB
        ↓
User Query
        ↓
Similarity Search
        ↓
LLM Response
```

---

## 📁 Project Structure

```
rag-chatbot/
│
├── app/
│   ├── main.py              # FastAPI app
│   ├── rag_pipeline.py      # Retrieval + LLM logic
│   ├── config.py            # Environment config
│   └── ingestion/
│       └── ingest.py        # Document ingestion
│
├── data/
│   └── documents/           # Your PDFs / TXT files
│
├── frontend/
│   └── index.html           # Simple UI
│
├── .env                     # API keys
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone <your-repo-url>
cd rag-chatbot
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv .venv
.venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create `.env` file:

```
PINECONE_API_KEY=your_pinecone_key
PINECONE_INDEX_NAME=rag-chatbot
OPENAI_API_KEY=your_openai_key   # optional
```

---

### 5️⃣ Add Documents

Place your fil
