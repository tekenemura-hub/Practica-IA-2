import os
import urllib.request
import joblib
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

MODEL_PATH = 'modelo_california.pkl'
# IMPORTANTE: Sustituye esta URL por el enlace 'Raw' de tu modelo_california.pkl en GitHub
GITHUB_RAW_URL = 'URL_RAW_GITHUB_AQUI'

# Apartado 8: Descarga del modelo desde GitHub
if not os.path.exists(MODEL_PATH):
    print(f"Modelo {MODEL_PATH} no encontrado. Descargando desde GitHub...")
    try:
        urllib.request.urlretrieve(GITHUB_RAW_URL, MODEL_PATH)
        print("Descarga completada con éxito.")
    except Exception as e:
        print(f"Error al descargar el modelo: {e}")

try:
    modelo = joblib.load(MODEL_PATH)
except:
    modelo = None

# Apartado 4: Endpoint Health-check
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "Servicio de Edgar y Sara activo", "modelo": "California Housing"})

# Apartado 4: Endpoint de predicción
@app.route('/predict', methods=['POST'])
def predict():
    if not modelo:
        return jsonify({"error": "Modelo no cargado"}), 500
    try:
        datos = request.get_json()
        df = pd.DataFrame([datos])
        prediccion = modelo.predict(df)
        return jsonify({"prediccion": prediccion.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
