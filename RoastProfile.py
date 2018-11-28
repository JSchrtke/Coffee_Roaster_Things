import time
import sys
import csv
import os


class RoastProfile():
    def __init__(self, temp_probe=None):
        """
        * temp_probe: an instance of a Phidget TemperatureSensor object
        """
        # create variable that holds the starting time; init to -1
        self.time_start = -1
        # create variable that holds the current time; init to -1
        self.time_current = -1
        # create variable that holds the current temperature
        self.temperature_current = -1
        # create variable to store the target temperature of the roaster
        self.temperature_target = -1
        # create a variable for the reference data
        self.reference_data = []
        # create a variable for the current data
        self.live_data = []
        # TODO: need to create a list with temperatures and their associated voltages to have it for comparison
        # create variable to hold the temperature sensor
        self.sensor = temp_probe

    # create import_profile in RoastProfile class
    def import_profile(self, path):
        """
        Loads an existing roast profile to be used as a reference for another roast
        * path: The path to the roast profile to be used as reference
        """
        # open the file given
        with open(str(path), "r") as file:
            # create csv reader
            csv_reader = csv.reader(file)
            self.reference_data = list(csv_reader)
            # close the reference profile file
            file.close()
            # TODO: splitting the reference data up into time and temp in seperate lists
                # TODO: after splitting, put in a check to see if they still have the same number of elements, just to be sure
        # TODO: DEBUG CODE, REMOVE ONCE DONE!
        for data in self.reference_data:
            print("DEBUG: Index: " + str(self.reference_data.index(data)) + " Data: " + str(data))

    def export_profile(self, data_list):
        """
        Saves the current roast to file
        * data_list: A list with the data to be saved
        """
        # create variable to hold the path for the profile folder
        path = None
        # create variable for the profile name
        name = None
        # ask user for path
        path = input("Enter the folder path to where the profile should be saved:\n")
        # ask user for a name for the profile
        name = input("Enter a name for the profile to be saved; must include .csv ending!:\n")
        # creating the file path name variable
        file_path_name = os.path.join(path, name)
        # open path/ create file
        # while loop to repeat after exception has been raised
        while True:
            try:
                print("Saving profile...")
                with open(file_path_name, "w", newline="") as file:  # empty newline is there to prevent the \r
                    csv_app = csv.writer(file, quoting=csv.QUOTE_ALL)
                    csv_app.writerows(data_list)
                file.close()
                print("Saved!")
                break
            except FileNotFoundError:
                print("Error! Invalid file path or name! Saving to Desktop as default.csv")
                path = os.path.abspath(os.path.expanduser("~/Desktop"))
                name = "default.csv"
                file_path_name = os.path.join(path, name)
                continue

    def set_target_temperature(self, temp_value):
        """
        This method set's the roasters target temperature
        * temp_value: The value that should be the target temperature
        """
        self.temperature_target = temp_value

    # create method to get current time
    def get_time_since_start(self, time_start):
        """
        Get's the time since a starting point in seconds and returns it
        * time_start: starting time in time_since_epoch format
        """
        time_current = time.time() - time_start
        return time_current

    # create method to get current temperature
    def get_current_temp(self):
        """
        Get's a temperature measured by self.sensor and returns it
        """
        temp = self.sensor.getTemperature()
        return temp

    # create start_roast method in RoastProfile
    def start_roast(self, ref_prof):
        """
        starts the roasting process, either with or without a reference profile
        """
        reference_profile = ref_prof
        # TODO: finish this method
        # check if there is a reference profile

            # if yes:
        if type(reference_profile) == RoastProfile:
            print("DEBUG: There is a reference profile\nDEBUG: roaster is doing things automatically")  # TODO: remove once rest is functional
            # set the variable that holds the starting time to the time now
            self.time_start = time.time()
            # create variable that holds info wether roast is finished
            is_roast_finished = False


            # TODO: DEBUG CODE, REMOVE ONCE DONE
            debug_while_loop_sentry = 10  # set this to the time in seconds you want the loop to run for
            debug_while_loop_counter = 0



            # every second, do the following:
            while debug_while_loop_counter < debug_while_loop_sentry:  # TODO: CHANGED FOR DEBUG, ORIGINAL LINE IS: while is_roast_finished is False:
                # create a variable that get's the time at loop start
                time_at_loop_start = time.time()
                # get the current time, store in it's variable
                self.time_current = self.get_time_since_start(self.time_start)
                print("DEBUG: self.time_current: " + str(self.time_current))
                # get the current temperature, store in it's variable
                self.temperature_current = self.get_current_temp()
                print("DEBUG: self.temperature_current: " + str(self.temperature_current))
                # TODO: comparison method:
                    # what do I need to do?
                        # compare the current temperature value with the reference temperature value corresponding to the same time
                        # so I need to first get the current time, then find the closest value in the list with the reference times and get it's index
                            # this needs to be a general purpose method, probably goes into the helper functions
                        # then get the temperature value with the same index from it's list
                            # put that into the temperature_target variable
                        # calculate the diff between the target value and the current value
                        # if the difference is larger than 0.5°C, lookup the voltage value associated with the target temperature and send it to the arduino
                # create time and temp tuple
                data_tuple = (self.time_current, self.temperature_current)
                # append time and temperature tuple to a list that will be used to later store the profile of the roast
                self.live_data.append(data_tuple)
                # TODO: check if the current time is greater or equal than the biggest time value in the reference profile
                    # TODO: if yes, set a variable that is used to check if the roast is finished to true
                    # TODO: if no, repeat unitl it is
                # create mechanism to handle if the time at end is bigger than the time at
                # start + 1
                debug_while_loop_counter = debug_while_loop_counter + 1  # TODO: DEBUG LINE, REMOVE
                try:
                    # create variable that get's the time at loop end
                    time_at_loop_end = time.time()
                    # make loop wait by 1 second minus the time it took to execute the code
                    time.sleep(1 - (time_at_loop_end - time_at_loop_start))
                except ValueError:
                    print("DEBUG: ValueError was raised at the end of"
                          + " RoastProfile.start_roast while loop")
                    continue
            self.export_profile(self.live_data)

            # if no:
        else:
            # tell user roaster is running in manual mode
            print("No reference profile was loaded, running roaster in manual mode!")
            # prompt user to enter a starting temperature for the roaster to be; store it
            # in a variable for it
            # variable that controls if the starting temp setting loop runs
            is_starting_temp_set = False
            while is_starting_temp_set is False:
                try:
                    starting_temp = int(input("Please enter the starting temperature:\n"))
                    self.set_target_temperature(starting_temp)
                    print("Starting temperature is: " + str(starting_temp) + "°C")
                    is_starting_temp_set = True
                except ValueError:
                    print("Invalid input!")
                    continue
            # TODO: display manual roasting menu
            print("DEBUG: roaster is doing manual things")
