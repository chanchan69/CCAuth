import requests
import hmac
import hashlib
import json
import subprocess


def verify_hmac(raw_body, client_signature: str, hmac_secret: bytes) -> bool:
    computed_sha = hmac.new(hmac_secret,
                            raw_body,
                            digestmod=hashlib.sha256).hexdigest()
    return computed_sha == client_signature


secret = b"your hmac client secret"
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
username = "chanchan"
password = "suchstrongpassword"
aid = "your aid"
api_key = "your api key"
reset_key = "user inputed reset key"

payload = {"username": username, "password": password, "hwid": hwid, "aid": aid, "key": api_key, "resetKey": reset_key}

h = hmac.new(secret, json.dumps(payload).encode("utf-8"), digestmod=hashlib.sha256).hexdigest()

r = requests.post("http://127.0.0.1:5000/api/v4/reset", headers={"X-CCAuth-Signature": h}, json=payload)

is_verified = verify_hmac(r.text.encode(), r.headers["X-CCAuth-Signature"], secret)

r = r.json()

if r["success"]:
    if is_verified:
        print("reset")
    else:
        print("invalid hmac")
else:
    if r["errorDetails"]["type"] == "invalid key":
        print("invalid reset key")
    elif r["errorDetails"]["type"] == "settings":
        print("hwid resets are disabled")
    elif r["errorDetails"]["type"] == "reseting too fast":
        print("reset hwid in last 24 hours")
    else:
        print(r["errorDetails"]["type"])
