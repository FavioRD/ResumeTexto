from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def generar_resumen(texto, num_oraciones=3):
    """
    Genera un resumen del texto dado usando el algoritmo LSA de Sumy.
    
    :param texto: El texto completo a resumir.
    :param num_oraciones: Número de oraciones en el resumen (por defecto 3).
    :return: Resumen generado como cadena de texto.
    """
    parser = PlaintextParser.from_string(texto, Tokenizer("spanish"))
    summarizer = LsaSummarizer()
    
    resumen = summarizer(parser.document, num_oraciones)
    resumen_texto = " ".join([str(oracion) for oracion in resumen])

    return resumen_texto if resumen_texto else "⚠ No se pudo generar un resumen."
