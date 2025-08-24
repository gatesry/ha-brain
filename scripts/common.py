import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()  # loads .env if present

HA_URL = os.environ.get("HA_URL", "").rstrip("/")
HA_TOKEN = os.environ.get("HA_TOKEN", "")

if not HA_URL:
    raise SystemExit("❌ HA_URL is not set. Add it to your .env")
if not HA_TOKEN:
    raise SystemExit("❌ HA_TOKEN is not set. Add it to your .env")

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "content-type": "application/json"
}

def _url(path: str) -> str:
    path = path.lstrip("/")
    if not path.startswith("api/"):
        path = f"api/{path}"
    return f"{HA_URL}/{path}"

def get(endpoint: str):
    url = _url(endpoint)
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()

def post(endpoint: str, payload: dict):
    url = _url(endpoint)
    r = requests.post(url, headers=HEADERS, json=payload or {}, timeout=30)
    r.raise_for_status()
    try:
        return r.json()
    except ValueError:
        return {"status": "ok", "http_status": r.status_code}

def pretty(obj) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)
