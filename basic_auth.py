import requests
import hmac
import hashlib
import json
import subprocess
import random


def verify_hmac(raw_body, client_signature: str, hmac_secret: bytes) -> bool:
    computed_sha = hmac.new(hmac_secret,
                            raw_body,
                            digestmod=hashlib.sha256).hexdigest()  # make sure to use sha256 otherwise ccauth will not be able to verify your request
    return computed_sha == client_signature


secret = b"your hmac client secret"
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
username = "chanchan"
password = "suchstrongpassword"
aid = "your aid"
api_key = "your api key"
nonce = random.randint(1000000000, 1000000000000)

payload = {"username": username, "password": password, "hwid": hwid, "aid": aid, "key": api_key, "nonce": nonce}  # add the hash key if ya wanna check hash

h = hmac.new(secret, json.dumps(payload).encode("utf-8"), digestmod=hashlib.sha256).hexdigest()  # make sure to use sha256 otherwise ccauth will not be able to verify your request

r = requests.post("http://api.ccauth.app/api/v4/authenticate", headers={"X-CCAuth-Signature": h}, json=payload)

is_verified = verify_hmac(r.text.encode(), r.headers["X-CCAuth-Signature"], secret)  # returns false if response has been tampered with or was signed with an invalid secret

r = r.json()

if r["success"] and r["nonce"] == nonce:   # make sure to check that the nonce in the response matches the nonce you sent in the request
    if is_verified:
        if not r["licenseInfo"]["expired"]:
            print("authenticated")
        else:
            print("expired")
    else:
        print("invalid hmac sig")
else:
    if r["errorDetails"]["type"] == "credentials":
        print("invalid user/pass")
    elif r["errorDetails"]["type"] == "hwid":
        print("invalid hwid")
    else:
        print(r["errorDetails"]["type"])
