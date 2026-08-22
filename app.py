import logging
import os

from flask import Flask, render_template
import requests

API_URL = os.getenv("NASA_APOD_API_URL", "https://api.nasa.gov/planetary/apod")
API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")

app = Flask(__name__)


@app.get("/healthz")
@app.get("/apod/healthz")
def healthz():
    return {"status": "ok"}, 200


@app.get("/")
@app.get("/apod/")
def apod():
    params = {
        "api_key": API_KEY,
    }

    try:
        resp = requests.get(API_URL, params=params, timeout=5)
        resp.raise_for_status()
        data = resp.json()
    except (requests.RequestException, ValueError):
        logging.exception("Unable to retrieve NASA Astronomy Picture of the Day")
        return render_template(
            "index.html",
            error="NASA's Astronomy Picture of the Day is temporarily unavailable.",
            data=None,
        )

    return render_template("index.html", error=None, data=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
