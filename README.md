# MyPdfAnnotations

My PDF Annotations es una aplicación web que permite a los usuarios subir archivos PDF y extraer automáticamente cualquier texto que esté subrayado, resaltado y texto libre.

## Características

- Carga de archivos PDF.
- Extracción de texto subrayado, resaltado y texto libre.
- Descarga de los textos extraídos en un archivo de texto (*extracted_text.txt*).

## Tecnologías Utilizadas

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **PDF Manipulation**: PyMuPDF
- **Estilo**: CSS personalizado

## Instalación & Ejecución

Para instalar y ejecutar este proyecto localmente, sigue estos pasos:

```bash
git clone https://github.com/javilopez27/mypdfannotations.git
cd mypdfannotations
pip install -r requirements.txt
flask run
```

Abre tu navegador y visita `http://127.0.0.1:5000` para subir un archivo PDF.

### Iniciar la aplicación

Al acceder a la aplicación a través de `http://127.0.0.1:5000`, verás una interfaz sencilla, como se muestra en la Figura 1, con un botón central que dice **Select File**. Esta es la pantalla inicial donde comenzarás el proceso de carga del archivo PDF.

![Pantalla de Carga](/assets/Upload%20PDF.png)
*Figura 1: Interfaz de usuario mostrando la pantalla de carga del archivo PDF.*

### Cargar el Archivo PDF

1. **Seleccionar el Archivo**: Haz clic en el botón **Select File** para abrir el diálogo de selección de archivos. Navega a través de tus archivos locales y selecciona el archivo PDF que deseas procesar. El nombre del archivo seleccionado se mostrará en la pantalla para confirmar que el archivo está listo para ser cargado.
2. **Subir el Archivo**: Después de seleccionar el archivo, haz clic en **Upload PDF** para enviar el archivo al servidor. Este proceso iniciará la extracción de texto del PDF.

### Extracción de Texto

Una vez que el archivo PDF es subido:
- La aplicación procesará el archivo y extraerá los textos de las anotaciones.
- Los textos **resaltados** serán precedidos por `(H)`, los **subrayados** por `(U)`, y cualquier **texto libre** por `(FT)` en el archivo de texto resultante.
- Este archivo de texto, llamado `extracted_text.txt`, será automáticamente generado y disponible para descarga una vez completado el proceso.

### Descargar el Resultado

Al completar la extracción, se te descargá directamente el archivo `extracted_text.txt` en tu carpeta predeterminada de descargas.

## Licencia
Distribuido bajo la licencia MIT. Ver `LICENSE` para más información.

## Autores
- Javier López Palacios

#### Contribución

Para los siguientes pasos y mejoras no dudeis en contactar conmigo. Contacto: 00javilopezp@gmail.com