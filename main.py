from functions import extract_text_from_pdf, score_cv

cv_path = "samples/"
cv_text = extract_text_from_pdf(cv_path)

#job_offer_text = """
#PYTHON DESARROLLADOR SQL BACKEND
#"""

score, palabras_comunes = score_cv(cv_text)

print(f"\nPuntaje del CV: {score}/10")
print(f"\nPalabras clave encontradas: {palabras_comunes}")
