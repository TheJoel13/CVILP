from flask import Flask, render_template, request
from functions import extract_text_from_pdf, extract_text_from_url, score_cv
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    score = None
    common_words = []

    if request.method == 'POST':
        job_text = request.form.get('job_text')
        job_url = request.form.get('job_url')
        file = request.files.get('cv_file')

        if job_url:
            job_text = extract_text_from_url(job_url)

        if file and job_text and file.filename.endswith('.pdf'):
            cv_text = extract_text_from_pdf(file.stream)
            score, common_words = score_cv(cv_text, job_text)

    return render_template('index.html', score=score, words=common_words)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
