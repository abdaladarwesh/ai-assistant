import os
import sys
import ctypes
from addingapps import getPathdir
from plyer import notification
import subprocess
from speakReco import *


funcs = ["shutdown", "restart", "sleep"]

def choose(command : str) -> None:
    if command == "shutdown":
        shutdown()
    elif command == "restart":
        restart()
    elif command == "sleep":
        sleep()

def makedir() -> None:
    asyncio.run(speak("please say the folder name you want to create"))
    name = listen()
    try:
        path = getPathdir()
        os.mkdir(path + f"/{name}")
    except:
        print("can't make a directory in this path ! , there is aleardy a folder with this name")
    asyncio.run(speak("the folder have been made sucessfully"))

def shutdown() -> None:
    os.system("shutdown /s /t 0")

def sleep() -> None:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    os.system("powercfg -h off") 
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  

def restart() -> None:
    os.system("shutdown /r /t 0")

def alarm() -> None:
    subprocess.run("start ms-clock:", shell=True)

