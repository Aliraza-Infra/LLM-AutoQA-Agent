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

    # Dummy scoring logic (replace with real later)
    hallucination_score = 0.4
    relevance_score = 0.9
    tone_score = 0.8
    overall_score = round((hallucination_score + relevance_score + tone_score) / 3, 2)

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
