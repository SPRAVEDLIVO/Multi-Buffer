import pyperclip
import tkinter as tk
from PIL import ImageGrab
import imagebuff
root = tk.Tk()
dct = {}
btnlist = []
filepath = 'buffers/'
crnt = 0
crntimage = 0
root.geometry('100x100')
def callback(e):
    tocopy = []
    f = open(filepath+dct[e]+'.txt', 'r')
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
def create_dct():
    clear()
    global crnt
    crnt+=1
    pasted = pyperclip.paste()
    f = open(filepath+'Buffer '+str(crnt)+'.txt', 'w')
    f.write(pasted)
    dct.update({crnt : 'Buffer '+str(crnt)})
    for k,v in dct.items():
        b = tk.Button(root, text=k, command=lambda e=k:callback(e))
        b.pack()
        btnlist.append(b)
    f.close()
def create_image():
    global crntimage
    crntimage+=1
    im = ImageGrab.grabclipboard()
    im.save(filepath+'Image'+' '+str(crntimage)+'.png','PNG')
    dct.update({crntimage: 'Image '+str(crntimage)})
    clear()
    for k,v in dct.items():
        b = tk.Button(root, text=k, command=lambda e=k:writeimage(e))
        b.pack()
        btnlist.append(b)
tk.Button(text='New', command = create_dct).place(x=0,y=0)
tk.Button(text='Img', command = create_image).place(x=0,y=26)
root.mainloop()