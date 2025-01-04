from dbm import error

from flask import Flask, request, jsonify, send_from_directory
from fileProcessing import file_to_array, FileProcessingException

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory("static", "index.html")


@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        # Expecting files to be sent as part of a FormData request
        files = request.files.getlist('files')  # Multiple files uploaded
        if not files:
            return jsonify({"error": "No files provided"}), 400

        # Delegate to processor module
        results = file_to_array(files)
        return jsonify({"message" :results})
    except FileProcessingException as e:
        return jsonify({"error": e.args[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
