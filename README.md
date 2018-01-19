# Raspberry Workshop for Université Paris 1 -  Sorbonne
Raspberry workshop course for basic concepts required to start developing software in Arduino Platform. It consists in a total of 5 classes (click for PDF):

* [Class 1 - Raspberry Fundamentals](https://raw.githubusercontent.com/tidusdavid/raspberry-workshop-paris/master/Slides/Class%201%20-%20Raspberry%20Fundamentals.pdf)

## Requirements
* [Raspberry Pi 3 Model B V1.2](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
* min 30 pcs [Jumper Wires H-H, M-H, M-M](https://www.amazon.com/Elegoo-120pcs-Multicolored-Breadboard-arduino/dp/B01EV70C78/ref=pd_bxgy_147_img_3?_encoding=UTF8&pd_rd_i=B01EV70C78&pd_rd_r=8R86GV0FSJYYR6FNNXK2&pd_rd_w=nM5v2&pd_rd_wg=mHeIO&psc=1&refRID=8R86GV0FSJYYR6FNNXK2)
* [DFROBOT Sensor Kit for Arduino](https://www.dfrobot.com/product-725.html).
* [DHT11 Temperature Humidity Sensor](https://www.dfrobot.com/product-174.html)

## Class examples
Below you can see the examples explanation and connection for each class:

### Class 1 - Raspberry Fundamentals
This class covers:
1. Introduction.
2. Raspberry Pi 3 Rev B Specs.
3. Detailed GPIO Pinout.
4. Raspberry Pi 3 Required Equipment.
5. Raspberry Pi 3 Operative Systems
6. Raspbian Basic CLI Commands.
7. Python common functions with Raspberry
8. Python Variables
9. Python Typical Operators
10. Python Program Structure for HW

#### Example 1.1 – Python common used commands
In PIN 40 (GPIO21) there is a LED (L1) connected. Blink the LED ½ second ON and ½ second OFF.
![alt text](https://raw.githubusercontent.com/tidusdavid/raspberry-workshop-paris/master/Resources/E11_Blink.png)

#### Example 1.2 – If statement with digital input
In the PIN 36 (GPIO16) there is a switch (SW) and in the PIN 40 there is a LED (L1). Turn ON the LED if the switch is activated, in other case, turn off the LED.
![alt text](https://raw.githubusercontent.com/tidusdavid/raspberry-workshop-paris/master/Resources/E12_LEDSW.png)

#### Example 1.3 – DHT11 Sensor
Monitor the current temperature and humidity of the environment every second using a DHT11 connected to GPIO21 (PIN 40).
![alt text](https://raw.githubusercontent.com/tidusdavid/raspberry-workshop-paris/master/Resources/E13_DHT11.png)

### Class 2 - Relative Timing and FSM with Raspberry
This class covers:
1. Relative timings in Raspberry Python using time.time() function.
2. Finite State Machines with Raspberry Python.

#### Example 2.1 – Relative timing in Raspberry with time.time()
Do a Python program that allows to blink a LED (L1) connected on PIN 40 (GPIO21) ½ sec ON and ½ sec OFF using the time.time() function
![alt text](https://raw.githubusercontent.com/tidusdavid/raspberry-workshop-paris/master/Resources/E21_BLINKTIME.png)

#### Example 2.2 – FSM with Python and Raspberry
Do an Python program that blinks a LED (𝑳𝟏) connected on pin 40, ½ sec ON and ½ sec OFF while the emergency button is not activated (𝑩𝑬𝑴𝑮) connected on pin 36. If 𝑩𝑬𝑴𝑮 is ON, the LED 𝑳𝟏 remains OFF and the LED 𝑳𝟐 connected on pin 38 turns ON. When there isn’t anymore an emergency, the process returns to its normal blinking.

![alt text](https://raw.githubusercontent.com/tidusdavid/raspberry-workshop-paris/master/Resources/E22_BLINKFSM.png)
