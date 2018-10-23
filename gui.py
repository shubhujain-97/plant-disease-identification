"""
@author: Shubham Jain
"""
# import the necessary packages

import os
import tkinter 
from tkinter import Button
from tkinter import LEFT
from tkinter import Frame
import tkinter.messagebox
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename

# for exit button

def g_quit():
    mExit=tkinter.messagebox.askyesno(title="Quit", message="Are You Sure?")
    if mExit>0:
        mGui.destroy()
        return

# for load button
        
def open_img():
    file = tkinter.filedialog.askopenfilename(initialdir='D:/Users/')
    w_box = 500
    h_box = 500

    pil_image = Image.open(file)

    w, h = pil_image.size

    pil_image_resized = resize(w, h, w_box, h_box, pil_image)
    # wr, hr = pil_image_resized.size

    tk_image = ImageTk.PhotoImage(pil_image_resized)

    label2.config(image=tk_image, width=w_box, height=h_box)

def resize(w, h, w_box, h_box, pil_image):
    '''
    resize a pil_image object so it will fit into
    a box of size w_box times h_box, but retain aspect ratio
    '''
    f1 = 1.0*w_box/w  # 1.0 forces float division in Python2
    f2 = 1.0*h_box/h
    factor = min([f1, f2])
    #print(f1, f2, factor)  # test
    # use best down-sizing filter
    width = int(w*factor)
    height = int(h*factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)


# for about button
def callback():
    abtfile = open("D:/New folder/project/Plant Leaf Disease Diagnosis/about.txt")



mGui = Tk()
mGui.title('Plant Leaf Disease Diagnosis')
mGui.geometry('600x550')

#Disable Resizeability

mGui.resizable(0, 0) 


photoFrame = Frame(mGui, width=500, height=500)
photoFrame.pack(side=TOP)
menu_bar = Frame(mGui, bg="white", width=500, height=250)
menu_bar.pack(side=BOTTOM, fill=Y)
label2 = Label(photoFrame)

#Create Buttons for options
load_btn = Button(menu_bar, text="LOAD", command=open_img)
load_btn.pack(side=LEFT)

check_btn = Button(menu_bar, text="CHECK")
check_btn.pack(side=LEFT)

accuracy_btn = Button(menu_bar, text="COMPARISION")
accuracy_btn.pack(side=LEFT)

about_btn = Button(menu_bar, text="ABOUT", command=callback)
about_btn.pack(side=LEFT)

exit_btn = Button(menu_bar, text="EXIT", command=g_quit)
exit_btn.pack(side=LEFT)


mGui.mainloop()