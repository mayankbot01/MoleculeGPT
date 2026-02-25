from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
from minion.agent import MinionAgent
import uuid
import os

app = FastAPI(title="MoleculeGPT API")

# In-memory storage for sessions (for demo purposes)
sessions = {}

class TaskRequest(BaseModel):
    task: str
    model: Optional[str] = "gpt-4-turbo"

class TaskResponse(BaseModel):
    session_id: str
    result: str

@app.post("/run", response_model=TaskResponse)
async def run_task(request: TaskRequest):
    session_id = str(uuid.uuid4())
    agent = MinionAgent(model=request.model)
    
    try:
        result = agent.run(request.task)
        sessions[session_id] = agent.history
        return TaskResponse(session_id=session_id, result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/session/{session_id}")
async def get_session(session_id: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    return {"history": sessions[session_id]}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Serve the frontend
app.mount("/web", StaticFiles(directory="web"), name="web")

@app.get("/")
async def read_index():
    return FileResponse("web/index.html")
