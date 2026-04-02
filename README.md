# Pipeline CI/CD — Docker + GitHub Actions + Render

<!--![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=flat&logo=render&logoColor=white) -->

![My Skills](https://skillicons.dev/icons?i=py,flask,html,css,docker,github,githubactions,gcp&theme=dark)

Proyecto académico de un pipeline CI/CD completo que integra **Docker**, **GitHub Actions** y **Render**. La aplicación es una web Flask contenerizada, diseñada como base para entornos de **preparación de datos y entrenamiento de modelos ML/IA** (en desarrollo).

<!-- [https://gestiondatosia-pipeline-cicd.onrender.com/](https://gestiondatosia-pipeline-cicd.onrender.com/) -->
🔗 **Demo en vivo:** 

---

## ¿Qué hace este proyecto?

- Sirve una aplicación web con **Flask** y **Gunicorn**
- Se conteneriza con **Docker** para garantizar portabilidad
- Cada push al repositorio dispara un workflow de **GitHub Actions** (CI)
- El despliegue es automático en **Render** (CD)

---

## Stack tecnológico

| Tecnología | Rol |
|---|---|
| Python + Flask | Backend / servidor web |
| Gunicorn | Servidor WSGI para producción |
| HTML / CSS | Frontend |
| Docker | Contenerización |
| GitHub Actions | Integración continua (CI) |
| Render | Despliegue continuo (CD) |

>  **NOTA:**  
> **WSGI (Web Server Gateway Interface)** es un estandar que usa una aplicación web hecha en Python (como Flask), para “hablar” con un servidor como Gunicorn y así recibir peticiones del usuario y devolver respuestas.

> **Flask** permite crear la aplicación web, pero su servidor integrado está pensado solo para desarrollo.  
> En producción se usa un servidor WSGI como **Gunicorn**, que se encarga de ejecutar la app y manejar las peticiones de forma más robusta.

---

## Estructura del proyecto
```
Pipeline-CICD/
├── .github/
│   └── workflows/
│       ├── ci.yml                  # CI/CD del proyecto
│       └── data.yml                # Pipeline de datos
├── app/
│   ├── static/
│   │   └── style.css               # Estilos de la interfaz web
│   ├── templates/
│   │   └── index.html              # Vista principal de Dashboard
│   └── app.py                      # Entrada y logica de la app Flask
├── data/
│   ├── processed/                  # Datos procesados
│   └── raw/                        # Datos de entrada 
├── src/
│   ├── temp/                       # Logicas de extracción de datos anteriores
│   ├── config.py                   # Configuración de procesos
│   ├── extract.py                  # Extracción de datos consultando a BigQuery 
│   ├── load.py                     # Carga de datos obtenidos para supervisión
│   └── transform.py                # Transformación y Limpieza de datos obtenidos
├── .env                            # Variables de entorno locales
├── .gitignore                      # Archivos y carpetas que Git debe ignorar
├── Dockerfile                      # Instrucciones para crear la imagen del contenedor
├── README.md                       # Documentacion tecnica y guia del proyecto
└── requirements.txt                # Listado de librerias Python (Flask, Gunicorn, pandas, etc.)
```

---

## Ejecución local

### Prerrequisitos
- Tener [Docker](https://docs.docker.com/get-docker/) instalado
- Tener la clave de una Service Account (BigQuery) en formato .json 

### Pasos
```bash
# 1. Clonar el repositorio
git clone https://github.com/Sebithaz-dev/Pipeline-CICD.git
cd Pipeline-CICD

# 2. Mover la clave de formato .json a la carpeta raíz del proyecto

# 3. Construir la imagen Docker
docker build -t pipeline-cicd .

# 4.
# Ejecutar el contenedor (Linux)
docker run -d --name pipeline-cicd -p 5000:5000 \
	-v $(pwd)/bigquery_private_key.json:/app/bigquery_private_key.json \
	-e GOOGLE_APPLICATION_CREDENTIALS=/app/bigquery_private_key.json \
  pipeline-cicd

# Ejecutar el contenedor (Windows)
docker run -d --name pipeline-cicd -p 5000:5000 `
-v ${PWD}/bigquery_private_key.json:/app/bigquery_private_key.json `
-e GOOGLE_APPLICATION_CREDENTIALS=/app/bigquery_private_key.json `
pipeline-cicd
```
<!-- # 2. Copiar las variables de entorno
cp .env.example .env -->

La aplicación estará disponible en `http://localhost:5000`

### Detener el contenedor
```bash
docker stop pipeline-cicd
docker rm pipeline-cicd
```

---

## Pipeline CI/CD

El flujo automatizado se activa con cada `push` a la rama `main`:
```
Push a main
    │
    ▼
GitHub Actions (CI)
    │  ├── Checkout del código
    │  ├── Build de imagen Docker
    │  └── Validaciones
    │
    ▼
Render (CD)
    └── Redeploy automático
```

---

## Roadmap

- [x] Aplicación Flask contenerizada
- [x] Pipeline CI/CD funcional con GitHub Actions + Render
- [ ] Módulo de preparación de datos para ML/IA
- [ ] Integración con almacenamiento de datasets
- [ ] Endpoints para entrenamiento de modelos

---

## Autores
**Kuaruan** — [GitHub](https://github.com/kuaruan) (*^_^*)/

**Sebithaz-dev** — [GitHub](https://github.com/Sebithaz-dev) (*^_^*)/
 
