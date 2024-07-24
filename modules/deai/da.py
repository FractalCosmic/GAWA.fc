import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

MODELS_DIR = 'models/'

@app.route('/upload_model', methods=['POST'])
def upload_model():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        filename = file.filename
        file.save(os.path.join(MODELS_DIR, filename))
        return jsonify({"message": "Model uploaded successfully"}), 200

@app.route('/list_models', methods=['GET'])
def list_models():
    models = os.listdir(MODELS_DIR)
    return jsonify({"models": models}), 200

@app.route('/evaluate_model/<model_name>', methods=['POST'])
def evaluate_model(model_name):
    # 这里应该实现模型评估逻辑
    evaluation_result = {"accuracy": 0.95, "f1_score": 0.92}
    return jsonify(evaluation_result), 200

if __name__ == '__main__':
    app.run(debug=True)
