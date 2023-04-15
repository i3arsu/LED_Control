import tkinter as tk
#import RPi.GPIO as GPIO
window = tk.Tk()

def setOff():
    powerSlider.pack_forget()

def setOn():
    powerSlider.pack()


powerSlider = tk.Scale(window, from_= 0, to=100, orient="horizontal")


btnOn = tk.Button(window,text="On", command=setOn)
btnOn.pack()
btnOff = tk.Button(window,text="Off",command=setOff)
btnOff.pack()

window.geometry("300x300")
window.mainloop()
