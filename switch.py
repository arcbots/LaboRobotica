import time
import board
from digitalio import DigitalInOut, Direction, Pull
from ideaboard import IdeaBoard
from time import sleep

# Digital Output on IO27
switch = DigitalInOut(board.IO27) # Choose pin 27
switch.direction = Direction.INPUT
ib = IdeaBoard()

while True:
    if switch.value:
        print("avanzar")
        ib.motor_1.throttle = 1.0
        ib.motor_2.throttle = 1.0
        time.sleep(0.1)
    else:
        print("Detenerse")
        ib.motor_1.throttle = 0
        ib.motor_2.throttle = 0
        time.sleep(0.1)
        