import board
import time
from ideaboard import IdeaBoard

ib = IdeaBoard()

#Digital In
# entrada = ib.DigitalIn(board.IO27, pull=ib.UP)
# pull can be ib.UP or ib.DOWN, default None)
entrada = ib.DigitalIn(board.IO32)
entrada2 = ib.DigitalIn(board.IO33)
while True:
    if ( entrada.value == True or entrada2.value == True ):
        print("Fuera de línea")
    else:
        print("En línea")
    time.sleep(0.8)