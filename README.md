```
       ______              _              ______            _      _   _       
       | ___ \            (_)             | ___ \          | |    | | | |      
       | |_/ /   _ ___ ___ _  __ _ _ __   | |_/ /___  _   _| | ___| |_| |_ ___ 
       |    / | | / __/ __| |/ _` | '_ \  |    // _ \| | | | |/ _ \ __| __/ _ \
       | |\ \ |_| \__ \__ \ | (_| | | | | | |\ \ (_) | |_| | |  __/ |_| ||  __/
       \_| \_\__,_|___/___/_|\__,_|_| |_| \_| \_\___/ \__,_|_|\___|\__|\__\___|
       -------------------------------------------------------------------------
                         Fun for some, devastating for some :)                    
```
# Welcome!

Want to destroy your OS with a twist? Run this script as root or as an administrator! Compatible with Linux and Windows.
On a serious note: Running this script will actually render your OS unusable. For Linux, the effect is immediate. For Windows, you won't be able to boot into the OS again. This is should used for educational purposes!

## Running this script
As root or administrator:
```
python russian_roulette.py
```

## What this really does
### Linux
Removes all the files and directories with `rm --no-preserve-root -rfv /`
### Windows
Takes ownership and file permissions in the directory `C:\Windows\System32` and deletes it.


## Tested OSes
- Windows 10 Pro
- kali-linux-2022.1
- Ubuntu 22.04
- Manjaro 

## References
[How to delete System32 by Shahriz Marks](https://medium.com/@shahrizmarks2208/how-to-delete-system32-windows-fec58eb6f8e)
