import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
RELAIS_1_GPIO = 17
GPIO.cleanup()
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode

def set_relay(state):
    if state == "high":
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
    if state == "low":
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
    
if __name__ == "__main__":
    while True:
        print("nyala" )
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)("high")
        time.sleep(1)
        print("mati")
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)("low")
        time.sleep(1)
