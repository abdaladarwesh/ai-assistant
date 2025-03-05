from google import genai
from google.genai import types
from sp import listen_for_keyword
from openApps import openingApps
from sp_tx import speak_to_text
import speech_recognition as sr
from playsound import playsound
import simpleaudio as sa
import time

def main() -> None:
    client = genai.Client(api_key="AIzaSyDfa4uJtXAcQXCmf0pde3D0fbM6_RvvNEM")
    config = types.GenerateContentConfig(max_output_tokens=500, temperature=1)
    keyword = "nova"

    while True:
        print("Waiting for keyword...")
        var = speak_to_text()
        if not var or var == "":
            print ("no keyword detected")
        else :
            if "nova" in var:
                command = var.replace("nova", " ").strip()
                wavObj = sa.WaveObject.from_wave_file('sfx.wav')
                wavObj.play()
                time.sleep(2)
                if "open" in command:
                    openingApps(command)
                    continue
                elif command == "shutdown" or command == "turn off":
                    print("shut down")
                    continue
                elif command == "exit":
                    exit()
                else : 
                    # respond = client.models.generate_content(model="gemini-2.0-flash", contents=[var], config=config)
                    # if respond.candidates:
                    #     generated_text = respond.candidates[0].content.parts[0].text
                    #     print("nova:", generated_text)
                        ...
                        continue
            else:
                print("no keyword detected")
                continue
            

        # if cond == True:
        #     print("Keyword detected. Listening for command...")
        #     print(var)
        #     if var:
        #         if 'open' in var:
        #             print(f"opening {var.replace('open', '')} ......")
        #             openingApps(var)
        #         elif var == "exit":
        #             print("Exiting...")
        #             exit()
        #         else:
        #             else:
        #                 print("No response generated.")
        #     else:
        #         print("No command detected.")
        # else:
        #     print("No keyword detected.")

if __name__ == "__main__":
    main()


