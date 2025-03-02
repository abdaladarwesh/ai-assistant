from google import genai
from google.genai import types
import speech_recognition as sr
import os
import re


def speak_to_text() -> str | None:
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as mic:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(mic, duration=1)
            print("Listening...")
            audio = recognizer.listen(mic, timeout=8, phrase_time_limit=30)
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
    client = genai.Client(api_key="AIzaSyDfa4uJtXAcQXCmf0pde3D0fbM6_RvvNEM")
    config = types.GenerateContentConfig(max_output_tokens=500, temperature=1)
    while True:
        content : str | None= speak_to_text()
        if content == None:
            continue
        if content == 'open':
            print(f"opening {re.sub(rf"\b{'open '}\b", "", content, flags=re.IGNORECASE).replace("  ", " ")} ......")
            openingApps(content)
        elif content == "exit":
            print("Exiting...")
            exit()
        else:
            respond = client.models.generate_content(model="gemini-2.0-flash", contents=[content], config=config)
            if respond.candidates:
                generated_text = respond.candidates[0].content.parts[0].text
                print("Generated Response:", generated_text)
            else:
                print("No response generated.")

        print("If you want to continue, say 'continue' or anything else. If you want to exit, say 'exit'.")
        response = speak_to_text()
        if response == 'continue':
            print("You said 'continue'")
            continue
        elif response == 'exit':
            print("Exiting...")
            exit()
        else:
            continue

def openingApps(name : str) -> None:
    newName : str = re.sub(rf"\b{'open '}\b", "", name, flags=re.IGNORECASE).replace("  ", " ")
    if newName == "visual studio code" or 'vs code':
        print (f"starting {newName} ...")
        os.startfile(r"P:\تطبيقات\Microsoft VS Code\Code.exe")



if __name__ == "__main__":
    # openingApps('open visual studio code')
    main()


