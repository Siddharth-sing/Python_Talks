import pyttsx3
import speech_recognition as sr
import wikipedia as wk
import datetime as dt
import webbrowser as wb
import os
# import smtplib 

def wishMe():
    hour = int(dt.datetime.now().hour)
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
        # str = "you said"+"..."+query 
        # speakBaby(str)
        # print(str)
         
    except Exception as e:
        query = "Say that again please!"
        # speakBaby("Say that again please!")  

    return query            

#main
def main(t):
    t =True
    query = takeCommand() 
    print(query)
    
    if 'wikipedia' in query.lower():
        speakBaby('Searching wikipedia ...')
        query = query.lower().replace("wikipedia","")
        result = wk.summary(query, sentences = 2)
        print(result)
        speakBaby(result)
    elif 'youtube' in query.lower():
        speakBaby('opening youtube ...')
        wb.open("https://www.youtube.com/")
    elif any(x in query.lower() for x in ['play','spotify','music']):
        speakBaby('opening Spotify ...')
        wb.open("https://open.spotify.com/")
    elif 'open documents' in query.lower():
        documents_dir = "C:\\Users\\KIIT\\OneDrive\\Documents"
        documents = os.listdir(documents_dir)
        print(documents)
    elif 'time' in query.lower():
        strTime = dt.datetime.now().strftime("%H:%M:%S")
        speakBaby(f"Sir the time is {strTime}")
    elif 'open vs code' in query.lower():
        vscode_path = "C:\\Users\\KIIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    
        speakBaby("opening code")
        os.startfile(vscode_path)
    elif 'quit' in  query.lower():
        t = False
        speakBaby("Hope you loved interacting ! Bye-Bye")
    return t        

wishMe()
t = True
while t:
    t = main(t)



       
    

