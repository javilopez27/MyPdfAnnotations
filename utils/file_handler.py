import os

def save_text_to_file(text, file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)  # Crea el directorio si no existe

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)
    print(f"Text successfully saved to {file_path}")
