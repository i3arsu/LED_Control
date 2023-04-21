import tkinter as tk
import RPi.GPIO as GPIO
window = tk.Tk()

ledPin = 14
pwmLEDPin = GPIO.PWM(ledPin, 100)
pwmLEDPin.start(0)
dutyCycle = 100

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(ledPin, GPIO.HIGH)

def setOff():
    powerSlider.pack_forget()
    pwmLEDPin.ChangeDutyCycle(0)

def setOn():
    powerSlider.pack()

def setStrength(val):
    pwmLEDPin.ChangeDutyCycle(val)


powerSlider = tk.Scale(window, from_= 0, to=100, orient="horizontal", command=setStrength)


btnOn = tk.Button(window,text="On", command=setOn)
btnOn.pack()
btnOff = tk.Button(window,text="Off",command=setOff)
btnOff.pack()

window.geometry("300x300")
window.mainloop()