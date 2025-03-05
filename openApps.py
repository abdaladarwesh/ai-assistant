import os
import pyttsx3
import webbrowser

engine = pyttsx3.init()


def openingApps(name : str) -> None:
    newName : str = name.replace('open', ' ').strip()
    if newName == 'visual studio code' or newName == 'code' or newName == 'vs code':
        print ("Nova : starting visual studio code ...")
        engine.say ("starting visual studio code ...")
        engine.runAndWait()
        os.startfile(r"P:\تطبيقات\Microsoft VS Code\Code.exe")
    elif newName == 'visual studio' or newName == 'visual studio community' or newName == 'vs community' or newName == 'vs':
        print (f"Nova : starting visual studio ...")
        engine.say (f"starting visual studio ...")
        engine.runAndWait()
        os.startfile(r"P:\programmes\visual studio\Common7\IDE\devenv.exe")
    elif newName == 'chrome':
        print (f"Nova : starting chrome ...")
        engine.say (f"starting chrome ...")
        engine.runAndWait()
        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    elif newName == 'git':
        print (f"Nova : starting git ...")
        engine.say (f"starting git ...")
        engine.runAndWait()
        os.startfile(r"P:\programmes\Git\git-bash.exe")
    elif newName == 'todo':
        print (f"Nova : starting todo ...")
        engine.say (f"starting todo ...")
        engine.runAndWait()
        os.startfile(r"C:\Users\Abdallah Darwesh\Desktop\todo.txt")
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
        print("wrong app .. ,  please say a valid app to open or if you want to ask ai just say your qusetion")
        engine.say("wrong app .. ,  please say a valid app to open or if you want to ask ai just say your qusetion")
        engine.runAndWait()
