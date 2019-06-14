import pyperclip
import tkinter as tk
from PIL import ImageGrab
from tkinter import simpledialog
#import imagebuff
root = tk.Tk()
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
#    IN DEVELOPING
#    imagebuff.sendtoclip(filepath+dct[e]+'.png')
    pass
def clear():
    for button in btnlist:
        button.pack_forget()
    del btnlist[:]
def create_dct():
    clear()
    global crnt
    crnt+=1
    pasted = pyperclip.paste()
    n = simpledialog.askstring('Input', 'Name your buffer')
    f = open(filepath+n+'.txt', 'w')
    f.write(pasted)
    dct.update({n : crnt})
    for k,v in dct.items():
        b = tk.Button(root, text=k, command=lambda e=k:callback(e))
        b.pack()
        btnlist.append(b)
    f.close()
def create_image():
    try:
        global crntimage
        crntimage+=1
        n = simpledialog.askstring('Input', 'Name your buffer')
        im = ImageGrab.grabclipboard()
        im.save(filepath+n+'.png','PNG')
        dct.update({n: crntimage})
        clear()
        for k,v in dct.items():
            b = tk.Button(root, text=k, command=lambda e=k:writeimage(e))
            b.pack()
            btnlist.append(b)
    except:
        pass
tk.Button(text='New', command = create_dct).place(x=0,y=0)
tk.Button(text='Img', command = create_image).place(x=0,y=26)
root.mainloop()
