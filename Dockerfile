# Usar una imagen base oficial de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /index

# Copiar el archivo requirements.txt en el directorio de trabajo
COPY requirements.txt .


# Install core dependencies.
RUN apt-get update && apt-get install -y libpq-dev build-essential

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el contenido de tu proyecto en el contenedor
COPY . .

# Exponer el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python3", "index.py"]
