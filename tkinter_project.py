from tkinter import*
#import pyttsx3
from gtts import gTTS
from playsound import playsound
import os

### create tkinter heading ####

kishan=Tk()
kishan.geometry("450x350")
kishan.config(bg="blue")
kishan.title("GUPTAG-->> Text-To-Speech")

##### show in tkinter #####

Label(kishan, text="Text-To-Speech",font="arial 25 bold",bg="blue").pack()
Label(kishan, text="Create By Guptag",font="arial 20 bold", bg="blue").pack(side=BOTTOM)

Label(kishan,text="tell me please,what can i speak",font="arial 18 bold",bg="blue").place(x=25,y=35)
#Label(kishan,text=z,font="arial 10 bold",bg="blue").place(x=25,y=1)

###### define function ######
def my_function():
    value=box.get()
    speech=gTTS(text=value)
    speech.save("a.mp3")
    playsound("a.mp3")
    os.remove('a.mp3')
    valuelabel.config(text=value)

    #engine = pyttsx3.init()
    #rate = engine.getProperty('rate') 
    #engine.setProperty('rate', 150)
    #voices = engine.getProperty('voices')
    #engine.setProperty('voice', voices[1].id)
    #engine.say(value)
    #engine.runAndWait()

def reset():
    my_string.set("")
    

def exit():
    kishan.destroy()


valuelabel=Label(kishan,text="hii",font="arial 10 bold",bg="red")
######## button   ########
Button(kishan,text="Play",font="arial 15 bold",command=my_function,width=5,bg="white").place(x=200,y=170)
Button(kishan,text="Reset",font="arial 15 bold",command=reset,width=5,bg="red").place(x=140,y=220)
Button(kishan,text="exit",font="arial 15 bold",command=exit,width=5,bg="red").place(x=260,y=220)



###### input ######
my_string=StringVar()
box=Entry(kishan,textvariable=my_string,font="arial 20 bold", width=27)
box.place(x=20,y=100)




kishan.mainloop()
