from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os

from engine import processar_pdf

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/processar")
async def processar(file: UploadFile = File(...)):
    
    os.makedirs("temp", exist_ok=True)

    input_path = f"temp/{file.filename}"
    output_path = f"temp/resultado.xlsx"

    # salva PDF
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # chama o motor
    processar_pdf(input_path, output_path)

    # retorna excel
    return FileResponse(
        output_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename="resultado.xlsx"
    )
