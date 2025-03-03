from google import genai
from google.genai import types
from sp import speak_to_text
from openApps import openingApps

def main() -> None:
    client = genai.Client(api_key="AIzaSyDfa4uJtXAcQXCmf0pde3D0fbM6_RvvNEM")
    config = types.GenerateContentConfig(max_output_tokens=500, temperature=1)
    while True:
        content : str | None = speak_to_text()
        if content == None:
            continue
        elif 'abido' in content:
            command = content.replace("abido", "").strip()
            if 'open' in command:
                print(f"opening{command.replace('open', '')} ......")
                openingApps(command)
            elif command == "exit":
                print("Exiting...")
                exit()
            else:
                respond = client.models.generate_content(model="gemini-2.0-flash", contents=[command], config=config)
                if respond.candidates:
                    generated_text = respond.candidates[0].content.parts[0].text
                    print("Generated Response:", generated_text)
                else:
                    print("No response generated.")
        else:
            continue


if __name__ == "__main__":
    main()


