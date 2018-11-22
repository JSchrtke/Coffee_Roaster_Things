import sys
import time
from Phidget22.Phidget import Phidget
from Phidget22.Devices.TemperatureSensor import TemperatureSensor
from Phidget22.PhidgetException import PhidgetException, ErrorCode


# define method to display phidget exceptions
def display_phidget_error(error):
    """
    * error: PhidgetException object
    """
    sys.stderr.write("Description: " + error.details + "\n")

    if error.code is ErrorCode.EPHIDGET_NOTATTACHED:
        sys.stderr.write("\tThis error occurs when a phidget function is called before a"
                         + "Phidget channel has been opened and attached")
    elif error.code is ErrorCode.EPHIDGET_NOTCONFIGURED:
        sys.stderr.write("\tThis error occurs when a Phidget function is called before all"
                         + "must-set parameters have been set for the channel")
    elif error.code is ErrorCode.EPHIDGET_TIMEOUT:
        sys.stderr.write("\tThis error occurs when a Phidget device could not be attached "
                         + "within the given wait time. Check the Phidget's connection and try "
                         + "again!")
    else:
        sys.stderr.write("Unhandled error code!\n Code: " + str(error.code) + "\n")


# define the attachement handler
def on_attach_handler(self, device_serial=118560, device_channel=0, device_temp_change_trigger=0,
                      device_data_polling_interval=32):
    """
    * Get's called an attachment event is registered
    * sets:
        - Device serial(default: 118560)
        - Channel(default: 0)
        - Temperature change trigger value (°C)[default: 0]
        - Data polling interval(ms)[default: 32]
    """
    try:
        # set the device serial number
        self.setDeviceSerialNumber(device_serial)

        # set the channel number
        self.setChannel(device_channel)

        # set the temperature change trigger
        self.setTemperatureChangeTrigger(device_temp_change_trigger)

        # set the data polling interval
        self.setDataInterval(device_data_polling_interval)
    except PhidgetException as e:
        print("\nError in attachment event!")
        self.display_phidget_error(e)


# define the temperature change handler
def on_temperature_change_handler(self, temp):
    """
    Get's called whenever the temperature change is greater than the trigger value
    """
    temperature = temp


# define the device attachment method
def attach_device(device, attach_handler, temp_change_handler):
    """
    * device: a Phidget TemperatureSensor instance
    * attach_handler: method to be called when attachment event is registered
    * temp_change_handler: method to be calle when temperature change event is registered
    """
    try:
        # set the attachment handler
        device.setOnAttachHandler(on_attach_handler)
        # set the temperature change handler
        device.setOnTemperatureChangeHandler(on_temperature_change_handler)

        print("Trying to attach temperature sensor\nOpening and waiting for attachment...")
        device.openWaitForAttachment(5000)
        # this sleep timer is here so the temperature change handler can collect atleast one
        # temperature value
        time.sleep(1)
        print("Attached!")

    except PhidgetException as e:
        print("\nError in attachment event!")
        display_phidget_error(e)
