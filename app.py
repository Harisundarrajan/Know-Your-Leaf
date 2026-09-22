import os
from flask import Flask, render_template, request, jsonify
from model import predict, disease_db, detect_dominant_color, chat_response

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/')
def index():
    plants = list(disease_db.keys())
    colors = ["green", "yellow", "brown", "white"]
    return render_template('index.html', plants=plants, colors=colors)


@app.route('/predict', methods=['POST'])
def predict_route():
    plant_name = request.form.get('plant', '')
    leaf_color = request.form.get('color', '')
    result = predict(plant_name, leaf_color)
    return jsonify({"result": result, "plant": plant_name, "color": leaf_color})


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    filename = file.filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    color = detect_dominant_color(filepath)
    return jsonify({"color": color, "filename": filename})


@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message', '')
    response = chat_response(message)
    return jsonify({"response": response})   
if __name__ == '__main__':
    app.run(debug=True)   