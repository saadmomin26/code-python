music = {
    "stealth":"https://www.youtube.com/watch?v=U47Trc=9BB_wE",
    "doorondooron":"https://youtu.be/LV_wiOhO40Q"
}


# # import speech_recognition as sr
# # import webbrowser
# # import pyttsx3  #text to speech



# # recognizer = sr.Recoginizer()#it is class
# # engine=pyttsx3.init()#intilization pyttsx

# # def speak(text):# fun we speek text
# #     engine.say( text)
# #     engine.runAndWait()

# # if __name__ == "__main__":
# #     speak("Hey sir how may i help you")

# import speech_recognition as sr
# import webbrowser
# import pyttsx3  # text to speech

# recognizer = sr.Recognizer()  # correct spelling
# engine = pyttsx3.init()  # initialization

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def processcommand(c):
#     print(c)
   

# if __name__ == "__main__":
#     speak("Initializing jarvis...")
#     while True:
#         # Listen for the wake word "Jarvis"
#         # obtain audio from the microphone
#         r = sr.Recognizer()
        
        
#         # recognize speech using Sphinx
#         print("recognizing...")
#         try:
#             with sr.Microphone() as source:
#               print("Listening...")
#               audio = r.listen(source,timeout=2,phrase_time_limit=1)
#             word =r.recognize_google(audio)
#             print("heard:",word)
#             if (word.lower()=="jarvis"):
#              speak("ya")
#              #listen command
#              with sr.Microphone() as source:
#               print("jarvis Active...")
#              audio = r.listen(source)
#              command =r.recognize_google(audio)
#             processcommand(command)
#         except Exception as e:
#             print("Error; {0}".format(e))