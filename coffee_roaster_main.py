# import necessary libraries
import sys
import time
from temp_phidget_helper_functions import *
from coffee_roaster_helper_functions import *
from Phidget22.Phidget import Phidget
from Phidget22.Devices.TemperatureSensor import TemperatureSensor
from Phidget22.PhidgetException import PhidgetException, ErrorCode

temp_sensor = -1

while True:
    # create instance of the Phidget Temperature Sensor
    temp_sensor = TemperatureSensor()

    # attach phidget
    try:
        attach_device(temp_sensor, on_attach_handler, on_temperature_change_handler)
    except SystemExit:
        sys.stderr.write("\nExiting...")
        break


    # create variable that hold the live roast profile
    live_roast = None
    # create the variable that holds the reference profile, if given
    reference_profile = None

    # show menu
    try:
        main_menu(live_roast, reference_profile, temp_sensor)
    except SystemExit:
        sys.stderr.write("\nExiting...")
        break
