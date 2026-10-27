# Practica-IA-2
Edgar y Sara Práctica 2

## Pasos para desplegar la aplicacion

1. Creamos una cuenta gratuita en Render (render.com).
2. Subimos el proyecto a un repositorio publico de GitHub con el codigo de Python, el modelo modelo_california.pkl, app.py y requirements.txt.
3. En Render creamos un Web Service y lo conectamos al repositorio de GitHub, rama main.
4. Comando de build: pip install -r requirements.txt
5. Comando de arranque (despliegue): gunicorn app:app
6. Dejamos activado el auto-deploy, asi cada cambio en GitHub se despliega solo.

## Para probar la aplicacion
- GET / devuelve {"status":"ok"} (health-check).
- POST /predict recibe los datos de una vivienda en JSON y devuelve el valor predicho (MedHouseVal).

## URL final
https://practica-ia-2.onrender.com/
