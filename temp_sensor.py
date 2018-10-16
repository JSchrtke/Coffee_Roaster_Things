import sys
import time
import threading
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *
from Phidget22.PhidgetException import *


class InputError(Exception):
    """
    Exception raised for input errors
    """
    def __init__(self, error_message):
        self.error_message = error_message


class Threading(threading.Thread):

    def __init__(self, thread_id, thread_name, method):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.method = method

    def run(self):
        print("starting " + self.thread_name)
        print(str(self.thread_name) + " called: " + str(self.method))
        self.method()
        print("terminating " + self.thread_name)


class LivePlot():

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel("T(s)")
    ax.set_ylabel("t(°C)")

    def __init__(self, sample_time, time_storage, temp_storage):
        self.sample_time = sample_time
        self.time_storage = time_storage
        self.temp_storage = temp_storage

    def update_live_plot(self, i):
        self.ax.plot(self.time_storage, self.temp_storage, color='blue', linestyle='-', lw=1)

    def set_animation(self):
        anim = animation.FuncAnimation(self.fig, self.update_live_plot, interval=1000, frames=self.sample_time)
        return anim

    def plot(self):
        anim = self.set_animation()
        anim
        plt.show()


def store_temp_data(time, temp, time_storage, temp_storage):
    """
    * Stores temperature and time data in two corresponding lists
    * args:
        - time: the time associated with a temperature measurement
        - temp: the temperature measured
    """
    time_storage.append(time)
    temp_storage.append(temp)


def display_error(self):
    """
    * Displays the error details
    * Tells the user what to do in case of an error/exception
    * e: The exception to be handled
    """
    e = self

    sys.stderr.write("Code: " + str(e.code) + "\n")
    sys.stderr.write("Desc: " + e.details + "\n")

    if (self.e.code == ErrorCode.EPHIDGET_TIMEOUT):
        sys.stderr.write("\nThis error most likely occurs because the Phidget isn't properly"
                         "attached to the computer. Please check the connection and try again. ")
        input("\nPress enter to continue.\n")
    else:
        sys.stderr.write("\n Unknown exception! ")


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
    temp_sensor = self
    try:
        temp_sensor.setDeviceSerialNumber(118560)
        temp_sensor.setHubPort(0)
        temp_sensor.setChannel(0)
        # Temperature change threshold in °C
        temp_sensor.setTemperatureChangeTrigger(0)
        # Data polling interval in ms
        temp_sensor.setDataInterval(50)
    except PhidgetException as e:
        print("\nError while setting the attach handler!")
        self.display_error(e)


def on_temperature_change_handler(self, temp):
    """
    * Get's called whenever a temperature change even occurs, i.e. whenever the temperature
        change goes over the value defined with setTemperatureChangeTrigger()
    * temp: the measured temperature value
    """
    time_now = time.time() - time_start
    # prints a percentage value to let the user know how much data has been collected during
    # collection
    print("\r" + str(round((time_now / sample_time * 100), 3)) + "%"
          + "...\tTime: " + str(round(time_now, 2)) + "s\tTemperature: "
          + str(round(temp, 2)) + "°C", end=" ")
    store_temp_data(time_now, temp, test_storage_x, test_storage_y)


def yes_no_menu(default):
    string = sys.stdin.readline(5)
    if not string:
        raise InputError("Empty input!")

    if (string[0] == '\n'):
        if (default == -1):
            raise InputError("Empty input!")
        return default

    if (string[0] == 'n' or string[0] == 'N'):
        return False

    if (string[0] == 'y' or string[0] == 'Y'):
        return True

    raise InputError("Invalid input!")


def save_profile_to_file(file_name, time_storage, temperature_storage):
    try:
        with open("C:\\Users\\Joharnis\\Desktop\\Coffee Roaster Testing\\data\\" + str(file_name)
                  + ".txt", "w") as filehandle:

                for time_value in time_storage:
                    filehandle.write("%s\n" % time_value)

                filehandle.write("\n")

                for temp_value in temperature_storage:
                    filehandle.write("%s\n" % temp_value)

                filehandle.write("\n")
                filehandle.close()
    except Exception as e:
        display_error(e)


def main():
    # Setting the AttachHandler and TempChangeHandler to the previously defined functions
    """
    Setting the onTemperatureChangeHandler is necessary, even if the defined handler doesn't
    any code in it's body. For the program be able to return a temperature via any method
    (specifically the getTemperature() method), it is necessary to set the
    onTemperatureChangeHandler, wait for atleast one DataInterval and then un-set the
    onTemperatureChangeHandler in order for the program to have atleast one temperature value to
    return. Otherwise, methods that try to return the temperature will throw an exception
    """
    temp_sens.setOnAttachHandler(on_attach_handler)
    temp_sens.setOnTemperatureChangeHandler(on_temperature_change_handler)


    # Waiting for the phidget to be attached
    while True:
        print("Opening an waiting for Attachement...")
        try:
            temp_sens.openWaitForAttachment(5000)
            break
        except PhidgetException as e:
            print("\nError in attachement event!")
            display_error(e)
    print("Attached!")
    print("Sampling data for " + str(sample_time) + " seconds...")

    # This sleep timer suspeds the further execution of the program
    # until the data collection has finished
    time.sleep(sample_time)

    print("\r100" + "%" + "...")
    print("Done sampling...")

    # Clearing the TemperatureChangeHandler
    print("Cleaning up...")
    temp_sens.setOnTemperatureChangeHandler(None)
    print("Done cleaning up.")

    while True:
        print("\nSave current data? [y/n]")
        try:
            yes_no = yes_no_menu(-1)
            if yes_no is True:
                save_profile_to_file(input("Enter filename: \n"), test_storage_x, test_storage_y)
                print("saving...")
                time.sleep(1)
                break
            elif yes_no is False:
                break
            else:
                pass
        except InputError as e:
            print("An Error occured!")
            continue

    # Wait's for the user to press Enter, or any key really, to terminate the program
    input("Press Enter to exit:\n")


# Test list for storing the time and temp data, need to be removed and replaced when implementing
# future storage/plotting system
test_storage_x = []
test_storage_y = []

# Creating an instance of the TemperatureSensor object
temp_sens = TemperatureSensor()

# Setting the time data will be sampled for
sample_time = 10

# Live plot yes or no
while True:
    try:
        print("Plot data live? [y/n]")
        yes_no = yes_no_menu(-1)
        if yes_no is True:
            # Setting a starting time for timestamp use later
            time_start = time.time()

            # Starting the main logic of the program in a second thread
            main_thread = Threading(1, "main-method-thread", main)
            main_thread.start()

            # Starting the plotting
            live_plot = LivePlot(sample_time, test_storage_x, test_storage_y)
            live_plot.plot()
            break
        elif yes_no is False:
            # Starting the main logic in the main(default) thread
            main()
            break
        else:
            print("Invalid input!")
            pass
    except InputError as e:
        print("Invalid input!")
        continue
