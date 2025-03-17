import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import warnings
import asyncio
from google import genai
from google.genai import types
from openApps import *
from speakReco import *
from prayers import *
from commands import *
import asyncio
from notification import *
from showCommands import *
from organize import *
def main() -> None:
    warnings.filterwarnings("ignore", category=UserWarning)
    client = genai.Client(api_key="AIzaSyDfa4uJtXAcQXCmf0pde3D0fbM6_RvvNEM")
    config = types.GenerateContentConfig(temperature=1, max_output_tokens=1000)

    while True:
            while True:
                    check_prayer_times()
                    break
            command: str = listenForKeyWord()
            if command:
                if "nova" in command:
                    # playAudio("sfx.wav")
                    asyncio.run(speak("Yes, how can I help?"))
                    while True:
                        command: str = listen()
                        if command:
                            if "hello" in command:
                                asyncio.run(speak("Hello! How can I assist?"))
                            elif "exit" in command or 'quit' in command:
                                asyncio.run(speak("Goodbye!"))
                                return
                            elif "open" in command:
                                if "website" in command:
                                    asyncio.run(speak("opening" + command.replace("open", " ")))
                                    openingWeb(command)
                                    break
                                else:
                                    appName = command.replace("open", "").strip()
                                    asyncio.run(speak("opening" + appName))
                                    openingApps(appName)
                                    break
                            elif "google" in command:
                                asyncio.run(speak("googleing" + command.replace("google", " ")))
                                google(command)
                                break
                            elif "what can i say" in command:
                                showingCommands()
                                break
                            elif command == "shutdown":
                                asyncio.run(speak("turnoff the pc ..."))
                                shutdown()
                            elif command == "sleep":
                                asyncio.run(speak("sleeping the pc ..."))
                                sleep()
                                break
                            elif command == "restart":
                                asyncio.run(speak("restarting the pc ..."))
                                restart()
                                break
                            elif "fold" in command or command == "make folder":
                                makedir()
                                break
                            elif "alaram" in command or "timer" in command:
                                alarm()
                                break
                            elif command == "organize":
                                path = getPathdir()
                                organize_files(path)
                            else:
                                respond = client.models.generate_content(model="gemini-2.0-flash", contents=[command], config=config)
                                if respond.candidates:
                                    generated_text = respond.candidates[0].content.parts[0].text
                                    print("Nova:", generated_text)
                                    asyncio.run(speak(generated_text))
                                    break

if __name__ == "__main__":
    main()


