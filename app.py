from flask import Flask, request, jsonify
from transformers import pipeline
import torch

app = Flask(__name__)

# Load pre-trained sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Sentiment Analysis API!",
        "usage": {
            "POST /predict-text": "Send JSON body: { 'text': 'your text here' }"
        }
    })

@app.route("/predict-text", methods=["POST"])
def predict_text():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON with a 'text' field"}), 400

    data = request.get_json()
    input_text = data.get("text", None)
    if not input_text:
        return jsonify({"error": "Missing 'text' field in JSON"}), 400

    try:
        prediction = sentiment_pipeline(input_text)[0]
        return jsonify({
            "input": input_text,
            "prediction": {
                "label": prediction["label"],
                "score": round(float(prediction["score"]), 4)
            }
        })
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)