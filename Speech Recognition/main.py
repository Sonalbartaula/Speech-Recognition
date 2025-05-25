import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import datetime
import pyjokes
import google.generativeai as genai

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi="831ecb1b80d04b94ab1576e111bad02b"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    genai.configure(api_key="AIzaSyDExPpqopu7OC7B6J_2olHLXZ72XE6nXUA")
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(command)
    return response.text

def processcommand(c):
    c=c.lower()   # Convert command to lowercase for consistent matching
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://Youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

        # Play song using musiclibrary mapping

    elif c.startswith("play"):
        song=c.split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    
    elif "time" in c:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time right now is:{time_now}")
    
    elif "date" in c:
        date_today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {date_today}")
    
    elif "joke" in c:
        speak(pyjokes.get_joke())

    elif "search for" in c:
        query = c.replace("search for", "").strip()
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "weather" in c:
        city = "kathmandu"
        if "in" in c:
            city = c.split("in")[-1].strip()
            weather_key="d8bd4cf557ff40bb9be150909252405"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric"
        try:
            r = requests.get(url)
            print("API status code:", r.status_code)
            if r.status_code == 200:
                data = r.json()
                if "main" in data and "weather" in data:
                    temp = data["main"]["temp"]
                    desc = data["weather"][0]["description"]
                    speak(f"The temperature in {city.title()} is {temp}°C with {desc}.")
                else:
                    speak("I couldn't retrieve full weather details.")
            else:
                speak("Sorry, I couldn't find the weather for that city.")
        except Exception as e:
            print("Weather API error:", e)
            speak("There was a problem getting the weather.")
    # Fetch and speak top news headlines

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
    else:
         #let OpenAI handle the request
         output= aiprocess(c)
         speak(output)




if __name__ == "__main__":
    speak("It's me Jarvis ")
    while True:
            #obtain audio through microphone
            #listen for the word 'jarvis'
            r = sr.Recognizer()

            print("recognizing...")
                
            try:
                with sr.Microphone() as source:
                    print("Say something!")
                    audio = r.listen(source, timeout=4, phrase_time_limit=3)

                # Convert speech to text
                command = r.recognize_google(audio)
                print(f"you said:{command}")
                if (command.lower()=="jarvis"):
                    speak("Ya bro")

                # Listen again for actual command after wake word

                    with sr.Microphone() as source:
                         print("Jarvis Activated")
                         audio=r.listen(source)
                         command = r.recognize_google(audio)
                         print(f"Command Recognized:{command}")
                         processcommand(command)
                
            except Exception as e:
                print("Error; {0}".format(e))

