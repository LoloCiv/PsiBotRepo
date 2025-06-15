# Usa imagen base oficial de Python
FROM python:3.11-slim

# Establece directorio de trabajo
WORKDIR /app

# Copia archivos de requirements e instala dependencias
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código al contenedor
COPY . .

# Expone el puerto en el que la app correrá (8080 para Cloud Run)
EXPOSE 8080

# Comando para correr la app usando Gunicorn (más estable para producción)
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
