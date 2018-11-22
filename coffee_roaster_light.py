# import necessary libraries
import sys
import time
from temp_phidget_helper_functions import *
from Phidget22.Phidget import Phidget
from Phidget22.Devices.TemperatureSensor import TemperatureSensor
from Phidget22.PhidgetException import PhidgetException, ErrorCode


# create instance of the Phidget Temperature Sensor
temp_sensor = TemperatureSensor()

# attach phidget
attach_device(temp_sensor, on_attach_handler, on_temperature_change_handler)

# TODO: show menu

print(temp_sensor.getTemperature())
