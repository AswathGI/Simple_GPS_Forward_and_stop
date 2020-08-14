# Summary
The above simple code is to make the MonsterBorg robot move forward and stop after reaching particular location. 
The code is very simple and gives you a quick look to start GPS autonomous project.
Here the MonsterBorg Robot has few different sensors integrated with RPi to make it move autonomously. 

This simple program Access two sensors:
- Adafruit Ultimate GPS sensor ( via USB port )
- Sharp Distance measure sonsor ( via ADC chip - MC3008 )

Both the sensors are attached to Raspberry Pi and uses python3 to execute. 

# Steps to runs this code:

To get sensor values, we are using few libraries from adafruit.
Adafruit has stopped using python 2 version and all its libraires can be executed only using python 3 version. 

Please follow the steps to install and execute this code

## Step 1
Go to terminal and enter the following commands

### Update the RPi
```shell
$ sudo apt-get update
$ sudo apt-get upgrade
```

### Install phython3 
```shell
$ sudo apt install python3
$ sudo apt-get install python3-pip
```

## Step 2 Install Libraries
### Adafuit GPIO Library
```shell
$ sudo apt-get install build-essential python-pip python-dev python-smbus git
$ git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
$ cd Adafruit_Python_GPIO
$ sudo python3 setup.py install
```
### Adafruit MCP3008
```shell
$ git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git
$ cd Adafruit_Python_MCP3008
$ sudo python3 setup.py install
```

### Adafruit GPS
```shell
$ sudo pip3 install adafruit-circuitpython-gps
```

## Step 3 Execute Main code
The main program is rewritten to work on python3 using python3 version of ThunderBorg.py
First, convert all files into executable format, by
```shell
$ cd GPS
$ chmod +x install.sh
$ sudo ./install.sh
```

To Run the main code:
```shell
$ sudo ./monsterGPS.py
```

Feel free to change the coordinates given in the if condition in the main program (monsterGPS.py)
##### You should be able to run the main program without any error at this point :)


