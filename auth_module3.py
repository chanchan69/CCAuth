from cryptography.fernet import Fernet
import requests
import hashlib
import sys
from time import sleep
import random
import string

aid = ''
client_secret = ''
apikey = ''
def authenticate(username, password, hwid):
    if int(len(password)) == 0 or int(len(username)) == 0:
        return 'Error: Invalid User or password'
    
    f = Fernet(client_secret)

    sessionID = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(40)))
    payload = f.encrypt(f'{username}:{password}:{hwid}:{sessionID}'.encode())

    s = requests.get(url=f'https://ccauth.pythonanywhere.com/api/v2/authenticate?key={apikey}', headers={"data": payload, "aid": aid}).text.encode()
    #This one for no hash ^
    #s = requests.get(url=f'https://ccauth.pythonanywhere.com/api/v2/authenticate?key={apikey}', headers={"data": payload, "aid": aid, "hash": Get_Hash()}).text.encode()
    #This one for hash ^
    
    try:
        r = str(f.decrypt(s))
    except:
        if 'Error: Invalid Hash' in str(s):
            return '4'
        else:
            return 'Error: Critical Error'

    if f'{username}:{password} is authenticated {sessionID}' in r:
        return '0'
    elif f'{username}:{password} has wrong hwid' in r:
        return '1'
    elif f'{username}:{password} has wrong username or password' in r:
        return '2'
    elif 'Error: Bad Everything' in r:
        return '3'
    else:
        return 'error'

def register(username, password, hwid, discordid, registerkey):
    if int(len(password)) == 0 or int(len(username)) == 0:
        return 'Error: Invalid User or password'
    
    s = requests.get(url=f'https://ccauth.pythonanywhere.com/api/v1/register?key={apikey}', headers={"user": username, "pass": password, "hwid": hwid, "regkey": registerkey, "discord": discordid, "aid": aid}).text.encode()
    f = Fernet(client_secret)
    try:
        r = str(f.decrypt(s))
    except:
        return 'Error: Critical Error'

    if f'{username}:{password} registered successfuly' in r:
        return '0'
    elif 'bad key' in r:
        return '1'
    else:
        return 'Error: Critical Error' 

def hwid_change(username, password, hwid, hwidresetkey):
    if int(len(password)) == 0 or int(len(username)) == 0:
        return 'Error: Invalid User or password'
    s = requests.get(url=f'https://ccauth.pythonanywhere.com/api/v2/reset?key={apikey}', headers={"user": username, "pass": password, "newhwid": hwid, "aid": aid, "hwidresetkey": hwidresetkey}).text.encode()
    f = Fernet(client_secret)
    try:
        r = str(f.decrypt(s))
    except:
        if 'Error: HWID Resets no Enabled' in str(s):
            return '3'
        elif 'Error: Invalid Key' in str(s):
            return '4'
        elif 'Error: Already reset today' in str(s):
            return '5'
        else:
            return s

    if f'{username}:{password} hwid updated successfuly' in r:
        return '0'
    elif 'Error: Bad Combo' in r:
        return '1'
    elif 'Error: An Error Has Occured' in r:
        return '2'
    else:
        return 'error'

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

