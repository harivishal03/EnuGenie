"""Personalized learning path recommendations using Google Gemini."""
from gemini_client import get_model


def get_learning_recommendations(topic: str) -> str:
    try:
        prompt = f"""
Create a personalized, structured learning path for the topic: "{topic}".

Include:
1. Beginner, Intermediate and Advanced stages, each with key concepts to learn.
2. Suggested timelines for each stage.
3. Useful resources (videos, articles, books, courses) for each stage.
4. A few practice ideas or mini-projects.

Keep it clear, well organized and adaptable to the learner's level.
"""
        response = get_model().generate_content(prompt)
        if not getattr(response, "text", None):
            return "⚠️ The model returned an empty response. Please try again."
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in learning recommendations: {e}"
