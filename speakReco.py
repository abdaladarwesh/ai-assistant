import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text:str) -> None:

    engine.say(text)
    engine.runAndWait()

def listenForKeyWord() -> str:
    with sr.Microphone() as source:
        print("Adjusting for ambient noise....")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for wake word...")
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        print("Could not request results")
        return None
    
def listen() -> str:
    with sr.Microphone() as source:



        print("Adjusting for ambient noise....")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        print("Could not request results")
        return None

# this block for testing only
def main():
    while True:
        command : str = listenForKeyWord()
        if command:
            if "nova" in command:
                speak("Yes, how can I help?")
                while True:
                    command : str = listen()
                    if command:
                        if "hello" in command:
                            speak("Hello! How can I assist?")
                        elif "exit" in command:
                            speak("Goodbye!")
                            return
                        elif "open" in command:
                            appName = command.replace("open", "").strip()
                            if appName == "chrome":
                                print ("pretend that this is chrome")
                                break

if __name__ == "__main__":
    main()
