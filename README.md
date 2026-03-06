#  Hellobooks AI — Accounting Assistant

An AI-powered bookkeeping assistant built with RAG (Retrieval-Augmented Generation).
Ask any accounting question and get accurate answers from a curated knowledge base.

---

##  How It Works
```
User Question → FAISS Retrieval → Groq LLM → Answer
```

1. Knowledge base documents are loaded and chunked
2. Chunks are embedded using Sentence Transformers
3. User question is embedded and matched against FAISS index
4. Top matching chunks are sent as context to Groq LLM
5. Groq generates a accurate, context-aware answer

---

##  Project Structure
```
hellobooks-ai/
├── knowledge_base/
│   ├── bookkeeping.md
│   ├── invoices.md
│   ├── profit_and_loss.md
│   ├── balance_sheet.md
│   └── cash_flow.md
├── rag/
│   ├── __init__.py
│   ├── loader.py       ← Loads & chunks documents
│   ├── embedder.py     ← Generates embeddings + builds FAISS index
│   ├── retriever.py    ← Retrieves relevant chunks
│   └── generator.py   ← Sends context to Groq LLM
├── main.py             ← Entry point
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

---

##  Tech Stack

| Component        | Tool                          |
|-----------------|-------------------------------|
| Language         | Python 3.11                   |
| LLM              | Groq API (llama3-8b-8192)     |
| Embeddings       | Sentence Transformers (MiniLM)|
| Vector Store     | FAISS                         |
| Containerization | Docker                        |

---

##  Setup & Run

### Option 1: Run Locally

**Step 1 — Clone the repository**
```bash
git clone https://github.com/your-username/hellobooks-ai.git
cd hellobooks-ai
```

**Step 2 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 3 — Add your Groq API key**

Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```
>  Get your free API key at https://console.groq.com

**Step 4 — Run the assistant**
```bash
python main.py
```

---

### Option 2: Run with Docker

**Step 1 — Build the image**
```bash
docker build -t hellobooks-ai .
```

**Step 2 — Run the container**
```bash
docker run -it -e GROQ_API_KEY=your_groq_api_key_here hellobooks-ai
```

---

##  Example Usage
```
========================================
   Hellobooks AI - Accounting Assistant
========================================
 Loaded 5 documents from knowledge base.
 Created 20 chunks from 5 documents.
 FAISS index built with 20 vectors.
 System ready! Ask me anything about accounting.

You: What is a balance sheet?

 Hellobooks AI: A balance sheet is a financial statement that provides
a snapshot of a company's financial position at a specific point in time.
It shows what the company owns (assets), what it owes (liabilities),
and the owner's equity. The fundamental equation is:
Assets = Liabilities + Equity

 Sources: Balance Sheet
--------------------------------------------------

You: How do I calculate gross profit?

 Hellobooks AI: Gross Profit = Revenue – Cost of Goods Sold (COGS).
It indicates profitability before operating expenses are deducted.

 Sources: Profit And Loss
--------------------------------------------------

You: exit
 Goodbye! Keep your books balanced!
```

---

##  Requirements

- Python 3.11+
- Groq API key (free at https://console.groq.com)
- Docker (optional, for containerized run)

---

##  Author

Built as part of the Hellobooks AI Internship Assignment.