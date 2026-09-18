# 🤖 AI Document & Code Assistant

An AI-powered Streamlit application that can summarize documents, answer questions from uploaded documents, and analyze source code.

## ✨ Features

### 📄 Document Summarizer
- Upload PDF and DOCX documents
- Extract text from documents
- Generate concise AI-powered summaries
- View extracted document text

### 💬 Document Q&A
- Ask questions about an uploaded document
- Splits long documents into smaller chunks
- Retrieves relevant document sections
- Generates answers using only the available document content
- Clearly indicates when information is not present in the document

### 💻 AI Code Analyzer
- Paste source code or upload a code file
- Supports Python, Java, C, C++, JavaScript, HTML, CSS and SQL
- Explains code in beginner-friendly language
- Identifies possible bugs and errors
- Suggests improvements
- Provides time and space complexity discussion
- Gives programming tips

## 🛠️ Technologies Used

- Python
- Streamlit
- OpenAI API
- PyPDF
- python-docx
- python-dotenv
- Git & GitHub

## 📁 Project Structure

```text
AI-Document-Code-Assistant/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env
│
├── modules/
│   ├── summarizer.py
│   ├── qa_assistant.py
│   └── code_analyzer.py
│
├── utils/
│   ├── document_loader.py
│   └── text_processor.py
│
├── uploads/
├── outputs/
└── venv/
```

> `.env`, `venv/`, uploaded documents, generated outputs and other local files are excluded from Git using `.gitignore`.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/rathoresaik-dotcom/AI-Document-Code-Assistant.git
cd AI-Document-Code-Assistant
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure the OpenAI API key

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key_here
```

Never upload or share your `.env` file or API key.

### 5. Run the application

```powershell
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal, usually:

```text
http://localhost:8501
```

## 🧠 How It Works

The application has three main AI workflows:

```text
Document
   ↓
PDF/DOCX Text Extraction
   ↓
Text Cleaning & Chunking
   ↓
Relevant Document Sections
   ↓
OpenAI
   ↓
Summary / Question Answer
```

For code:

```text
Code File / Pasted Code
   ↓
Language Selection / Detection
   ↓
OpenAI Code Analysis
   ↓
Explanation + Bugs + Improvements
   ↓
Complexity + Beginner Tips
```

## 🔐 Security

The OpenAI API key is stored in `.env` and excluded from GitHub using `.gitignore`.

Do not put API keys directly inside Python source files.

## 🎓 Project Purpose

This project demonstrates practical use of:

- Generative AI
- Document processing
- Natural-language question answering
- Retrieval-based document processing
- Source-code analysis
- Python application development
- Streamlit UI development
- Git and GitHub

## 🔮 Future Improvements

Possible future upgrades include:

- Multiple-document Q&A
- Embeddings and vector database retrieval
- Conversation history
- Automatic code-language detection improvements
- Code file download/export
- More advanced document formats
- Authentication
- Cloud deployment
- Automated testing

## 👨‍💻 Author

**rathoresai**

Built as an AI-powered Python project for learning, portfolio development, and practical application of generative AI.

## 📄 License

This project is currently intended for educational and portfolio use.
