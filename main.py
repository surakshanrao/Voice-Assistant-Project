import time

import pyttsx3
import pyaudio
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
chrome_path ='"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("Enter your name")
name=input("Enter your name")

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<4:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your Assistant")

def takeCommand():# takes any command from microphone and gives text
   r=sr.Recognizer()
   with sr.Microphone() as source:
       print("Listening....")
       r.pause_threshold=1
       audio=r.listen(source)
   try:
        print("recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print("user said:",query)
   except Exception as e:
       print(e)
       speak("sorry, can you speak again?")
       return "None"
   return query


if __name__=="__main__":
    wishMe()
    while True:
        speak("How can I help you"+name)
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching in wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
           webbrowser.get(chrome_path).open("youtube.com")
           print("youtube opened")
           speak("youtube is opened")
        elif 'open instagram' in query:
           webbrowser.get(chrome_path).open("instagram.com")
           print("Instagram opened")
           speak("instagram is opened")
        elif 'open gmail' in query:
           webbrowser.get(chrome_path).open("gmail.com")
           print("gmail opened")
           speak("gmail is opened")
        elif 'play music' in query:
            music_dir='E:\\songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            speak("music is being played")
            time.sleep(2)
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")
            print(strTime)
        elif 'end' in query:
            speak("Thank you for your time"+name)
            exit()









