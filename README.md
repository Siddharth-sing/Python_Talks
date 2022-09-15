# Voice-Assistant-Python
Picachu assistant

# App's Overview 
<p>
* In this tutorial, we will be going through a voice assistant build with python for beginners. Prerequisites for reading this article are basic knowledge of python and python package importing.
<p> 

# Table Of Content

- [Project Setup ](#setup)
- [Imports & package installation](#imports)
- [Features and more](#features)
- [GitHub Repo ](#github)
- [Writer's Support ❤️](#support)

<a name="setup"></a>
# Project Setup
* I have used the VS code editor for this project. PyCharm is also equally recommended, it depends upon your personal choice which among the two to choose. But other than these two I won't strongly recommend any editor.

* Create a file `my_assistant.py`.

<a name="imports"></a>
# Imports & Packages Installation

* We will be using various python packages for creating our smart assistant. Some of them need to be installed while some are pre-installed packages.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/sb57gsww29d71p634yrd.png)  

* The imports visible in the above image are the brain cells of our assistant 😁. 

>**pyttsx3** - The most important package is `pyttsx3`.
 it is a **_text-to-speech conversion_** library in Python. Unlike alternative libraries, it works offline and is compatible with both Python 2 and 3.

```
# to download the package, write it in the terminal

pip install pyttsx3

# to import write this in my_assistant.py

import pyttsx3 

```

>**speech_recognition** - It allows computers to understand human language. Speech recognition is a machine's ability to listen to spoken words and identify them.
```
# to download the package, write it in the terminal

pip install SpeechRecognition

# to import write this in my_assistant.py

import speech_recognition as sr 
```
>**wikipedia** - Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia. Search Wikipedia, get article summaries, get data like links and images from a page, and more.

```
# to download the package, write it in the terminal

pip install wikipedia

# to import write this in my_assistant.py

import wikipedia as wk 
```

>**datetime** - For accessing date and time.
```
# to import write this in my_assistant.py

import datetime as dt
```
>**webbrowser** - For accessing the browser.
```
# to import write this in my_assistant.py

import webbrowser as wb
```
>**os** - For accessing operating system's operations.
```
# to import write this in my_assistant.py

import os
```

<a name="features"></a>
# Features and More

* This can be extended immensely as per the developer's interest. I have provided basic steps with a few features in this tutorial. But you can fork the [GitHub Repo ](#github) for various features.

### Feature - 1 (Listening) 
* We will make our assistant listen us firstly 😁 .
* `takeCommand()` function is ears for our assistant.

```
def takeCommand():
    r = sr.Recognizer()  # sr-> speech_recognition
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # for cancelling the backgroud noise 
        r.pause_threshold = 1
        print("Listening...")
        maudio = r.listen(source)
       
    print("Listened")   
    try: 
        print("Recognizing...")
        query = r.recognize_google(maudio, language = 'en-in')  # this step will recogize the text you spoke and store it into var query
         
    except Exception as e:
        query = "Say that again please!"

    return query        
```
* Now, you can use the `query` returned from `takeCommand()` for various tasks.


### Feature - 2 (speaking)

* It's time for our assistant to respond, because conversation must be two sided. 😊
* `speakBaby()` function will let our assistant speak.
```
def speakBaby(audio):
    engine = pyttsx3.init('sapi5')  # learn more about sapi5 in pyttsx3 documentation 
    voices = engine.getProperty('voices') # for getting all the voices (male and female)
    engine.setProperty('voice', voices[1].id) # set a voice with your choice
    engine.say(audio)
    engine.runAndWait()

```

### Feature - 3 (Wishing)
* `wishMe()` function allows our assistant to wish us according to the time of the day.

```
def wishMe():
    hour = int(dt.datetime.now().hour)
    if hour in range(0,12):
        speakBaby("Good morning Sid .. How may I help you !")
    elif hour in range(12,17):
        speakBaby("Good Afternoon Sid .. How may I help you !")
    else:
        speakBaby("Good Evening Sid .. How may I help you !")        
```
* We used `speakBaby()` for our assistant to speak out time.

> Note : These are the basic features for a working assistant and for more features checkout the GitHub repo attached below. 

<a name="github"></a>
{% github Siddharth-sing/Picachu_Talks%} 

<a name="support"></a> 
# Writer's Support
* If you find the article useful show some ❤️ by staring some of my repositories and following me on dev.to and github.
 <div>
  <p align="middle">
  <a href="https://www.linkedin.com/in/siddharth-singh-baghel-912866190/">
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
  </a>
  <a href="https://github.com/Siddharth-sing">
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
  </a>
  <a href="https://dev.to/siddharthsing">
  <img src="https://img.shields.io/badge/dev.to-0A0A0A?style=for-the-badge&logo=dev.to&logoColor=white">
  </a>


 


