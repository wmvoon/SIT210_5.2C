from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

##SETTING LED PINS
redled = LED(18)
greenled = LED(23)
blueled = LED(24)

##GUI DEFINITIONS
win = Tk()
win.title("RGB LEDs Toggler")
##set font
myFont = tkinter.font.Font(family='Helvetica', size=20)

##DEFINE LED FUNCTIONS
def REDledtoggle():
    if redled.is_lit:
        redled.off()
        redButton["text"] = "Turn RED ON"
    else:
        redled.on()
        redButton["text"] = "Turn RED OFF"
        
def GREENledtoggle():
    if greenled.is_lit:
        greenled.off()
        greenButton["text"] = "Turn GREEN ON"
    else:
        greenled.on()
        greenButton["text"] = "Turn GREEN OFF"
        
def BLUEledtoggle():
    if blueled.is_lit:
        blueled.off()
        blueButton["text"] = "Turn BLUE ON"
    else:
        blueled.on()
        blueButton["text"] = "Turn BLUE OFF"
        
def byebye():
    GPIO.cleanup()
    win.destroy()
        

##WIDGETS
redButton = Button(win, text='Turn RED ON', font=myFont, command=REDledtoggle, bg='red', height=1, width = 24)
greenButton = Button(win, text='Turn GREEN ON', font=myFont, command=GREENledtoggle, bg='green', height=1, width = 24)
blueButton = Button(win, text='Turn BLUE ON', font=myFont, command=BLUEledtoggle, bg='blue', height=1, width = 24)
redButton.grid(row=0,column=1)
greenButton.grid(row=1,column=1)
blueButton.grid(row=2,column=1)

exitButton =Button(win, text='EXIT', font=myFont, command=byebye, bg='bisque2', height=1, width = 15)
exitButton.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", byebye) #exit cleanly (using 'x' button)

win.mainloop() #loop forever