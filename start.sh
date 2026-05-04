#!/bin/bash

pip install --upgrade pip
pip install fastapi uvicorn pdfplumber openpyxl python-multipart

python3 -m uvicorn main:app --host 0.0.0.0 --port 10000
