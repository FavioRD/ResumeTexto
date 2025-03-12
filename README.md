📄 Generador de Resúmenes Automáticos

📌 Descripción:
Este proyecto es una aplicación en Python que permite generar resúmenes automáticos de textos largos.
Utiliza técnicas de Procesamiento de Lenguaje Natural (NLP) con la biblioteca Sumy y permite la exportación de los resúmenes en formato PDF.
Además, incluye un análisis de sentimiento del texto original.

✨ Características

✅ Generación de resúmenes a partir de un texto largo.

✅ Uso de Sumy para aplicar el algoritmo LSA.

✅ 📊 Análisis de sentimiento con TextBlob.

✅ 🖨️ Exportación del resumen en formato PDF con ReportLab.

🚀 Instalación

📥 Clonar el repositorio:

git clone https://github.com/tuusuario/Generador-Resumenes.git

cd Generador-Resumenes

🏗️ Crear y activar un entorno virtual (opcional pero recomendado):

python -m venv venv

source venv/bin/activate  # En Windows: venv\Scripts\activate

📦 Instalar dependencias:

pip install -r requirements.txt

📌 Descargar los datos necesarios para NLTK:

import nltk

nltk.download('punkt')

🛠️ Uso

Ejecutar el script principal:

python src/main.py

📂 Estructura del Proyecto

Generador-Resumenes/
│── 📁 assets/               # Archivos adicionales (íconos, imágenes, etc.)
│── 📁 src/                  # Código fuente del proyecto
│   │── 📜 summarizer.py     # Módulo para generar resúmenes
│   │── 📜 sentiment.py      # Módulo para el análisis de sentimientos
│   │── 📜 pdf_exporter.py   # Módulo para exportar resúmenes a PDF
│   └── 🚀 main.py           # Script principal
│── 📄 requirements.txt      # Lista de dependencias
└── 📖 README.md             # Documentación del proyecto

🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto, abre un issue o envía un pull request. 🚀


