from ctypes import windll
from yaml import safe_load
from os import path, system
import requests

def config():
    ConfigData = '''
Admin_Panel:
    admin_username:
    admin_password:
    aid: 
    apikey: 
'''

    if path.exists("config.yml"):
        config = safe_load(open('config.yml', 'r'))
        global username
        username = str(config["Admin_Panel"]["admin_username"])
        global password
        password = str(config["Admin_Panel"]["admin_password"])
        global aid
        aid = str(config["Admin_Panel"]["aid"])
        global apikey
        apikey = str(config["Admin_Panel"]["apikey"])
    else:
        open('config.yml', 'w', encoding='utf-8', errors="ignore").write(ConfigData)
        exit(0)

config()

class AdminPanel:
    def __init__(self):
        self.auth = CCAUth(apikey, username, password, aid)
        self.get_stats()
        while True:
            a = input(f'[1] Get Key\n[2] Get log\n[3] Get Databse\n[4] Enable/Disable HWID Resets\n[5] Enable/Disable Registration\n[6] Enable/Disable Use Hash\n[7] Change Hash\n[8] Change Version\n[9] Change Annoucment\n[10] Get HWID Reset Key\n')
            system('cls')
            if a == '1':
                self.get_key()
            elif a == '2':
                self.get_log()
            elif a == '3':
                self.get_database()
            elif a == '4':
                self.change_hwid_reset()
            elif a == '5':
                self.change_registration_status()
            elif a == '6':
                self.change_hash_status()
            elif a == '7':
                self.change_hash()
            elif a == '8':
                self.change_version()
            elif a == '9':
                self.change_announcement()
            elif a == '10':
                self.get_hwid_key()
            else:
                continue
            input('press any key to continue')
            system('cls')

    def get_key(self):
        a = input('Timed or Lifetime (1/2): ')
        if a == '1':
            time = input('How Long (1d, 1w, 1m, 12d, 17w, 69m): ')
            typeb = input('Account Type (blank for none): ')
            error, key = self.auth.get_key('timed', typeb, time)
        elif a == '2':
            typeb = input('Account Type (blank for none): ')
            error, key = self.auth.get_key('lifetime', typeb)
        else:
            print('invalid option')
            return

        if not error:
            print("key: " + key)
        else:
            print(key)
        return

    def get_hwid_key(self):
        a = input('discord name: ')
        error, key = self.auth.get_hwid_key(a)
        if not error:
            print("key: " + key)
            return
        else:
            print(key)
        return

    def get_stats(self):
        error, name, signins, users, teir = self.auth.get_stats()
        if not error:
            windll.kernel32.SetConsoleTitleW(f'{name} | Signins: {signins} | Users: {users} | Plan: {teir}')
        else:
            print(name)
        return

    def get_log(self):
        error, log = self.auth.get_log()
        if not error:
            print("log: \n" + log)
        else:
            print(log)
        return

    def get_database(self):
        error, db = self.auth.get_database()
        if not error:
            print("database: \n" + db)
        else:
            print(db)
        return

    def change_hwid_reset(self):
        error, status = self.auth.change_hwid_status()
        if not error:
            print('HWID Resets: ' + status)
        else:
            print(status)
        return

    def change_registration_status(self):
        error, status = self.auth.change_registration_status()
        if not error:
            print('Registration: ' + status)
        else:
            print(status)
        return

    def change_hash_status(self):
        error, status = self.auth.change_hash_status()
        if not error:
            print('Use Hash: ' + status)
        else:
            print(status)
        return

    def change_hash(self):
        a = input('New Hash: ')
        error, hasha = self.auth.change_hash(a)
        if not error:
            print('Hash Changed To: ' + hasha)
        else:
            print(hasha)
        return

    def change_version(self):
        a = input('New Version: ')
        error, ver = self.auth.change_version(a)
        if not error:
            print('Version Changed To: ' + ver)
        else:
            print(ver)
        return

    def change_announcement(self):
        a = input('New Announcement: ')
        error, anc = self.auth.change_announcement(a)
        if not error:
            print('Announcement Changed To: ' + anc)
        else:
            print(anc)
        return

