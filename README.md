# Preparacion del entorno tecnico

## Tecnologias usadas
- Python
- Flask
- Docker
- Github
- Github Action
- Render

## Estructura del proyecto
- app.py: Aplicacion principal
- requirements.txt: Dependencias
- Dockerfile: Configuracion del contenedor
- .gitignore: Archivos ignorados por Git
- .env.example: Variables de entorno de ejemplo
- .github/workflows/ci.yml: Pipeline CI/CD

## Ejecucion local
docker build -t entorno-ia .
docker run -p 5000:5000 entorno-ia
