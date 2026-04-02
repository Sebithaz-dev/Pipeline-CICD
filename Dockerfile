# Imagen base de Python (version slim)
FROM python:3.11-slim

# Directorio donde se copiaran los archivos en el contenedor
WORKDIR /app

# Copiamos requisitos y los instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el codigo del repositorio dentro del contenedor
COPY . .

# Exponemos el puerto 5000 (para la app de Flask)
EXPOSE 5000

# Comando por defecto para iniciar la app Flask con Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app.app:app"]