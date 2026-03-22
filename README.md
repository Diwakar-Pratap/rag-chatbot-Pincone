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

Place your files inside:

```
data/documents/
```

Supported formats:

* `.txt`
* `.pdf`

---

### 6️⃣ Run Ingestion

```
python -m app.ingestion.ingest
```

This will:

* Load documents
* Split into chunks
* Generate embeddings
* Store in Pinecone

---

### 7️⃣ Run Backend Server

```
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

### 8️⃣ Run Frontend

Open:

```
frontend/index.html
```

---

## 💬 API Usage

### POST `/chat`

Request:

```
{
  "question": "What is RAG?"
}
```

Response:

```
{
  "answer": "RAG stands for Retrieval-Augmented Generation..."
}
```

---

## 🧠 Technologies Used

* **Python 3.11**
* **FastAPI**
* **LangChain**
* **Pinecone**
* **Sentence Transformers**
* **Uvicorn**
* **HTML + JavaScript**

---

## 🔥 Future Improvements

* 📌 Source citations (PDF page numbers)
* 💬 Conversation memory
* ⚡ Streaming responses
* 📤 File upload UI
* 🔍 Hybrid search (BM25 + vector)
* 🐳 Docker deployment
* ☁️ AWS deployment

---

## 📌 Key Learnings

* RAG pipeline design
* Vector similarity search
* Embedding generation
* FastAPI backend development
* Handling real-world data ingestion

---

## 🤝 Contributing

Feel free to fork this repo and improve the system.

---

## 📄 License

This project is open-source and available under the MIT License.
