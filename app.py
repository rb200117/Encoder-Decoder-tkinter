#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 15:30:28 2021

@author: rakshitbatra
"""

from tkinter import *
import base64

window = Tk()
window.title("Encoder Decoder")
window.geometry('400x400')
window.configure(background="#191A19");
mystring = StringVar(window)
l1 = Label(window,
           text='Welcome To Encoder-Decoder',
           fg="#54E346",
           bg="#191A19",
           font="Helvetica 25 bold",
           padx=10,
           pady=20).pack()
l2 = Label(window,
           text='Please Select One Operation',
           fg="#54E346",
           bg="#191A19",
           font="Helvetica 16",
           padx=10,
           pady=5).pack()


def encode(str):
    sample_string = str
    sample_string_bytes = sample_string.encode("ascii")

    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string


def decode(str):
    base64_string = str
    base64_bytes = base64_string.encode("ascii")

    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    return sample_string

try:
    def labelController(event):
        if event == "Encode":
            label1.config(text=event, fg="#E02401")
            label1.pack()
            entry1.config(fg="#8E0505")
            entry1.pack()
            b1.config(text=event, fg="#8E0505", bg="#191A19", command=lambda m="Encode": getvalue(m))
            b1.pack()

        if event == "Decode":
            label1.config(text=event, fg="#54E346")
            label1.pack()
            entry1.config(fg="#1E5128")
            entry1.pack()
            b1.config(text=event, fg="#1E5128", bg="#191A19", command=lambda m="Decode": getvalue(m))
            b1.pack()


    def getvalue(m):
        if m == "Encode":
            label2.config(text="Result: " + encode(mystring.get()), font="Helvetica 16 bold", fg="#E02401", bg="#191A19")
            label2.pack()
            print(encode(mystring.get()))
        if m == "Decode":
            label2.config(text="Result: " + decode(mystring.get()), font="Helvetica 16 bold", fg="#54E346", bg="#191A19")
            label2.pack()
            print(decode(mystring.get()))
            
except Exception as e:
    print("Exception: ",e.__class__," occurred")



def getHome():
    label1.pack_forget()
    label2.pack_forget()
    entry1.pack_forget()


label1 = Label(window, text="Encoding", font="Helvetica 16 bold", fg="#E02401", bg="#191A19")
label1.pack_forget()
entry1 = Entry(window, textvariable=mystring)
entry1.pack_forget()
b1 = Button(window, text="Encode", command=lambda em="Encode": labelController(em))
b1.pack_forget()
label2 = Label(window, text="label2", padx=20, pady=20)
label2.pack_forget()


operation = Menubutton(window, text='Operations', justify=CENTER, padx=10, pady=10, bg='#191A19')
options = Menu(operation)
operation.config(menu=options)
options.add_radiobutton(label='Encode', value='Encode', command=lambda m="Encode": labelController(m))
options.add_radiobutton(label='Decode', value='Decode', command=lambda m="Decode": labelController(m))

operation.pack()
window.mainloop()
