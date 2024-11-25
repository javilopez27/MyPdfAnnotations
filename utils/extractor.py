import fitz  # Importa PyMuPDF

import fitz  # Importa PyMuPDF

def extract_marked_text(doc):
    extracted_text = ""
    for page in doc:
        annotations = page.annots()
        if annotations:
            for annot in annotations:
                # Detectar resaltados
                if annot.type[0] == 8:  # Tipo para resaltados
                    rect = annot.rect
                    words = page.get_text("words")
                    words_in_rect = [w for w in words if fitz.Rect(w[:4]).intersects(rect)]
                    extracted_text_part = " ".join(w[4] for w in words_in_rect)
                    extracted_text += f"(H) {extracted_text_part}\n"
                # Detectar subrayados
                elif annot.type[0] == 9:  # Tipo para subrayados
                    rect = annot.rect
                    words = page.get_text("words")
                    words_in_rect = [w for w in words if fitz.Rect(w[:4]).intersects(rect)]
                    extracted_text_part = " ".join(w[4] for w in words_in_rect)
                    extracted_text += f"(U) {extracted_text_part}\n"
                # Detectar texto libre (FreeText)
                elif annot.type[0] == 17:  # Suponemos que 17 es el tipo para 'FreeText'
                    freetext_content = annot.info['content']  # Asegúrate de que 'content' es la clave correcta
                    if freetext_content:
                        extracted_text += f"(FT) {freetext_content}\n"
    return extracted_text

