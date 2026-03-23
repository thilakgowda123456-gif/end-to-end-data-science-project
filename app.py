rom flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("task 3\model.pkl")
scaler = joblib.load("task 3\scaler.pkl")

@app.route("/")
def home():
    return "ML Model API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = np.array([
        data["age"],
        data["salary"]
    ]).reshape(1, -1)

    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)

    return jsonify({
        "prediction": int(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)
