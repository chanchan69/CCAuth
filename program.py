# -*- coding: utf-8 -*-
from colorama import Fore, Style
from yaml import full_load
import os
import requests
import time
import subprocess
import sys

import auth_module3 as auth_module2

class Auth:
    def __init__(self):
        os.system('cls')
        print(Style.BRIGHT)
        self.startMenu()

    def startMenu(self):
        print(f"[{Fore.MAGENTA}1{Fore.CYAN}] Login\n[{Fore.MAGENTA}2{Fore.CYAN}] Register\n[{Fore.MAGENTA}3{Fore.CYAN}] Change HWID\n  ")
        menuinput = input(f">{Fore.MAGENTA} ")
        if menuinput.__contains__("1"):
            os.system('cls')
            hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
            username = input(f"{Fore.LIGHTCYAN_EX}[{Fore.MAGENTA}1{Fore.LIGHTCYAN_EX}] Username:{Fore.MAGENTA} ")
            password = input(f"{Fore.LIGHTCYAN_EX}[{Fore.MAGENTA}2{Fore.LIGHTCYAN_EX}] Password:{Fore.MAGENTA} ")
            
            r = auth_module2.authenticate(username, password, hwid)

            if '0' in r:
                print('authemticated')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Exit')
                sys.exit()
            elif '2' in r:
                print(f'{Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTGREEN_EX}]{Fore.LIGHTRED_EX} Invalid Username or Password')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Exit')
                sys.exit()
            elif '1' in r:
                print(f'{Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTGREEN_EX}]{Fore.LIGHTRED_EX} Invalid HWID')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Exit')
                sys.exit()
            elif '3' in r:
                print(f'{Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTGREEN_EX}]{Fore.LIGHTRED_EX} Invalid Username or Password and HWID')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Exit')
                sys.exit()
            elif '4' in r:
                print(f'{Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTGREEN_EX}]{Fore.LIGHTRED_EX} Your License Has Expired')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Exit')
                sys.exit()
            elif 'error' in r:
                print(f'{Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTGREEN_EX}]{Fore.LIGHTRED_EX} An Error has Occured, Please Try Again')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Exit')
                sys.exit()
            elif 'Error: Invalid User or password' in r:
                print(f'{Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTGREEN_EX}]{Fore.LIGHTRED_EX} Invalid Username or Password')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Exit')
                sys.exit()
            else:
                print(f'{Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTGREEN_EX}]{Fore.LIGHTRED_EX} An Error has Occured, Please Try Again')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Return to the Main Menu')
                os.system('cls')
                self.startMenu()
        
        elif menuinput.__contains__("2"):
            os.system('cls')
            username = input(f"{Fore.LIGHTCYAN_EX}[{Fore.MAGENTA}1{Fore.LIGHTCYAN_EX}] Username:{Fore.MAGENTA} ")
            password = input(f"{Fore.LIGHTCYAN_EX}[{Fore.MAGENTA}2{Fore.LIGHTCYAN_EX}] Password:{Fore.MAGENTA} ")
            discordid = input(f"{Fore.LIGHTCYAN_EX}[{Fore.MAGENTA}3{Fore.LIGHTCYAN_EX}] Your Discord Username:{Fore.MAGENTA} ")
            registerkey = input(f"{Fore.LIGHTCYAN_EX}[{Fore.MAGENTA}4{Fore.LIGHTCYAN_EX}] Registration Key:{Fore.MAGENTA} ")
            hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

            r = auth_module2.register(username, password, hwid, discordid, registerkey)

            if '0' in r:
                print(f"{Fore.LIGHTRED_EX}[{Fore.LIGHTGREEN_EX}!{Fore.LIGHTRED_EX}]{Fore.LIGHTGREEN_EX} Congrats, {discordid}, You're Registered")
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Return to the Main Menu')
                os.system('cls')
                self.startMenu()
            elif '1' in r:
                print(f'{Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTGREEN_EX}]{Fore.LIGHTRED_EX} Bad Key, Please Try Again')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Return to the Main Menu')
                os.system('cls')
                self.startMenu()
            elif 'Error: Invalid User or password' in r:
                print(f'{Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTGREEN_EX}]{Fore.LIGHTRED_EX} Invalid Username or Password')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Return to the Main Menu')
                os.system('cls')
                self.startMenu()
            elif r == 'error':
                print(f'{Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTGREEN_EX}]{Fore.LIGHTRED_EX} An Error has Occured')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Exit')
                os.system('cls')
                self.startMenu()
            else:
                print(f'{Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTGREEN_EX}]{Fore.LIGHTRED_EX} An Error has Occured, Please Try Again')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Return to the Main Menu')
                os.system('cls')
                self.startMenu()
    
        elif menuinput.__contains__("3"):
            os.system('cls')
            username = input(f"{Fore.LIGHTCYAN_EX}[{Fore.MAGENTA}1{Fore.LIGHTCYAN_EX}] Username:{Fore.MAGENTA} ")
            password = input(f"{Fore.LIGHTCYAN_EX}[{Fore.MAGENTA}2{Fore.LIGHTCYAN_EX}] Password:{Fore.MAGENTA} ")
            hwidresetkey = input(f"{Fore.LIGHTCYAN_EX}[{Fore.MAGENTA}2{Fore.LIGHTCYAN_EX}] Hwid Reset Key:{Fore.MAGENTA} ")
            hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

            r = auth_module2.hwid_change(username, password, hwid, hwidresetkey)
            print(r)
            if r == '1':
                print(f'{Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTGREEN_EX}]{Fore.LIGHTRED_EX} Bad Credentials')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Exit')
                sys.exit()
            elif r == '2':
                print(f'{Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTGREEN_EX}]{Fore.LIGHTRED_EX} Error')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Exit')
                sys.exit()
            elif r == '0':
                print(f'{Fore.LIGHTGREEN_EX}Your HWID is changed to: {Fore.LIGHTRED_EX}{hwid}')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Return to the Main Menu')
                os.system('cls')
                self.startMenu()
            elif r == '3':
                print(f'{Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTGREEN_EX}]{Fore.LIGHTRED_EX} HWID Resets no Available')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Return to the Main Menu')
                os.system('cls')
                self.startMenu()
            elif r == 'error':
                print(f'{Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTGREEN_EX}]{Fore.LIGHTRED_EX} An Error has Occured')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Exit')
                sys.exit()
            else:
                print(f'{Fore.LIGHTGREEN_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTGREEN_EX}]{Fore.LIGHTRED_EX} An Error has Occured, Please Try Again')
                input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}EXIT{Fore.LIGHTCYAN_EX}] Press ENTER to Return to the Main Menu')
                os.system('cls')
                self.startMenu()

Auth()
