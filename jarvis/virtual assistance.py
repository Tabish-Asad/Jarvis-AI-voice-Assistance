import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import musicLibrary

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Tabish!")     
    elif 12 <= hour < 18:
        speak("Good Afternoon Tabish")
    else:
        speak("Good Evening Tabish")
    speak("I am Jarvis. Say Jarvis to activate me anytime.")

def listen(limit=4):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=limit)
    try:
        return r.recognize_google(audio, language="en-in").lower()
    except:
        return "none"

# ---------------- MAIN ----------------
wishMe()

while True:
    print("Waiting for wake word...")
    wake = listen(limit=2)   # short listen for "jarvis"

    if "jarvis" in wake:
        speak("Yes")   # immediate response
        print("Jarvis Active...")

        # Now listen for actual command
        command = listen(limit=5)
        print(f"Command: {command}")

        if 'wikipedia' in command:   
            speak("Searching Wikipedia")
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif 'facebook' in command:
            speak("Opening Facebook")
            webbrowser.open("https://facebook.com")

        elif 'stack overflow' in command:
            speak("Opening Stack Overflow")
            webbrowser.open("https://stackoverflow.com")

        elif 'google' in command:
            if "open google" in command:
                speak("Opening Google")
                webbrowser.open("https://google.com")
            else:
                command = command.replace("google", "").replace("search", "").strip()
                if command:
                    speak(f"Searching Google for {command}")
                    webbrowser.open(f"https://google.com/search?q={command}")
                else:
                    speak("Opening Google")
                    webbrowser.open("https://google.com")


        elif command.startswith("play"):
            parts = command.split(" ")
            if len(parts) > 1:
                song = parts[1]
                if song in musicLibrary.music:
                    link = musicLibrary.music[song]
                    speak(f"Playing {song}")
                    webbrowser.open(link)
                else:
                    speak("Sorry, I could not find that song.")
            else:
                speak("Please tell me which song to play.")

        elif 'linkedin' in command:
            speak("Opening LinkedIn")
            webbrowser.open("https://linkedin.com")

        elif 'time' in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak("Sir, the time is")
            speak(time)

        elif 'today date' in command:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak("Sir, today is")
            speak(date)

        elif 'sleep' in command or 'exit' in command or 'quit' in command:
            speak("Thank you, shutting down.")
            break
