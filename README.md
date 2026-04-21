# 📄 Ask Your PDF — AI-Powered Document Q&A

An intelligent PDF question-answering app built using RAG (Retrieval-Augmented Generation). Upload any PDF and chat with it using AI.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-latest-green)
![Streamlit](https://img.shields.io/badge/Streamlit-latest-red)

---

## 🚀 Live Demo
[Click here to try the app](https://your-app-link.streamlit.app)

---

## 💡 What It Does
- Upload any PDF document
- Ask questions about it in natural language
- Get intelligent, accurate answers powered by LLaMA 3.1
- Full chat history with conversation memory
- Works on resumes, invoices, reports, textbooks — any PDF!

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| LangChain | AI pipeline orchestration |
| ChromaDB | Vector database for document storage |
| HuggingFace Embeddings | Converting text to vectors |
| Groq + LLaMA 3.1 | LLM for generating answers |
| Streamlit | Web application interface |
| Python | Core programming language |

---

## 🧠 How It Works

1. PDF is uploaded and loaded
2. Document is split into small chunks
3. Each chunk is converted to embeddings (vectors)
4. Vectors are stored in ChromaDB
5. User asks a question
6. Most relevant chunks are retrieved
7. LLaMA 3.1 reads chunks and generates a real answer

This is the core architecture behind enterprise AI document systems like ChatPDF, Adobe AI Assistant, and similar tools.

---

## ⚙️ Installation & Setup

### 1. Clone the repository
git clone https://github.com/rubaharmaien/AI-powered-PDF-Q-A-app-using-RAG.git
cd AI-powered-PDF-Q-A-app-using-RAG

### 2. Install dependencies
pip install -r requirements.txt

### 3. Set up your API key
Create a .env file in the project folder:
GROQ_API_KEY=your_groq_api_key_here

Get your free API key at console.groq.com

### 4. Run the app
streamlit run app.py

---

## 📁 Project Structure

RAG-PDF-App/
├── app.py              # Main application
├── requirements.txt    # Dependencies
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation

---

## 🙋 About

Built by Harmaien Ruba — Final Year ECE Student at HKBK College of Engineering (VTU).

Connect with me on LinkedIn: https://linkedin.com/in/harmaien-ruba-31551232a

---

## 📌 Key Concepts Learned

- RAG (Retrieval-Augmented Generation) architecture
- Vector embeddings and semantic search
- LangChain pipeline building
- ChromaDB vector database
- LLM integration via Groq API
- Streamlit deployment
