from flask import Flask, jsonify
import config

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "message": "Welcome to a Simple Flask App's API",
        "note": "This service shows how configuration is used"
    })

@app.route("/whoami")
def whoami():
    return jsonify({
        "service": "simple-api",
        "api_key_preview": config.API_KEY[:8] + "..." if config.API_KEY else None
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
