import pyttsx3
import datetime
import webbrowser
import speech_recognition as sr
from random import choice
import os
import subprocess
import wikipedia
import pywhatkit as kit
import traceback
from tkinter import *
# from decouple import config

query=''
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 180)

bot_name = "Tiffany"
User_name = "rishi"

paths = {
    'notepad': "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\\Notepad",
    'google chrome': 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s',
    'calculator': "C:\\Windows\\System32\\calc.exe",


}

positive_response = ["Cool, I am on it sir!", " Okay sir, I'm working on it!", "Just a second sir!"]
negative_response = ["I think its invalid Command ", "My inventor didn't taught me this!", "Sorry!, i dont know how to do this" ]
gratitude = ["I am happy to help!", "My pleasure sir!", "No problem!"]







def speak(text):
    engine.say(text)
    engine.runAndWait()

def unauthorized():
    speak("You are unauthorized")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("listening")
        print('Listening....')
        r.pause_threshold = 2
        audio = r.listen(source, phrase_time_limit=5 )

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if 'exit' in query or 'stop' in query:
            hour = datetime.datetime.now().hour
            if 21 <= hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
        return query



    except Exception as e:
        traceback.print_exc()
        speak('Sorry, I could not understand. Could you please say that again?')
        query = take_command()
    return query


def validate_command(query):
    if "text file" in query:
        speak(choice(positive_response))
        new_text_file()
    elif "command prompt" in query:
        speak(choice(positive_response))
        open_cmd()
    elif "calculator" in str.lower(query):
        speak(choice(positive_response))
        open_calculator()
    elif "notepad" in str.lower(query):
        speak(choice(positive_response))
        open_notepad()
    elif "google" in str.lower(query):
        speak(choice(positive_response))
        open_google()
    elif "send a WhatsApp message" in query:
        speak(choice(positive_response))
        send_whatsapp_message()
    elif "according to google" in query:
        speak(choice(positive_response))
        search_on_google()
    elif "according to Wikipedia" in query:
        speak(choice(positive_response))
        search_on_wikipedia()
    elif "thank you" in query:
        speak(choice(gratitude))

    elif "close" in query:
        speak('goodbye, have a nice day')
    else:
        speak(choice(negative_response))





def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
        except Exception:
            speak('Sorry, I could not understand. Could you please say that again?')
            query = 'None'
        return query

def search_on_wikipedia():

    query = take_command()
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)


def search_on_google():
    query = take_command()
    webbrowser.get(paths['google chrome']).open(query)

def open_cmd():
    os.system('start cmd')

def open_calculator():
    subprocess.Popen(paths['calculator'])

def open_google():
    webbrowser.get(paths['google chrome']).open('www.google.com ')
def open_notepad():
    os.startfile(paths['notepad'])

def open_opera():
    os.startfile(paths['opera'])

def new_text_file():
    # make new notepad file
    speak("What will be the name of the file? ")
    file_name = take_user_input()
    file = "C:\\Users\\rishi Mukesh Jain\\desktop\\"+file_name + ".txt"
    f = open(file, "w+")
    speak("What do you want to write into the file")
    content = take_user_input()
    f.write(content)
    speak("New text file made with name " + file_name)
    f.close()

def send_whatsapp_message():
    speak("whom do you want to send? please enter on console")
    number = input("enter the number: ")
    speak("what do you want to send")
    message = take_user_input()
    kit.sendwhatmsg_instantly(f"+91{number}", message)

    file_name = take_user_input()
def greet():
    current_time = datetime.datetime.now().hour

    if 4 < current_time <= 12:
        speak("Good morning " + User_name + "!")
    elif 12 < current_time <= 16:
        speak("Good afternoon " + User_name + "!")
    elif 16 < current_time <= 21:
        speak("Good evening " + User_name + "!")
    elif 21 < current_time < 23 or 0 <= current_time <= 4:
        speak("Its a late night " + User_name + "!")

    speak("What would you like to do ?")

'''
if __name__ == "__main__":

    greet()
    while True:
        query = take_command()
        print("You said \" " + query + " \"")
        validate_command(query)
        if 'close' in query:
            break

#btn = Button(root, text='Speak', font=('railways', 10, 'bold'), bg='red', fg='white', command=Tiffany).pack(fill='x', expand='no')

root.mainloop()
'''
r = Tk()


def tiffany(event):
    query = take_command()
    print("You said \" " + query + " \"")
    validate_command(query)
    return query

r.wm_geometry('450x850')
mic = PhotoImage(file="002-microphone.png")
widget = Button(r, image=mic, bg="#151B54", borderwidth='0' )
widget.pack(side=BOTTOM, anchor=N, pady=300)
widget.bind('<Button-1>', tiffany)
r.configure(bg="#151B54")
if 'close' in query:
    r.destroy()

r.mainloop()







'''        
def send_email():
    try:
        speak("Whom do you want to mail?, write correct mail id on console")
        receiver_address = input("Write mail id here: ")
        speak("What should be the subject?")
        subject = take_user_input()
        speak("What should i write?")
        message = take_user_input()

        draft = EmailMessage()
        draft["To"] = receiver_address
        draft["subject"] = subject
        draft["From"] = email_id
        draft.set_content(message)

        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(email_id, password)
        s.send_message(draft)
        s.close()
        speak("Email sent successfully")

    except Exception as e:
        speak("There was an error!")
        print(e)
'''