# SPDX-FileCopyrightText: 2021ladyada for Adafruit Industries
# SPDX-License-Identifier- MIT

import time
import board
import adafruit_hcsr04
from time import sleep
#import adafruit_dht


#ib = IdeaBoard()

#servo1 = ib.Servo(board.IO4)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.IO18, echo_pin=board.IO19)

while True:
    try:
        print((sonar.distance,))
        if(sonar.distance<15.0):
            print("alto")
     
       #     servo1.angle = 0
            sleep(2)
        #    servo1.angle = 180
            sleep(2)
        if(sonar.distance>=15.0):
            print("avanzando")
      
            sleep(2)
    except RuntimeError:
            sleep(2)
            print("error de lectura")
      
            time.sleep(0.8)