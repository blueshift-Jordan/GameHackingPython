from microbit import *
import random

choice = 0

paper = Image("99999:"
            "90009:"
            "90009:"
            "90009:"
            "99999")

rock = Image("00000:"
            "09990:"
            "09990:"
            "09990:"
            "00000:")

scissors = Image("00099:"
                "99090:"
                "00900:"
                "99090:"
                "00099:")
while True:
    if accelerometer.was_gesture("shake"):
        choice = random.randint(1, 3)

    if choice == 1:
        display.show(rock)
    elif choice == 2:
        display.show(paper)
    elif choice == 3:
        display.show(scissors)
    else:
        display.clear()