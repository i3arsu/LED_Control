import tkinter as tk
import RPi.GPIO as GPIO
window = tk.Tk()

ledPin = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)
pwmLEDPin = GPIO.PWM(ledPin, 100)
pwmLEDPin.start(0)
dutyCycle = 100
GPIO.output(ledPin, GPIO.HIGH)

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
