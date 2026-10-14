from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    environment = os.getenv("APP_ENV", "development")

    return f"""
    <h1>🐳 Hello from Docker!</h1>
    <p>My Python application is running inside a container.</p>
    <p>Environment: {environment}</p>
"""

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
