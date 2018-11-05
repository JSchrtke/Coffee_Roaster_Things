import time

# set up temperature probe
# import neccessary libraries
# import the Phidget22 Phidget library
from Phidget22.Phidget import Phidget

# import the Phidget22 TemperatureSensor Device library
from Phidget22.Devices.TemperatureSensor import TemperatureSensor

# import the Phidget22 Exception library
from Phidget22.PhidgetException import PhidgetException, ErrorCode


# define the on_attach_handler
def on_attach_handler(self):
    """
    * Get's called when a channel registers an attachement event
    * sets:
        - Device serial
        - Hub Port
        - Channel
        - Temperature change trigger value
        - Data polling interval
    """
    # create variable that holds and instance of the TemperatureSensor object
    temp_sensor = self

    # set the device serial number given by user
    temp_sensor.setDeviceSerialNumber(118560)

    # set the channel number given by user
    channel_number = 0
    channel_number = input("Enter the channel number (default = 0):")
    temp_sensor.setChannel(channel_number)

    # set the temperature change trigger
    trigger_value = 0
    temp_sensor.setTemperatureChangeTrigger(trigger_value)

    # set the data polling interval
    polling_interval = 0
    temp_sensor.setDataInterval(polling_interval)


# define the on_temperature_change_handler
def on_temperature_change_handler(self, temp):
    # create a variable that holds the current time
    current_time = -1

    # create a variable that hold the current temperature
    current_temp = -1

    # send current time and temperature to the RoastProfile class via one of it's
    # member methods
    live_profile.get_time_and_temperature(current_time, current_temp)  # TODO: create get_time_and_temperature method inside RoastProfile class
    pass
# ***********************************************************************************************
# ************************************program starts here****************************************
# ***********************************************************************************************
# TODO: create a variable that controls if the base thread loop is running
# TODO: create a while loop in which the base thread, so the entirety of the program will run
#       while it's true
# TODO: create an instance of the Phidget TemperatureSensor object
# TODO: create an instance of the RoastProfile class for storing the live roast profile

# TODO: create variable that controls if the main() method loop is running

# TODO: create while loop in which the main() method's thread will run while it's true

# TODO: create second thread for the main program logic, as the live plotting needs to run in
#       it's own thread to function properly, which needs to be the programs main thread aswell.
#       TODO: import threading
#             TODO: create Threading class to handle all the multithreading things, needs to be
#                   a subclass of threading.Thred
#                   TODO: create init method
#                         TODO: the default __init__ method coming from threading.Thread needs
#                               to be overridden to add additional arguments
#                         TODO: set thread id
#                         TODO: set thread name
#                         TODO: set method that the thread will run

# TODO: run main method in second thread, the main method contains all the programs logic except
#       the plotting of the data
# TODO: main(): 1.4: set the attach handler to the previously defined method
#               1.5: set the temperature change handler to previously defined method
#               1.6: attach the temperature probe
#                   1.6.1: tell the user you are trying to attach the temperature probe
#                   1.6.2: open the channel and wait for the attachement event
#                   1.6.3: if the attachement is successfull, tell the user it was
#                   1.6.4: if the attachement failed, tell the user it failed
#                   1.6.5: tell the user you are retrying to attach the probe
#                   1.6.6: retry up to 3 times
#                   1.6.7: if still not successfull, tell user the program needs to be restarted
#                   1.6.8: terminate the program

# TODO: Show live plot and current temperature
#       TODO: create a variable live_plot to hold an instance of the DataPlot class
#             TODO: create DataPlot class
#       TODO: call the DataPlot plotting method to show the plot and current temperature
#             TODO: create plotting method in DataPlot class

# TODO: main(): show menu
#       TODO: create menu method
