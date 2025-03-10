# import asyncio
# import wave
# import pygame
# from google import genai

# client = genai.Client(api_key="AIzaSyDfa4uJtXAcQXCmf0pde3D0fbM6_RvvNEM", http_options={'api_version': 'v1alpha'})
# chat = client.start_chat(history=[])
# config = {"response_modalities": ["AUDIO"]}
# async def speakToAi(text:str) -> None:
#     with wave.open("audio.wav", "wb") as wf:
#         wf.setnchannels(1)
#         wf.setsampwidth(2)
#         wf.setframerate(24000)

#         async with client.aio.live.connect(model=chat, config=config) as session:
#             await session.send(input=f"{text}", end_of_turn=True)

#             async for response in session.receive():
#                 if response.data:
#                     wf.writeframes(response.data)

#     # Initialize Pygame and play the audio
#     pygame.mixer.init()
#     pygame.mixer.music.load("audio.wav")
#     pygame.mixer.music.play()

#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
    
# if __name__ == "__main__":
#     asyncio.run(speakToAi("i have 2 dogs"))
