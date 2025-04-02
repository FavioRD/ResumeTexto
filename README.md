# Generador de Resúmenes Automáticos

## Descripción
El **Generador de Resúmenes Automáticos** es una aplicación en Python diseñada para resumir textos largos de manera eficiente utilizando técnicas de **Procesamiento de Lenguaje Natural (NLP)**.

### Características principales:
- 📖 **Generación de resúmenes** a partir de textos largos.
- 🔍 **Uso del algoritmo LSA** de la biblioteca **Sumy**.
- 📊 **Análisis de sentimiento** con **TextBlob**.
- 🖨️ **Exportación en formato PDF** con **ReportLab**.

---

## 🚀 Instalación
### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/FavioRD/ResumeTexto.git
cd Generador-Resumenes
```

### 2️⃣ Crear y activar un entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Descargar datos necesarios para NLTK
```python
import nltk
nltk.download('punkt')
```

---

## 🛠️ Uso
Ejecutar el script principal:
```bash
python src/main.py
```

---

## 📂 Estructura del Proyecto
```
Generador-Resumenes/
│── 📁 assets/               # Archivos adicionales (íconos, imágenes, etc.)
│── 📁 src/                  # Código fuente del proyecto
│   │── 📜 summarizer.py     # Módulo para generar resúmenes
│   │── 📜 sentiment.py      # Módulo para el análisis de sentimientos
│   │── 📜 pdf_exporter.py   # Módulo para exportar resúmenes a PDF
│   └── 🚀 main.py           # Script principal
│── 📄 requirements.txt      # Lista de dependencias
└── 📖 README.md             # Documentación del proyecto
```

---

## 🤝 Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, puedes:
1. **Abrir un issue** con sugerencias o errores detectados.
2. **Enviar un pull request** con mejoras o nuevas funcionalidades.

¡Gracias por tu interés en mejorar este proyecto! 🚀

