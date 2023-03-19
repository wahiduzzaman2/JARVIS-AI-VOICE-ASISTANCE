import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import cv2
import random
import webbrowser
import smtplib
from requests import get
# import pywhatkit as kit
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #getting details of current voice
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

# Text to speech
def speak(audio):
    engine.say(audio)
    print(audio )
    engine.runAndWait()

# To convert voice into text
def takeCommand():  #It takes microphone input from the user and returns string output
    var_voice = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        var_voice.pause_threshold = 1
        audio = var_voice.listen(source)

        # audio = var_voice.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print("Recognizing...")    
        query = var_voice.recognize_google(audio, language ='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query


# To wish user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!") 
    else:
        speak("Good Evening!") 
    speak("I am Jarvis Sir. Please tell me how can I help you") 
# send email 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id @gmail.com', 'your-password')
    server.sendmail('your email id @gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
   
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            # print(results)
            speak(results)

        elif 'open command prompt' in query:
            os.system('start cmd')

        elif "open notepad" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories"
            os.startfile(npath)

        # elif 'open camera' in query:
        #     cap = cv2.VideoCapture(0)
        #     while True:
        #         ret, img = cap.read()
        #         cv2.inshow('webcam', img)
        #         k = cv2.waitKey(50)
        #         if k == 27:
        #             break
        #     cap.release()
        #     cv2.destroyAllWindows()

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your Ip address is {ip}")

        elif 'play music' in query:
            music_dir = 'F:\\SONGS\\Audio'
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs[0]))


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        # elif "play songs on youtube" in query:
        #     kit.playonyt("Faded")

        elif 'open google' in query:
            speak("Sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            webbrowser.open("google.com")

        elif 'email to zaman' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "wahiduzzaman991@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Wahid. I am not able to send this email")   
        
        # elif "send message" in query:
        #     kit.sendwhatmsg('01710472913', "Hello world",2 ,25)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  
        elif 'open code' in query:
            codePath = "C:\\Users\\WAHID\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)
        elif "no thanks" in query:
            speak("Thanks for using me Sir, have a good day")
            sys.exit()
        speak("Sir, do you have any other work")
