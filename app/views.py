from flask import Blueprint, render_template, request, jsonify
from utils.extractor import extract_marked_text
import fitz  # Importa PyMuPDF

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']
        if pdf_file and pdf_file.content_type == 'application/pdf':
            doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
            extracted_text = extract_marked_text(doc)
            return jsonify({'extracted_text': extracted_text})
        else:
            return jsonify({'error': 'Archivo no válido. Por favor, suba un archivo PDF.'}), 400

    return render_template('index.html')
