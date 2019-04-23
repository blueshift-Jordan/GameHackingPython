from microbit import *
import random

aCount = 0
bCount = 0
maxGameTime = 30000

# a and b player screen
aImage = Image('00900:09000:90000:09000:00900:')
bImage = Image('00900:00090:00009:00090:00900:')

# a and b click player screen
aClickImage = Image('99900:99000:90000:99000:99900:')
bClickImage = Image('00999:00099:00009:00099:00999:')

# display get ready on screen
display.scroll('GET READY')
# delay saying Go!
sleep(500)
# display Go! on screen
display.scroll('GO!')

while True:
    while running_time() < maxGameTime:

        delay = 3000
        while delay > 0:
            display.show(aImage)
            if button_a.is_pressed():
                aCount = aCount + 1
                display.show(aClickImage)

            if button_b.is_pressed():
                bCount = bCount - 1
            delay = delay - 1

        delay = 3000
        while delay > 0:
            display.show(bImage)
            if button_b.is_pressed():
                bCount = bCount + 1
                display.show(bClickImage)

            if button_a.is_pressed():
                aCount = aCount - 1
            delay = delay - 1

    display.clear()

    if aCount > bCount:
        display.scroll("PLAYER 1 WINS!")
    else:
        display.scroll("PLAYER 2 WINS!")