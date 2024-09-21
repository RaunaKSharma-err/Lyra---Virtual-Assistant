import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from gtts import gTTS
from playsound import playsound
import os

recongnizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    tts = gTTS(text=text, lang='en', tld='com.au')
    tts.save("assistant.mp3")
    playsound("assistant.mp3")
    os.remove("assistant.mp3")

def processCommand(command):
    if "open google" in command.lower():
        speak("opening google")
        webbrowser.open("https://youtube.com")
    elif "open facebook" in command.lower():
        speak("opening facebook")
        webbrowser.open("https://facebook.com")
    elif "open instagram" in command.lower():
        speak("opening instagram")
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in command.lower():
        speak("opening linkedin")
        webbrowser.open("https://linkedin.com")
    elif "open whatsapp" in command.lower():
        speak("opening whatsapp")
        webbrowser.open("https://whatsapp.com")
    elif command.startswith("play"):
        song = command.lower().split(" ")[1]
        speak(f"Playing {song}")
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif command.startswith("speak"):
        speech = command.split(" ")[1]
        speak(speech)
    else:
        speak("is there Anything else to do sir")

if __name__ == "__main__":
    speak("Initializing Lyra.....")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source,timeout=2,phrase_time_limit=2)
                print("recognizing......")
            word = r.recognize_google(audio)
            print(word)
            if word.lower() == "lyra":
                speak("Yes sir i am listening how can i help you")

            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source,timeout=5,phrase_time_limit=3)
                print("recognizing......")
                command = r.recognize_google(audio)
                print(command)

                processCommand(command)
        except Exception as e:
            print("error; {0}".format(e))
