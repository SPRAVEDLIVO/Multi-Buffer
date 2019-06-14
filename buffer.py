import pyperclip
import shutil
import tkinter as tk
from PIL import ImageGrab
from tkinter import simpledialog
import os
root = tk.Tk()
root.title('Multi-Buffer')
dct = {}
btnlist = []
filepath = 'buffers/'
crnt = 0
crntimage = 0
root.geometry('100x100')
def callback(e):
    tocopy = []
    f = open(filepath+str(e)+'.txt', 'r')
    for line in f:
        tocopy.append(line)
    pyperclip.copy(''.join(tocopy))
    f.close()
def writeimage(e):
    pass
def clear():
    for button in btnlist:
        button.pack_forget()
    del btnlist[:]
def create_dct():
    n = simpledialog.askstring('Input', 'Name your buffer')
    if n is not None:
        global crnt
        crnt+=1
        pasted = pyperclip.paste()
        clear()
        f = open(filepath+n+'.txt', 'w')
        f.write(pasted)
        dct.update({n : crnt})
        f.close()
        simplepack('text')
    else: pass
def simplepack(typeof):
    for k in dct.keys():
        b = tk.Button(root, text=k, command=lambda e=k:writeimage(e)) if typeof == 'image' else tk.Button(root, text=k, command=lambda e=k:callback(e))
        b.pack()
        btnlist.append(b)
def create_image():
    try:
        n = simpledialog.askstring('Input', 'Name your buffer')
        if n is not None:
            global crntimage
            crntimage+=1
            im = ImageGrab.grabclipboard()
            im.save(filepath+n+'.png','PNG')
            clear()
            dct.update({n: crntimage})
            clear()
            simplepack('image')
        else: pass
    except: pass
def clearfiles():
    global dct
    shutil.rmtree('buffers')
    os.makedirs('buffers')
    dct = {}
    clear()
tk.Button(text='New', command = create_dct).place(x=0,y=0)
tk.Button(text='Img', command = create_image).place(x=0,y=26)
tk.Button(text='Clear', command = clearfiles).place(x=0,y=52)
root.mainloop()
