
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import musicLibrary


recognizer=sr.Recognizer()
engine = pyttsx3.init()
newsapi="a1661d6bc7d74accbede2e4c76d7ca40"
# masicLibrary=

def speak(text):
    engine.say(text)
    engine.runAndWait()

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

if __name__ == "__main__": 
    speak("Initializing Jarvis...")
    
    while True:
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                # 1. Listen for the wake word with relaxed limits
                print("Listening for 'Jarvis'...")
                # Increased timeout (5s) and phrase_time_limit (3s)
                audio = r.listen(source, timeout=5, phrase_time_limit=3) 
            
            # 2. Try to recognize the word
            word = r.recognize_google(audio)
            print(f"Heard: {word}") # Print what was heard for debugging
            
            if word.lower() == "jarvis":
                speak("Ya")
                print("Ya")
                
                # ---- Command listener ----
                with sr.Microphone() as source:
                    # You can be less strict on command listening
                    print("Jarvis Active. Listening for command...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"Command Heard: {command}")
                    
                    processCommand(command)

        # 3. Handle common speech recognition errors specifically
        except sr.WaitTimeoutError:
            print("Did not detect speech within the timeout.")
        except sr.UnknownValueError:
            # This happens if audio was recorded but couldn't be understood
            print("Google Speech Recognition could not understand audio")
        except Exception as e:
            # Handle all other, unexpected errors
            print(f"An unexpected error occurred: {e}")
