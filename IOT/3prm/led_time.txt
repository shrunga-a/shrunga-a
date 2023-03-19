#3. Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

led = 15

gpio.setup(led, gpio.OUT, initial = 1)

fh = open("ledTime.txt")
lst = fh.readlines()
f = lst[0].split("=")
a = int(f[1])
f1 = lst[1].split("=")
b = int(f1[1])

try:
	while(True):
		gpio.output(led, False)  #ON
		time.sleep(a)
		gpio.output(led, True)   #OFF
		time.sleep(b)

except KeyboardInterrupt:
	#cleaning GPIO settings before exiting
	gpio.cleanup()
