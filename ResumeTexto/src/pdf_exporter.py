from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def exportar_a_pdf(texto, nombre_archivo="resumen.pdf"):
    """
    Exporta el texto dado a un archivo PDF.

    :param texto: Contenido a guardar en el PDF.
    :param nombre_archivo: Nombre del archivo de salida (por defecto 'resumen.pdf').
    """
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont("Helvetica", 12)

    # Margen inicial
    x, y = 50, 750  
    line_height = 20  

    for linea in texto.split("\n"):
        c.drawString(x, y, linea)
        y -= line_height  # Moverse hacia abajo para la siguiente línea
        if y < 50:  # Si llega al final de la página, crear una nueva
            c.showPage()
            c.setFont("Helvetica", 12)
            y = 750  

    c.save()
