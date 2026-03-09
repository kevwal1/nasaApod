import os

from flask import Flask, render_template
import requests

API_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")

app = Flask(__name__)


@app.route("/")
def apod():
    params = {
        "api_key": API_KEY,
    }

    try:
        resp = requests.get(API_URL, params=params, timeout=5)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return render_template("index.html", error=str(e), data=None)

    return render_template("index.html", error=None, data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

