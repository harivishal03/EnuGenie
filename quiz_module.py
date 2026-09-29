"""Quiz generation (3 MCQs, 4 options each) using Google Gemini."""
import json
import re

from gemini_client import get_model


def clean_json_block(text: str) -> str:
    """Remove Markdown ```json code fences from a model response."""
    return re.sub(r"```(?:json)?\n?(.*?)```", r"\1", text, flags=re.DOTALL).strip()


def generate_quiz(text: str) -> list:
    try:
        prompt = f"""
You are a quiz generator.

From the following passage or topic, create 3 multiple-choice questions. Each question should include:
- A "question"
- A list of 4 "options"
- A correct "answer" that must exactly match one of the options.

Format your output as **valid JSON**, like this:
[
  {{
    "question": "What is ...?",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Return only the JSON.

Passage:
{text}
"""
        response = get_model().generate_content(prompt)
        cleaned = clean_json_block(response.text.strip())
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        return [{"question": f"⚠️ Could not parse quiz JSON: {e}", "options": [], "answer": ""}]
    except Exception as e:
        return [{"question": f"⚠️ Error generating quiz: {e}", "options": [], "answer": ""}]
