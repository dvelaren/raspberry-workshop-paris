#Class 1 - Example 1 - Blink
#Description: In PIN 40 (GPIO21) there is a LED (L1) connected. Blink the LED ½ second ON and ½ second OFF.

#Library declaration
import RPi.GPIO as GPIO
import time

#I/O pin labeling
L1 = 40 #Label LED connected in pin 40 as “L1”

#Constant declaration
TBLINK = 0.5 #Blink constant TBLINK initialized on 0.5s

#SETUP
#I/O Pin Configuration
GPIO.setmode(GPIO.BOARD) #Configures all pins reference using pin #
GPIO.setup(L1, GPIO.OUT) #Set pin L1 as Output
#Output cleaning
GPIO.output(L1,0) #Turn OFF L1 (also posible GPIO.output(L1,False))

#EXECUTION
while True:
	GPIO.output(L1,1) #Turn ON L1
	time.sleep(TBLINK); #Delay of TBLINK secs(0.5s)
	GPIO.output(L1,0) #Turn OFF L1
	time.sleep(TBLINK); #Delay of TBLINK secs(0.5s)