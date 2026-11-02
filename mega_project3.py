 #install this all in terminal
# pip install SpeechRecognition
# pip install pyttsx3
# pip install gTTS
# pip install pygame
# pip install requests
# pip install pyaudio
#pip install openai


import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import musicLibrary
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer=sr.Recognizer()
engine = pyttsx3.init()
newsapi="a1661d6bc7d74accbede2e4c76d7ca40"
# masicLibrary=

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts =gTTS(text)
    tts.save('temp.mp3')

    
    
    pygame.mixer.init()

    pygame.mixer.music.load("temp.mp3")   # put your music file in same folder
    pygame.mixer.music.play()


    while  pygame.mixer.music.get_busy():
      pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")
    os.remove






def aiprocess(command):
   Client=OpenAI(
    api_key="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"
)
   completion = Client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant, skilled in general task like alexa and google and cloud. give short resposes please"},
        {"role": "user", "content": command}
    ]
)


   return completion.choices[0].message.content

def processCommand(c):
 
    if "open google" in c.lower():
       webbrowser.open("http://google.com")
    elif "open facebook" in c.lower():
       webbrowser.open("http://facebook.com")
    elif "open youtube" in c.lower():
       webbrowser.open("http://youtube.com")
    elif "open linkedin" in c.lower():
       webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower() or "new" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
        # Parse the JSON response
          data = r.json()

        # Extract the articles
          articles = data.get('articles', [])

        # Print the headlines (titles only)
          for article in articles:
            speak(article['title'])

    else:
        #let open ai handel the request
        output=aiprocess(c)


if __name__ == "__main__": 
    speak("Initializing Jarvis...")
    
    while True:
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                print("ya")
                # ---- Command listener ----
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error:", e)
