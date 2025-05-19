from ideaboard import ADC, Pin
import time

# Initialize the ADC pin (change GPIO34 to the pin you connected the sensor's AO to)
adc_pin = Pin(34)  # Replace with your actual ADC pin
adc = ADC(adc_pin)
adc.atten(ADC.ATTN_0DB)  # Set attenuation to read voltage from 0 to 1V (change if needed)
adc.width(ADC.WIDTH_12BIT)  # Set ADC resolution to 12 bits

def read_soil_moisture():
    # Read the raw ADC value
    raw_value = adc.read()
    
    # Convert ADC value to voltage
    voltage = raw_value * (3.3 / 4095)  # Adjust this based on your ADC resolution and reference voltage
    
    # Print raw value and voltage
    print("Raw ADC Value:", raw_value)
    print("Soil Moisture Voltage:", voltage)
    
    # Optionally convert to percentage if needed
    # Here, assuming that 0V is dry and 3.3V is wet
    moisture_percentage = (voltage / 3.3) * 100
    print("Soil Moisture Percentage:", moisture_percentage)

    return raw_value, voltage, moisture_percentage

# Main loop to read and print soil moisture data
while True:
    read_soil_moisture()
    time.sleep(1)  # Read every second; adjust as needed
