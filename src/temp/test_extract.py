import os
from dotenv import load_dotenv
from pathlib import Path
from google.cloud import bigquery

# Configuracion de rutas
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data" / "raw"
OUTPUT_PATH = DATA_DIR / "test.parquet"

# Consulta seleccionada (Usuarios 20-30 años)
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

def setup_client():
    """Carga entorno y devuelve cliente de BigQuery."""
    load_dotenv(dotenv_path=BASE_DIR.parent / ".env")
    try:
        return bigquery.Client()
    except Exception as e:
        print(f"Error de configuracion: {e}")
        return None

def main():
    client = setup_client()
    if not client:
        return

    try:
        print("Extrayendo datos de BigQuery...")
        df = client.query(QUERY).to_dataframe()
       
        if not df.empty:
            DATA_DIR.mkdir(parents=True, exist_ok=True)
            df.to_parquet(OUTPUT_PATH)
            print(f"Archivo guardado en: {OUTPUT_PATH}")
            print(f"Registros: {len(df)}")
        else:
            print("La consulta no devolvió resultados.")
           
    except Exception as e:
        print(f"Error en el proceso de extraccion: {e}")

if __name__ == "__main__":
    main()