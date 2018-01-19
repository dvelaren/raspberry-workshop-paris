#Class 2 - Example 2 - BlinkFSM
#Description: Do an Python program that blinks a LED (𝑳𝟏) connected on pin 40,
#½ sec ON and ½ sec OFF while the emergency button is not activated (𝑩𝑬𝑴𝑮)
#connected on pin 36. If 𝑩𝑬𝑴𝑮 is ON, the LED 𝑳𝟏 remains OFF and the LED 𝑳𝟐
#connected on pin 38 turns ON. When there isn’t anymore an emergency, the
#process returns to its normal blinking.

#Library declaration
import RPi.GPIO as GPIO
import time

#States
SLEDOFF = 0 #State LED OFF
SLEDON = 1 #State LED ON
SAEMG = 2 #State alarm

#I/O Pin definition
L1 = 40 #LED L1 connected on pin #40
L1 = 38 #LED L2 connected on pin #38
SW = 36 #SW connected on pin #36

#Constants definition
BLINK = 0.5 #Blink time constant 0.5 secs

#Variable definition
tact = 0.0 #Actual time variable
tini = 0.0 #Initial time variable
trel = 0.0 #Relative time variable
state = SLEDOFF #Initial state

#Subroutines and functions
#FSM
def FSLEDOFF():
    global tini
    global state
    #Outputs state
    GPIO.output(L1, 0) #Turn OFF L1
    GPIO.output(L2, 0) #Turn OFF L2
    #Variables Computation
    trel = tact - tini
    #Transition questions
    if trel >= BLINK:
        state = SLEDON #Change state
        print("State: SLEDON")
        tini = time.time()
    elif GPIO.input(SW) == 1:
        state = SAEMG
        print("State: SAEMG")

def FSLEDON():
    global tini
    global state
    #Outputs state
    GPIO.output(L1, 1) #Turn ON L1
    GPIO.output(L2, 0) #Turn OFF L2
    #Variables Computation
    trel = tact - tini
    #Transition questions
    if trel >= BLINK:
        state = SLEDOFF #Change state
        print("State: SLEDOFF")
        tini = time.time()
    elif GPIO.input(SW) == 1:
        state = SAEMG
        print("State: SAEMG")

def FSAEMG():
    global tini
    global state
    #Outputs state
    GPIO.output(L1, 0) #Turn OFF LED
    GPIO.output(L2, 1) #Turn ON L2
    #Transition questions
    if GPIO.input(SW) == 0:
        state = SLEDOFF
        print("State: SLEDOFF")
        tini = time.time()

FSM = {0: FSLEDOFF,
       1: FSLEDON,
       2: FSAEMG,
}

#Configuration
#IO Pin Setup
GPIO.setmode(GPIO.BOARD) #Set pin to board number
GPIO.setup(L1, GPIO.OUT) #LED L1 as output
GPIO.setup(L2, GPIO.OUT) #LED L2 as output
GPIO.setup(SW, GPIO.IN) #SW as input
#Output cleaning
GPIO.output(L1, 0) #Turn off L1
GPIO.output(L2, 0) #Turn off L2
#Reset tini
tini = time.time() #Reset tini time

#Execution
while True:
    tact = time.time() #Acquire actual time
    FSM[state]() #Execute FSM
