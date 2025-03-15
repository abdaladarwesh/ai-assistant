import requests
from datetime import datetime
import pyttsx3
import pygame
from speakReco import *
import asyncio
from notification import *

engine = pyttsx3.init()
time = datetime.now().strftime("%I:%M %p")



url = "https://prayer-times-in-egypt.p.rapidapi.com/prayer?gov=1"

headers = {
    'x-rapidapi-key': "2132763819msh998f7b73f4f7095p184069jsn69f46316c049",
    'x-rapidapi-host': "prayer-times-in-egypt.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

data :dict= response.json()
class prayers():
    def __init__(self):
        self.duhr = data['prayer-timees']['Dhuhr'].replace("ص", "AM").strip()
        self.asar = data['prayer-timees']['Asr'].replace("م", "PM").strip()
        self.maghrb = data['prayer-timees']['Maghrib'].replace("م", "PM").strip()
        self.isha = data['prayer-timees']['Isha'].replace("م", "PM").strip()
    def __repr__(self) -> str:
        return f"Dhuhr : {self.duhr} , Asr : {self.asar} , Maghrib : {self.maghrb}, Isha : {self.isha}"
    def get(self, pray:str) -> str:
        Prayers = {"dhuhr" : self.duhr,"asr" :self.asar, "maghrb" :self.maghrb, "isha" :self.isha }
        return Prayers[pray]
    def getall(self) -> dict:
        Prayers = {"dhuhr" : self.duhr,"asr" :self.asar, "maghrb" :self.maghrb, "isha" :self.isha }
        return Prayers
    
def playAudio(pathToFile : str) -> None:
    pygame.mixer.init()
    pygame.mixer.music.load(pathToFile)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue


def check_prayer_times(prayer = prayers()) -> None:
        
        current_time = datetime.now().strftime("%I:%M %p")
        try:
            if prayer.get("dhuhr") == current_time:
                noti("Dhuhr Azan time")
                asyncio.run(speak("Dhuhr Azan time"))
                playAudio("azan.mp3")
            elif prayer.get("asr") == current_time:
                noti("Asr Azan time")
                asyncio.run(speak("Asr Azan time"))
                playAudio("azan.mp3")
            elif prayer.get("maghrb") == current_time:
                noti("Maghrib Azan time")
                asyncio.run(speak("Maghrib Azan time"))
                playAudio("azan.mp3")
            elif prayer.get("isha") == current_time:
                noti("Isha Azan time")
                asyncio.run(speak("Isha Azan time"))
                playAudio("azan.mp3")
        except Exception as e:
            noti(f"Error playing sound: {e}")

#'Ishraq': '4:50 ص', 
# 'Dhuhr': '6:16 ص', 
# 'Asr': '12:6 م', 
# 'Maghrib': '3:27 م'
# , 'Isha': '5:57 م'}