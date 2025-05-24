import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi="831ecb1b80d04b94ab1576e111bad02b"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    c=c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://Youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        song=c.split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c:
        r= requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        

# Check if the request was successful
        if r.status_code==200:
            data =r.json()
            articles=data.get('articles', [])
            if articles:
                    speak("Here are the top news headlines.")
                    for article in articles[:5]:
                        title = article.get("title")
                        if title:
                            speak(title)
            else:
                    speak("No news articles found.")





if __name__ == "__main__":
    speak("It's me Jarvis ")
    while True:
            r = sr.Recognizer()

            print("recognizing...")
                
            try:
                with sr.Microphone() as source:
                    print("Say something!")
                    audio = r.listen(source, timeout=4, phrase_time_limit=3)
                
                command = r.recognize_google(audio)
                print(f"you said:{command}")
                if (command.lower()=="jarvis"):
                    speak("Ya bro")

                    with sr.Microphone() as source:
                         print("Jarvis Activated")
                         audio=r.listen(source)
                         command = r.recognize_google(audio)
                         print(f"Command Recognized:{command}")
                         processcommand(command)
                
            except Exception as e:
                print("Error; {0}".format(e))

