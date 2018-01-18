#Class 1 - Example 2 - LEDSW
#Description: In the PIN 36 (GPIO16) there is a switch (SW) and in the PIN 40 there is a LED (L1). Turn ON the LED if the switch is activated, in other case, turn off the LED

#Library declaration
import RPi.GPIO as GPIO

#I/O pin labeling
L1 = 40 #Label LED connected in pin 40 as “L1”
SW = 36 #Label Switch connected in pin 36 as “SW”

#SETUP
#I/O Pin Configuration
GPIO.setmode(GPIO.BOARD) #Configures all pins reference using pin #
GPIO.setup(L1, GPIO.OUT) #Set pin L1 as Output
GPIO.setup(SW, GPIO.IN) #Set pin SW as Output

#Output cleaning
GPIO.output(L1,0) #Turn OFF L1 (also posible GPIO.output(L1,False))

#EXECUTION
while True:
	if GPIO.input(SW) == 1:
		GPIO.output(L1,1) #Turn ON L1
	else:
		GPIO.output(L1,0) #Turn OFF L1
