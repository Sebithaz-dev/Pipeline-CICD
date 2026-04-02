import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR.parent / "data" / "raw" / "test.parquet"

def load_and_display():
    """Carga el archivo parquet y muestra un resumen tecnico."""
    if not DATA_PATH.exists():
        print(f"Error: Archivo no encontrado en {DATA_PATH}")
        return

    try:
        df = pd.read_parquet(DATA_PATH)
       
        print("--- Resumen de Datos ---")
        print(f"Registros totales: {len(df)}")
        print(f"Columnas: {', '.join(df.columns)}")
        print("\n--- Vista Previa ---")
        print(df.head())
       
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

if __name__ == "__main__":
    load_and_display()
