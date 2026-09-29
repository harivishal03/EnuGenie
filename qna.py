"""Question answering using Google Gemini."""
from gemini_client import get_model


def answer_question_with_gemini(question: str) -> str:
    try:
        response = get_model().generate_content(question)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in QnA: {e}"
