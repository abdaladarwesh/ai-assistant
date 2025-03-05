import speech_recognition as sr
from playsound import playsound
import simpleaudio as sa
import time

PAUSE_THRESHOLD = 3

def listen_for_keyword(keyword: str) -> bool:
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = PAUSE_THRESHOLD

    while True:
        try:
            with sr.Microphone() as mic:
                print("Adjusting for ambient noise...")
                recognizer.adjust_for_ambient_noise(mic, duration=1)
                print("Listening for keyword...")
                audio = recognizer.listen(mic, timeout=50, phrase_time_limit=5)
                print("Recognizing...")
                text = recognizer.recognize_google(audio)
                text = text.lower()
                print(f"You: {text}")
                if keyword in text:
                    wavObj = sa.WaveObject.from_wave_file("sfx.wav")
                    wavObj.play()
                    time.sleep(3)
                    print("Nova: What do you want me to do?")
                    return True
                else:
                    print("Didn't detect any keyword.")
        except sr.UnknownValueError:
            print("No keyword detected.")
        except sr.WaitTimeoutError:
            print("You didn't say anything for a long time.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
    return False





