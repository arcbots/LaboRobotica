import time
import board
import adafruit_hcsr04 #libreria sensor de proximidad y distancia
from IdeaBoard import IdeaBoard
from time import sleep


ib = IdeaBoard()
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.IO18, echo_pin=board.IO19) #pines del sensor

#definir movimiento

def avanzar(vel, tiempo):
    ib.motor_1.throttle = vel
    ib.motor_2.throttle = vel
    sleep(tiempo)
    
def detenerse():
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0
    
def adelante():
    ib.motor_1.throttle = 1.0
    ib.motor_2.throttle = 1.0
    
def izquierda():
    ib.motor_1.throttle = 1.0
    ib.motor_2.throttle = 0

def derecha():
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 1.0

def atras():
    ib.motor_1.throttle = -1.0
    ib.motor_2.throttle = -1.0



while True:
    try:
        print((sonar.distance,))
        if(sonar.distance<15.0):
            print("sacar sumo")
            adelante()
            sleep(1.0) 
        if(sonar.distance>=15.0):
            print("retroceder")
      
            sleep(2)
    except RuntimeError:
            sleep(2)
            print("buscar sumo")
      
            time.sleep(0.5)
ib.motor_1.throttle = 1.0
ib.motor_2.throttle = -1.0

