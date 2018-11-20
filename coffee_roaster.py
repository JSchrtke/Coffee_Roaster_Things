# import sys module
import sys

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


# create TempProbeCantAttachException class
class TempProbeCantAttachException(Exception):
    def __init__(self, message):
        self.code = 1
        self.details = message


# TODO: create LiveProfile class wtf was this meant for? LiveProfile as in Live roast? this can probably go away


# create RoastProfile class
class RoastProfile():
    # create variable to store the largest time value in the reference profile
    largest_reference_time = -1
    # TODO: set the largest_reference_time variable to the largest time in the reference profile;
    #       what method to use? Use last/biggest index?
    # create a variable that holds the starting time
    start_time = -1
    # create variable that holds info wether or not the roast is finished; bool
    is_roast_finished = False
    # create a variable that holds the data polling interval; how is this variable going to be
    # set?
    data_polling_interval = -1
    # create a variable that holds the last polled time
    current_time = -1
    # create a variable that holds the last polled temperature
    current_temp = -1
    # create variable that holds the last polled time/temperature value pair
    current_data = current_time, current_temp
    # TODO: create list to hold the roast data

    # create init method
    def __init__(self, data_interval):
        # set the data interval
        self.data_polling_interval = data_interval

    # create get_current_data method in RoastProfile class
    def get_current_data(self, temp_sensor):
        # get current time
        self.current_time = time.time() - self.start_time
        # get current temperature
        self.current_temp = temp_sensor.getTemperature()

    # create load_reference method in RoastProfile class
    def load_reference_profile(self):
        # TODO: how is the profile saved? what format? how do I get it out of the file and into
        #       the respecitve list? 
        pass  # TODO: remove pass once load_reference method is done

    # create create_reference method in RoastProfile class
    def create_reference_profile(self):
        pass

    # create save_profile_to_file method
    def save_profile_to_file(self):
        pass  # TODO: remove pass once method is done

    # TODO: create manual_roast_menu method
    def manual_roast_menu(self):
        # TODO: option one: Enter new target temperature; this option allows to set a new
        #       temperature for the roaster to reach and keep; to be used during a manual roast
        # TODO: option two: roast is done: tells the program the current roast is finished,
        #       probably raises a flag, same as with a rost using a reference profile.
        # TODO: option three: exit program: raise exit program exception
        pass  # TODO: remove pass once manual_roast_menu is finished

    # create start_roast method in the RoastProfile class
    def start_roast(self, ref_prof):
        """
        ref_prof: an instance of RoastProfile, passed to be the reference profile for the roast
        """
        # create variable to hold the reference profile
        reference_profile = None
        # setting reference_profile to the profile passed to start_roast
        reference_profile = ref_prof
        # wrap entire function body in while loop that repeats every data polling interval, while
        # the roast is not finished
        while self.is_roast_finished is False:
            # set starting time variable to the current time
            self.start_time = time.time()
            # if manual roast:
            if reference_profile is not type(RoastProfile):
                # display menu that controls things during the roast
                self.manual_roast_menu()
            # TODO: all the display, so everything that runs things from pyplot needs to run in
            #       the base thread. This all is currently main(), which doesn't run in the base
            #       thread but the main thread. I need to figure out a method for displaying the
            #       plot which get's triggered from this method, but get's called in the
            #       other/base thread so it all works properly.
                # TODO: display the current time in the roast in a seperate window (or subplot in the
                #       plotting window)
                # TODO: display the current temperature in a seperate window (or subplot in the
                #       plotting window)
                # TODO: display the plot
                # TODO: every second, call the method to get the current time and temperature;
                #       get_current_time_temp
                # TODO: every second, update the plot
                # TODO: append data from the temporary variables to the logging lists, so the
                #       live_profile can be saved to file after the roast. Do I save the values
                #       individually or as a Tuple?
                # TODO: once the user uses during roast menu option two: roast done, set the roast
                #       is done variable to true, thus ending the while loop
            # TODO: if roast with reference:
            elif reference_profile is type(RoastProfile):
                # TODO: display the current time in the roast in a seperate window (or subplot in the
                #       plotting window)
                # TODO: display the current temperature in a seperate window (or subplot in the
                #       plotting window)
                # TODO: display the plot
                # TODO: plot the reference profile
                # TODO: every second, call the method to get the current time and temperature;
                #       get_current_data
                # TODO: every second, update the plot
                # TODO: every second, call the method that compares the live and reference profile.
                    # TODO: create method to compare two profiles in RostProfile class
                        # TODO: This method needs to check what the largest time value in
                        #       the reference profile is beforehand
                        # TODO: method needs to raise a flag once the current_time value of the
                        #       live_roast is >= to the largest time value in the reference_profile
                        #       as a signal that the roast is done
                # TODO: append data from the temporary variables to the logging lists, so the
                #       live_profile can be saved to file after the roast. Do I save the values
                #       individually or as a Tuple?
                # TODO: once the last polled time variable is greater or equal to the maximum time
                #       in reference variable, set roast is done variable to true, thus ending the
                #       loop
                pass  # TODO: remove pass once the elif is done
            else:
                # TODO: raise some Exception
                pass  # TODO: remove pass once the else is done
        # TODO: once the rost is finished, call method to save the roast; live_profile.save_to_file
        # TODO: return to main menu
        pass  # TODO: remove pass once start_roast method is done
    pass  # TODO: remove pass once RoastProfile class is done


