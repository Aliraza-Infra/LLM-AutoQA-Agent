from fastapi import FastAPI
from app.routers import evaluate

app = FastAPI(
    title="LLM-AutoQA-Agent",
    description="Automated LLM evaluation and QA framework using FastAPI and pandas.",
    version="0.1.0"
)

# Include routers
app.include_router(evaluate.router, prefix="/evaluate", tags=["Evaluation"])

@app.get("/")
def root():
    return {"message": "LLM-AutoQA-Agent is running."}
