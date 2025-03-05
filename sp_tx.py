import speech_recognition as sr
from playsound import playsound
import simpleaudio as sa
import time

def speak_to_text() -> str:
    recog = sr.Recognizer()
    recog.pause_threshold = 3

    while True:
        try:
            with sr.Microphone() as mic:
                print("Adjusting for ambient noise...")
                recog.adjust_for_ambient_noise(mic, duration=1)
                print("Listening...")
                try:
                    audio_r = recog.listen(mic, timeout=10, phrase_time_limit=10)  # adjusted timeouts
                except Exception as e:
                    print(f"Error during listening: {e}")
                    continue  # Continue the loop if an error occurs during listening

                print("Recognizing...")
                try:
                    text = recog.recognize_google(audio_r)
                    text = text.lower()
                    print(f"You: {text}")
                    return text  # Return the recognized text
                except sr.UnknownValueError:
                    print("Sorry, I did not get that.")
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service; {e}")
                except Exception as e:
                    print(f"Error during recognition: {e}")

        except sr.WaitTimeoutError:
            print("You didn't say anything for a long time.")
        except Exception as e:
            print(f"Error: {e}")

    return ""  # Return an empty string if no valid text is recognized

if __name__ == "__main__":
    while True:
        text = speak_to_text()
        if text:
            print(f"Recognized text: {text}")
        else:
            print("No valid text recognized.")