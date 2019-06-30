import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 1000)
dutyCycle = 0
pwm.start(dutyCycle)

GPIO.setup(24, GPIO.OUT)
pwm2 = GPIO.PWM(24, 1000)
dutyCycle2 = 0
pwm2.start(dutyCycle2)

while(True):
    time.sleep(0.01)
    dutyCycle = dutyCycle + 2
    if(dutyCycle > 100):
        dutyCycle = 0
    pwm.ChangeDutyCycle(dutyCycle)
    
    dutyCycle2 = dutyCycle2 + 1
    if(dutyCycle2 > 100):
        dutyCycle2 = 0
    pwm2.ChangeDutyCycle(dutyCycle2)