#Reference: https://www.raspinews.com/blinking-led-on-raspberry-pi-using-python/
# Edited by: ArashMath

import RPi.GPIO as GPIO
import time

LedPin = 11

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
	GPIO.output(LedPin, GPIO.HIGH)

def blink():
	while True:
		GPIO.output(LedPin, GPIO.HIGH)
		time.sleep(0.5) #The number in this parentheses, shows the time LED is ON (in seconds)
		GPIO.output(LedPin, GPIO.LOW)
		time.sleep(0.5) #The number in this parentheses, shows the time LED is OFF (in seconds)

def destroy():
	GPIO.output(LedPin, GPIO.LOW)
	GPIO.cleanup()
	
if __name__ == '__main__':
	setup()
	try:
		blink()
	except KeyboardInterrupt:
		destroy()	
