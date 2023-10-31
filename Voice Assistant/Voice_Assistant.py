import pyttsx3   #a text-to-speech conversion library in Python
import datetime     #imported to work with the date as well as time.
import speech_recognition as s   #Speech recognition is a machine's ability to listen to spoken words and identify them
import webbrowser       # to allow displaying web-based documents to users
import wikipedia        #to fetch a variety of information from the Wikipedia website.
import pywhatkit as pk      #to search and play the top most reccomended video on youtube
from AppOpener import *     #open/close any application without knowing it's absoulute path.
import pyautogui    #lets Python control the mouse and keyboard, and other GUI automation tasks.  
import os       #provides easy functions that allow us to interact and get Operating System information

#To fetch the inbluit voice of the computer 
engine=pyttsx3.init('sapi5')    
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#To let computer speak 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# To wish the user according to the time
def greet(): 
    a=datetime.datetime.now().hour
    if (0<=a<12):
        speak('Good morning')
    elif(12<=a<18):
        speak('Good afternoon')
    else:
        speak('Good evening')
    speak('Hello I am your personal assistant, how may I help you? ')

#To recognize and understand the command given
def command():
    a = s.Recognizer()
    with s.Microphone() as source:
        print('Taking Command....')
        audio=a.listen(source)
        a.pause_threshold=0.5 #After the pause of 0.5 seconds it starts to recognize
        a.energy_threshold = 50 #This is use to define the microphone sensitivity 
    try:
        print('Recognizing')
        query = a.recognize_google(audio,language='en-in')  #Converts the speech into string 
        print('user said',query)
    except Exception as e:
        print('say that again please')
        return 'None'
    return query

greet()

while True:
    query=command().lower()
    
    #To search any info on wikipedia
    if 'wikipedia' in query:
        speak('search wikipedia')
        query=query.replace('wikipedia','')
        results= wikipedia.summary(query,sentences=2)
        speak('according to wikipedia')
        speak(results)
    
    #To Quit the program
    elif 'stop' in query:
        speak('Bye Bye')
        exit(0)   
    
    #To open the Youtube
    elif 'open youtube' in query:
        speak('opening youtube')
        webbrowser.open('youtube.com')
    
    #To open the mail
    elif 'open mail' in query:
        speak('opening gmail')
        webbrowser.open('gmail.com')
    
    #To open the google
    elif 'open google' in query:
        speak('opening google')
        webbrowser.open('google.com')
    
    #To open the whatsapp 
    elif 'open whatsapp' in query:
        speak('opening whatsapp')
        webbrowser.open('whatsapp .com')
    
    #To playing a commanded video on youtube
    elif 'search youtube' in query:
        query=query.replace('search youtube','')
        pk.playonyt(query)
    
    #To open any software present inside the system
    elif 'open' in query:
        query=query.replace('open','')
        open(query)   
    
    #To take the screenshots 
    elif "screenshot" in query:
        screenshot = pyautogui.screenshot()
        screenshot.save(r'D:\\screenshot\\screenshot.png')
    
    #To Calculate the basic calculation
    elif 'calculate' in query:
        query=query.replace('calculate','')
        d=query
        c=list(d)
        if c[3]=='+':           #addition
            b=float(c[1]) + float(c[5])
            speak(b)
        elif c[3]=='-':         #substraction
            b=int(c[1]) - int(c[5])
            speak(b)
        elif c[3]=='/':         #division
            b=int(c[1]) / int(c[5])
            speak(b)
        elif c[3]=='x':         #multiply
            b=int(c[1]) * int(c[5])
            speak(b)   
    
    #To give search results from google for a particular website
    elif '.com' in query:
        query=query.replace('open','')
        webbrowser.open(query)
    
    #To Quit the program 
    elif 'shutdown' in query:
        speak('shutting down')
        os.system("shutdown /s /t 1")