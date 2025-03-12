from summarizer import generar_resumen
from sentiment import analizar_sentimiento
from pdf_exporter import exportar_a_pdf

def main():
    print("📝 Generador de Resúmenes Automáticos")
    print("=" * 40)

    # Entrada del usuario
    texto = input("📌 Ingresa el texto a resumir:\n")
    num_oraciones = int(input("🔢 ¿Cuántas oraciones deseas en el resumen? "))

    # Generar resumen
    resumen = generar_resumen(texto, num_oraciones)
    print("\n📌 Resumen Generado:\n" + resumen)

    # Analizar sentimiento
    sentimiento = analizar_sentimiento(resumen)
    print("\n📊 Análisis de Sentimiento: " + sentimiento)

    # Exportar a PDF
    exportar = input("\n📂 ¿Quieres exportar el resumen a PDF? (s/n): ").strip().lower()
    if exportar == "s":
        exportar_a_pdf(resumen)
        print("✅ Resumen exportado como 'resumen.pdf'.")

if __name__ == "__main__":
    main()
