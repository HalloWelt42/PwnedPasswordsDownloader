from flask import Flask, request, jsonify, render_template
from flasgger import Swagger
import hashlib
import os

app = Flask(__name__, template_folder="templates")
swagger = Swagger(app)

HASH_DIR = "./hashes"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check_password():
    """
    Check if a password exists in the local Pwned Passwords hash database.
    ---
    parameters:
      - name: password
        in: body
        required: true
        schema:
          type: object
          properties:
            password:
              type: string
              example: "123456"
    responses:
      200:
        description: Check result
        schema:
          type: object
          properties:
            found:
              type: boolean
            count:
              type: integer
    """
    data = request.get_json()
    password = data.get("password")
    if not password:
        return jsonify({"error": "No password provided"}), 400

    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    path = os.path.join(HASH_DIR, prefix + ".txt")

    if not os.path.exists(path):
        return jsonify({"found": False, "count": 0})

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if ':' in line:
                h, count = line.strip().split(':')
                if h.upper() == suffix:
                    return jsonify({"found": True, "count": int(count)})

    return jsonify({"found": False, "count": 0})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
