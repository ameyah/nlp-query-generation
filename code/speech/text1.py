from gtts import gTTS
import os
tts = gTTS(text='Hello My name is Amayaa Hanamsagar', lang='en')
tts.save('hello.mp3')
os.system('hello.mp3')