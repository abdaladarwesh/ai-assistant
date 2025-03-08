import tkinter as tk
from tkinter import filedialog
import json

def getPath() -> str:
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a file")
    return file_path

def checkifexist(appname: str) -> bool:
    with open("appsdirectory.json", 'r') as file:
        paths = json.load(file)
        allPaths = paths["apps"]
    if appname in allPaths:
        return True
    else:
        return False

def findPath(appname : str) -> None | str:
    if checkifexist(appname):
        with open("appsdirectory.json", 'r') as file:
            paths = json.load(file)
            allPaths = paths["apps"]
            return allPaths[appname]
    else:
        return None


def addApps (appname : str) -> None:
    dir = getPath()
    with open("appsdirectory.json", "r+") as file:
        paths = json.load(file)
        if not checkifexist(appname):
            paths["apps"].update({appname:dir})
            file.seek(0)
            json.dump(paths, file, indent=4)
            file.truncate()
        else:
            print("already exist")

def addAppsDefPath (appname : str, dir : str) -> None:
    with open("appsdirectory.json", "r+") as file:
        paths = json.load(file)
        if not checkifexist(appname):
            paths["apps"].update({appname:dir})
            file.seek(0)
            json.dump(paths, file, indent=4)
            file.truncate()
        else:
            print("already exist")

