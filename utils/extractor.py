import fitz  # Importa PyMuPDF

def extract_marked_text(doc):
    extracted_text = ""
    for page in doc:
        annotations = page.annots()
        if annotations:
            for annot in annotations:
                if annot.type[0] == 8:  # Tipo 8 usualmente corresponde a Highlight
                    rect = annot.rect
                    words = page.get_text("words")  # Obtiene todas las palabras en la página
                    # Filtra las palabras que intersectan con el rectángulo de la anotación
                    words_in_rect = [w for w in words if fitz.Rect(w[:4]).intersects(rect)]
                    # Une las palabras para formar el texto extraído
                    text = " ".join(w[4] for w in words_in_rect)
                    extracted_text += f"Highlight: {text}\n"
    return extracted_text
