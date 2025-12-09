import pywhatkit
import speech_recognition as sr
import webbrowser
import pyttsx3
from newsdataapi import NewsDataApiClient
import random
import re
import urllib.parse

# Initialize components
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change this index after testing
engine.setProperty('rate', 175)
newsapi = NewsDataApiClient(apikey='pub_c106470c22294bcfb8062ddbaddf05ed')

# Text-to-speech function
def speak(text):
    engine.say(text)
    engine.runAndWait()

def professor_greeting():
    greetings = [
        "Hello! How can I help you today?",
        "Yes, I'm listening. What would you like to do?",
        "Professor here. Ready when you are.",
        "I'm here. Go ahead, I'm listening."
    ]
    speak(random.choice(greetings))

# Handle commands
def processCommand(command):
    c = command.lower()

    # Search on YouTube
    match_search = re.search(r"search (.+?) on youtube", c)
    if match_search:
        query = match_search.group(1).strip()
        encoded_query = urllib.parse.quote_plus(query)
        url = f"https://www.youtube.com/results?search_query={encoded_query}"
        speak(f"Searching for {query} on YouTube.")
        webbrowser.open(url)
        return
    # Search on Google
    match_search = re.search(r"search (.+?) on google", c)
    if match_search:
        query = match_search.group(1).strip()
        encoded_query = urllib.parse.quote_plus(query)
        url = f"https://www.google.com/search?q={encoded_query}"
        speak(f"Searching for {query} on google.")
        webbrowser.open(url)
        return

    # Play on YouTube
    match_play = re.search(r"play (.+?) (on )?youtube", c)
    if match_play:
        video_query = match_play.group(1).strip()
        speak(f"Playing {video_query} on YouTube.")
        pywhatkit.playonyt(video_query)
        return

    # Open websites
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    # News headlines
    elif "news" in c:
        response = newsapi.latest_api(q='latest', country='pk', language='en')
        articles = response.get('results', [])
        if not articles:
            speak("Sorry, I couldn't find any news right now.")
        else:
            speak("Here are the top headlines.")
            for article in articles[:5]:
                title = article.get('title', '')
                if title:
                    print("News:", title)
                    speak(title)
    elif "exit" in c or "quit" in c or "stop" in c:
        speak("Goodbye. Professor going offline.")
        exit()

# Main loop
if __name__ == "__main__":
    speak("Initializing Professor, your virtual assistant.")
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
            word = recognizer.recognize_google(audio)

            if "professor" in word.lower():
                professor_greeting()
                with sr.Microphone() as source:
                    print("Professor Active...")
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)
        except sr.UnknownValueError:
                speak("Sorry, I didn't catch that.")
        except sr.RequestError as e:
                speak("Could not request results; check your internet connection.")
        except Exception as e:
            print(f"Error: {e}")
