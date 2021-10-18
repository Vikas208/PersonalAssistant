import pyttsx3
import speech_recognition as sr
import datetime as dt
import getpass
from googlesearch import search
from youtube_search import YoutubeSearch
import wikipedia
import webbrowser
from pyttsx3.driver import sapi5

# Set Voice Property
try:
    engin = pyttsx3.init(sapi5)
    voices = engin.getProperty('voices')
    engin.setProperty('voice', voices[0].id)
    rate = engin.setProperty('rate', '100')
except Exception as e:
    print(e)


def speak(audio):
    engin.say(audio)
    engin.runAndWait()


def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said:{query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognizing your voice")
        return "None"
    return query


def wishMe():
    hour = int(dt.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("Good Morning Sir !")
    elif hour >= 12 and hour < 18:
        speak("Good AfterNoon Sir !")
    else:
        speak("Good Evening Sir !")

    speak("I am your Personal Assistant, Version 2 point O")


if __name__ == '__main__':

    try:
        wishMe()

        while(True):
            query = Listen().lower()

            if 'stop' in query:
                speak("Shuting Down sir")
                speak("Good Bye have nice day")
                break

            elif 'How are you' in query:
                speak("I am Fine Sir!")

            elif 'search on google' in query:
                query = query.replace('search on Goolge', " ")
                speak(f"Searching {query}")
                for j in search(query, tld="co.in", num=1, start=0, stop=5, pause=2):
                    webbrowser.open(j)

            elif 'google' and 'open google' in query:
                speak("Opening Google")
                webbrowser.open('https://google.com')

            elif 'who is' and 'search in wikipedia' and 'wikipedia' in query:
                speak("Search on Wikipedia")
                if('wikipedia' in query):
                    query = query.replace('wikipedia', " ")
                else:
                    query = query.replace("who is", " ")
                speak("According to wikipedia")
                print("According to wikipedia...")
                summary = wikipedia.summary(query, sentences=2)
                print(summary)
                speak(summary)

            elif 'search on youtube' and 'play on youtube' in query:
                query = query.replace("youtube", " ")
                speak("Search on Youtube")
                result = YoutubeSearch(query, max_result=2).to_json()
                webbrowser.open(result)

            elif 'open youtube' and 'youtube' in query:
                speak("Open youtube")
                webbrowser.open('https://youtube.com')
    except Exception as e:
        print(e)
