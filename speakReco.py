import speech_recognition as sr
import asyncio
import wave
import pygame
from google import genai
import os

client = genai.Client(api_key="AIzaSyDfa4uJtXAcQXCmf0pde3D0fbM6_RvvNEM", http_options={'api_version': 'v1alpha'})
model = "gemini-2.0-flash-exp"
config = {"response_modalities": ["AUDIO"]}
recognizer = sr.Recognizer()

async def speak(text:str) -> None:
    if os.path.exists("audio.wav"):
        os.remove("audio.wav")
    with wave.open("audio.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)

        async with client.aio.live.connect(model=model, config=config) as session:
            await session.send(input=f"say {text} exactly", end_of_turn=True)

            async for response in session.receive():
                if response.data:
                    wf.writeframes(response.data)

    # Initialize Pygame and play the audio
    pygame.mixer.init()
    pygame.mixer.music.load("audio.wav")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()  # Stop playing
    pygame.mixer.quit()        # Release the file




def listenForKeyWord() -> str:
    with sr.Microphone() as source:
        print("Adjusting for ambient noise....")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for wake word...")
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        print("Could not request results")
        return None
    
def listen() -> str:
    with sr.Microphone() as source:



        print("Adjusting for ambient noise....")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        print("Could not request results")
        return None

# this block for testing only
def main():
    text :str = listen()
    asyncio.run(speak(text))



if __name__ == "__main__":
    main()
