#!/usr/bin/python

import rospy
import time
import RPi.GPIO as GPIO


if __name__ == '__main__':
	#rospy.init_node("tank_drive")

	GPIO.setmode(GPIO.BOARD) # Use GPIO pins number
	GPIO.setup(13, GPIO.OUT)
	GPIO.setup(15, GPIO.OUT)
	GPIO.setup(16, GPIO.OUT)
	GPIO.setup(18, GPIO.OUT)
	GPIO.setup(22, GPIO.OUT)
	pwm = GPIO.PWM(22, 1000)
	pwm.start(25)
	GPIO.output(13, True)
	time.sleep(1)
	GPIO.output(13, False)

	GPIO.output(15, True)
	time.sleep(1)
	GPIO.output(15, False)
	GPIO.output(16, True)
	time.sleep(1)
	GPIO.output(16, False)

	GPIO.output(18, True)
	time.sleep(1)
	GPIO.output(18, False)
	GPIO.cleanup() # Reset pins mode
