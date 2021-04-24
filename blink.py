import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.IN)
while True:
    value=GPIO.input(13)
    if value == 1:
        GPIO.output(11,1)
    else:
        GPIO.output(11,1)
        time.sleep(1)
        GPIO.output(11,0)
        time.sleep(1)
