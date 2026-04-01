import os
from google.cloud import bigquery

FILE_NAME='test.parquet' # Puedes cambiar este
PATH='../data/raw/'+FILE_NAME

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../citibike-analysis-fa61.json"
cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

if not cred_path or not os.path.exists(cred_path):
    print("Archivo de credenciales (.json) no encontrado:", cred_path)
else:
  client = bigquery.Client()
      
  query = """
  SELECT
    tripduration,
    starttime,
    bikeid
  FROM
    `bigquery-public-data.new_york_citibike.citibike_trips`
  WHERE
    EXTRACT(YEAR FROM starttime) = 2017
  LIMIT 10;
  """

  df = client.query(query).to_dataframe()
  try:
    df.to_parquet(PATH)
    print(f'Datos obtenidos en el directorio: data/raw/{FILE_NAME}')
  except Exception as e:
    print(f'Directorio de guardado no existe:', PATH)