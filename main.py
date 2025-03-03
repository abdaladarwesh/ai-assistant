from google import genai
from google.genai import types
from sp import speak_to_text
from openApps import openingApps

def main() -> None:
    client = genai.Client(api_key="AIzaSyDfa4uJtXAcQXCmf0pde3D0fbM6_RvvNEM")
    config = types.GenerateContentConfig(max_output_tokens=500, temperature=1)
    while True:
        content : str | None= speak_to_text()
        if content == None:
            continue
        if 'open' in content:
            print(f"opening{content.replace('open', '')} ......")
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


if __name__ == "__main__":
    main()


