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
##Imports & Packages Installation

* We will be using various python packages for creating our smart assistant. Some of them need to be installed while some are pre-installed packages.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/sb57gsww29d71p634yrd.png)  

* The imports visible in the above image are the brain cells of our assistant 😁. 

>**pyttsx3** - The most important package is `pyttsx3`.
 it is a **_text-to-speech conversion_** library in Python. Unlike alternative libraries, it works offline and is compatible with both Python 2 and 3.

```
## to download the package, write it in the terminal

pip install pyttsx3

## to import write this in my_assistant.py

import pyttsx3 

```

>**speech_recognition** - It allows computers to understand human language. Speech recognition is a machine's ability to listen to spoken words and identify them.
```
## to download the package, write it in the terminal

pip install SpeechRecognition

## to import write this in my_assistant.py

import speech_recognition as sr 
```
>**wikipedia** - Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia. Search Wikipedia, get article summaries, get data like links and images from a page, and more.

```
## to download the package, write it in the terminal

pip install wikipedia

## to import write this in my_assistant.py

import wikipedia as wk 
```

>**datetime** - For accessing date and time.
```
## to import write this in my_assistant.py

import datetime as dt
```
>**webbrowser** - For accessing the browser.
```
## to import write this in my_assistant.py

import webbrowser as wb
```
>**os** - For accessing operating system's operations.
```
## to import write this in my_assistant.py

import os
```


 


