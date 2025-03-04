from google import genai
from google.genai import types
from sp import speak_to_text, listen_for_keyword
from openApps import openingApps

def main() -> None:
    client = genai.Client(api_key="AIzaSyDfa4uJtXAcQXCmf0pde3D0fbM6_RvvNEM")
    config = types.GenerateContentConfig(max_output_tokens=500, temperature=1)
    keyword = "nova"

    while True:
        print("Waiting for keyword...")
        cond = listen_for_keyword(keyword)
        if cond:
            command = speak_to_text()
            if 'open' in command:
                print(f"opening {command.replace('open', '')} ......")
                openingApps(command)
            elif command == "exit":
                print("Exiting...")
                # exit()
            else:
                respond = client.models.generate_content(model="gemini-2.0-flash", contents=[command], config=config)
                if respond.candidates:
                    generated_text = respond.candidates[0].content.parts[0].text
                    print("Abdio:", generated_text)
                else:
                    print("No response generated.")
        else:
            print("No keyword detected.")

if __name__ == "__main__":
    main()


