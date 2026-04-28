# Founder Intake App

A Flask-based AI chat prototype for conducting structured intake conversations with startup founders.

Built for a classwork assignment in Greg Nudelman's [UX for AI Certification](https://uxforai.com/) course.

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

**IMPORTANT:** You need to replace the placeholder below with your actual API key.

Get your key from [platform.openai.com/api-keys](https://platform.openai.com/api-keys) (requires a free OpenAI account with some credits).

Then run this in your terminal, but **paste your full real key** inside the quotes:

```bash
export OPENAI_API_KEY="sk-proj-YOUR_FULL_KEY_GOES_HERE"
```

**What NOT to do:**
- ❌ `export OPENAI_API_KEY="sk-proj-..."` — literally sets the key to `sk-proj-...`
- ❌ `export OPENAI_API_KEY="***"` — won't work either
- ✅ Copy and paste the entire key, including the `sk-proj-` prefix

**Note:** This `export` only lasts while your terminal window is open. If you close it, you'll need to run the export command again when you restart the server.

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

---

## Troubleshooting

### "Could not find a version that satisfies the requirement flask>=3.0.0"

Your Python version might be too old (Flask 3.x requires Python 3.8+).

**Fix:** The `requirements.txt` now uses `flask>=2.0.0` which works with Python 3.7+.

If you still see this error, make sure you're using the latest `requirements.txt` from the repo:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

If that still fails, install manually:

```bash
pip install "flask>=2.0.0" "openai>=1.0.0"
```

### "Invalid username or token" when pushing to GitHub

GitHub no longer accepts passwords for git operations. You need a **Personal Access Token**.

**Fix:** Go to [github.com/settings/tokens](https://github.com/settings/tokens) → Generate new token (classic) → check `repo` → copy the token → use that as your password when `git push` asks.
