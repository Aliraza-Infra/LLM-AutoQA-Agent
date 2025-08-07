import pytest
from app.core import scorer

def test_evaluate_response_structure():
    prompt = "What is the capital of Germany?"
    response = "The capital of Germany is Berlin."
    result = scorer.evaluate_response(prompt, response)

    assert isinstance(result, dict)
    assert "hallucination_score" in result
    assert "relevance_score" in result
    assert "tone_score" in result
    assert "overall_score" in result
    assert "flags" in result
    assert isinstance(result["flags"], list)

def test_scores_within_bounds():
    result = scorer.evaluate_response("Prompt?", "Response.")
    assert 0.0 <= result["hallucination_score"] <= 1.0
    assert 0.0 <= result["relevance_score"] <= 1.0
    assert 0.0 <= result["tone_score"] <= 1.0
    assert 0.0 <= result["overall_score"] <= 1.0
