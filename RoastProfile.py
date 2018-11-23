import time
import sys


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
        # create variable to hold the temperature sensor
        self.sensor = temp_probe

    # create load_reference in RoastProfile class
    def load_reference(self, path):
        """
        Loads an existing roast profile to be used as a reference for another roast
        * path: The path to the roast profile to be used as reference
        """
        # TODO: figure out how this is supposed to work
        # open the file given
        with open(str(path)) as file:
            # read the contents line by line
            for line in file:
                # append the line read to the reference_data list
                self.reference_data.append(file.readline(1))
            # close the reference profile file
            file.close()
        print("DEBUG: RoastProfile.load_reference() was called; path: " + str(path))  # TODO: remove this once the method is done
        # TODO: DEBUG CODE, REMOVE ONCE DONE!
        for data in self.reference_data:
            print("DEBUG: Index: " + str(self.reference_data.index(data)) + " Data: " + str(data))

    def save_current_profile(self, data_list):
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
        name = input("Enter a name for the profile to be saved:\n")
        print("Saving profile...")
        # open path/ create file
        with open(path + name + ".txt", "w") as file:
            # TODO: for every datapoint in the data list, save it to the file into a new line
            for data_tuple in data_list:
                file.write(str(data_tuple))  # TODO: I think this is a really crude way of doing things, this needs some work
        file.close()
        print("Saved!")

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
        time_current = time_start - time.time()
        return time_current

    # TODO: create method to get current temperature
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
            # every second, do the following:
            while is_roast_finished is False:
                # create a variable that get's the time at loop start
                time_at_loop_start = time.time()
                # get the current time, store in it's variable
                self.time_current = self.get_time_since_start(self.time_start)
                print("DEBUG: self.time_current: " + str(self.time_current))
                # get the current temperature, store in it's variable
                self.temperature_current = self.get_current_temp()
                print("DEBUG: self.temperature_current: " + str(self.temperature_current))
                # TODO: find the closest time value in the reference profile to the current time value in the live roast
                    # TODO: create method to find the closest value to a given value in a list
                # TODO: compare it's temperature value to the current temperature in the live roast
                    # TODO: create a method to take to values and calculate the difference between them
                # TODO: calculate correction factor based on the temperature differential
                    # TODO: is the temp differenc between live and ref is larger than x, try to correct
                            # how big is x? make is so this can be set dynamically
                            # this is probably some lookup table, so use the method to find a close value to a given value for it
                # TODO: send correction factor to arduino
                    # TODO: create arduino interface
                # create time and temp tuple
                data_tuple = (self.time_current, self.temperature_current)
                # append time and temperature tuple to a list that will be used to later store the profile of the roast
                self.reference_data.append(data_tuple)
                # TODO: check if the current time is greater or equal than the biggest time value in the reference profile
                    # TODO: if yes, set a variable that is used to check if the roast is finished to true
                    # TODO: if no, repeat unitl it is
                # create variable that get's the time at loop end
                time_at_loop_end = time.time()
                # create mechanism to handle if the time at end is bigger than the time at
                # start + 1
                try:
                    # make loop wait by the difference to the start time + 1 second and the end time
                    time.sleep((time_at_loop_start + 1) - time_at_loop_end)
                except ValueError:
                    print("DEBUG: ValueError was raised at the end of"
                                     + " RoastProfile.start_roast while loop")
                    continue



                # TODO: DEBUG CODE, REMOVE ONCE DONE!
                is_roast_finished = True
                print("DEBUG: is_roast_finished = True")
                self.save_current_profile(self.reference_data)



            # if no:
        else:
            print("DEBUG: There is no reference profile")  # TODO: remove once rest is functional
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
