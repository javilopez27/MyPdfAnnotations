from flask import Blueprint, render_template, request, send_file, current_app
from utils.extractor import extract_marked_text
from utils.file_handler import save_text_to_file
import os
import fitz  # Importa PyMuPDF

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']
        if pdf_file and pdf_file.content_type == 'application/pdf':
            doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
            extracted_text = extract_marked_text(doc)
            doc.close()

            output_filename = 'extracted_text.txt'
            output_filepath = os.path.join(current_app.root_path, 'static', output_filename)
            save_text_to_file(extracted_text, output_filepath)

            return send_file(output_filepath, as_attachment=True, download_name=output_filename)
        else:
            return 'Archivo no válido. Por favor, suba un archivo PDF.'
    return render_template('index.html')

