from fastapi import FastAPI
from src.agent import CarAgent
from pydantic import BaseModel

app = FastAPI()
agent = CarAgent()

class DiagnosticRequest(BaseModel):
    code: str
    description: str

@app.post("/diagnose")
async def get_diagnosis(request: DiagnosticRequest):
    try:
        # Ensure the agent is called correctly
        result = agent.get_diagnosis(request.code, request.description)
        return {"diagnosis": result}
    except Exception as e:
        # This will show you the REAL error in the browser if it fails again
        return {"error": str(e)}
@app.get("/")
async def root():
    return {"message": "🚗 Car Diagnostic AI API is Online"}