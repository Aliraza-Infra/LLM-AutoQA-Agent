from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Define the request body model
class EvaluationRequest(BaseModel):
    prompt: str
    response: str

# Define the response model
class EvaluationResult(BaseModel):
    hallucination_score: float
    relevance_score: float
    tone_score: float
    overall_score: float
    flags: List[str]

@router.post("/", response_model=EvaluationResult)
def evaluate_llm_output(payload: EvaluationRequest):
    prompt = payload.prompt
    response = payload.response

    if not prompt or not response:
        raise HTTPException(status_code=400, detail="Prompt and response must be provided.")

    from app.core import scorer

# Inside evaluate_llm_output
result = scorer.evaluate_response(prompt, response)

return EvaluationResult(**result)

    flags = []
    if hallucination_score < 0.5:
        flags.append("hallucination")

    return EvaluationResult(
        hallucination_score=hallucination_score,
        relevance_score=relevance_score,
        tone_score=tone_score,
        overall_score=overall_score,
        flags=flags
    )
