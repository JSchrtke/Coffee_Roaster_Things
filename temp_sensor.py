import sys
import time
import matplotlib.pyplot as plt

from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *
from Phidget22.PhidgetException import *


def storeTemperatureData(time, temperature, storage_list_x, storage_list_y):
    """
    * Stores the data, time and temperature pairs, in a given list
    * time: the time associated with a temperature measurement
    * temperature: the temperature measured
    * storage_list: a particular list used for storing the data Tuples
    """
    storage_list_x.append(time)
    storage_list_y.append(temperature)


def displayError(e):
    """
    * Displays the error details
    * Tells the user what to do in case of an error/exception
    * e: The exception to be handled
    """
    sys.stderr.write("Code: " + str(e.code) + "\n")
    sys.stderr.write("Desc: " + e.details + "\n")

    if (e.code == ErrorCode.EPHIDGET_TIMEOUT):
        sys.stderr.write("\nThis error most likely occurs because the Phidget isn't properly attached to the computer. Please check the connection and try again. ")
        input("\nPress enter to continue.\n")

def onAttachHandler(self):
    """
    * Set's the DataInterval and ChangeTrigger
    * Get's called when a channel registers an attachment event
    """
    # creating an instance of the TemperatureSensor class to assign the 
    # triggers to
    tempPhidget = self

    try:
        tempPhidget.setTemperatureChangeTrigger(0.0)
        tempPhidget.setDataInterval(50)
    except PhidgetException as e:
        print("\nError while setting the attach handler!")
        displayError(e)


def onTemperatureChangeHandler(self, temperature):
    """
    * Gets called when the temperature change is over the set threshold
    """
    time_now = time.time() - time_start
    
    # prints a percentage value to let the user know how much data has been 
    # collected during collection
    print("\r" + str(round((time_now / sample_time * 100), 3)) + "%" + "...", end = " ")

    storeTemperatureData(time_now, temperature, test_storage_x, test_storage_y)


# Creating an instance of the TemperatureSensor object
tempSens = TemperatureSensor()

# Define serials, channels and such to connect phidget
tempSens.setDeviceSerialNumber(118560)
tempSens.setHubPort(0)
tempSens.setChannel(0)

# Setting a starting time for timestamp use later
time_start = time.time()

# Test list for storing the time and temp data, need to be removed and replaced
# when implementing future storage/plotting system
test_storage_x = []
test_storage_y = []

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


# Waiting for the phidget to be attached
while True:
    print("Opening an waiting for Attachement...")
    try:
        tempSens.openWaitForAttachment(5000)
        break
    except PhidgetException as e:
        print("\nError in attachement event!")
        displayError(e)
print("Attached!")

# Setting the time data will be sampled for
sample_time = 10
print("Sampling data for " + str(sample_time) + " seconds...")

# This sleep timer suspeds the further execution of the program until the data 
# collection has finished
time.sleep(sample_time)

# Newline here is needed because of the way the progress counter works, see 
# in def of onTemperatureChangeHandler
print("\r100"+ "%" + "...")
print("Done sampling...")

# Clearing the TemperatureChangeHandler
print("Cleaning up...")
tempSens.setOnTemperatureChangeHandler(None)
print("Done cleaning up.")

#TESTING-----------------------------------------------------------------------
# Printing the storage list as a test
print(test_storage_x)
print(test_storage_y)
plt.plot(test_storage_x, test_storage_y)
plt.xlabel("time in s")
plt.ylabel("temperature in C")
ax = plt.gca()
#ax.set_ylim([0, 500])
ax.set_xlim([0, sample_time])
plt.show()
#END---------------------------------------------------------------------------

# Wait's for the user to press Enter, or any key really, to terminate the 
# program
input("Press Enter to exit:\n")
