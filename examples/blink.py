import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

i = 0 
while (i < 5):
    i = i + 1
    time.sleep(0.5)
    GPIO.output(17, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17, GPIO.LOW)


i = 0 
while (i < 5):
    i = i + 1
    time.sleep(0.1)
    GPIO.output(17, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(17, GPIO.LOW)
    
GPIO.cleanup()