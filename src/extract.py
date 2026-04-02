import os
from dotenv import load_dotenv
from pathlib import Path
from google.cloud import bigquery
from google.auth.exceptions import DefaultCredentialsError

# Nombre del archivo a guardar
FILE_NAME = "test.parquet" 
# Directorio donde esta el script /src
BASE_DIR = Path(__file__).resolve().parent 

# Donde se guardara el parquet
# usamos "../data/raw" relativo a /src 
OUTPUT_PATH = BASE_DIR / "../data/raw" / FILE_NAME 

# Query de ejemplo (Cambiar de acuerdo a contexto)
QUERY = """
SELECT
    bikeid,
    tripduration,
    usertype,
    birth_year,
    (2026 - birth_year) as edad
FROM
    `bigquery-public-data.new_york_citibike.citibike_trips`
WHERE
    birth_year BETWEEN 1996 AND 2006
    AND birth_year IS NOT NULL
LIMIT 500;
"""

def load_environment():
    """
    Carga variables de entorno desde el .env que esta en la raiz del proyecto.
    En Docker esto se reemplaza por secrets o env vars directamente.
    """
    env_path = BASE_DIR.parent / ".env"
    load_dotenv(dotenv_path=env_path)

def get_bigquery_client():
    """
    Crea el cliente de BigQuery usando la var de entorno GOOGLE_APP...
    Recomendacion Docker/CI/CD:
    - La variable de entorno debe estar definida en el contenedor.
    - Evitar hardcodear paths relativos al host; usar mounts de volumen o secrets.
    """
    try:
        cred_path = Path(os.getenv("GOOGLE_APPLICATION_CREDENTIALS")).resolve()
        if not cred_path:
            raise ValueError("La variable GOOGLE_APPLICATION_CREDENTIALS no esta definida en .env")
        if not Path(cred_path).exists():
            raise FileNotFoundError(f"No se encontro el archivo: {cred_path}")
        return bigquery.Client()

    except DefaultCredentialsError as e:
        print(f"Error de credenciales: {e}")
        return None
    
    except Exception as e:
        print(f"Error creando cliente: {e}")

def run_query(client):
    """
    Ejecuta la Query de ejemplo y devuelve un DataFrame
    """
    try:
        print("Extrayendo datos de BigQuery...")
        return client.query(QUERY).to_dataframe()

    except Exception as e:
        print(f"Error ejecutando query: {e}")
        return None

def save_parquet(df):
    """
    Guarda el DataFrame como parquet.
    - Crea los directorios si no existe.
    - En Docker asegurarnos de montar /app/data/raw para persistencia
    """
    try:
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(OUTPUT_PATH)
        print("\n--- Extraccion finalizada ---")
        print(f"Datos guardados en: {OUTPUT_PATH}")
        print(f"Cant. Registros: {len(df)}\n")
    except Exception as e:
        print(f"Error guardando archivo: {e}")

def main():
    """
    Flujo principal del extract:
    1. Carga variables de entorno.
    2. Crea cliente BigQuery.
    3. Ejecuta Query.
    4. Guarda resultados.
    5. Muestra pequeño analisis.
    """
    load_environment()
    
    client = get_bigquery_client()
    if not client:
        return 
    
    df = run_query(client)
    if df is None or df.empty:
        return 
    
    save_parquet(df)

if __name__ == "__main__":
    main()