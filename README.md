# Pipeline CI/CD - Docker
Consiste en un proyecto donde se demuestra la **interoperabilidad** que existe entre diferentes tecnologias como Render, Github, Docker, etc. 
Aplicando todo esto a un entorno que esta dirigido a la **preparacion de datos y entrenamiento para ML/IA** (futura actualizacion).

https://gestiondatosia-pipeline-cicd.onrender.com/

## Tecnologias usadas
![My Skills](https://skillicons.dev/icons?i=py,flask,html,css,docker,github,githubactions&theme=dark)
```
['Python', 'Flask/Gunicorn', 'HTML/CSS', 'Docker', 'Github/actions', 'Render']
```

## Estructura del proyecto
```
entorno-ia/
├── .github/workflows/    # Automatizacion CI/CD con GitHub Actions
├── static/               # Archivos CSS 
├── templates/            # Archivos HTML 
├── .env.example          # Plantilla de variables de entorno 
├── .gitignore            # Archivos y carpetas que Git debe ignorar
├── app.py                # Logica principal de la aplicacion Flask
├── Dockerfile            # Instrucciones para crear la imagen del contenedor
├── README.md             # Documentacion tecnica y guia del proyecto
└── requirements.txt      # Listado de librerias Python (Flask, Gunicorn)
```

## Ejecucion local
### **Docker debe estar instalado en el dispositivo!**

Para una ejecucion local del repositorio, primero se debe clonar el repositorio. 
```
$ git clone https://github.com/Sebithaz-dev/Pipeline-CICD.git
```
Una vez clonado el repositorio, en la misma terminal nos posicionamos dentro de la carpeta del repositorio, y con los siguientes comandos ejecutamos la imagen Docker:
```
$ docker build -t entorno-ia .
$ docker run -d --name entorno-ia -p 5000:5000 entorno-ia
```
