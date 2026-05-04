from openpyxl import Workbook
import os

def processar_pdf(input_pdf, output_excel):
    # cria pasta temp se não existir
    os.makedirs("temp", exist_ok=True)

    wb = Workbook()
    ws = wb.active

    ws["A1"] = "Sistema funcionando"
    ws["A2"] = f"Arquivo recebido: {input_pdf}"

    # salva exatamente no caminho que o main espera
    wb.save(output_excel)
