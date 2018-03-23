import winsound
from gtts import gTTS

tts=gTTS(text="hello",lang="en")
tts.save("def.mp3")
winsound.PlaySound("abc.mp3",winsound)