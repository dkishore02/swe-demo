from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
import httpx
from PyPDF2 import PdfReader
import io

app = FastAPI()

class ExtractionRequest(BaseModel):
    pdf_url: str
    fields: List[str]

class ExtractionResponse(BaseModel):
    extracted_fields: Dict[str, Any]


def download_pdf(url: str) -> bytes:
    try:
        response = httpx.get(url)
        response.raise_for_status()
        return response.content
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to download PDF: {e}")

def extract_fields_from_pdf(pdf_bytes: bytes, fields: list[str]) -> dict:
    reader = PdfReader(io.BytesIO(pdf_bytes))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    extracted = {}
    for field in fields:
        idx = text.lower().find(field.lower())
        if idx != -1:
            after = text[idx+len(field):].strip().split()
            extracted[field] = after[0] if after else None
        else:
            extracted[field] = None
    return extracted

@app.post("/extract", response_model=ExtractionResponse)
async def extract_fields(request: ExtractionRequest):
    pdf_bytes = download_pdf(request.pdf_url)
    extracted = extract_fields_from_pdf(pdf_bytes, request.fields)
    return ExtractionResponse(extracted_fields=extracted)


