# EduGenie: Google Gemini Powered Learning Assistant

A lightweight AI tutor built with **FastAPI** and a simple **HTML + CSS** frontend.

Features: Q&A, concept explanation, quiz generation (3 MCQs), summarization, and personalized learning paths.

| Feature | Endpoint | Model |
|---|---|---|
| Ask a question | `GET /qa?question=...` | Gemini |
| Explain a concept | `POST /explain/` `{"topic": "..."}` | LaMini-Flan-T5-783M (local) |
| Generate quiz | `POST /quiz` `{"text": "..."}` | Gemini |
| Summarize | `POST /summarize/` `{"text": "..."}` | Gemini |
| Learning path | `GET /learn/recommendations?topic=...` | Gemini |

## Setup

1. Install Python 3.10+.
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Get a Gemini API key from https://aistudio.google.com/ and configure it:
   ```bash
   cp .env.example .env            # then edit .env and paste your key
   ```
4. Run:
   ```bash
   uvicorn main:app --reload
   ```
5. Open http://127.0.0.1:8000

## Notes

- The explanation feature downloads the LaMini-Flan-T5-783M model (~3 GB) from Hugging Face on first use, so the first "Explain" request is slow. It runs fine on CPU / Mac M1.
- The original report used `gemini-1.5-pro`, which Google has retired. The model is set by `GEMINI_MODEL` in `.env` (default `gemini-2.5-flash`).
- Interactive API docs are available at http://127.0.0.1:8000/docs

## Structure

```
EduGenie/
├── main.py                # FastAPI app
├── gemini_client.py       # Shared Gemini config
├── explanation_module.py  # Concept explanation (local model)
├── qna.py                 # Question answering
├── quiz_module.py         # Quiz generation
├── summary_module.py      # Summarization
├── learning_path.py       # Learning recommendations
├── templates/index.html   # Frontend
├── static/style.css       # Styling
├── requirements.txt
└── .env.example
```
