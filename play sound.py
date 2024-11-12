#Building Virtual Assistant using python
#import gtts
#Google Text to speech
from gtts import gTTS
import speech_recognition as sr
import playsound
from time import ctime
import os
import re
import uuid
import smtplib
import webbrowser
from tkinter import *
from tkinter import ttk
#to make sure it listnes
global data
def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Start talking")
        audio=r.listen(source,phrase_time_limit=5)
    data=""
    try:
        data=r.recognize_google(audio,language='en-US')
        print("you said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data
def response(string):
    print(string)
    tts=gTTs(text=string,lang='en-US')
    tts.save("speech.mp3")
    filename="Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def virtual_assistant(data):
    if "how are you" in data:
        listening=True
        entry1['text']="Good and doing well"
        root.update()
        respond("Good and doing well")

        if "time" in data:
            listening=True
            entry1['text']=clime()
            root.update()
            respond(clime())
        if "ok google" in data.casefold():
            listening=True
            reg_ere.search('open google(.*)',data)
            ur1="https://www.google.com/"
            if reg_ex:
                sub=reg_ex.group(1)
                ur1=ur1+'r/'
            entry1['text']='opening google'
            root.update()
            respond('opening google')
            webbrowser.open(ur1)
        if"locate" in data:
            webbrowser.open('hhts://www.google.com/maps/search/'+data.replace("locate","Nellore"))
            result="Located"
            entry1['text']='Located'
            root.update()
            respond("Located{}".format(data.replace("locate","Nellore")))


        try:
            return listening
        except UnboundLocalError:
            print("Timedout")
def final():
    data=listen()
    entry1['text']=data
    root.update()
root=Tk()
root.title('Virtual Assistant')
root.iconbitmap('mic.ico')
style=ttk.Style()
style.theme_use('winnative')
photo=PhotoImage(file='microphone.png').subsample(17,17)
entry1=Label(root,text='Hey PFS10 How are you',bg='white',fg='\
black',height=2,width=75,font=('callibri',13,'bold'))
entry1.pack(side=LEFT)
MyButton6 = Button(root,image=photo, bd=0,command=final,
                   activebackground='#c1bfbf', overrelief='groove',relief='sunken')
MyButton6.pack(side=RIGHT)
root.geometry('800x250')
root.resizable(False,False)
root.mainloop()
