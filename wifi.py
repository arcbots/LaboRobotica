# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
from random import randint
import ssl
import socketpool
import wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT
from adafruit_io.adafruit_io import IO_MQTT
from ideaboard import IdeaBoard
import time
import board
import adafruit_dht
from time import sleep

dhtDevice = adafruit_dht.DHT11(board.IO26)

ib = IdeaBoard()

AZUL = (0,0,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
NEGRO = (0,0,0)
### WiFi ###

ib.arcoiris = 70
   

# Add a secrets.py to your filesystem that has a dictionary called secrets with "ssid" and
# "password" keys with your WiFi credentials. DO NOT share that file or commit it into Git or other
# source control.
# pylint: disable=no-name-in-module,wrong-import-order
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# Set your Adafruit IO Username and Key in secrets.py
# (visit io.adafruit.com if you need to create an account,
# or if you need your Adafruit IO key.)
aio_username = secrets["aio_username"]
aio_key = secrets["aio_key"]

print("Connecting to %s" % secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to %s!" % secrets["ssid"])

# Define callback functions which will be called when certain events happen.
# pylint: disable=unused-argument
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print("Connected to Adafruit IO!  Listening for DemoFeed changes...")
    # Subscribe to changes on a feed named DemoFeed.
    client.subscribe("DemoFeed")
    client.subscribe("led")
    client.subscribe("color")
    client.subscribe("temp")
    client.subscribe("humid")

def subscribe(client, userdata, topic, granted_qos):
    # This method is called when the client subscribes to a new feed.
    print("Subscribed to {0} with QOS level {1}".format(topic, granted_qos))


def unsubscribe(client, userdata, topic, pid):
    # This method is called when the client unsubscribes from a feed.
    print("Unsubscribed from {0} with PID {1}".format(topic, pid))


# pylint: disable=unused-argument
def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print("Disconnected from Adafruit IO!")


# pylint: disable=unused-argument
def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    #print("Feed {0} received new value: {1}".format(feed_id, payload))
    print(client,feed_id,payload)
    if feed_id == "led" and payload == "ON":
        ib.pixel = AZUL
    if feed_id and payload == "OFF":
        ib.pixel = NEGRO
    if feed_id == "color":
        ib.arcoiris = int(payload)
  
    #if feed_id == "temp":
        #ib.dht11 = int(payload)
   
# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

# Initialize a new MQTT Client object
mqtt_client = MQTT.MQTT(
    broker="io.adafruit.com",
    port=1883,
    username=secrets["aio_username"],
    password=secrets["aio_key"],
    socket_pool=pool,
    ssl_context=ssl.create_default_context(),
)

# Initialize an Adafruit IO MQTT Client
io = IO_MQTT(mqtt_client)

# Connect the callback methods defined above to Adafruit IO
io.on_connect = connected
io.on_disconnect = disconnected
io.on_subscribe = subscribe
io.on_unsubscribe = unsubscribe
io.on_message = message

# Connect to Adafruit IO
print("Connecting to Adafruit IO...")
io.connect()

# Below is an example of manually publishing a new  value to Adafruit IO.
last = 0
print("Publishing a new message every 2 minutes...")
while True:
    # Explicitly pump the message loop.
    io.loop()
    # Send a new message every 10 seconds.
    if (time.monotonic() - last) >= 120:
        value = randint(0, 100)
        if value <= 20:
            #ib.motor_1.throttle = 1.0
            #ib.motor_2.throttle = 1.0
            time.sleep(0.1)
        else:
            ib.motor_1.throttle = 0
            ib.motor_2.throttle = 0
        print("Publishing {0} to DemoFeed.".format(value))
        io.publish("DemoFeed", value)
        try:
        # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            print("Publishing {0} to temp.".format(temperature_c))
            print("Publishing {0} to humidity.".format(humidity))
            io.publish("temp", temperature_c)
            io.publish("humid", humidity)
            print(
                "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                    temperature_f, temperature_c, humidity
                )
            )
            time.sleep(2.0)

        except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
      
            time.sleep(2.0)
         

   
