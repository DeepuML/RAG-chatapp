**# 📚 EURI RAG Chatbot

An advanced Retrieval-Augmented Generation (RAG) chatbot built with **Streamlit**, powered by **Euriai API** for both LLM responses and embeddings, and backed by **FAISS** vector search.

This app allows:
- 📂 Uploading multiple documents (`PDF`, `DOCX`, `TXT`)
- 🔍 Indexing documents with custom embeddings
- 🤖 Chatting with your own knowledge base
- 💬 Storing chat history
- ✨ Clean, modern Streamlit interface

---

## 🧠 Tech Stack

- **Frontend:** Streamlit
- **LLM & Embeddings:** [Euriai](https://euriai.ai)
- **Vector Search:** FAISS
- **File Parsing:** PyMuPDF, python-docx
- **Environment Management:** `dotenv`

---

## 📂 Features

- 🗂️ **Multiple Document Upload**: PDF, DOCX, TXT supported
- 📇 **FAISS Vector Indexing**
- 🧠 **Euriai GPT-4.1-Nano** LLM integration
- 💬 **Chat with Knowledge Base**
- 💾 **Chat History Storage**
- 🎨 **Prettified UI with larger fonts and styled components**

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/your-username/euri-rag-chatbot.git
cd euri-rag-chatbot
**

2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Set Up .env
Create a .env file:

bash
Copy
Edit
touch .env
And add your Euriai API key:

env
Copy
Edit
EURI_API_KEY=your_actual_key_here
Important: .env is already added to .gitignore.

4. Run the App
bash
Copy
Edit
streamlit run app.py
📎 File Upload Formats
You can upload: .pdf , .docx, .txt

Uploaded documents will be parsed, embedded, indexed, and made available for chat.

🛡️ Security

API key is securely loaded from environment using dotenv.

.env file is excluded from Git.

📈 Future Features (Optional Ideas)


🧠 Conversational memory (history-aware answers)

🔐 User login and session-based history

📤 Export chat history

☁️ Deploy to Streamlit Cloud / Hugging Face Spaces

🤝 Contributions
PRs welcome! Please open issues first for major feature changes.

📝 License
MIT License © 2025 Deepu
