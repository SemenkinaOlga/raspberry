from flask import Flask, send_file
from flask_socketio import SocketIO
import RPi.GPIO as GPIO
 
app = Flask('feedback')
socketio = SocketIO(app)

GPIO.setmode(GPIO.BCM)
 
buttons = [2, 3, 4, 8]

for btn in buttons:
    GPIO.setup(btn, GPIO.IN)

leds = [14, 15, 17, 18, 24, 10, 26, 12, 21, 13, 19, 16]

for led in leds:
    GPIO.setup(led, GPIO.OUT)    
 
@app.route('/')
def index():
    return send_file('feedback.html')
 
@app.route('/images/<filename>')
def get_image(filename):
    return send_file('images/' + filename)

@socketio.on('isPressed')
def checkButton(receivedData):
    data = {btn : GPIO.input(btn) for btn in buttons}
    socketio.emit('button', data)
    
@socketio.on('toggle')
def checkLed(receivedData):
    if receivedData['state']:
        GPIO.output(receivedData['id'], GPIO.HIGH)
    else:
        GPIO.output(receivedData['id'], GPIO.LOW)

 
try: 
    socketio.run(app, port=3000, host='0.0.0.0')
except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
finally:
    GPIO.cleanup()
    print('GPIO cleanup completed.')