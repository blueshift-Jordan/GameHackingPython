from microbit import *

while True:

    x_acceleration = accelerometer.get_x()

    if x_acceleration > 100:
         display.show(Image.ARROW_E)

    if  x_acceleration < 100:
         display.show(Image.ARROW_W)
