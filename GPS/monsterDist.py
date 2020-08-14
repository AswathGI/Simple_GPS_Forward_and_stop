#!/usr/bin/env python3
# coding: Latin-1

import ThunderBorg3 as ThunderBorg
import time
import math
import sys
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


#Setup ThunderBorg
TB = ThunderBorg.ThunderBorg()
TB.Init()
if not TB.foundChip:
    boards = ThunderBorg.ScanForThunderBorg()
    if len(boards) == 0:
        print ("No ThunderBorg found, check you are attached :)")
    else:
        print ("No ThunderBorg at address %02X, but we did find boards:" % (TB.i2cAddress))
        for board in boards:
            print ("    %02X (%d)" % (board, board))
        print ("If you need to change the I²C address change the setup line so it is correct, e.g.")
        print ("TB.i2cAddress = 0x%02X" % (boards[0]))
    sys.exit()
TB.SetCommsFailsafe(False) 

maxPower = 1.0

'''
# Function to perform a general movement
def PerformMove(driveLeft, driveRight):
    # Set the motors running
    TB.SetMotor1(driveRight * maxPower)
    TB.SetMotor2(driveLeft * maxPower)
    # Wait for the time
    time.sleep(numSeconds)
    # Turn the motors off
    TB.MotorsOff()
'''

####################
# Distance measure #

CLK = 18
MISO = 23
MOSI = 24
CS = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)


#Test = Continous drive and stop when distance <=50cm
while True:
    v0 = (mcp.read_adc(0) / 1023.0) * 3.3
    dist0 = 16.2537 * v0**4 - 129.893 * v0**3 + 382.268 * v0**2 - 512.611 * v0 + 301.439

    print("******************************")
    print("Distance0 {:.2f}".format(dist0))
    print("******************************")

    if dist0 <= 50.00:
    	TB.SetMotor1(0.0 * maxPower)
    	TB.SetMotor2(0.0 * maxPower)
    	print("Stop")
    else:
    	TB.SetMotor1(1.0 * maxPower)
    	TB.SetMotor2(1.0 * maxPower)
    	print("forward")






