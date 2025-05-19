#Iniciar o importar las librerias
#import prueba
from ideaboard import IdeaBoard
import time
import board
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20
from time import sleep
from adafruit_rtttl import play
#importe las librerias de parlante, sensor e ideaboard.


#iniciar la ideaboard
ib = IdeaBoard()
# codigo iniciar el sensor de temperatura 13 y 14
ow_bus = OneWireBus(board.IO27)
ds18 = DS18X20(ow_bus, ow_bus.scan()[0])
alerta = "smb:d=4,o=5,b=100:16e6,16e6,32p,8e6,16c6,8e6,8g6,8p,8g,8p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,16p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16c7,16p,16c7,16c7,p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16d#6,8p,16d6,8p,16c6"

# Proceso del robot
# 19-21 lectura del sensor e imprime el resultado.
while True:
    print("Temperature: {0:0.3f}C".format(ds18.temperature))
    time.sleep(2.0)

    if (ds18.temperature > 24):
        ib.motor_1.throttle = -0.2
        ib.motor_2.throttle = -0.2
        time.sleep(2.0)
        play(board.IO25, alerta)
        print("alerta, hacia atrás")

    elif (ds18.temperature <= 24):
        print("alerta, hacia adelante")
        ib.motor_1.throttle = 0.5
        ib.motor_2.throttle = 0.5
        time.sleep(3.0)

    else:
        print("revisar codigo")
#codigo del motor 23 y 24, negativo atrás, positivo hacia adelante.
#ib.motor_1.throttle = 1.0
#ib.motor_2.throttle = 1.0

#codigo de parlante
#song000 = "smb:d=4,o=5,b=100:16e6,16e6,32p,8e6,16c6,8e6,8g6,8p,8g,8p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,16p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16c7,16p,16c7,16c7,p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16d#6,8p,16d6,8p,16c6"

#play(board.IO25, song000)
