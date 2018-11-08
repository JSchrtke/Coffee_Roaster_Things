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


# create RoastProfile class
class RoastProfile():
    # TODO: create variable to store the largest time value in the reference profile
    #       Is there a list operation I can use to find the largest time value? Or do I just use
    #       the value with the biggest/last index?
    # TODO: create a variable that holds the starting time
    # TODO: create variable that holds info wether or not the roast is finished; bool
    # TODO: create a variable that holds the data polling interval
    #       how is this variable going to be set?
    # TODO: create variable that holds the last polled time/temperature value pair
    # TODO: create a variable that holds the last polled time
    # TODO: create a variable that hold the last polled temperature
    # TODO: create get_current_time_temp method in RoastProfile class
    # TODO: create load_reference method in RoastProfile class
    # TODO: create create_reference method in RoastProfile class
    # TODO: create start_roast method in the RoastProfile class
    # TODO: create save_profile_to_file method
    # TODO: wrap entire function body in while loop that repeats every data polling interval,
    #       while the roast is not finished
        # TODO: start_roast needs to have the reference profile as an argument. If a profile is
        #       passed, do a roast using a reference profile, else do a roast with manual
        #       temperature input
        # TODO: set starting time variable to the current time; start_time = time.time()
        # TODO: if manual roast:
            # TODO: display menu that controls things during the roast
                # TODO: option one: Enter new target temperature; this option allows to set a new
                #       temperature for the roaster to reach and keep; to be used during a manual
                #       roast
                # TODO: option two: roast is done: tells the program the current roast is
                #       finished, probably raises a flag, same as with a rost using a reference
                #       profile.
                # TODO: option three: exit program: raise exit program exception
                    # TODO: create exit program exception
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
            # TODO: display the current time in the roast in a seperate window (or subplot in the
            #       plotting window)
            # TODO: display the current temperature in a seperate window (or subplot in the
            #       plotting window)
            # TODO: display the plot
            # TODO: plot the reference profile
            # TODO: every second, call the method to get the current time and temperature;
            #       get_current_time_temp
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
    # TODO: once the rost is finished, call method to save the roast; live_profile.save_to_file
    # TODO: return to main menu
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
    # uses a reference profile or not
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
            # menu option 1: load reference profile
            # create a new instance of the roast profile class to hold the reference
            reference_profile = RoastProfile()
            # call the load_reference method from RoastProfile class
            reference_profile.load_reference()
            roast_uses_reference = True
            is_menu_loop_running = False
        elif user_menu_choice == 2:
            print("Reference profile creation is not yet implemented!")
            continue
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


# TODO: create variable to store wether or not the temperature probe was already attached successfully, so that if you run 


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
                attachment_loop_running = False
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
        except SystemExit:
            # TODO: create exit logic
            pass  # TODO: remove pass once exit exception thing is done
        except PhidgetException:
            # TODO: create PhidgetException handling logic
            pass  # TODO: remove pass once PhidgetException handling is done
        except:
            # anything I might not catch with other exceptions
            print("\nUnexpected fatal error occured!")
        pass  # TODO: everything except the plotting logic needs to wrapped up in this while loop; remove pass when everything else is done
    pass  # TODO: the entirety of the program needs to be wrapped up in this while loop while the program is supposed to run. Remove this pass once all the rest is done.
