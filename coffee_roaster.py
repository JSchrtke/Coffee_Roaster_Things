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
    # member method
    # TODO: put in some method so I dont have to use the live_profile instance of the DataProfile class hardcoded in, but rather have it handled some different way. Perhaps passing it as an argument could work
    live_profile.get_time_and_temperature(current_time, current_temp)  # TODO: create get_time_and_temperature method inside RoastProfile class
    pass
# ***********************************************************************************************
# ************************************program starts here****************************************
# ***********************************************************************************************
# TODO: create a variable that controls if the base thread loop is running
# TODO: create a while loop in which the base thread, so the entirety of the program will run
#       while it's true
# TODO: create an instance of the Phidget TemperatureSensor object
# TODO: create an instance of the RoastProfile class for storing the live roast profile;
#       live_profile

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

# Maybe this entire next part should be omitted for simplicity, so I don't have to deal with
# setting up the plot and such, then close it and reopen it. Maybe just show the temperature if
# possible, since that window could stay untouched
# TODO: Show live plot and current temperature
#       TODO: create a variable live_plot to hold an instance of the DataPlot class
#             TODO: create DataPlot class
#       TODO: call the DataPlot plotting method to show the plot and current temperature
#             TODO: create plotting method in DataPlot class

# TODO: main(): show menu
#       TODO: create menu method

# TODO: main(): menu option 1: load reference profile
#       TODO: create load_reference method in RoastProfile class
# TODO: main(): menu option 2: create reference profile
#       TODO: create create_reference method in RoastProfile class
# TODO: main(): menu option 3: start roast
#       TODO: create start_roast method in RoastProfile class
# TODO: main(): menu option 4: exit program
#       TODO: when exit program is selected, turn the flags that contorl if the two main loops
#            are running to False

# Maybe this feature can be entirely omitted, since I will create reference profiles by doing
# manual test roasts for dialing in anyway, which can then be saved and used as a reference
# TODO: main(): option one selected; create reference profile:
#       TODO: create another instance of the RoastProfile class; new_reference_profile
#       TODO: call new_reference_profile.create_reference to create the new profile
#       TODO: save the new profile to file by calling the save_to_file method from the
#             RoastProfile class
#             TODO: create method to save a profile to file (which type of file to use?)

# TODO: main(): option two selected; load reference profile
#       TODO: create another instance of the RoastProfile class to store the reference profile
#             in, called reference_profile
#       TODO: call reference_profile.load_reference
#             TODO: create method to load a reference profile in RoastProfile class
#       TODO: create and set a flag so the method for roasting with the use of a reference
#             profile can be called. If no reference profile was loaded, run a version of the
#             roast method that doesn't need the reference profile

# TODO: main(): option three selected; start roast
#       TODO: call live_profile.start_roast
#             TODO: create start_roast method in the RoastProfile class
#             There needs to be a difference here between a roast controlled by a reference
#             profile and one without. Since I will need to be able to run the roaster without a
#             reference profile loaded, to find an ideal roast profile for a certain coffee.
#             There also needs to be a function to control the temperature manually during the
#             roast, so that I'm able to do a manual roast for dialing in for a specific coffee.
#             Maybe display a menu the entire time the roast is running, along with the running
#             time in the console, which allows entering of a new target temperature that the
#             roaster will follow
#                   TODO: display menu that controls things during the roast
#                         TODO: option one: Enter new target temperature; this option allows to
#                               set a new temperature for the roaster to reach and keep; to be
#                               used during a manual roast
#                         TODO: option two: roast is done: tells the program the current roast
#                               is finished, probably raises a flag, same as with a rost using a
#                               reference profile
#                   TODO: reset the plot so the live roast can be plotted; do I need to stop and
#                         restart the plotting thread for this to work? What do I need to do to
#                         clear an already existing plot? Can I just close the existing plot and
#                         reopen it to reset? can I make it so the x-axis is limited to zero
#                         before the roast starts, so all the data that it collected before the
#                         roast starts is put into the -x part of the plot and then it continues
#                         from 0 to +x from the roast start on out? This would be my prefered
#                         method, but it may just be to complicated to be worth it to implement;
#                         the easiest way to do this is probably to just close and reopen the
#                         plotting window.
#                   TODO: plot the reference profile
#                   TODO: every second, call the method to get the current temperature;
#                         get_current_temp
#                         TODO: create get_current_temp method in RoastProfile class
#                   TODO: every second, call the method that compares the live and
#                         reference profile.
#                         TODO: create method to compare two profiles in RostProfile class
#                               TODO: This method needs to check what the largest time value in
#                                     the reference profile is beforehand
#                               TODO: method needs to raise a flag once the current_time value
#                                     of the live_roast is >= to the largest time value in the
#                                     reference_profile as a signal that the roast is done
#                   TODO: start appending data to the logging lists, so the live_profile can be
#                         saved to file after the roast
#                         TODO: this will have to use a variable to store the values to be
#                               compared and not take them straing from the list's/arrays, so
#                               that it can be overridden for the purpose of a manual roast
#                   How do I detemine the roast is done? When doing a manual roast, there needs
#                   to be an option in that menu during the roast to tell the program the roast
#                   is finished. When using a reference profile, there needs to be thing in the
#                   comparison method that raises a flag once the time value of the live roast
#                   has reached >= than the largest time value in the reference profile
#                   TODO: once the rost is finished, call method to save the roast;
#                         live_profile.save_to_file
#                   TODO: return to main menu