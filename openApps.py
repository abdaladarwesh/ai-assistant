import os

def openingApps(name : str) -> None:
    newName : str = name.replace('open', ' ').strip()
    if newName == 'visual studio code' or newName == 'code' or newName == 'vs code':
        print (f"Nova : starting visual studio code ...")
        os.startfile(r"P:\تطبيقات\Microsoft VS Code\Code.exe")
    elif newName == 'visual studio' or newName == 'visual studio community' or newName == 'vs community' or newName == 'vs':
        print (f"Nova : starting visual studio ...{newName}")
        os.startfile(r"P:\programmes\visual studio\Common7\IDE\devenv.exe")
    elif newName == 'chrome':
        print (f"Nova : starting chrome ...")
        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    elif newName == 'git':
        print (f"Nova : starting git ...")
        os.startfile(r"P:\programmes\Git\git-bash.exe")
    elif newName == 'whatsapp':
        print (f"Nova : starting whatsapp ...")
        os.startfile(r"C:\Users\Abdallah Darwesh\Desktop\whatsapp.txt")
    elif newName == 'todo':
        print (f"Nova : starting todo ...")
        os.startfile(r"C:\Users\Abdallah Darwesh\Desktop\todo.txt")
    else:
        print("wrong app .. ,  please say a valid app to open or if you want to ask ai just say your qusetion")
