# Usa una imagen base de Python
FROM python:3.9-slim

# Instala dependencias del sistema necesarias para pygame
RUN apt-get update && apt-get install -y \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libfreetype6-dev \
    libjpeg-dev \
    zlib1g-dev \
    && apt-get clean

# Crea un directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto a /app
COPY . /app

# Instala las dependencias de Python
RUN pip install -r requirements.txt

# Comando para ejecutar el juego
CMD ["python", "main.py"]
