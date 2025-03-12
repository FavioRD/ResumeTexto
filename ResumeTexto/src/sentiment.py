from textblob import TextBlob

def analizar_sentimiento(texto):
    """
    Analiza el sentimiento del texto y devuelve si es positivo, negativo o neutral.
    
    :param texto: Texto a analizar.
    :return: Cadena con el sentimiento detectado.
    """
    blob = TextBlob(texto)
    polaridad = blob.sentiment.polarity  # Valor entre -1 (negativo) y 1 (positivo)

    if polaridad > 0:
        return "😊 Positivo"
    elif polaridad < 0:
        return "😠 Negativo"
    else:
        return "😐 Neutral"
