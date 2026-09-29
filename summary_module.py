"""Summarization using Google Gemini."""
from gemini_client import get_model


def summarize_text(text: str) -> str:
    try:
        prompt = (
            "Summarize the following passage into a concise, easy-to-understand version "
            "suitable for quick revision. Keep the core information and remove redundancy.\n\n"
            f"{text}"
        )
        response = get_model().generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in summarization: {e}"
