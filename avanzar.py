from ideaboard import IdeaBoard
from time import sleep
import board
from adafruit_rtttl import play

ib = IdeaBoard()

AZUL = (0,0,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
NEGRO =(0,0,0)

def adelante(vel, tiempo):
    ib.motor_1.throttle = vel
    ib.motor_2.throttle = vel
    sleep(tiempo)
    
def parar():
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0
    
def adelante():
    ib.motor_1.throttle = -1.0
    ib.motor_2.throttle = 1.0
    
while True:
    adelante()
    ib.pixel = VERDE
    sleep(3.0)
    song000 = "The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f# "#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6"
    play(board.IO25, song000)
    parar()
    ib.pixel = ROJO
    sleep(3.0)
    
    
    
    
    
    
    