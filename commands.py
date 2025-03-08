import os
import sys
import ctypes


def shutdown() -> None:
    os.system("shutdown /s /t 0")

def sleep() -> None:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()
    os.system("powercfg -h off") 
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  

def restart() -> None:
    os.system("shutdown /r /t 0")


