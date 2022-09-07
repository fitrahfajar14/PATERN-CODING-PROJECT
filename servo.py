import RPi.GPIO as GPIO
import pigpio
import time

servo_1 = 21
servo_2 = 20
pwm = pigpio.pi()

def set_servo_1(state):
    if state == "high":
        pwm.set_mode(servo_1, pigpio.OUTPUT)
 
        pwm.set_PWM_frequency( servo_1, 50 )
 
        print( "0 deg" )
        pwm.set_servo_pulsewidth( servo_1, 1290 ) ;
        time.sleep( 1 )
 
        print( "25 deg" )
        pwm.set_servo_pulsewidth( servo_1, 1500 ) ;
        time.sleep( 1 )
 
        # turning off servo
        pwm.set_PWM_dutycycle(servo_1, 0)
        pwm.set_PWM_frequency( servo_1, 0 )

    if state == "low":
        pass
    
def set_servo_2(state):
    if state == "high":
        pwm.set_mode(servo_2, pigpio.OUTPUT)
 
        pwm.set_PWM_frequency( servo_2, 50 )
 
        print( "0 deg" )
        pwm.set_servo_pulsewidth( servo_2, 1150 ) ;
        time.sleep( 1 )
 
        print( "25 deg" )
        pwm.set_servo_pulsewidth( servo_2, 1500 ) ;
        time.sleep( 1 )
 
        # turning off servo
        pwm.set_PWM_dutycycle(servo_2, 0)
        pwm.set_PWM_frequency( servo_2, 0 )
    if state == "low":
        pass
