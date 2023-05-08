# libraries and modules used

import cv2
import numpy as np
import face_recognition as fr
import os
import pyttsx3
import datetime
import webbrowser
import speech_recognition as sr
from random import choice
import subprocess
import wikipedia
import pywhatkit as kit
import traceback
from tkinter import *
from PIL import Image , ImageTk
import time
from tkinter import ttk
# main code
query = ''
root = Tk()
window_width = 376
window_height = 373
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.overrideredirect(True)
img1 = Image.open("logo.png")
photo = ImageTk.PhotoImage(img1)
label = Label(root, image=photo)
label.pack(expand=True, side=BOTTOM)
grip = ttk.Sizegrip()
grip.place()
grip.lift(label)
root.after(3000, lambda: root.destroy())
root.mainloop()

path = 'rishi data'
image = []
classn = []
mlist = os.listdir(path)
print(mlist)
for cl in mlist:
    l = cv2.imread(f'{path}/{cl}')
    image.append(l)
    classn.append(os.path.splitext(cl)[0])
print (classn)
print(l)

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 150)
bot_name = "Tiffany"

paths = {
    'notepad': "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\\Notepad",
    'google chrome': 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s',
    'calculator': "C:\\Windows\\System32\\calc.exe",}

positive_response = ["Cool, I am on it sir!", " Okay sir, I'm working on it!", "Just a second sir!"]
negative_response = ["I think its invalid Command ", "My inventor didn't taught me this!",
                     "Sorry!, i dont know how to do this" ]
gratitude = ["I am happy to help!", "My pleasure sir!", "No problem!"]



def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("listening")
        print('Listening....')
        r.pause_threshold = 2
        audio = r.listen(source, phrase_time_limit=5)

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
    elif "according to wikipedia" in query:
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
        r.pause_threshold = 2
        audio = r.listen(source, phrase_time_limit=7)
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
        speak("Good morning " + name + "!")
    elif 12 < current_time <= 16:
        speak("Good afternoon " + name + "!")
    elif 16 < current_time <= 21:
        speak("Good evening " + name + "!")
    elif 21 < current_time <= 23 or 0 <= current_time <= 4:
        speak("Its a late night " + name + "!")

    speak("What would you like to do ?")

def findencoding(image):
    encodel=[]
    for img in image:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encodel.append(encode)

    return encodel


e = findencoding(image)
print(e)
print('encoding complete')
cam = cv2.VideoCapture(0)
name = ''
timeout = time.time() + 5
speak("face recognition in process")
while True:

    test = 0
    success, img = cam.read()
    imgs = cv2.resize(img, (644,555), None, 0.25, 0.25, 0)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

    faclocreal = fr.face_locations(imgs)
    encode1 = fr.face_encodings(imgs, faclocreal)

    for encodeface, faceloc in zip(encode1, faclocreal):
        m = fr.compare_faces(e, encodeface)
        facdis = fr.face_distance(e, encodeface)
        print(facdis)
        matchindex = np.argmin(facdis)
        print(matchindex)
        if m[matchindex]:
            name += classn[matchindex]

    cv2.waitKey(1)

    print(name)
    if name in classn:
        break
    else:
        print('not reg')

    if test == 5 or time.time() > timeout:
        break
    test = test - 1

print(name)
print(classn)

if name in classn:
    greet()
    r = Tk()

    def tiffany(event):
        query = take_command()
        print("You said \" " + query + " \"")
        validate_command(query)
        return query


    r.wm_geometry('450x850')
    mic = PhotoImage(file="002-microphone.png")
    widget = Button(r, image=mic, bg="#151B54", borderwidth='0')
    widget.pack(side=BOTTOM, anchor=N, pady=300)
    widget.bind('<Button-1>', tiffany)
    r.configure(bg="#151B54")
    if 'close' in query:
        r.destroy()

    r.mainloop()
else:
    win = Tk()
    win.wm_geometry("890x600")
    Label(win, text="New User Portal",bg ="#4863A0", fg="#50C878", font="comicsans 50 bold", borderwidth=3,
          relief='sunken').grid(row=0, column=3)

    def reg_cap():
        n=namevalue.get()
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("test")
        d = r'C:\Users\User\PycharmProjects\pythonProject\main\tiffany\rishi data'
        os.chdir(d)
        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)

            k = cv2.waitKey(1)
            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:
                # SPACE pressed
                speak("faceID is registered")
                img_name = "{}.png".format(n)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))


        cam.release()

        cv2.destroyAllWindows()

    name = Label(win, text="Name", bg="#342D7E", fg="#50C878")
    n = Label(win, text="* hit spacebar to click", bg="#342D7E", fg="#50C878", font="comicsans 10 bold")
    n1 = Label(win, text="* hit esc to exit camera portal", bg="#342D7E", fg="#50C878", font="comicsans 10 bold")
    n2 = Label(win, text="* once registration is done you can exit and try again", bg="#342D7E", fg="#50C878",
               font="comicsans 10 bold")

    name.grid(row=3, column=2)
    n.grid(row=11,column=3)
    n1.grid(row=12,column=3)
    n2.grid(row=14, column=3)
    namevalue = StringVar()
    nameentry = Entry(win, textvariable=namevalue)
    nameentry.grid(row=3, column=3)
    Button(win, fg="red", text="click your photo", command=reg_cap, anchor=S).grid(row=9, column=3)
    win.configure(bg="#342D7E")

    if namevalue.get() in classn:
        n2 = Label(win, text="* registered you can exit and try again", bg="#342D7E", fg="#50C878",
                   font="comicsans 10 bold")
        n2.grid(row=14, column=3)
    speak("register your face id and name as follow")
    win.mainloop()






