from microbit import *

while True:
    if button_a.is_pressed():
        display.scroll("A")
    else:
        display.show(Image.ASLEEP)