import fitz  # Importa PyMuPDF

def extract_marked_text(doc):
    extracted_text = ""
    for page in doc:
        annotations = page.annots()
        if annotations:
            for annot in annotations:
                if annot.type[0] == 8:  # Asumiendo que 8 es el tipo para texto resaltado
                    rect = annot.rect
                    words = page.get_text("words")  # Obtiene todas las palabras de la página
                    words_in_rect = [w for w in words if fitz.Rect(w[:4]).intersects(rect)]
                    extracted_text_part = " ".join(w[4] for w in words_in_rect)
                    print(f"Extracted text from annotation: {extracted_text_part}")  # Impresión para depuración
                    extracted_text += extracted_text_part + "\n"
    print(f"Total extracted text: {extracted_text}")  # Más impresiones para depuración
    return extracted_text
