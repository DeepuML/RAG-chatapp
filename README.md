# 📚 EURI RAG Chatbot

![EURI Banner](https://i.imgur.com/TPxNkkV.png)

An elegant, modern Retrieval-Augmented Generation (**RAG**) chatbot built using **Streamlit**, powered by **Euriai API** for both LLM completions and custom embeddings, with document similarity search via **FAISS**. It brings the power of generative AI to your own documents.

---

## 🌟 Key Features

✅ Upload and index multiple document types: **PDF, DOCX, TXT**
🔍 Smart retrieval with **custom embeddings** (Euriai)
🧠 Chat with your **own data** (Retrieval-QA chain)
💬 Elegant **Streamlit-based UI** with large fonts & animations
📜 **Chat history** saving and retrieval
⚡ Blazing fast **FAISS** vector indexing

---

## 🎥 Demo Preview

![Demo](https://media.giphy.com/media/xT5LMHxhOfscxPfIfm/giphy.gif)

---

## 🧠 Tech Stack

| Component           | Tool/Library           |
| ------------------- | ---------------------- |
| UI Framework        | Streamlit              |
| LLM & Embeddings    | Euriai API             |
| Vector Store        | FAISS                  |
| Document Parsing    | PyMuPDF, python-docx   |
| State Management    | Streamlit SessionState |
| Environment Secrets | Python-dotenv          |

---

## 📁 Folder Structure

```
├── app.py                # Main Streamlit app
├── faiss_index/          # Vector index directory
├── uploads/              # Uploaded documents
├── .env                  # API key securely stored here
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/euri-rag-chatbot.git
cd euri-rag-chatbot
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables

Create a `.env` file:

```bash
touch .env
```

Add your Euriai API key:

```env
EURI_API_KEY=your_actual_key_here
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

## 📂 Supported File Uploads

* ✅ `.pdf`
* ✅ `.docx`
* ✅ `.txt`

Uploaded documents will be automatically embedded and indexed via FAISS. You can upload files from the **left sidebar**.

---

## 🛡️ Security

* API key is **loaded securely** via `.env` (not hard-coded)
* `.env` is already in `.gitignore` to avoid GitHub leaks

---

## 🧱 How It Works

1. Upload documents (PDF, DOCX, TXT)
2. The app parses and chunks them
3. Each chunk is embedded using Euriai's embedding API
4. FAISS builds a vector index
5. You ask a question → relevant docs are retrieved → passed to LLM

![RAG Pipeline](https://i.imgur.com/GxF9sHa.png)

---

## 📈 Roadmap & Future Ideas

* 🧠 Conversational memory (contextual chat)
* 🔐 User authentication and access control
* 📤 Chat export (PDF, Markdown)
* ☁️ Streamlit Cloud or Hugging Face deployment
* 📊 Upload analytics dashboard

---

## 🤝 Contributing

Pull requests are welcome! If you want to add features or fix bugs, feel free to open an issue or submit a PR.

---

## 📝 License

MIT License © 2025 Deepu

---

## 📬 Contact

For feedback or collaboration, connect on  email at [yourname@example.com](mailto:mahakal123321@gmail.com)

---

> *Built with ❤️ and Euriai by Deepu*
