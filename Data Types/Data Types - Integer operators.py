from microbit import *

celsiusTemp = temperature()
fahrenheitTemp = celsiusTemp * 9 / 5 + 32

while True:
    display.show(str(fahrenheitTemp))
    sleep(2000)