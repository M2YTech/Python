import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from newsdataapi import NewsDataApiClient
import requests
import re
import urllib.parse


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = NewsDataApiClient(apikey='pub_c106470c22294bcfb8062ddbaddf05ed')
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    match = re.serach(r"search (.+?) on youtube", c.lower())
    if match:
        query = match.group(1).strip()
        encoded_query = urllib.parse.quote_plus(query)
        url = f"https://www.youtube.com/results?search_query={encoded_query}"
        speak(f"Searching for {query} on YouTube.")
        webbrowser.open(url)
        return
    if("open google" in c.lower()):
        webbrowser.open("https://google.com")
    elif("open facebook" in c.lower()):
        webbrowser.open("https://facebook.com")
    elif("open youtube" in c.lower()):
        webbrowser.open("https://youtube.com")
    elif("open linkedin" in c.lower()):
        webbrowser.open("https://linkedin.com")
    # elif(c.lower().startswith("play")):
    #     song = c.lower().replace("play", "").strip()
    #     link = musicLibrary.music.get(song)
    #     if link:
    #         webbrowser.open(link)
    #     else:
    #         speak("Sorry, I couldn't find that song in your library.")
    elif("news" in c.lower()):
        response = newsapi.latest_api(q='latest', country='pk', language='en')
        print("Raw response:", response)
        articles = response.get('results', [])
        if not articles:
            speak("Sorry, I couldn't find any news right now.")
        else:
            speak("Here are the top headlines.")
            for article in articles[:5]:  # Limit to 5 headlines
                title = article.get('title', '')
                if title:
                    print("News: ", title)  # Debug
                    speak(title)




if __name__ == "__main__":
    speak("Initializing Professor, your virtual assistant.")
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
            word = recognizer.recognize_google(audio)
            if("professor" in word.lower()):
                speak("Yes, how can I assist you?")
                with sr.Microphone() as source:
                    print("Professor Active...")
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))




