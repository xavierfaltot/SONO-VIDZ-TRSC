# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, send_from_directory
from faster_whisper import WhisperModel
import tempfile
import os

BASE = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
model = WhisperModel("small", device="cpu", compute_type="int8")

@app.get("/")
def home():
    return send_from_directory(BASE, "index.html")

@app.get("/SONO-VIDZ-TRSC-logo.jpg")
def logo():
    return send_from_directory(BASE, "SONO-VIDZ-TRSC-logo.jpg")

@app.post("/transcribe")
def transcribe():
    if "file" not in request.files:
        return jsonify(error="NO FILE"), 400

    uploaded = request.files["file"]
    ext = os.path.splitext(uploaded.filename or "audio")[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        uploaded.save(tmp.name)
        path = tmp.name

    try:
        segments, info = model.transcribe(
            path,
            beam_size=5,
            vad_filter=True
        )
        return jsonify(
            text="\n".join(s.text.strip() for s in segments),
            language=info.language
        )
    except Exception as exc:
        return jsonify(error=str(exc)), 500
    finally:
        try:
            os.remove(path)
        except OSError:
            pass

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8777, debug=False)
