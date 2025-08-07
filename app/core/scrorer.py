import random

def evaluate_response(prompt: str, response: str) -> dict:
    """
    Evaluate an LLM response against a prompt.
    This is a placeholder — later you can add:
    - Hallucination detection
    - Relevance matching
    - Tone/formality matching
    """

    # Mock scoring logic (can be replaced with AI/NLP models)
    hallucination_score = round(random.uniform(0.3, 0.9), 2)
    relevance_score = round(random.uniform(0.5, 1.0), 2)
    tone_score = round(random.uniform(0.5, 1.0), 2)

    overall_score = round((hallucination_score + relevance_score + tone_score) / 3, 2)

    # Flag any issues
    flags = []
    if hallucination_score < 0.5:
        flags.append("hallucination")
    if relevance_score < 0.6:
        flags.append("irrelevant")
    if tone_score < 0.6:
        flags.append("tone-mismatch")

    return {
        "hallucination_score": hallucination_score,
        "relevance_score": relevance_score,
        "tone_score": tone_score,
        "overall_score": overall_score,
        "flags": flags
    }
