import simpleaudio as sa

wavObj = sa.WaveObject.from_wave_file("sfx.wav")
playObj = wavObj.play()
playObj.wait_done()


