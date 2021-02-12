from tkinter import *;
# import time
import random;


def readTemp():
    return random.choice([34,36.2,38]);


root = Tk();
root.geometry('360x240')
v = StringVar();
l = Label(root, textvariable=v, font=("Helvetica", 128));
l.pack();

def chooseColor(temp):
    if (temp<35):
        return 'blue';
    elif (temp<37.2):
        return 'orange';
    else:
        return 'red';



def updateTime():
    temp = readTemp();
    msg = str(temp);
    l.config(fg=chooseColor(temp));
    v.set(msg);
    root.after(2000, updateTime);

v.set('--.-');

root.after(2000, updateTime)
root.mainloop()