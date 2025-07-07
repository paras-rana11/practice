import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')  # Use app password here
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'open chatgpt' in query:
            speak("Opening ChatGPT")
            webbrowser.open("https://chat.openai.com")

        elif 'open odoo' in query:
            speak("Opening Odoo")
            webbrowser.open("https://www.odoo.com")

        elif 'play music' in query or 'play songs' in query:
            speak("Playing music from YouTube")
            # Open a specific YouTube playlist or video link
            webbrowser.open("https://youtu.be/lrIKt5uDWZo?si=BZk8spz8_ngodXLs")

        elif 'play local music' in query:
            music_dir = r'C:\\paras\\Assignment\\Python\\Jarvis'  # Path to the directory
            music_file = 'Play_date.mp3'  # Your music file
            full_music_path = os.path.join(music_dir, music_file)

            if os.path.exists(full_music_path):
                os.startfile(full_music_path)
            else:
                speak("Sorry, I couldn't find the music file.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Path\\To\\Your\\IDE.exe"  # Replace with your editor path
            if os.path.exists(codePath):
                os.startfile(codePath)
            else:
                speak("Code editor path is incorrect or doesn't exist.")

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pavanrana469@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't send this email.")
        else:
            speak("I didn't understand. Please repeat that.")
