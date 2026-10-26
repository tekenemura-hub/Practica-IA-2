"""Práctica 1 - Predicción del precio de casas en California.
Autores: Sara Ibarz Abella y Edgar Aurich Ballano
"""
from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree

# Todo se guarda en la misma carpeta donde está este script
CARPETA = Path(__file__).resolve().parent

TARGET = "MedHouseVal"
RANDOM_STATE = 42
TEST_SIZE = 0.2
MAX_DEPTH = 5
MAX_DEPTH_LIMITE = 5
MAX_DEPTH_DEFECTO = 3
MODEL_PATH = CARPETA / "modelo_california.pkl"
TREE_IMAGE_PATH = CARPETA / "arbol_decision.png"
AUTORES = "Sara Ibarz Abella y Edgar Aurich Ballano P1"


def cargar_datos() -> pd.DataFrame:
    return fetch_california_housing(as_frame=True).frame


def check_nulls(df: pd.DataFrame):
    """Muestra el número de valores nulos por columna."""
    print("Valores nulos por columna:")
    print(df.isnull().sum())


def handle_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """Descarta las filas con valores nulos."""
    return df.dropna()


def plot_decision_tree(X, y, max_depth=None):
    """Valida max_depth, entrena un árbol y guarda su dibujo en un .png."""
    if max_depth is None or max_depth < 1 or max_depth > MAX_DEPTH_LIMITE:
        print(f"Aviso: max_depth no válido. Usando valor por defecto ({MAX_DEPTH_DEFECTO}).")
        max_depth = MAX_DEPTH_DEFECTO

    model = DecisionTreeRegressor(max_depth=max_depth, random_state=RANDOM_STATE)
    model.fit(X, y)

    plt.figure(figsize=(25, 12), dpi=150)
    plot_tree(model, feature_names=list(X.columns), filled=True, rounded=True, fontsize=8)
    plt.title(AUTORES)
    plt.savefig(TREE_IMAGE_PATH)
    plt.close()
    return model


def compute_errors(y_true, y_pred):
    """Calcula MAE y MSE y los muestra por pantalla."""
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    print(f"MAE: {mae:.4f}")
    print(f"MSE: {mse:.4f}")
    return mae, mse


def build_model(df: pd.DataFrame):
    """Entrena el árbol con los datos de entrenamiento y lo evalúa con los de prueba."""
    X = df.drop(columns=[TARGET])
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )
    model = DecisionTreeRegressor(max_depth=MAX_DEPTH, random_state=RANDOM_STATE)
    model.fit(X_train, y_train)
    compute_errors(y_test, model.predict(X_test))
    return model


def main():
    df = cargar_datos()

    # Ejercicio 3: nulos
    check_nulls(df)
    df = handle_nulls(df)

    # Ejercicio 4 y 5: dibujo del árbol
    plot_decision_tree(df.drop(columns=[TARGET]), df[TARGET], max_depth=None)

    # Ejercicio 7: entrenar, evaluar y guardar
    model = build_model(df)
    joblib.dump(model, MODEL_PATH)

    print()
    print("Archivos guardados en:", CARPETA)
    print(" -", MODEL_PATH.name)
    print(" -", TREE_IMAGE_PATH.name)
    print(AUTORES)


if __name__ == "__main__":
    main()