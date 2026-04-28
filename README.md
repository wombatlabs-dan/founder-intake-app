# Founder Intake App

A Flask-based AI chat prototype for conducting structured intake conversations with startup founders.

## What It Does

- Founder describes their target user in natural language
- AI reflects back what it heard, structured around 6 key topics
- AI flags gaps and contradictions in the founder's thinking
- RAG file provides the AI with structured guidance on how to conduct the intake

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/wombatlabs-dan/founder-intake-app.git
cd founder-intake-app
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your OpenAI API key

```bash
export OPENAI_API_KEY="sk-proj-..."
```

### 5. Run the server

```bash
python3 server.py
```

### 6. Open the app

Go to `http://127.0.0.1:5000` in your browser.

---

## Project Structure

```
founder-intake-app/
├── server.py              # Flask + OpenAI + RAG loader
├── templates/
│   └── index.html         # Chat UI
├── rag_files/
│   └── founder-intake-rag.txt   # RAG context (server-side)
├── requirements.txt
└── README.md
```

## Features

- ✅ Flask "Hello World" server
- ✅ Text input + echo (via LLM)
- ✅ LLM call (OpenAI GPT-4o-mini)
- ✅ RAG file loaded from backend directory
- ✅ Prompt template with system instructions
- ✅ Clean UI with Quicksand font, #149911 buttons
