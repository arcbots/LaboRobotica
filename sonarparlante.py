import time
import board
import adafruit_hcsr04
from IdeaBoard import IdeaBoard
from time import sleep
from adafruit_rtttl import play

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.IO18, echo_pin=board.IO19)

while True:
    try:
        print((sonar.distance,))
        if(sonar.distance>=10.0):
            print("avanzando")
            sleep(0.5)

        if(sonar.distance<10.0):
            print((sonar.distance,))
            print("alto")
            song000 = "The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f# "#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6"
            play(board.IO25, song000)
            sleep(0.5)
    except RuntimeError:
            print("error de lectura")
            #print(error.args[0])
            time.sleep(1.0)
            continue
    except Exception as error:
            dhtDevice.exit()
            raise error
