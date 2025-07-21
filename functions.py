import re
import PyPDF2
import requests
from bs4 import BeautifulSoup

def extract_text_from_pdf(file_stream):
    reader = PyPDF2.PdfReader(file_stream)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text

def extract_text_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        return text
    except Exception as e:
        return f"Error al extraer texto: {e}"

def clean_and_tokenize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    tokens = text.split()
    return set(tokens)

def score_cv(cv_text, job_text):
    cv_words = clean_and_tokenize(cv_text)
    job_words = clean_and_tokenize(job_text)
    common = cv_words.intersection(job_words)
    match_percent = len(common) / len(job_words) if job_words else 0
    score = round(min(10, match_percent * 10), 2)
    return score, common
