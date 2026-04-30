from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os
from engine import processar_importacao

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/processar")
async def processar(pdf: UploadFile = File(...)):
    os.makedirs("temp", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    pdf_path = f"temp/{pdf.filename}"

    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(pdf.file, buffer)

    output_path = processar_importacao(pdf_path)

    os.remove(pdf_path)

    return FileResponse(output_path, filename="resultado.xlsx")