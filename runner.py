from flask import Flask, request, jsonify
import subprocess
from pathlib import Path

app = Flask(__name__)
AUTOCODER_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = AUTOCODER_DIR / "autofile"

@app.route("/run", methods=["POST"])
def run_autocoder():
    data = request.get_json()
    if not data or "prompt" not in data:
        return jsonify({"error": "Missing 'prompt' in request body"}), 400

    prompt = data["prompt"]

    try:
        subprocess.run(
            ["python3", "main.py", prompt],
            cwd=AUTOCODER_DIR,
            capture_output=True,
            text=True,
            timeout=60
        )

        files = sorted(OUTPUT_DIR.glob("generated_code_*.py"), key=lambda f: f.stat().st_mtime, reverse=True)
        if not files:
            return jsonify({"status": "failed", "message": "No generated files found."}), 500

        latest_file = files[0]
        with open(latest_file, "r") as f:
            code = f.read()

        result = subprocess.run(
            ["python3", str(latest_file)],
            capture_output=True,
            text=True,
            timeout=10
        )

        return jsonify({
            "status": "success",
            "filename": str(latest_file),
            "code": code,
            "output": result.stdout,
            "error": result.stderr
        })

    except subprocess.TimeoutExpired:
        return jsonify({"error": "Code generation or execution timed out"}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5005, debug=True)
