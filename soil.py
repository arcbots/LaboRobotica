import time
import board
from digitalio import DigitalInOut, Direction, Pull
from ideaboard import IdeaBoard
from time import sleep

# Set up the ADC (Analog to Digital Converter) pin
# Change the pin number as per your board (assuming A0 is GPIO36)
ib = IdeaBoard()
soil_sensor = ib.AnalogIn(board.IO33)


#def read_soil_moisture():
    # Read sensor value (0-4095 for 12-bit resolution)
    #moisture_value = soil_sensor.read()
    
    # Convert to percentage (optional, depends on calibration)
    #moisture_percent = (moisture_value / 4095.0) * 100
#   return moisture_value, moisture_percent

while True:
    print(soil_sensor.value)
    time.sleep(0.5)
    moisture_value = soil_sensor.value
    moisture_percent = (moisture_value / 4095.0) * 100
#soil_sensor = DigitalInOut(board.IO33) 
#soil_sensor.atten(ADC.ATTN_11DB)  # Set attenuation for max input voltage (3.3V)
 #   moisture_value, moisture_percent = read_soil_moisture()
    print("Soil Moisture (Raw Value):", moisture_value)
    print("Soil Moisture (%):", moisture_percent)
    
    time.sleep(2)  # Wait for 2 seconds before next reading
