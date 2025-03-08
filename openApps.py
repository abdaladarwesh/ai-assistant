import os
import pyttsx3
import webbrowser
from speakReco import listen, speak
from addingapps import *

engine = pyttsx3.init()


def updateFilePath(newName) -> None:
            while True:
                answer = listen()
                if answer == None:
                    continue
                elif "yes" in answer or "yea" in answer:
                    addApps(newName)
                    break
                elif "no" in answer:
                    break
                    return
                else:
                    print("please say a valid answer")
                    engine.say("please say a valid answer")
                    continue



def openingApps(name : str) -> None:
    newName : str = name.replace('open', ' ').strip()
    if newName == 'visual studio code' or newName == 'code' or newName == 'vs code':
        print ("Nova : starting visual studio code ...")
        engine.say ("starting visual studio code ...")
        engine.runAndWait()
        path = findPath(newName)
        if path == None:
            print("the path to this app is wrong or doesnt exsit do you want to update it ?")
            speak("the path to this app is wrong or doesnt exsit you want to update it ?")
            updateFilePath(newName)
        else:
            os.startfile(path)
    elif newName == 'visual studio' or newName == 'visual studio community' or newName == 'vs community' or newName == 'vs':
        print (f"Nova : starting visual studio ...")
        engine.say (f"starting visual studio ...")
        engine.runAndWait()
        path = findPath(newName)
        if path == None:
            print("the path to this app is wrong or doesnt exsit do you want to update it ?")
            speak("the path to this app is wrong or doesnt exsit you want to update it ?")
            updateFilePath(newName)
        else:
            os.startfile(path)
    elif newName == 'chrome':
        print (f"Nova : starting chrome ...")
        engine.say (f"starting chrome ...")
        engine.runAndWait()
        path = findPath(newName)
        if path == None:
            print("the path to this app is wrong or doesnt exsit do you want to update it ?")
            speak("the path to this app is wrong or doesnt exsit you want to update it ?")
            updateFilePath(newName)
        else:
            os.startfile(path)
    elif newName == 'git':
        print (f"Nova : starting git ...")
        engine.say (f"starting git ...")
        engine.runAndWait()
        path = findPath(newName)
        if path == None:
            print("the path to this app is wrong or doesnt exsit do you want to update it ?")
            speak("the path to this app is wrong or doesnt exsit you want to update it ?")
            updateFilePath(newName)
        else:
            os.startfile(path)
    elif newName == 'todo':
        print (f"Nova : starting todo ...")
        engine.say (f"starting todo ...")
        engine.runAndWait()
        path = findPath(newName)
        if path == None:
            print("the path to this app is wrong or doesnt exsit do you want to update it ?")
            speak("the path to this app is wrong or doesnt exsit you want to update it ?")
            updateFilePath(newName)
        else:
            os.startfile(path)
    elif newName == 'facebook':
        print (f"Nova : starting {newName} ...")
        engine.say (f"starting {newName} ...")
        engine.runAndWait()
        webbrowser.open(f"https://www.{newName}.com")
    elif newName == 'youtube':
        print (f"Nova : starting {newName} ...")
        engine.say (f"starting {newName} ...")
        engine.runAndWait()
        webbrowser.open(f"https://www.{newName}.com")
    elif newName == 'github':
        print (f"Nova : starting {newName} ...")
        engine.say (f"starting {newName} ...")
        engine.runAndWait()
        webbrowser.open(f"https://www.{newName}.com")
    elif newName == 'instagram':
        print (f"Nova : starting {newName} ...")
        engine.say (f"starting {newName} ...")
        engine.runAndWait()
        webbrowser.open(f"https://www.{newName}.com")
    elif newName == 'stack overflow':
        print (f"Nova : starting {newName} ...")
        engine.say (f"starting {newName} ...")
        engine.runAndWait()
        webbrowser.open(f"https://stackoverflow.com/")
    elif newName == 'chat gpt':
        print (f"Nova : starting {newName} ...")
        engine.say (f"starting {newName} ...")
        engine.runAndWait()
        webbrowser.open(f"https://chatgpt.com/?model=gpt-4o")
    elif newName == 'deepseek':
        print (f"Nova : starting {newName} ...")
        engine.say (f"starting {newName} ...")
        engine.runAndWait()
        webbrowser.open(f"https://chat.deepseek.com/")
    elif newName == 'gemini':
        print (f"Nova : starting {newName} ...")
        engine.say (f"starting {newName} ...")
        engine.runAndWait()
        webbrowser.open(f"https://gemini.google.com/app")
    elif newName == 'whatsapp':
        print (f"Nova : starting {newName} ...")
        engine.say (f"starting {newName} ...")
        engine.runAndWait()
        webbrowser.open(f"https://web.whatsapp.com/")   
    elif newName == 'google keep':
        print (f"Nova : starting {newName} ...")
        engine.say (f"starting {newName} ...")
        engine.runAndWait()
        webbrowser.open(f"https://keep.google.com/")   
    else:
        print("wrong app .. ,  do you want to add the app ? say yes or no")
        speak("wrong app .. ,  do you want to add the app ? say yes or no")
        updateFilePath(newName)

