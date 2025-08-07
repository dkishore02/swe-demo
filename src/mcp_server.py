from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI()

class ExtractionRequest(BaseModel):
    pdf_url: str
    fields: List[str]

class ExtractionResponse(BaseModel):
    extracted_fields: Dict[str, Any]

@app.post("/extract", response_model=ExtractionResponse)
async def extract_fields(request: ExtractionRequest):
    # Placeholder for extraction logic
    # This will be implemented in the next steps
    return ExtractionResponse(extracted_fields={f: None for f in request.fields})

