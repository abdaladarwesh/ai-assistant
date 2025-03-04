import speech_recognition as sr
import simpleaudio as sa
import time

def listen_for_keyword(keyword: str) -> bool:
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 3

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
        except Exception as e:
            print(f"Error: {e}")
    return False

def speak_to_text() -> str:
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 3

    try:
        with sr.Microphone() as mic:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(mic, duration=1)
            print("Listening...")
            audio = recognizer.listen(mic, timeout=10, phrase_time_limit=10)  # adjusted timeouts
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"You: {text}")
            return text
    except sr.UnknownValueError:
        print("Sorry, I did not get that.")
    except sr.WaitTimeoutError:
        print("You didn't say anything for a long time.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"Error: {e}")
    return ""  # Return an empty string instead of None or undefined variable
