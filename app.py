from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "mensaje": "Entorno funcionando correctamente",
        "curso": "Gestion de datos para IA"
    }

@app.route("/status")
def status():
    return {
        "status": "ok"
    }

if __name__ == "__name__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
