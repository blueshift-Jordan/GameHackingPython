from microbit import *

count = 0

while True:
    if button_a.was_pressed():
        count = count - 1
    elif button_b.was_pressed():
        count = count + 1
    display.scroll(str(count))
    sleep(1000)

