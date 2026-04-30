from openpyxl import Workbook
import os

def processar_importacao(pdf_path):
    # cria pasta output se não existir
    os.makedirs("output", exist_ok=True)

    # cria um excel simples
    wb = Workbook()
    ws = wb.active

    ws["A1"] = "Sistema funcionando"
    ws["A2"] = f"Arquivo recebido: {pdf_path}"

    # salva o arquivo
    output_path = "output/resultado.xlsx"
    wb.save(output_path)

    return output_path