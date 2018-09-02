import sys
import time

from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *
from Phidget22.PhidgetException import *


def onAttachHandler(self):
    """
    * Set's the DataInterval and ChangeTrigger
    * Get's called when a channel registers an attachment event
    """
    tempPhidget = self

    print("Attaching...")
    tempPhidget.setTemperatureChangeTrigger(0.0)
    tempPhidget.setDataInterval(32)
    print("Attached!")


def onTemperatureChangeHandler(self, temperature):
    """
    *Gets called when the temperature change is over the set threshold
    """
    #print("Temperature: " + str(temperature))


# Creating an instance of the TemperatureSensor object
tempSens = TemperatureSensor()
# Define serials, channels and such to connect phidget
tempSens.setDeviceSerialNumber(118560)
tempSens.setHubPort(0)
tempSens.setChannel(0)
# Setting the AttachHandler and TempChangeHandler to the previously defined 
# functions
"""
Setting the onTemperatureChangeHandler is necessary, even if the defined 
handler doesn't execute any code in it's body.
For the program be able to return a temperature via any method (specifically
the getTemperature() method), it is necessary to set the 
onTemperatureChangeHandler, wait for atleast one DataInterval and then un-set
the onTemperatureChangeHandler in order for the program to have atleast one 
temperature value to return. Otherwise, methods that try to return the 
temperature will throw an exception
"""
tempSens.setOnTemperatureChangeHandler(onTemperatureChangeHandler)
tempSens.setOnAttachHandler(onAttachHandler)

tempSens.openWaitForAttachment(5000)

time.sleep(0.032)
tempSens.setOnTemperatureChangeHandler(None)

print(tempSens.getTemperature())

print("Press Enter to exit")
# Wait's for the user to press Enter, or any key really, to terminate the 
# program
sys.stdin.readline(1)
