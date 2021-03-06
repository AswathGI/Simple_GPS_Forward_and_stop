#!/usr/bin/env python3
# coding: Latin-1

import time
import board
import busio
import os, time
import serial
import adafruit_gps
import ThunderBorg3 as ThunderBorg
import math
import sys
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#####################################################
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
#****************************************************#



#####################################################
#Setup GPS
uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")
last_print = time.monotonic()
#****************************************************#



#####################################################
#Setup Distance Sensor
CLK = 18
MISO = 23
MOSI = 24
CS = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
#****************************************************#



while True:
    #Get Distance Sensor Data
    v0 = (mcp.read_adc(0) / 1023.0) * 3.3
    dist0 = 16.2537 * v0**4 - 129.893 * v0**3 + 382.268 * v0**2 - 512.611 * v0 + 301.439

    #Get GPS Data
    gps.update()
    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            # Try again if we don't have a fix yet.
            print("Waiting for fix...")
            continue
#Print 
##############################################################################
        # We have a fix! (gps.has_fix is true)
        # Print out GPS details about the fix like location, date, etc.
        print("=" * 40)  # Print a separator line.
        print(
            "Fix timestamp: {}/{}/{} {:02}:{:02}:{:02}".format(
                gps.timestamp_utc.tm_mon,  # Grab parts of the time from the
                gps.timestamp_utc.tm_mday,  # struct_time object that holds
                gps.timestamp_utc.tm_year,  # the fix time.  Note you might
                gps.timestamp_utc.tm_hour,  # not get all data like year, day,
                gps.timestamp_utc.tm_min,  # month!
                gps.timestamp_utc.tm_sec,
            )
        )
        print("Latitude: {0:.6f} degrees".format(gps.latitude))
        print("Longitude: {0:.6f} degrees".format(gps.longitude))
        print("Fix quality: {}".format(gps.fix_quality))
        # Some attributes beyond latitude, longitude and timestamp are optional
        # and might not be present.  Check if they're None before trying to use!
        if gps.satellites is not None:
            print("# satellites: {}".format(gps.satellites))
        if gps.altitude_m is not None:
            print("Altitude: {} meters".format(gps.altitude_m))
        if gps.speed_knots is not None:
            print("Speed: {} knots".format(gps.speed_knots))
        if gps.track_angle_deg is not None:
            print("Track angle: {} degrees".format(gps.track_angle_deg))
        if gps.horizontal_dilution is not None:
            print("Horizontal dilution: {}".format(gps.horizontal_dilution))
        if gps.height_geoid is not None:
            print("Height geo ID: {} meters".format(gps.height_geoid))

        # Print out Distance sensor reading
        print("******************************")
        print("Distance0 {:.2f}".format(dist0))
        print("******************************")
        
        lat1 = gps.latitude

        if lat1>= 51.452300 or dist0 <= 50.00:
            TB.SetMotor1(0.0 * maxPower)
            TB.SetMotor2(0.0 * maxPower)
            print("STOP")
        else:
            TB.SetMotor1(1.0 * maxPower)
            TB.SetMotor2(1.0 * maxPower)
            print("forward ===>>>")

