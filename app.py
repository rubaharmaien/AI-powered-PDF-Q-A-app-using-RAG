import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
import tempfile
import os
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")


# --- Page Config ---
st.set_page_config(page_title="Ask Your PDF", page_icon="📄", layout="centered")

st.markdown("""
    <style>
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .user-msg {
        background-color: #1e3a5f;
        color: white;
    }
    .bot-msg {
        background-color: #1e2a1e;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📄 Ask Your PDF")
st.caption("Upload any PDF and chat with it using AI")

# --- Session State ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "db" not in st.session_state:
    st.session_state.db = None

# --- File Upload ---
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file and st.session_state.db is None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        f.write(uploaded_file.read())
        temp_path = f.name

    with st.spinner("📖 Reading and understanding your PDF..."):
        loader = PyPDFLoader(temp_path)
        pages = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        chunks = splitter.split_documents(pages)
        embeddings = HuggingFaceEmbeddings()
        st.session_state.db = Chroma.from_documents(chunks, embeddings)

    st.success("✅ PDF ready! Start asking questions below.")

# --- Chat Interface ---
if st.session_state.db:

    # Show chat history
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"""
                <div class='chat-message user-msg'>
                🧑 <b>You:</b> {msg['content']}
                </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class='chat-message bot-msg'>
                🤖 <b>AI:</b> {msg['content']}
                </div>""", unsafe_allow_html=True)

    # Question input
    question = st.chat_input("Ask anything about your PDF...")

    if question:
        st.session_state.chat_history.append({
            "role": "user",
            "content": question
        })

        with st.spinner("🤔 Thinking..."):
            llm = ChatGroq(
                api_key=GROQ_API_KEY,
                model_name="llama-3.1-8b-instant"
            )

            docs = st.session_state.db.similarity_search(question, k=10)
            context = "\n".join([d.page_content for d in docs])

            prompt = f"""You are a helpful AI assistant. Answer the question based on the context below.
Be thorough and complete. Include ALL sections and details you find. Do not summarize briefly.
If the answer is not in the context, say "I couldn't find that in the document."

Context:
{context}

Question: {question}

Answer:"""

            response = llm.invoke(prompt)
            answer = response.content

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": answer
        })

        st.rerun()

    # Clear chat button
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.session_state.db = None
        st.rerun()