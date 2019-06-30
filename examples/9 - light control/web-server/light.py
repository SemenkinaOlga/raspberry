from flask import Flask, send_file
import RPi.GPIO as GPIO
 
led = 24
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
 
app = Flask('lightControl')
 
 
@app.route('/')
def index():
    return send_file('light.html')
 
 
@app.route('/images/<filename>')
def get_image(filename):
    return send_file('images/' + filename)
 
 
@app.route('/turn<state>')
def turn(state):
    if state == 'On':
        GPIO.output(led, GPIO.HIGH)
    else:
        GPIO.output(led, GPIO.LOW)        
    return 'OK'
 

 
try: 
    app.run(port=3000, host='0.0.0.0')
except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed.')