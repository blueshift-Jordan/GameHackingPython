from microbit import *

myCount = 0

while True:
    myCount = myCount + 1
    sleep(1000)
    display.show(str(myCount))


