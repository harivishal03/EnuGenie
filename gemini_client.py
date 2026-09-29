"""Shared Gemini configuration used by all cloud-powered modules."""
# pyright: reportMissingImports=false
import os

try:
    import google.generativeai as genai  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - handled at runtime when dependency is absent.
    genai = None

try:
    from dotenv import load_dotenv  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - optional dependency at runtime
    def load_dotenv(*args, **kwargs):
        return False

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

if API_KEY and genai is not None:
    genai.configure(api_key=API_KEY)


def get_model():
    if not API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not set. Add it to your .env file.")
    if genai is None:
        raise RuntimeError(
            "google-generativeai is not installed. Install the package to use Gemini features."
        )
    return genai.GenerativeModel(model_name=MODEL_NAME)
