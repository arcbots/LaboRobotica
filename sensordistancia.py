# SPDX-FileCopyrightText: 2021ladyada for Adafruit Industries
# SPDX-License-Identifier- MIT

import time
import board
import adafruit_hcsr04
from time import sleep
#from Ideaboard import Ideaboard


#ib = IdeaBoard()


sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.IO18, echo_pin=board.IO19)

while True:
    try:
        print((sonar.distance,))
        if(sonar.distance<15.0):
            print("alto")
            sleep(2)
        if(sonar.distance>=15.0):
            print("avanzando")
            sleep(2)
    except RuntimeError:
            sleep(2)
            print("error de lectura")
            time.sleep(0.8)