# SPDX-FileCopyrightText: 2021ladyada for Adafruit Industries
# SPDX-License-Identifier- MIT

import time
import board
import adafruit_hcsr04
from IdeaBoard import IdeaBoard
from time import sleep
import adafruit_dht
from adafruit_rtttl import play


ib = IdeaBoard()
dhtDevice = adafruit_dht.DHT11(board.IO26)

servo1 = ib.Servo(board.IO4)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.IO18, echo_pin=board.IO19)

while True:
    try:
        print((sonar.distance,))
        if(sonar.distance>=10.0):
            print("avanzando")
            ib.motor_1.throttle = 1.0
            ib.motor_2.throttle = 1.0
            sleep(2.0)
            ib.motor_1.throttle = 0.0
            ib.motor_2.throttle = 0.0
            sleep(0.5)

        if(sonar.distance<10.0):
            print((sonar.distance,))
            print("alto")
            song000 = "StarWars:d=4,o=5,b=45:32p,32f#,32f#,32f#,8b.,8f#.6,32e6,32d#6,32c#6,8b.6,16f#.6,32e6,32d#6,32c#6,8b.6,16f#.6,32e6,32d#6,32e6,8c#.6,32f#,32f#,32f#,8b.,8f#.6,32e6,32d#6,32c#6,8b.6,16f#.6,32e6,32d#6,32c#6,8b.6,16f#.6,32e6,32d#6,32e6,8c#6"
            ##song000 = "The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f# "#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6"
            play(board.IO25, song000)
            ib.motor_1.throttle = 0.0
            ib.motor_2.throttle = 0.0
            servo1.angle = 0
            sleep(2)
            servo1.angle = 180
            sleep(2)
            #song000 = "HappyBday:d=4,o=5,b=125:8d.,16d,e,d,g,2f#,8p"#, 8d.,16d,e,d,a,2g,8p, 8d.,16d,d6,b,g,f#,2e,8p,8c6.,16c6,b,g,a,2g"
            ib.motor_1.throttle = -1.0
            ib.motor_2.throttle = -1.0
            sleep(0.4)
            ib.motor_1.throttle = 0.0
            ib.motor_2.throttle = 0.0
            sleep(0.3)
            
            
                # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            print(    
                "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
                )
            )
            time.sleep(1.0)
       
    except RuntimeError:
            print("error de lectura")
            #print(error.args[0])
            time.sleep(1.0)
            continue
    except Exception as error:
            dhtDevice.exit()
            raise error
          






            


