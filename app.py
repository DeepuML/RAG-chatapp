import os
import streamlit as st
import requests
import numpy as np
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from euriai import EuriaiLangChainLLM
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader
import tempfile
import fitz  # PyMuPDF
from docx import Document as DocxDocument

# --------------------
# 🎨 Streamlit UI Config
# --------------------
st.set_page_config(
    page_title="📚 EURI RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stTextInput>div>div>input {
            font-size: 18px;
        }
        .stButton>button {
            background-color: #4B8BBE;
            color: white;
            font-size: 18px;
            padding: 0.6em 2em;
            border-radius: 10px;
        }
        .stMarkdown h1 {
            text-align: center;
            color: #4B8BBE;
            font-size: 45px;
        }
        .chat-bubble {
            background-color: #f5f5f5;
            border-radius: 12px;
            padding: 12px 18px;
            margin: 10px 0;
            font-size: 17px;
        }
        .user {
            background-color: #e0f7fa;
        }
        .bot {
            background-color: #ede7f6;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📚 EURI RAG Chatbot")
st.caption("Upload documents and ask questions using Euriai & FAISS")

# --------------------
# 🔐 Load API Key
# --------------------
load_dotenv()
euri_api_key = os.getenv("EURI_API_KEY")

if not euri_api_key:
    st.error("❌ Please set your EURI_API_KEY in the .env file.")
    st.stop()

# --------------------
# 🧠 Embedding Function
# --------------------
def generate_embeddings(text: str):
    url = "https://api.euron.one/api/v1/euri/alpha/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {euri_api_key}"
    }
    payload = {
        "input": text,
        "model": "text-embedding-3-small"
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return np.array(response.json()['data'][0]['embedding'])

# --------------------
# 📄 Text Splitter
# --------------------
def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    return splitter.create_documents([text])

# --------------------
# 📄 File Text Extractor
# --------------------
def extract_text_from_file(file):
    text = ""
    if file.name.endswith(".txt"):
        text = file.read().decode("utf-8")
    elif file.name.endswith(".pdf"):
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
    elif file.name.endswith(".docx"):
        doc = DocxDocument(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text

# --------------------
# 📄 Multi-file Upload & Indexing (Sidebar)
# --------------------
st.sidebar.header("📂 Document Upload")
uploaded_files = st.sidebar.file_uploader(
    "Upload `.txt`, `.pdf`, or `.docx` files", type=["txt", "pdf", "docx"], accept_multiple_files=True
)

all_docs = []

if uploaded_files:
    with st.sidebar:
        with st.spinner("Indexing uploaded files..."):
            for file in uploaded_files:
                file_text = extract_text_from_file(file)
                docs = split_text(file_text)
                all_docs.extend(docs)

            if all_docs:
                st.session_state.vector_store = FAISS.from_documents(
                    documents=all_docs,
                    embedding=generate_embeddings
                )
                st.session_state.vector_store.save_local("faiss_index")
                st.sidebar.success("✅ Documents indexed!")

# --------------------
# Load or create vector store
# --------------------
if "vector_store" not in st.session_state:
    try:
        st.session_state.vector_store = FAISS.load_local(
            "faiss_index", generate_embeddings, allow_dangerous_deserialization=True
        )
    except:
        st.warning("⚠️ No index found. Please upload a document first.")
        st.stop()

# --------------------
# 🔍 RAG Chain Setup
# --------------------
retriever = st.session_state.vector_store.as_retriever(search_kwargs={"k": 3})
llm = EuriaiLangChainLLM(
    api_key=euri_api_key,
    model="gpt-4.1-nano",
    temperature=0.3,
    max_tokens=300
)
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=False
)

# --------------------
# 💬 Chat Interface
# --------------------
query = st.text_input("💬 Ask a question", placeholder="e.g., What is this document about?")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("🧠 Generate Answer") and query.strip():
    with st.spinner("Thinking..."):
        result = rag_chain.invoke(query)
        st.session_state.chat_history.append(("You", query))
        st.session_state.chat_history.append(("Bot", result["result"]))
        st.success("Answer ready!")

# --------------------
# 📝 Chat History Display
# --------------------
for speaker, message in st.session_state.chat_history:
    with st.chat_message("user" if speaker == "You" else "assistant"):
        st.markdown(message)
        st.markdown(f'<div class="chat-bubble {"user" if speaker == "You" else "bot"}">{message}</div>', unsafe_allow_html=True)
# --------------------