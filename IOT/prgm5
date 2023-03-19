from picamera import PiCamera
from time import sleep
import datetime

current_date = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

camera = PiCamera()

camera.start_preview()

sleep(10)

camera.capture(current_date+".jpg")

print("PiCamera captured the image")

camera.stop_preview()
