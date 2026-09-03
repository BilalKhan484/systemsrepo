from flask import Flask, jsonify, render_template
import os
from datetime import datetime, timezone

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        app_name="CI/CD Dashboard",
        environment=os.getenv("ENVIRONMENT", "Development"),
        version=os.getenv("APP_VERSION", "1.0.0"),
        commit=os.getenv("GIT_COMMIT", "local"),
        deployed_at=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    )


@app.route("/health")
def health():
    return jsonify(
        status="healthy",
        application="CI/CD Dashboard",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)