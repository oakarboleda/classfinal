import os
import re
import streamlit
from pathlib import Path
from pypdf import PdfReader


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def parse_info(text):
    # Basic example parsing
    info = {}

    account_match = re.search(r'Account Number[:\s]*([0-9\-xX*]+)', text)
    if account_match:
        info['account_number'] = account_match.group(1)

    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    if email_match:
        info['email'] = email_match.group(0)

    name_match = re.search(r'Name[:\s]*([A-Z][a-z]+\s[A-Z][a-z]+)', text)
    if name_match:
        info['name'] = name_match.group(1)

    return info

def main():
    input_dir = Path("pdfs")  # Folder with PDF files
    for file in input_dir.glob("*.pdf"):
        print(f"Analyzing {file.name}")
        text = extract_text_from_pdf(file)
        parsed = parse_info(text)
        print("Parsed Info:", parsed)
        print("-" * 40)

if __name__ == "__main__":
    main()