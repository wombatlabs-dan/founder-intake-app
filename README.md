# Founder Intake App

A Flask-based AI chat prototype for conducting structured intake conversations with business founders.

Build for a classwork assignment in Greg Nudleman's [UX for AI Certification ](https://uxforai.com/) course.

## What It Does

- Founder describes their target user in natural language
- AI reflects back what it heard, structured around 6 key topics
- AI flags gaps and contradictions in the founder's thinking
- RAG file provides the AI with structured guidance on how to conduct the intake

## Setup

1. Set your Anthropic API key:
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-api03-..."
   ```

2. Run the server:
   ```bash
   source venv/bin/activate
   python3 server.py
   ```

3. Open http://127.0.0.1:5000 in your browser

## Project Structure

```
founder-intake-app/
├── server.py              # Flask app + LLM integration
├── templates/
│   └── index.html         # Chat UI
├── rag_files/
│   └── founder-intake-rag.txt   # RAG context (loaded server-side)
├── requirements.txt
└── README.md
```

## Features

- ✅ Flask "Hello World" server
- ✅ Text input + echo (via LLM)
- ✅ LLM call (Claude Haiku)
- ✅ RAG file loaded from backend directory
- ✅ Prompt template with system instructions
- ✅ Clean UI with Quicksand font, #149911 buttons
