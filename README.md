# Practica-IA-2
Edgar y Sara Práctica 2

## Pasos seguidos para el despliegue
1. **Cuenta:** creamos una cuenta gratuita en [render.com](https://render.com).
2. **Repositorio:** subimos a GitHub (repositorio público) `Californiahousing.py`, `modelo_california.pkl`, `app.py` y `requirements.txt`.
3. **Servicio:** en Render creamos un *Web Service* y lo conectamos al repositorio, rama `main`.
4. **Build Command:** `pip install -r requirements.txt`
5. **Start Command:** `gunicorn app:app`
6. **Auto-Deploy:** activado "On Commit"; cada cambio en `main` redespliega el servicio.

## Uso
- Health-check: `GET /` devuelve `{"status":"ok"}`.
- Predicción: `POST /predict` con un JSON con las 8 variables (`MedInc`, `HouseAge`, `AveRooms`, `AveBedrms`, `Population`, `AveOccup`, `Latitude`, `Longitude`) devuelve `MedHouseVal`.

## URL final
https://practica-ia-2.onrender.com/
