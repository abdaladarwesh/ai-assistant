import os

def openingApps(name : str) -> None:
    newName : str = name.replace('open', ' ').strip()
    if newName == 'visual studio code' or newName == 'code' or newName == 'vs code':
        print (f"starting visual studio code ...")
        os.startfile(r"C:\Users\Abdallah Darwesh\Desktop\New WinRAR ZIP archive.zip")
    elif newName == 'visual studio' or newName == 'visual studio community' or newName == 'vs community' or newName == 'vs':
        print (f"starting visual studio ...{newName}")
        os.startfile(r"C:\Users\Abdallah Darwesh\Desktop\vscommunity.txt")
    elif newName == 'chrome':
        print (f"starting chrome ...")
        os.startfile(r"C:\Users\Abdallah Darwesh\Desktop\chrome.txt")
    elif newName == 'git':
        print (f"starting git ...")
        os.startfile(r"C:\Users\Abdallah Darwesh\Desktop\git.txt")
    elif newName == 'whatsapp':
        print (f"starting whatsapp ...")
        os.startfile(r"C:\Users\Abdallah Darwesh\Desktop\whatsapp.txt")
    elif newName == 'todo':
        print (f"starting todo ...")
        os.startfile(r"C:\Users\Abdallah Darwesh\Desktop\todo.txt")
    else:
        print("wrong app .. ,  please say a valid app to open or if you want to ask ai just say your qusetion")
