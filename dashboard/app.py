from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)
log_file = "dashboard/data.json"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    if os.path.exists(log_file):
        with open(log_file) as f:
            data = json.load(f)
    else:
        data = []
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
