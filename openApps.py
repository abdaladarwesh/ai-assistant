import os
import asyncio
import webbrowser
from speakReco import listen, speak
from addingapps import *
from google import genai
from google.genai import types
from notification import *


client = genai.Client(api_key="AIzaSyDfa4uJtXAcQXCmf0pde3D0fbM6_RvvNEM")
config = types.GenerateContentConfig(max_output_tokens=100, temperature=1)


def updateFilePath(newName) -> None:
            while True:
                answer = listen()
                if answer == None:
                    continue
                elif "yes" in answer or "yea" in answer:
                    updateApps(newName)
                    break
                elif "no" in answer:
                    return
                else:
                    noti("please say a valid answer")
                    asyncio.run(speak("please say a valid answer"))
                    continue


def openingApps(name : str) -> None:
    newName : str = name.replace('open', ' ').strip()
    if checkifexist(newName):
        path = findPath(newName)
        try:
            os.startfile(path)
        except:
            noti("wrong app .. ,  do you want to add the app ? say yes or no")
            asyncio.run(speak("wrong app .. ,  do you want to add the app ? say yes or no"))
            updateFilePath(newName)

    else :
        respond = client.models.generate_content(model="gemini-2.0-flash", contents=[f"what is the original path to {newName} in windows using forward slash return the path only without any extra talk"], config=config)
        defPath = respond.candidates[0].content.parts[0].text.replace("\n", " ")
        try:
            addAppsDefPath(newName, defPath)
            try:
                openingApps(newName)
            except:
                noti("wrong app .. ,  do you want to add the app ? say yes or no")
                asyncio.run(speak("wrong app .. ,  do you want to add the app ? say yes or no"))
                updateFilePath(newName)
        except Exception as e:
            noti (e)
             
def openingWeb(name : str) -> None:
    newName : str = name.replace('open', ' ').replace("website"," ").strip()

    respond = client.models.generate_content(model="gemini-2.0-flash", contents=[f"give me the url of {newName} return the url only and if it doesnt have a url then give me the url only of this when i google it"], config=config)
    if respond.candidates:
        url = respond.candidates[0].content.parts[0].text
        webbrowser.open_new_tab(url)
    
def google(name : str) -> None:
    newName : str = name.replace('google', ' ').strip()
    webbrowser.open_new_tab(f"https://www.google.com/search?q={newName}")
         

def main() -> None:
    openingApps('git')