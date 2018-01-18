#Class 1 - Example 3 - DHT11
#Description: Monitor the current temperature and humidity of the environment every second using a DHT11 connected to GPIO21 (PIN 40).

#Library declaration
import time
import Adafruit_DHT

#I/O pin labeling
DHTPIN = 21 #Label DHT sensor connected in pin 40 (GPIO21) as “DHTPIN”
DHTTYPE = Adafruit_DHT.DHT11 #Specify the DHT sensor type

#Variable declaration
h = 0.0 #Variable to store humidity
t = 0.0 #Variable to store temperature

#EXECUTION
while True:
	h, t = Adafruit_DHT.read_retry(DHTTYPE, DHTPIN) #Reads current temp & humid and stores it
	print(“Temp: ” + str(t) + “Humid: ” + str(h)) #Prints in the console the t, h vars
