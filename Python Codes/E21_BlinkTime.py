#Class 2 - Example 1 - BlinkTime
#Description: Do a Python program that allows to blink a LED (L1) connected on PIN 40 (GPIO21) ½ sec ON and ½ sec OFF using the time.time() function.

#Library declaration
import RPi.GPIO as GPIO
import time

#I/O pin labeling
L1 = 40 #Label LED connected in pin 40 as “L1”

#Constant declaration
TBLINK = 0.5 #Blink constant TBLINK initialized on 0.5s

#Variable declaration
tact = 0 #Actual time (tact)
tini = 0 #Initial time (tini)
trel = 0 #Relative time (trel)

#SETUP
#I/O Pin Configuration
GPIO.setmode(GPIO.BOARD) #Configures all pins reference using pin #
GPIO.setup(L1, GPIO.OUT) #Set pin L1 as Output
#Output cleaning
GPIO.output(L1,0) #Turn OFF L1 (also posible GPIO.output(L1,False))
#Reset first time
tini = time.time() #Reset tini to current time

#EXECUTION
while True:
	tact = time.time()
	trel = tact - tini  #Calculate the relative time
 	if trel < TBLINK: #If relative time (trel) is less than the blinking time constant (TBLINK)
		GPIO.output(L1,1) #Turn ON L1
	elif trel < TBLINK: #If trel is greater than blinking time constant but less than blinking time x 2 (1/2 sec ON and ½ sec OFF)
		GPIO.output(L1,0) #Turn OFF L1
	else: #In other case (if trel is greater than 2 times the blinking time constant)
		tini = time.time()  #Take a new initial time in order to begin again the blinking cycle (reset rel time to 0 in next iteration)
