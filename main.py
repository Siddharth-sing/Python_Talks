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
        speakBaby("Good morning Sid!")
    elif hour in range(12,16):
        speakBaby("Good Afternoon Sid!")
    else:
        speakBaby("Good Evening Sid!")        

def speakBaby(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

speakBaby("Initialized...")
wishMe()    

