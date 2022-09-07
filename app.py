import paho.mqtt.client as paho
from paho import mqtt
#from relay import set_relay
# from servo import set_servo_1,set_servo_2
import RPi.GPIO as GPIO

# define static variable
# broker = "localhost" # for local connection
broker = "industrial.api.ubidots.com"  # for online version
port = 1883
timeout = 60

username = 'BBFF-msUz1oCTyANwP7pOhefc56jKQAUKD7'
password = 'BBFF-msUz1oCTyANwP7pOhefc56jKQAUKD7'


# topic subscribe
relay_topic = '/v1.6/devices/control_sensor/relay/lv' # -> contoh : /v1.6/devices/device_01/relay/lv
# servo_1_topic = '/v1.6/devices/control_sensor/servo_1/lv'
# servo_2_topic = '/v1.6/devices/control_sensor/servo_2/lv'

# inisiasi relay
relay = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(relay_topic)
#     client.subscribe(servo_1_topic)
#     client.subscribe(servo_2_topic)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload.decode('utf-8')))
    payload_decoded = msg.payload.decode('utf-8')

    if payload_decoded != '':

     if msg.topic == relay_topic:
        if float(payload_decoded) == 0.0:
            print("matikan relay")
            GPIO.output(relay, GPIO.LOW)
        if float(payload_decoded) == 1.0:
            print("nyalakan relay")
            GPIO.output(relay, GPIO.HIGH)

#      if msg.topic == servo_1_topic:
#         if float(payload_decoded) == 0.0:
#             print("matikan servo 1")
#             set_servo_1("low")
#         if float(payload_decoded) == 1.0:
#             print("nyalakan servo 1")
#             set_servo_1("high")
             
#     if msg.topic == servo_2_topic:
#         if float(payload_decoded) == 0.0:
#             print("matikan servo 2")
#             set_servo_2("low")
#         if float(payload_decoded) == 1.0:
#             print("nyalakan servo 2")
#             set_servo_2("high")
        
# Create an MQTT client and attach our routines to it.
client = paho.Client()
# client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username=username,password=password)
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(broker, port, timeout)

client.loop_forever()

