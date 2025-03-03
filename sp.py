import speech_recognition as sr

def speak_to_text() -> str | None:
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 3  # Increase pause threshold to allow longer pauses

    try:
        with sr.Microphone() as mic:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(mic, duration=1)
            print("Listening...")
            audio = recognizer.listen(mic, timeout=50, phrase_time_limit=20)  
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"Recognized text: {text}")
            return text
    except sr.UnknownValueError:
        print("Sorry, I did not get that")
    except sr.WaitTimeoutError:
        print("You didn't say anything for a long time")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"Error: {e}")
    return None
        

def main() -> None:
    """ for testing only """
    while True:
        if speak_to_text == "exit":
            exit()
        else:
            print(speak_to_text())
        

if __name__ == "__main__":
    main()