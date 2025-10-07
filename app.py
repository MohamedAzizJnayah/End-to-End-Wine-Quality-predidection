from flask import Flask, render_template, request
from ML_Project.pipeline import prediction
import pandas as pd
from ML_Project.pipeline.prediction import PredictionPipeline  # import ton module prediction

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")  # vérifie le nom exact du fichier

@app.route("/predict", methods=['POST','GET'])
def predict_wine():
    try:
        # 1️ Récupérer les valeurs du formulaire
        features = {
            "fixed acidity": float(request.form["fixed_acidity"]),
            "volatile acidity": float(request.form["volatile_acidity"]),
            "citric acid": float(request.form["citric_acid"]),
            "residual sugar": float(request.form["residual_sugar"]),
            "chlorides": float(request.form["chlorides"]),
            "free sulfur dioxide": float(request.form["free_sulfur_dioxide"]),
            "total sulfur dioxide": float(request.form["total_sulfur_dioxide"]),
            "density": float(request.form["density"]),
            "pH": float(request.form["pH"]),
            "sulphates": float(request.form["sulphates"]),
            "alcohol": float(request.form["alcohol"])
        }
        # 2️ Convertir en DataFrame pour sklearn
        
        df = pd.DataFrame([features])
        df["Id"] = 0  # shape = (1, n_features)
        model=PredictionPipeline()
        # 3️ Charger le modèle et prédire
        pred = model.predict(df)

        # 4️ Retourner le résultat
        return render_template("results.html", prediction=pred[0])

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
