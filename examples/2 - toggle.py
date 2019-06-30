import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
GPIO.setup(24, GPIO.OUT)

while (True):
    #time.sleep(0.5)
    button = GPIO.input(2)
    res = not button
    GPIO.output(24, res)
    print(res)

GPIO.cleanup()