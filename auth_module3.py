from cryptography.fernet import Fernet
import requests
import hashlib
import sys
from time import sleep
import random
import string
from json import loads

aid = ''
client_secret = ''
apikey = ''
def authenticate(username, password, hwid):
    if int(len(password)) == 0 or int(len(username)) == 0:
        return 'Error: Invalid User or password'
    
    f = Fernet(client_secret)

    sessionID = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(40)))
    payload = '{"username": "' + username + '", "password": "' + password + '", "hwid": "' + hwid + '", "sessionID": "' + sessionID + '"}'
    payload = f.encrypt(payload.encode())

    s = requests.get(url=f'https://api.ccauth.app/api/v3/authenticate?key={apikey}', headers={"data": payload.decode(), "aid": aid}).text
    #This one for no hash ^
    #s = requests.get(url=f'https://api.ccauth.app/api/v3/authenticate?key={apikey}', headers={"data": payload, "aid": aid, "hash": Get_Hash()}).text.encode()
    #This one for hash ^
    
    try:
        r = str(f.decrypt(s.encode()).decode())
        r = loads(r)
    except:
        r = loads(s)
        if eval(r["error"]):
            print('an error has occurred because:')
            print(r["type"])
            return 'error'
        else:
            print(r)
            return 'error'

    if eval(r["is_Authenticated"]) and eval(r["session_ID"]) == sessionID:
        return '0'
    elif eval(r["invalid_hwid"]) and eval(r["invalid_credentials"]):
        return '3'
    elif eval(r["invalid_credentials"]) and not eval(r["invalid_hwid"]):
        return '2'
    elif not eval(r["invalid_credentials"]) and eval(r["invalid_hwid"]):
        return '1'
    elif eval(r["expired_license"]):
        return '4'
    else:
        return 'error'

def register(username, password, hwid, discordid, registerkey):
    if int(len(password)) == 0 or int(len(username)) == 0:
        return 'Error: Invalid User or password'
    
    r = requests.get(url=f'https://api.ccauth.app/api/v2/register?key={apikey}', headers={"user": username, "pass": password, "hwid": hwid, "regkey": registerkey, "discord": discordid, "aid": aid}).json()

    if not eval(r["error"]):
        if eval(r["success"]):
            return '0'
        elif not eval(r["registration_enabled"]):
            print('reg not enabled')
        elif eval(r["invalid_key"]):
            return '1'
        elif eval(r["max_users"]):
            print('max users')
        else:
            return 'Error: Critical Error'
    else:
        print(r["error"])

def hwid_change(username, password, hwid, hwidresetkey):
    if int(len(password)) == 0 or int(len(username)) == 0:
        return 'Error: Invalid User or password'
    r = requests.get(url=f'https://api.ccauth.app/api/v3/reset?key={apikey}', headers={"user": username, "pass": password, "newhwid": hwid, "aid": aid, "hwidresetkey": hwidresetkey}).json()

    if not eval(r["error"]):
        if eval(r["success"]):
            return '0'
        elif not eval(r["hwid_resets"]):
            return '3'
        elif eval(r["invalid_key"]):
            return '4'
        elif eval(r["reset_today"]):
            return '5'
        elif eval(r["invalid_credentials"]):
            return '1'
        else:
            return 'error'
    else:
        print(r["error"])

def Get_Hash() -> str:
    hash = ""
    BUF_SIZE = 65536
    md5 = hashlib.md5()
    try:
        with open(sys.argv[0], "rb") as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                md5.update(data)
        return (md5.hexdigest())
    except Exception:
        return

