from microbit import *

wave1 = Image("99999:"
              "99999:"
              "99999:"
              "99999:"
              "99999")

wave2 = Image("00000:"
              "99999:"
              "99999:"
              "99999:"
              "99999")

wave3 = Image("00000:"
              "00000:"
              "99999:"
              "99999:"
              "99999")

wave4 = Image("00000:"
              "00000:"
              "00000:"
              "99999:"
              "99999")

wave5 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "99999")

wave6 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")

all_waves = [wave1, wave2, wave3, wave4, wave5, wave6, wave6, wave5, wave4, wave3, wave2, wave1]

display.show(all_waves, loop = True, delay=200)
