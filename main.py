from google import genai
from google.genai import types
from openApps import openingApps
from speakReco import *
from prayers import *
from commands import *

def main() -> None:
    client = genai.Client(api_key="AIzaSyDfa4uJtXAcQXCmf0pde3D0fbM6_RvvNEM")
    config = types.GenerateContentConfig(max_output_tokens=100, temperature=1)

    while True:
            while True:
                    check_prayer_times()
                    break
            command: str = listenForKeyWord()
            if command:
                if "nova" in command:
                    playAudio("sfx.wav")
                    speak("Yes, how can I help?")
                    while True:
                        command: str = listen()
                        if command:
                            if "hello" in command:
                                speak("Hello! How can I assist?")
                            elif "exit" in command or 'quit' in command:
                                speak("Goodbye!")
                                return
                            elif "open" in command:
                                appName = command.replace("open", "").strip()
                                openingApps(appName)
                                break
                            elif command == "shutdown":
                                engine.say("turnoff the pc ...")
                                engine.runAndWait()
                                shutdown()
                            elif command == "sleep":
                                engine.say("sleeping the pc ...")
                                engine.runAndWait()
                                sleep()
                            elif command == "restart":
                                engine.say("restarting the pc ...")
                                engine.runAndWait()
                                restart()
                            else:
                                respond = client.models.generate_content(model="gemini-2.0-flash", contents=[command], config=config)
                                if respond.candidates:
                                    generated_text = respond.candidates[0].content.parts[0].text
                                    print("Nova:", generated_text)
                                    speak(generated_text)
                                    break

if __name__ == "__main__":
    main()


