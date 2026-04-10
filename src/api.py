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
    # This is where the phone sends data to your Python server
    result = agent.get_diagnosis(request.code, request.description)
    return {"diagnosis": result}
@app.get("/")
async def root():
    return {"message": "🚗 Car Diagnostic AI API is Online"}