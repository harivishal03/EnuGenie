"""Concept explanation using the local LaMini-Flan-T5-783M model."""
try:
    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - optional dependency at runtime
    AutoModelForSeq2SeqLM = None
    AutoTokenizer = None

MODEL_ID = "MBZUAI/LaMini-Flan-T5-783M"

_tokenizer = None
_model = None


def _load():
    """Lazy-load so the server starts fast and other endpoints work without the model."""
    global _tokenizer, _model
    if AutoTokenizer is None or AutoModelForSeq2SeqLM is None:
        raise ImportError(
            "The 'transformers' package is not installed. Please install it to use explanation features."
        )
    if _model is None:
        _tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
        _model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_ID)
    return _tokenizer, _model


def explain_topic(topic: str) -> str:
    try:
        tokenizer, model = _load()
        input_text = f"Explain the concept of '{topic}' in a simple and clear way for a school student."
        inputs = tokenizer(input_text, return_tensors="pt")
        outputs = model.generate(
            **inputs,
            max_new_tokens=150,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            do_sample=True,
        )
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        return f"⚠️ Error in explanation: {e}"