# create method to display exception errors
def display_error(self):
    # create variable to hold the exception passed to the function
    e = self
    # open try/except to catch exceptions caused by them not having 'code' or 'details'
    try:
        pass
        # create variable that holds the error code, if it exists; init as False
        e_code = False
        # set error code variable to the exceptions error code
        e_code = e.code
        # write error code to console via stderr.write
        sys.stderr.write("Code: " + str(e_code))
        # create variable that holds the error details, if they exist; init as False
        e_details = False
        # set error detail variable to exceptions error details
        e_details = e.details
        # write error details to console via stderr.write
        sys.stderr.write("Details: " + str(e_details))
    except:
        # if an exception occured; the exception doesn't have e.code or e.details, write the
        # exception to console via stderr.write
        if e_code is False and e_details is False:
            sys.stderr.write("Error: " + str(e))
        else:
            sys.stderr.write("Unknown exception occured!")


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
    temperature = temp


# create menu method
def main_menu():
    # variable that get's returned by the main_menu() method to let main() know if the roast
    # uses a reference profile or not 20181120: Why does main() need to know this? Nothing in main that would use that info
    roast_uses_reference = False
    # wrap menu in while loop that runs until the user made a choice
    # create variable to control the menu loop
    is_menu_loop_running = True
    # create while loop
    while is_menu_loop_running is True:
        # show options to user
        print("===== MAIN MENU =====")
        print("[1] Load reference profile")
        print("[2] Create reference profile (not yet functional)")  # TODO: remove "not yet functional once reference creation feature is implemented"
        print("[3] Start roast")
        print("[4] Exit program")
        # get user choice
        user_menu_choice = input("\n: ")
        if user_menu_choice == 1:
            # If a reference profile is loaded, the roast uses a reference; set variable
            # accordingly
            roast_uses_reference = True
            # menu option 1: load reference profile
            # create a new instance of the roast profile class to hold the reference
            reference_profile = RoastProfile()
            # call the load_reference method from RoastProfile class
            reference_profile.load_reference_profile()
            is_menu_loop_running = False
        elif user_menu_choice == 2:
            print("Reference profile creation is not yet implemented!")
            continue  # TODO: remove continue once the creation of reference profiles is implemented
            # Maybe this feature can be entirely omitted, since I will create reference
            # profiles by doing manual test roasts for dialing in anyway, which can then be
            # saved and used as a reference
            # TODO: main(): option two selected; create reference profile:
                # TODO: create another instance of the RoastProfile class;
                #       new_reference_profile
                # TODO: call new_reference_profile.create_reference to create the new profile
                # TODO: save the new profile to file by calling the save_profile_to_file
                #       method from the RoastProfile class
            is_menu_loop_running = False
        elif user_menu_choice == 3:
            # menu option 3: start roast
            # run the start_roast method with a reference profile if it was loaded
            if roast_uses_reference is True:
                live_profile.start_roast(reference_profile)
            # run the start_roast method without a reference profile if none was loaded
            else:
                live_profile.start_roast(None)
            is_menu_loop_running = False
        elif user_menu_choice == 4:
            # menu option 4: exit program
            raise SystemExit("\nYou chose to exit the program\nExiting...")
        else:
            print("Invalid input!")
            continue


# TODO: create variable to store wether or not the temperature probe was already attached successfully, so that if you run 20181120: Run what? learn to finish your fucking comments.


# create main()
def main():
    # set the attach handler to the previously defined method
    temp_sens.setOnAttachHandler(on_attach_handler)
    # set the temperature change handler to previously defined method
    temp_sens.setOnTemperatureChangeHandler(on_temperature_change_handler)
    # attach the temperature probe, everything needs to be wrapped in a while loop for
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
            display_error(e)  # TODO: create display_error method
            attachement_tries_counter += 1
            # tell the user you are retrying to attach the probe
            print("retrying attachment, try # " + str(attachement_tries_counter) + "/3...")
            # retry up to 3 times
            if attachement_tries_counter >= 3:  # attachment failed to many times
                # if still not successfull, tell user the program needs to be restarted
                # terminate the program
                raise TempProbeCantAttachException("\nFatal error during attachment process!"
                                                   + "\nTemperature probe could not be attached!"
                                                   + "\nThe program needs to be restarted!"
                                                   + "\nExiting...")
        # add wait timer here so that the temperature change handler can collect atleast one
        # temperature value
        time.sleep(1)
        # if the attachment is successfull, tell the user it was
        print("Attached!")

    # show menu
    main_menu()
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
    live_profile = RoastProfile()

    # create variable that controls if the main() method loop is running
    is_main_thread_running = True

    # create while loop in which the main() method's thread will run while it's true
    while is_main_thread_running is True:

        # create second thread for the main program logic, as the live plotting needs to run in
        # it's own thread to function properly, which needs to be the programs base thread
        # aswell.
        # wrap this thread in a try/except block to catch any exceptions it might raise.
        try:
            main_thread = Threading(1, "main-method-thread", main)
            main_thread.start()
            pass  # TODO: remove pass once try block is done
        except SystemExit as e_exit:
            display_error(e_exit)
        except PhidgetException as e_phidget:
            display_error(e_phidget)
        except Exception as e:
            # anything I might not catch with other exceptions
            print("\nUnexpected fatal error occured!")
            display_error(e)
        pass  # TODO: everything except the plotting logic needs to wrapped up in this while loop; remove pass when everything else is done
    pass  # TODO: the entirety of the program needs to be wrapped up in this while loop while the program is supposed to run. Remove this pass once all the rest is done.
