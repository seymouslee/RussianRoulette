import os
import sys

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
print(banner)
try:
    bullet = sys.argv[1]
    bullet = int(bullet)
except IndexError:
    print("Usage: %s <Enter a number from 1 to 6> " % sys.argv[0])
    sys.exit()
except (TypeError, ValueError) as err:
    print("Input has to be a numerical number from 1 to 6")
    sys.exit()

if bullet < 1 and bullet > 6:
    print("[Error] Enter a number from 1 to 6")
    sys.exit()
