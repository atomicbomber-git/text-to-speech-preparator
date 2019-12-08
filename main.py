from flask import Flask, jsonify, request
from preprocessor import preprocess
from tagger import tag
from chunker import chunk
from normalizer import normalize
from flask_cors import CORS
import waitress

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def process():

    # Mengakses data form dari request HTTP
    text = request.form.get("text", "") 
    
    # Melakukan preprocessing
    text = preprocess(text)

    # Melakukan tagging
    text = tag(text, "http://localhost:7000")
    
    # Melakukan chunking
    text = chunk(text)

    # Melakukan proses normalisasi
    text = normalize(text)

    # Membuat response HTTP dengan format JSON yang berisi teks yang telah diproses
    return jsonify({
        "status": "success",
        "message": "Request successful",
        "data": {
            "text": text
        }
    })

# Menjalankan server
waitress.serve(app, host="0.0.0.0", port=8070)
