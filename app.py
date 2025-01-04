from flask import Flask, send_from_directory, jsonify, request
from fileProcessing import file_to_string

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400


    try:
        result = file_to_string(file)
        return jsonify({"message": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500




if __name__ == "__main__":
    app.run(debug=True)