class CCAUth:
    def __init__(self, api_key, username, password, aid):
        self.user = username
        self.password = password
        self.api_key = api_key
        self.aid = aid

    def get_key(self, type1,  typea, timea=''):
        try:
            headers = {
                "user": self.user,
                "pass": self.password,
                "aid": self.aid,
                "data": '{"type": "' + type1 + '", "time": "' + timea + '"}',
                "userType": typea
            }
            r = requests.get(f'https://api.ccauth.app/api/v3/getkey?key={self.api_key}', headers=headers).json()

            if eval(r["success"]):
                return False, r["key"]
            else:
                return True, 'an error has occurred: ' + str(r["reason"])

        except Exception as ex:
            return True, 'an error has occurred: ' + str(ex)

    def get_hwid_key(self, discord):
        try:
            headers = {
                "user": self.user,
                "pass": self.password,
                "aid": self.aid,
                "discord": discord
            }
            r = requests.get(f'https://api.ccauth.app/api/v2/gethwidkey?key={self.api_key}', headers=headers).json()

            if eval(r["success"]):
                return False, r["key"]
            else:
                return True, 'an error has occurred: ' + str(r["reason"])

        except Exception as ex:
            return True, 'an error has occurred: ' + str(ex)

    def get_stats(self):
        try:
            headers = {
                "user": self.user,
                "pass": self.password,
                "aid": self.aid
            }
            r = requests.get(f'https://api.ccauth.app/api/v2/getstats?key={self.api_key}', headers=headers).json()

            if eval(r["success"]):
                return False, r["app_name"], r["signins"], r["users"], r["plan"]
            else:
                return True, 'an error has occurred: ' + str(r["reason"]), '', '', ''

        except Exception as ex:
            return True, 'an error has occurred: ' + str(ex), '', '', ''

    def get_log(self):
        try:
            headers = {
                "user": self.user,
                "pass": self.password,
                "aid": self.aid
            }
            r = requests.get(f'https://api.ccauth.app/api/v2/getlog?key={self.api_key}', headers=headers).json()

            if eval(r["success"]):
                return False, r["log"]
            else:
                return True, 'an error has occurred: ' + str(r["reason"])

        except Exception as ex:
            return True, 'an error has occurred: ' + str(ex)

    def get_database(self):
        try:
            headers = {
                "user": self.user,
                "pass": self.password,
                "aid": self.aid
            }
            r = requests.get(f'https://api.ccauth.app/api/v2/getdatabase?key={self.api_key}', headers=headers).json()

            if eval(r["success"]):
                return False, r["database"]
            else:
                return True, 'an error has occurred: ' + str(r["reason"])

        except Exception as ex:
            return True, 'an error has occurred: ' + str(ex)

    def change_hwid_status(self):
        try:
            headers = {
                "user": self.user,
                "pass": self.password,
                "aid": self.aid
            }
            r = requests.get(f'https://api.ccauth.app/api/v2/changehwidreset?key={self.api_key}', headers=headers).json()

            if eval(r["success"]):
                return False, r["enabled"]
            else:
                return True, 'an error has occurred: ' + str(r["reason"])

        except Exception as ex:
            return True, 'an error has occurred: ' + str(ex)

    def change_registration_status(self):
        try:
            headers = {
                "user": self.user,
                "pass": self.password,
                "aid": self.aid
            }
            r = requests.get(f'https://api.ccauth.app/api/v2/changeregistration?key={self.api_key}', headers=headers).json()

            if eval(r["success"]):
                return False, r["enabled"]
            else:
                return True, 'an error has occurred: ' + str(r["reason"])

        except Exception as ex:
            return True, 'an error has occurred: ' + str(ex)

    def change_hash_status(self):
        try:
            headers = {
                "user": self.user,
                "pass": self.password,
                "aid": self.aid
            }
            r = requests.get(f'https://api.ccauth.app/api/v2/changehashmode?key={self.api_key}', headers=headers).json()

            if eval(r["success"]):
                return False, r["enabled"]
            else:
                return True, 'an error has occurred: ' + str(r["reason"])

        except Exception as ex:
            return True, 'an error has occurred: ' + str(ex)

    def change_hash(self, hasha):
        try:
            headers = {
                "user": self.user,
                "pass": self.password,
                "aid": self.aid,
                "hash": hasha
            }
            r = requests.get(f'https://api.ccauth.app/api/v2/changehash?key={self.api_key}', headers=headers).json()

            if eval(r["success"]):
                return False, r["hash"]
            else:
                return True, 'an error has occurred: ' + str(r["reason"])

        except Exception as ex:
            return True, 'an error has occurred: ' + str(ex)

    def change_version(self, ver):
        try:
            headers = {
                "user": self.user,
                "pass": self.password,
                "aid": self.aid,
                "version": ver
            }
            r = requests.get(f'https://api.ccauth.app/api/v2/changeversion?key={self.api_key}', headers=headers).json()

            if eval(r["success"]):
                return False, r["version"]
            else:
                return True, 'an error has occurred: ' + str(r["reason"])

        except Exception as ex:
            return True, 'an error has occurred: ' + str(ex)

    def change_announcement(self, ver):
        try:
            headers = {
                "user": self.user,
                "pass": self.password,
                "aid": self.aid,
                "announcement": ver
            }
            r = requests.get(f'https://api.ccauth.app/api/v2/changeannoucment?key={self.api_key}', headers=headers).json()

            if eval(r["success"]):
                return False, r["announcement"]
            else:
                return True, 'an error has occurred: ' + str(r["reason"])

        except Exception as ex:
            return True, 'an error has occurred: ' + str(ex)


if __name__ == '__main__':
    AdminPanel()
