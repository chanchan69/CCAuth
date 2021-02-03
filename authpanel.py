
import subprocess
import requests
from yaml import safe_load
from os import path, system
from sys import exit
from ctypes import windll
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
        config()

config()


r = requests.get(url=f'http://SirChanChan21.pythonanywhere.com/api/v1/getstats?key={apikey}', headers={"user": username, "pass": password, "aid": aid}).text
split = r.split('\n')
windll.kernel32.SetConsoleTitleW(f'{str(split[0])} | {str(split[1])} | {str(split[2])}')

def getkey():
    r = requests.get(url=f'http://SirChanChan21.pythonanywhere.com/api/v1/getkey?key={apikey}', headers={"user": username, "pass": password, "aid": aid})
    print(f'''\n    ===========================
     key: {r.text}
    ===========================''')
    input(f'\n[ENTER] Return to the Main Menu ')
    system('cls')
    menu()

def getlog():
    r = requests.get(url=f'http://SirChanChan21.pythonanywhere.com/api/v1/getlog?key={apikey}', headers={"user": username, "pass": password, "aid": aid})
    print(r.text)
    input(f'\n[ENTER] Return to the Main Menu ')
    system('cls')
    menu()

def getdatabase():
    r = requests.get(url=f'http://SirChanChan21.pythonanywhere.com/api/v1/getdatabase?key={apikey}', headers={"user": username, "pass": password, "aid": aid})
    print(r.text)
    input(f'\n[ENTER] Return to the Main Menu ')
    system('cls')
    menu()

def changehwidreset():
    r = requests.get(url=f'http://SirChanChan21.pythonanywhere.com/api/v1/changehwidreset?key={apikey}', headers={"user": username, "pass": password, "aid": aid})
    print(r.text)
    input(f'\n[ENTER] Return to the Main Menu ')
    system('cls')
    menu()
def changeregistration():
    r = requests.get(url=f'http://SirChanChan21.pythonanywhere.com/api/v1/changeregistration?key={apikey}', headers={"user": username, "pass": password, "aid": aid})
    print(r.text)
    input(f'\n[ENTER] Return to the Main Menu ')
    system('cls')
    menu()
def changehashmode():
    r = requests.get(url=f'http://SirChanChan21.pythonanywhere.com/api/v1/changehashmode?key={apikey}', headers={"user": username, "pass": password, "aid": aid})
    print(r.text)
    input(f'\n[ENTER] Return to the Main Menu ')
    system('cls')
    menu()
def changehash():
    newhash = input('New Hash: ')
    r = requests.get(url=f'http://SirChanChan21.pythonanywhere.com/api/v1/changehash?key={apikey}', headers={"user": username, "pass": password, "aid": aid, "hash": newhash})
    print(r.text)
    input(f'\n[ENTER] Return to the Main Menu ')
    system('cls')
    menu()

def menu():
    a = input(f'[1] Get Key\n[2] Get log\n[3] Get Databse\n[4] Enable/Disable HWID Resets\n[5] Enable/Disable Registration\n[6] Enable/Disable Use Hash\n[7] Change Hash\n')
    system('cls')
    if a == '1':
        getkey()
    elif a == '2':
        getlog()
    elif a == '3':
        getdatabase()
    elif a == '4':
        changehwidreset()
    elif a == '5':
        changeregistration()
    elif a == '6':
        changehashmode()
    elif a == '7':
        changehash()
menu()
