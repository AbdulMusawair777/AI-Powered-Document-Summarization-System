import os
from PyPDF2 import PdfReader

def load_text_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading text file: {e}")
        return ""

def load_pdf_file(filepath):
    try:
        reader = PdfReader(filepath)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

        return text

    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""