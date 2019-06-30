from flask import Flask
import time

app = Flask('simpleServer')

@app.route('/')
def index():
    return 'Hello, world! Current time is ' + time.ctime() 

app.run(debug=True, port=3000, host='0.0.0.0')