import pyttsx3
import speech_recognition as sr
import wikipedia as wk
import datetime
import webbrowser
import os
import smtplib 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour in range(0,12):
        speakBaby("Good morning Sid .. How may I help you !")
    elif hour in range(12,17):
        speakBaby("Good Afternoon Sid .. How may I help you !")
    else:
        speakBaby("Good Evening Sid .. How may I help you !")        

def speakBaby(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        print("Listening...")
        maudio = r.listen(source)
       
    print("Listened")   
    try: 
        print("Recognizing...")
        query = r.recognize_google(maudio, language = 'en-in'    )
        print(f"user said: {query}\n")  
    except Exception as e:
        print("Say that again please!")          

#main
speakBaby("Initialized...")
wishMe()   
takeCommand() 

