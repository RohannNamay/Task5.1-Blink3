from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)
YELLOW = 17
GREEN = 27
RED = 22
LED_PINS = [YELLOW, GREEN, RED]

# GUI setup
win = Tk()
win.geometry("350x125")
win.title("LED Controller")

var = IntVar()

# Setup pins as output and turn all off initially
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Function to turn on only the selected LED
def select_led():
    selected = var.get()
    for pin in LED_PINS:
        GPIO.output(pin, GPIO.HIGH if pin == selected else GPIO.LOW)

# Function to clean up and exit
def exit_program():
    GPIO.cleanup()
    win.destroy()

# Radio buttons
Radiobutton(win, text="Yellow", variable=var, value=YELLOW, command=select_led).pack(anchor='w')
Radiobutton(win, text="Green", variable=var, value=GREEN, command=select_led).pack(anchor='w')
Radiobutton(win, text="Red", variable=var, value=RED, command=select_led).pack(anchor='w')

# Exit button
Button(win, text="Exit", command=exit_program).pack(pady=10)

win.protocol("WM_DELETE_WINDOW", exit_program)

win.mainloop()