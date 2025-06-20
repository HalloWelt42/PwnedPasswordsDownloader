from flask import Flask, request, jsonify
import hashlib
import os

HASH_DIR = "hashes"  # Ordner, in dem die 5-stelligen Präfix-Dateien gespeichert sind

app = Flask(__name__)

def check_password(password):
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    hash_file = os.path.join(HASH_DIR, f"{prefix}.txt")

    if not os.path.exists(hash_file):
        return {"found": False, "count": 0, "note": "Prefix nicht vorhanden"}

    with open(hash_file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if ':' in line:
                hash_suffix, count = line.strip().split(':', 1)
                if hash_suffix.upper() == suffix:
                    return {"found": True, "count": int(count)}

    return {"found": False, "count": 0}

@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    password = data.get("password")
    if not password:
        return jsonify({"error": "Passwort fehlt"}), 400
    result = check_password(password)
    return jsonify(result)

@app.route("/", methods=["GET"])
def index():
    return '''
    <form method="post" action="/check" onsubmit="event.preventDefault(); fetch('/check', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({password: document.getElementById('pw').value})
    }).then(res => res.json()).then(data => alert(JSON.stringify(data)))">
        <input type="password" id="pw" placeholder="Passwort eingeben" required>
        <button type="submit">Prüfen</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
