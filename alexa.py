import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import os

alexa = pyttsx3.init('sapi5')
voices = alexa.getProperty('voices')
print(voices[1])

alexa.setProperty('voice', voices)


def speak(audio):
    alexa.say(audio)
    alexa.runAndWait()


def message():
    hour = datetime.datetime.now().hour

    if (hour >= 0 and hour < 12):
        speak("good morning sir")
    elif (hour >= 12 and hour < 18):
        speak("good afternoon sir")
    else:
        speak("good evening sir")

    speak("I am your google alexa tell me how can i help you")


def command():
    a = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am listening.....")
        print("I am listening.....")
        audio = a.listen(source)
        a.pause_threshold = 1
    try:

        speak("Recognition")
        query = a.recognize_google(audio, language="en-in")
        print(query)
    except Exception as e:
        speak("sorry sir i didn't hear you please say it again")

        return "empty"
    return query


if __name__ == "__main__":
    message()

    while True:
        query = command().lower()

        if 'chrome' in query:
            speak("Opening chrome please wait....")
            os.system('chrome')

        elif 'notepad' in query:
            speak("i am opening please wait...")
            os.system('notepad')

        elif 'youtube' in query:
            speak("youtube is opening please wait....")
            webbrowser.open("https://www.youtube.com/")

        elif 'linkedin' in query:
            speak("linkedin is opening please wait....")
            webbrowser.open("https://www.linkedin.com/")

        elif 'facebook' in query:
            speak("facebook is opening please wait....")
            webbrowser.open("https://www.facebook.com/")

        elif 'instagram' in query:
            speak("opening instagram please wait.....")
            webbrowser.open("https://www.instagram.com/")

        elif 'your name' in query:
            speak("my name is google alexa")

        elif 'how are you' in query:
            speak("i am fine what about you")

        elif 'play music' in query:
            dir = 'give path'
            song = os.listdir(dir)
            os.startfile(os.path.join(dir, songs[random.randrange(0, 50)]))

        elif 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace('wikipedia', '')

            result = wikipedia.summary(query, sentences=10)
            print(result)
            speak(result)

        elif 'bye' in query:
            speak("thankyou sir for using me..")
            break

        else:
            speak("thankyou sir")