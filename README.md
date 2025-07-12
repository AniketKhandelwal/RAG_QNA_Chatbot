
# 🧠 RAG QnA Chatbot for Loan Data Analysis

A **Retrieval-Augmented Generation (RAG)** chatbot built to answer natural language questions on tabular **loan application data** using document retrieval + LLM-based answer generation.

> This project allows domain-specific question-answering from structured tabular datasets using vector search and OpenAI/Gemini models.

---

## 🚀 Features

- 🔄 Converts tabular loan data into natural language documents
- 🔍 Retrieves relevant chunks using semantic vector similarity (FAISS)
- 🧠 Generates accurate responses using OpenAI or Gemini LLMs
- 💻 Interactive frontend with Streamlit interface
- 🛠️ Modular codebase with preprocessing, retrieval, and generation pipelines

---

## 📁 Project Structure

```
rag_qna_project/
│
├── main.py                        # Entry point to answer queries programmatically
├── requirements.txt              # Python dependencies
│
├── data/
│   ├── Training Dataset.csv      # Raw training data
│   └── Test Dataset.csv
│
├── docs/
│   └── README.md                 # Project documentation
│
├── config/
│   └── settings.py               # Model names, API keys, paths
│
├── preprocessing/
│   └── tabular_to_text.py        # Tabular row to document text conversion
│
├── retrieval/
│   ├── embedder.py               # Embedding logic using Hugging Face/Google/OpenAI
│   └── retriever.py              # FAISS-based similarity retriever
│
├── generation/
│   └── generator.py              # Uses LLM to generate final answer
│
├── utils/
│   └── helpers.py                # File I/O, formatting, logging etc.
│
└── interface/
    └── app.py                    # Streamlit web interface
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/AniketKhandelwal/RAG_QNA_Chatbot.git
cd RAG_QNA_Chatbot
```

### 2. Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your-openai-api-key
GOOGLE_API_KEY=your-gemini-api-key
```

Or manually add keys to `config/settings.py`.

---

## 🧪 Run the App

Launch the Streamlit interface:
```bash
streamlit run interface/app.py
```

---

## 📌 Example Queries

- "What are the traits of applicants who got their loans approved?"
- "How many married applicants applied from urban areas?"
- "Compare income of applicants with different credit histories."

---

## 💡 Future Work

- Add evaluation and metrics module
- Support multiple document formats (PDF, DOCX)
- Add context-aware follow-up Q&A
- Cache responses to reduce API costs

---

## 🤝 Acknowledgements

- OpenAI API
- Google Gemini Pro API
- FAISS (Facebook AI Similarity Search)
- Streamlit

---

## 🧑‍💻 Author

**Aniket Khandelwal**  
📬 [aniketkhandelwal.in](https://github.com/AniketKhandelwal)  
🌐 [linkedin.com/in/aniketkhandelwal](https://linkedin.com/in/aniketkhandelwal)

---

## 📄 License

This project is open-sourced under the MIT License.
