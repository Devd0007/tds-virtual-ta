# app.py - Main FastAPI application

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import base64
from search import search_knowledge_base

app = FastAPI(
    title="TDS Virtual TA", 
    description="Virtual Teaching Assistant for IIT Madras Tools in Data Science course",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Link(BaseModel):
    url: str
    text: str

class Query(BaseModel):
    question: str
    image: Optional[str] = None

class Answer(BaseModel):
    answer: str
    links: List[Link]

@app.get("/")
async def root():
    return {"message": "TDS Virtual TA API", "version": "1.0.0"}

@app.post("/api/", response_model=Answer)
async def answer_question(query: Query):
    try:
        if not query.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        # Search knowledge base
        result = search_knowledge_base(query.question)
        
        return Answer(
            answer=result["answer"],
            links=[Link(**link) for link in result["links"]]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
