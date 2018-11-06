# import time module
import time

# import threading module
import threading

# set up temperature probe
# import neccessary libraries
# import the Phidget22 Phidget library
from Phidget22.Phidget import Phidget

# import the Phidget22 TemperatureSensor Device library
from Phidget22.Devices.TemperatureSensor import TemperatureSensor

# import the Phidget22 Exception library
from Phidget22.PhidgetException import PhidgetException, ErrorCode


# create Threading class to handle all the multithreading things, needs to be a subclass of
# threading.Thred
class Threading(threading.Thread):
    # create init method
    def __init__(self, thread_id, thread_name, method_thread_runs):
        # add docstring for method
        """
        * initializes an instance of the Threading class
        * args:
            - thread_id: Identifier for the thread
            - thread_name: Name of the thread
            - method_thread_runs: The method the thread is supposed to run
        """
        # the default __init__ method coming from threading.Thread needs to be overridden to add
        # additional arguments
        threading.Thread.__init__(self)
        # set thread id
        self.thread_id = thread_id
        # set thread name
        self.thread_name = thread_name
        # set method that the thread will run
        self.method_thread_runs = method_thread_runs


# define the on_attach_handler
def on_attach_handler(self):
    """
    * Get's called when a channel registers an attachment event
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
    # TODO: put in some method so I dont have to use the live_profile instance of the
    #       DataProfile class hardcoded in, but rather have it handled some different way.
    #       Perhaps passing it as an argument could work
    live_profile.get_time_and_temperature(current_time, current_temp)  # TODO: create get_time_and_temperature method inside RoastProfile class
    pass


# create main()
def main():
    # set the attach handler to the previously defined method
    temp_sens.setOnAttachHandler(on_attach_handler)
    # set the temperature change handler to previously defined method
    temp_sens.setOnTemperatureChangeHandler(on_temperature_change_handler)
    # TODO 1.6: attach the temperature probe, everything needs to be wrapped in a while loop for
    #           the 3 tries
    # create sentry variable that controls the loop
    attachment_loop_is_running = True
    # create while loop that controls the connection tries
    while attachment_loop_is_running is True:
        # create counter variable that counts failed tries
        attachement_tries_counter = 1
        # wrap this entire attachment logic into try/except block
        try:
            # tell the user you are trying to attach the temperature probe
            print("Trying to attach the temperature sensor: ")
            print("Opening and waiting for attachment...")
            # open the channel and wait for the attachment event
            temp_sens.openWaitForAttachment(5000)
            attachment_loop_is_running = False  # attachement was successfull
        except PhidgetException as e:
            # if the attachment failed, tell the user it failed
            print("Error in attachment event!")
            display_error(e)  # TODO: implement error display method
            # when the attachment fails, the exception handling will increment the fail counter
            attachement_tries_counter += 1
            # tell the user you are retrying to attach the probe
            print("retrying attachment, try # " + str(attachement_tries_counter) + "/3...")
            # retry up to 3 times
            if attachement_tries_counter >= 3:  # attachment failed to many times
                # if still not successfull, tell user the program needs to be restarted
                print("Temperature probe could not be attached!\nThe program needs to be"
                      + "restarted\nExiting...")
                # terminate the program
                attachment_loop_running = False
                terminate_program()  # TODO: create terminate_program method
        # if the attachment is successfull, tell the user it was
        print("Attached!")
    pass  # TODO: remove pass once main method is finished

# ***********************************************************************************************
# ************************************program starts here****************************************
# ***********************************************************************************************
# create a variable that controls if the base thread loop is running
is_base_thread_running = True

# create a while loop in which the base thread, so the entirety of the program will run
#       while it's true
while is_base_thread_running is True:

    # create an instance of the Phidget TemperatureSensor object
    temp_sens = TemperatureSensor()

    # create an instance of the RoastProfile class for storing the live roast profile;
    live_profile = RoastProfile()  # TODO: create roast profile class

    # create variable that controls if the main() method loop is running
    is_main_thread_running = True

    # create while loop in which the main() method's thread will run while it's true
    while is_main_thread_running is True:

        # create second thread for the main program logic, as the live plotting needs to run in
        # it's own thread to function properly, which needs to be the programs base thread
        # aswell.
        main_thread = Threading(1, "main-method-thread", main)  # TODO: create main() method, see top
        main_thread.start()

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
        pass  # TODO: everything except the plotting logic needs to wrapped up in this while loop; remove pass when everything else is done
    pass  # TODO: the entirety of the program needs to be wrapped up in this while loop while the program is supposed to run. Remove this pass once all the rest is done.
