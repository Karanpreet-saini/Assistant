import os
import random
import sys
import datetime
import webbrowser
import subprocess

from gtts import gTTS   # converts text to speech
import pyttsx3
import playsound as playsound   # to play Audio

import speech_recognition as sr  # converts speech to text
import wikipedia
import pywhatkit
import pyjokes


from tkinter import *
from PIL import ImageTk, Image

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    print("Voice Assistant" + " : " + text)
    engine.runAndWait()


def take_command(ask=False):
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            talk(ask)
        talk("You can Speak now")
        print("listening")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        print("stop")

    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("Recognized Voice : " + command)
        return command

    except:
        return "None"


def wishMe():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:

        talk("Hello,Good Morning")

    elif hour >= 12 and hour < 18:

        talk("Hello,Good Afternoon")

    else:

        talk("Hello,Good Evening")


wishMe()

def date():
    now = datetime.datetime.now()
    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    ordinalnames = ['1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                    '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24rd', '25th',
                    '26th', '27th', '28th', '29th', '30th', '31st']

    talk("Today is " + month_names[month_name - 1] + " " + ordinalnames[day_name - 1] + '.')


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"

    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def respond():
    run = 1
    if __name__ == '__main__':
        while run == 1:
            order = take_command()
            results = ''
            run += 1

        if 'what is your name' in order:
            talk('My name is karan')

        elif 'search' in order:
            search = take_command('what do you want to search')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            talk('here is what i found for' + search)

        elif 'find location' in order:
            location = take_command('what is the location')
            url = 'https://google.nl/maps/place/' + location
            webbrowser.get().open(url)
            talk('here is what i found for' + location)

        elif 'play' in order:
            song = order.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)

        elif 'joke' in order:
            talk(pyjokes.get_joke())

        elif 'who' in order:
            thing = order.replace('who', '')
            info = wikipedia.summary(thing, 1)
            talk(info)

        elif 'what' in order:
            thing = order.replace('what', '')
            info = wikipedia.summary(thing, 1)
            talk(info)

        elif 'how' in order:
            thing = order.replace('how', '')
            info = wikipedia.summary(thing, 1)
            talk(info)

        elif 'tell me' in order:
            thing = order.replace('tell me', '')
            info = wikipedia.summary(thing, 1)
            talk(info)

        elif 'close program' in order:
            sys.exit()


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
    btn = Button(screen, text='Speak', font=('railways', 10, 'bold'), bg='red', fg='white', command=respond()).pack(fill='x', expand='no')
    btn2 = Button(screen, text='Close', font=('railways', 10, 'bold'), bg='yellow', fg='black', command=screen.destroy).pack(fill='x', expand='no')
    screen.mainloop()

main_screen()