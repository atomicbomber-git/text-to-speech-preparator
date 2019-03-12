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

    text = request.form.get("text", "")
    text = preprocess(text)
    text = tag(text, "http://localhost:7000")
    text = chunk(text)
    text = normalize(text)

    return jsonify({
        "status": "success",
        "message": "Request successful",
        "data": {
            "text": text
        }
    })


waitress.serve(app, host="0.0.0.0", port=8070)
