import board
import time
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC

# -------------------------
# INICIALIZACIÓN I2C
# -------------------------
i2c = board.I2C()
sensor = LSM6DS3TRC(i2c, 0x6a)  # dirección 0x6a (la que te funcionó)

print("Giroscopio iniciado...")

# -------------------------
# LOOP
# -------------------------
while True:
    gx, gy, gz = sensor.gyro  # radianes/segundo

    print("GX:", gx, "| GY:", gy, "| GZ:", gz)

    time.sleep(0.2)