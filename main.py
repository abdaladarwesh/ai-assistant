from google import genai
from google.genai import types
from openApps import *
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
                                if "website" in command:
                                    openingWeb(command)
                                    break
                                else:
                                    appName = command.replace("open", "").strip()
                                    openingApps(appName)
                                    break
                            elif "google" in command:
                                google(command)
                            elif command == "shutdown":
                                engine.say("turnoff the pc ...")
                                engine.runAndWait()
                                shutdown()
                            elif "what can i say" in command:
                                print(
                                    "================== Nova commands ==================\n\n",
                                    "1 - (open APP_NAME) to open an app\n\n",
                                    "2 - (open WEBSITE_NAME website) to open a specific website\n\n",
                                    "3 - (google SOMTHING) to google something\n\n",
                                    "4 - (shutdown , restart , sleep)\n\n",
                                    "5 - or ask a question immediately to have a response from our generative ai\n\n",
                                    "============== Enter q to back to the ai ==========\n\n"
                                )
                                while True:
                                    choice : str = input()
                                    if choice == "q":
                                        break
                                    else:
                                        print ("enter a valid answer")
                                        continue
                                break
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


