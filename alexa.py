# from multiprocessing.connection import Listener
import speech_recognition as sr  # listener
import pyttsx3  # engine
import pywhatkit  # play to youtube
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
# engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 145)
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)
engine.say('Hello my name is alexa')
engine.say('What can I do for you')
engine.runAndWait()


def talk(text):
    engine.setProperty('rate', 139)
    engine.say(text)
    engine.runAndWait()


def take_command():

    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                # talk(command)
            else:
                return talk("wrong keyword")
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk(' Ok playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again')


while True:

    run_alexa()
