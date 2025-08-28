# app.py (Flask starter)

from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load saved model
with open("/Users/paramshah/Desktop/bootcamp/homework/stage13_productization/notebooks/soxx_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # expect {"features": [[...]]}
    X = pd.DataFrame(data["features"])
    preds = model.predict(X).tolist()
    return jsonify({"predictions": preds})


if __name__ == "__main__":
    app.run(debug=True)
