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
license_key = "user inputed license key"
contact_method = "user inputed contact method (email discord etc)"

payload = {"username": username, "password": password, "hwid": hwid, "aid": aid, "key": api_key, "license": license_key, "contact": contact_method}

h = hmac.new(secret, json.dumps(payload).encode("utf-8"), digestmod=hashlib.sha256).hexdigest()

r = requests.post("https://api.ccauth.app/api/v4/register", headers={"X-CCAuth-Signature": h}, json=payload)

is_verified = verify_hmac(r.text.encode(), r.headers["X-CCAuth-Signature"], secret)

r = r.json()

if r["success"]:
    if is_verified:
        print("registered")
    else:
        print("invalid hmac")
else:
    if r["errorDetails"]["type"] == "invalid license":
        print("invalid registration key")
    elif r["errorDetails"]["type"] == "settings":
        print("registration is disabled")
    else:
        print(r["errorDetails"]["type"])
