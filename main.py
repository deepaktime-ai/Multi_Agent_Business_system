from fastapi import FastAPI
from pydantic import BaseModel
from agents.orchestrator import OrchestratorAgent

app = FastAPI()

# Initialize Orchestrator
orchestrator = OrchestratorAgent()


# Request Schema
class UserRequest(BaseModel):
    query: str


# Health Check
@app.get("/")
def home():
    return {"message": "Multi-Agent Business AI is running 🚀"}


# Main Endpoint
@app.post("/run")
def run_agent(request: UserRequest):
    try:
        result = orchestrator.run(request.query)
        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }