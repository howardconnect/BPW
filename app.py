from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route("/")
def serve_index():
    return send_from_directory(".", "index.html")

@app.route("/static/<path:path>")
def serve_static(path):
    return send_from_directory("static", path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 👈 Reads from env variable
    app.run(host="0.0.0.0", port=port)
