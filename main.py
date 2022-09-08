import pyttsx3
import speech_recognition as sr
import wikipedia as wk
import datetime
import webbrowser
import os
import smtplib 

def speakBaby():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    for voice in voices:
        engine.setProperty('voice', voice.id)
        engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()

speakBaby()    
