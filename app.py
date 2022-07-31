import speech_recognition as sr  # To convert speech into text
import pyttsx3  # To convert text into speech
import datetime  # To get the date and time
import wikipedia  # To get information from wikipedia
import webbrowser  # To open websites
import os  # To open files
import time  # To calculate time
import subprocess  # To open files
from tkinter import *  # For the graphics
import pyjokes  # For some bad jokes
from playsound import playsound  # To playsound
from PIL import ImageTk, Image

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    print("Voice Assistant" + " : " + text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:

        speak("Hello,Good Morning")

    elif hour >= 12 and hour < 18:

        speak("Hello,Good Afternoon")

    else:

        speak("Hello,Good Evening")


def get_audio(ask=False):
    r = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        if ask:
            speak(ask)
        speak("You can speak now")
        print("Listening")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=3)
        print("Stop.")

    try:
        text = r.recognize_google(audio, language='en-US')
        print('You: ' + ': ' + text)
        return text


    except:

        return "None"


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"

    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def date():
    now = datetime.datetime.now()
    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    ordinalnames = ['1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                    '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24rd', '25th',
                    '26th', '27th', '28th', '29th', '30th', '31st']

    speak("Today is " + month_names[month_name - 1] + " " + ordinalnames[day_name - 1] + '.')


wishMe()


def Process_audio():
    run = 1
    if __name__ == '__main__':
        while run == 1:

            statement = get_audio().lower()
            results = ''
            run += 1

            if "hello" in statement or "hi" in statement:
                wishMe()

            if "good bye" in statement or "ok bye" in statement or "stop" in statement:
                speak('Your personal assistant ' + "name_assistant" + ' is shutting down, Good bye')
                screen.destroy()
                break

            elif 'search' in statement:
                search = get_audio('what do you want to search')
                url = 'https://google.com/search?q=' + search
                webbrowser.get().open(url)
                speak('here is what i found for' + search)

            elif 'tell me' or 'who' or 'what' or 'how' or 'wikipedia' in statement:
                thing = statement.replace('tell me', '')
                info = wikipedia.summary(thing, 1)
                speak(info)

            if 'joke' in statement:
                speak(pyjokes.get_joke())

            if 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(5)

            if 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google chrome is open now")
                time.sleep(5)

            if 'open gmail' in statement:
                webbrowser.open_new_tab("mail.google.com")
                speak("Google Mail open now")
                time.sleep(5)

            if 'open netflix' in statement:
                webbrowser.open_new_tab("netflix.com/browse")
                speak("Netflix open now")

            if 'open prime video' in statement:
                webbrowser.open_new_tab("primevideo.com")
                speak("Amazon Prime Video open now")
                time.sleep(5)

            elif 'find location' in statement:
                location = get_audio('what is the location')
                url = 'https://google.nl/maps/place/' + location
                webbrowser.get().open(url)
                speak('here is what i found for' + location)

            if 'news' in statement:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/city/mangalore")
                speak('Here are some headlines from the Times of India, Happy reading')
                time.sleep(6)

            if 'cricket' in statement:
                news = webbrowser.open_new_tab("cricbuzz.com")
                speak('This is live news from cricbuzz')
                time.sleep(6)

            if 'corona' in statement:
                news = webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/")
                speak('Here are the latest covid-19 numbers')
                time.sleep(6)

            if 'time' in statement:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            if 'date' in statement:
                date()

            if 'who are you' in statement or 'what can you do' in statement:
                speak(
                    'I am ' + "name_assistant" + ' your personal assistant. I am programmed to perform tasks like opening youtube, google chrome, gmail and search wikipedia etc')

            if "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                speak("I was built by Karanpreet Saini")

            if 'make a note' in statement:
                statement = statement.replace("make a note", "")
                note(statement)

            if 'note this' in statement:
                statement = statement.replace("note this", "")
                note(statement)

            speak(results)

def main_screen():
    global screen
    screen = Tk()
    screen.title('Voice Assistant')
    screen.geometry('800x320')
    img = ImageTk.PhotoImage(Image.open('chatbot.jpg'))
    panel = Label(screen, image=img)
    panel.pack(side='right', fill='both', expand='no')

    compText = StringVar()
    userText = StringVar()

    userText.set('Your Virtual Assistant')
    userFrame = LabelFrame(screen, text='Karan', font=('Railways', 24, 'bold'))
    userFrame.pack(fill='both', expand='yes')

    top = Message(userFrame, textvariable=userText, bg='black', fg='white')
    top.config(font=("Century Gothic", 15, 'bold'))
    top.pack(side='top', fill='both', expand='yes')
    btn = Button(screen, text='Speak', font=('railways', 10, 'bold'), bg='red', fg='white', command=Process_audio).pack(fill='x', expand='no')
    btn2 = Button(screen, text='Close', font=('railways', 10, 'bold'), bg='yellow', fg='black', command=screen.destroy).pack(fill='x', expand='no')
    screen.mainloop()

main_screen()