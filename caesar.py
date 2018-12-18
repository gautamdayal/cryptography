# Caesar cipher implementation with Tkinter powered GUI

from tkinter import *

def getCharVal(c):
    return ord(c) - 97

def cipher():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipherlist = []
    plaintext = textentry.get()
    plaintext = plaintext.lower()
    shift = int(shiftentry.get())
                
    for c in plaintext:
        if not in alphabet:
            cipherlist.append(c)
        else:
            cipherlist.append(alphabet[getCharVal(c) + shift])
    ciphertext = ''.join(cipherlist)

    answindow = Tk()
    cipherlabel = Label(answindow,text = ciphertext, bg = "gray", fg = "black", font=("Courier", 42))
    cipherlabel.pack()
    answindow.mainloop()

window = Tk()
window.configure(background = "gray")

framet = Frame(window, height = 100)
framet.pack(side = TOP)

frameb = Frame(window, height = 100)
frameb.pack(side = BOTTOM)

heading = Label(window, text = 'Caesar Cipher', fg = "black", font = ("Courier", 36))
heading.pack(side = TOP)

textlabel = Label(window, text = 'Text:     ', fg = "black", font = ("Courier", 14))
textlabel.pack(side = LEFT)
textentry = Entry(window, bd = 4,bg = "green")
textentry.pack(side = LEFT)

shiftlabel = Label(window, text = '     Shift Number:     ', fg = "black", font = ("Courier", 14))
shiftlabel.pack(side = LEFT)
shiftentry = Entry(window, bd = 4, bg = "green")
shiftentry.pack(side = LEFT)

enterbutton = Button(window, text = "Get ciphered text!", command = cipher)
enterbutton.pack(side = BOTTOM)

window.mainloop()
