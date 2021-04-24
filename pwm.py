import RPi.GPIO as GPIO
import time 

led_pin =12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.output(led_pin,GPIO.LOW)

p =GPIO.PWM(led_pin,1000)
p.start(0)

while True:
	for dc in range(0,100,5):
		p.ChangeDutyCycle(dc)
		time.sleep(0.05)
	time.sleep(2)
	for dc in range(100,-1,-5):
		p.ChangeDutyCycle(dc)
		time.sleep(0.05)
	time.sleep(2)

