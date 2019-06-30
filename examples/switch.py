import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.IN)
GPIO.setup(3, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

stopButton = GPIO.input(3)

while (stopButton == True):
    button = GPIO.input(8)
    stopButton = GPIO.input(3)        
    if(button == False):
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(26, GPIO.LOW)
    else:
        GPIO.output(24, GPIO.LOW)
        GPIO.output(26, GPIO.HIGH)

GPIO.cleanup()