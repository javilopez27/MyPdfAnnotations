import os
import sys
sys.path.append('C:/Users/00jav/Downloads/MyPdfAnnotations')
import pytest
from flask_testing import TestCase
from app import create_app
from utils.extractor import extract_marked_text
import fitz

class TestPDFExtraction(TestCase):
    def create_app(self):
        # Configura tu aplicación Flask para pruebas
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_pdf_upload_and_text_extraction(self):
        # Asume que tienes un archivo PDF de prueba en la misma carpeta que este script
        test_pdf_path = '../javier_generated_resume.pdf'
        with open(test_pdf_path, 'rb') as pdf:
            response = self.client.post('/', data={'pdf_file': (pdf, test_pdf_path)}, content_type='multipart/form-data')
            self.assert200(response)
            # Aquí puedes verificar que la respuesta contenga el texto esperado
            assert 'First Name: Javier Last Name: López Palacios\n' in response.json['extracted_text']

    def test_direct_extraction(self):
        # Prueba directamente la función de extracción con un archivo local
        doc = fitz.open('../javier_generated_resume.pdf')  # Asegúrate de tener este archivo en tu directorio de pruebas
        extracted_text = extract_marked_text(doc)
        doc.close()
        assert 'First Name: Javier Last Name: López Palacios\n' in extracted_text

# Si quieres que pytest reconozca y ejecute las pruebas
if __name__ == '__main__':
    pytest.main()
