from flask import Flask, request
import requests

app = Flask(__name__)

SERVICES = {
    "auth": "http://auth-service:5001",
    "tools": "http://tools-service:5002",
    "billing": "http://billing-service:5003",
    "analytics": "http://analytics-service:5004"
}


@app.route("/api/auth/<path:path>", methods=["GET", "POST"])
def auth_proxy(path):

    url = f"{SERVICES['auth']}/{path}"

    response = requests.request(
        method=request.method,
        url=url,
        json=request.get_json()
    )

    return response.json()
