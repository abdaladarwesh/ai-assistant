import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"  # Hide welcome message
import warnings
import asyncio
import speech_recognition as sr
import wave
import pygame
from google import genai
from notification import *
# Initialize Google Gemini API Client
client = genai.Client(api_key="AIzaSyDfa4uJtXAcQXCmf0pde3D0fbM6_RvvNEM", http_options={'api_version': 'v1alpha'})
model = "gemini-2.0-flash-exp"
config = {"response_modalities": ["AUDIO"]}

recognizer = sr.Recognizer()

async def speak(text: str) -> None:
    try:
        # Remove previous audio file if exists
        if os.path.exists("audio.wav"):
            os.remove("audio.wav")

        # Connect to AI model and generate audio
        async with client.aio.live.connect(model=model, config=config) as session:
            warnings.filterwarnings("ignore", category=UserWarning)
            await session.send(input=f"say \"{text}\" exactly", end_of_turn=True)

            with wave.open("audio.wav", "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(24000)
                
                async for response in session.receive():
                    if response.data:
                        wf.writeframes(response.data)

    except Exception as e:
        print(f"Error in AI model connection: {e}")
        return

    # Play the generated audio using pygame
    pygame.mixer.init(frequency=24000)  # Match sample rate
    try:
        pygame.mixer.music.load("audio.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.stop()  
        pygame.mixer.quit()        
    except Exception as e:
        print(f"Error playing audio: {e}")

def listenForKeyWord() -> str:
    with sr.Microphone() as source:
        print("Adjusting for ambient noise....")
        recognizer.adjust_for_ambient_noise(source)
        noti("Listening for wake word...")
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
        noti("Listening...")
        audio = recognizer.listen(source, phrase_time_limit=25)
    
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

# Testing block
def main():
    text = listen()
    if text:
        asyncio.run(speak(text))

if __name__ == "__main__":
    main()

