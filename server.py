"""
Founder Intake App
A Flask server that uses OpenAI GPT + RAG to conduct structured
intake conversations with startup founders.
"""

import os
import glob
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

# ------------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------------
app = Flask(__name__)

# Read API key from environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
if not OPENAI_API_KEY:
    print("WARNING: OPENAI_API_KEY not set. Set it before running the server.")
    print("  export OPENAI_API_KEY='sk-...'")

client = OpenAI(api_key=OPENAI_API_KEY)

# Path to the directory containing RAG files
RAG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rag_files")

# ------------------------------------------------------------------
# RAG LOADER
# ------------------------------------------------------------------
def load_rag_files():
    """
    Load all .txt files from the rag_files/ directory.
    Returns a single string with all RAG content.
    """
    rag_content = []
    pattern = os.path.join(RAG_DIR, "*.txt")
    for filepath in sorted(glob.glob(pattern)):
        with open(filepath, "r", encoding="utf-8") as f:
            rag_content.append(f.read())
    return "\n\n".join(rag_content)

# Load RAG once at startup
RAG_CONTEXT = load_rag_files()
print(f"Loaded RAG files from {RAG_DIR}")

# ------------------------------------------------------------------
# PROMPT TEMPLATE
# ------------------------------------------------------------------
SYSTEM_PROMPT = f"""You are an expert startup coach conducting a founder intake conversation.

Your goal is to help the founder clearly articulate their target user by listening, reflecting back what you heard, and flagging gaps in their thinking.

---
RAG CONTEXT (use this as your guide):
{RAG_CONTEXT}
---

INSTRUCTIONS:
1. Read the founder's message carefully.
2. Reflect back what you heard using: "So what I'm hearing is [summary]. Is that right?"
3. Flag any gaps from the six topics (WHO, PAIN, CURRENT SOLUTION, TRIGGER, DECISION, SUCCESS).
4. If you spot contradictions, flag them gently.
5. Keep your tone warm, direct, and conversational — like a smart friend who knows startups.
6. Do NOT dump all gaps at once. Prioritize the most important gap first.
7. If the founder's input is vague, say "I don't have enough to work with yet on [topic]."

Remember: the most valuable thing you do is catch what the founder DIDN'T say.
"""

# ------------------------------------------------------------------
# ROUTES
# ------------------------------------------------------------------
@app.route("/")
def index():
    """Serve the main chat UI."""
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    """
    Receive a user message, send it to GPT with the RAG context,
    and return the AI's response.
    """
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"reply": "I didn't catch that — could you say more?"})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=1024,
            temperature=0.7,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        print(f"Error calling OpenAI: {e}")
        return jsonify({"reply": "Sorry, I ran into an error processing your message. Please try again!"})

# ------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 50)
    print("Founder Intake App starting...")
    print("Open http://127.0.0.1:5000 in your browser")
    print("=" * 50)
    app.run(debug=True, port=5000)
