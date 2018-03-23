import os
from gtts import gTTS
from playsound import playsound

tts=gTTS(text="this is a python workshop",lang="en")
tts.save("abc.mp3")
playsound("abc.mp3")