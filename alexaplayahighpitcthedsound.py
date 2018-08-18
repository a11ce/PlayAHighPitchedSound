import pyTone
import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()
print("mic ready")
with mic as source:
    recognizer.adjust_for_ambient_noise(source)
pyTone.sine_tone(400, 0.5)
while True:
    print("ok")
    with mic as source:
        audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio)
    print(text)
    if "play a high-pitched" in text or "play a high pitch" in text: #most common way for it to be wrong
        pyTone.sine_tone(800, 3)
