import RPi.GPIO as gpio 
import time
from flask import Flask,render_template
import datetime
app=Flask(__name__)
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
led1=13
sw1=35
gpio.setup(led1,gpio.OUT,initial=1)
gpio.setup(sw1,gpio.IN)
Light_status="OFF"

def glowled(event):
	print("Enterd here")
	global Light_status
	if event==sw1 and Light_status=="OFF":
		gpio.output(led1,False)
		Light_status="ON"
	
	elif event==sw1 and Light_status=="ON":
		gpio.output(led1,True)
		Light_status="OFF"
@app.route('/')
def led_status():
	now=datetime.datetime.now()
	timeString=now.strftime("%H:%M:%D-%m-%y")
	templateData={
	'status':Light_status,
	'time':timeString}
	return render_template('web.html',**templateData)

	
gpio.add_event_detect(sw1,gpio.RISING,callback=glowled,bouncetime=100)
app.run(debug=True,port=4000,host='172.16.201.94')
