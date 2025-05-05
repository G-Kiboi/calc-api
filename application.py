from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv

# Load the .env file based on APP_ENV
env_file = os.environ.get("APP_ENV", ".env")
env_path = os.path.join(os.getcwd(), env_file)
load_dotenv(env_path)

# DEBUG prints
print("Loaded from:", env_file)
print("ENV value:", os.getenv("ENV"))
print("DEBUG value:", os.getenv("DEBUG"))

# Flask app setup
application = Flask(__name__)
app.config["ENV"] = os.getenv("ENV", "development")
app.config["DEBUG"] = os.getenv("DEBUG", "False") == "True"


@app.route("/env")
def env_info():
    return jsonify({
        "environment": app.config["ENV"],
        "debug": app.config["DEBUG"]
    })

@app.route("/add")
def add():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"result": a + b})

@app.route("/subtract")
def subtract():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"result": a - b})

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
