class RoastProfile():
    def __init__(self):
        # create variable that holds the starting time; init to -1
        self.time_start = -1
        # create variable that holds the current time; init to -1
        self.time_current = -1
        # create variable that holds the current temperature
        self.temperature_current = -1
        # create variable to store the target temperature of the roaster
        self.temperature_target = -1

    # create load_reference in RoastProfile class
    def load_reference(self, path):
        """
        Loads an existing roast profile to be used as a reference for another roast
        * path: The path to the roast profile to be used as reference
        """
        # TODO: figure out how this is supposed to work
        print("DEBUG: RoastProfile.load_reference() was called; path: " + str(path))

    def set_target_temperature(self, temp_value):
        """
        This method set's the roasters target temperature
        * temp_value: The value that should be the target temperature
        """
        self.temperature_target = temp_value

    # create start_roast method in RoastProfile
    def start_roast(self, ref_prof):
        """
        starts the roasting process, either with or without a reference profile
        """
        reference_profile = ref_prof
        # TODO: finish this method
        # check if there is a reference profile
            # TODO: if yes:
        if reference_profile is type(self):
            print("DEBUG: There is a reference profile\nDEBUG: roaster is doing things automatically")  # TODO: remove once rest is functional
                # TODO: set the variable that holds the starting time to the time now
                # TODO: every second, do the following:
                    # get the current time, store in it's variable
                    # get the current temperature, store in it's variable
                    # find the closest time value in the reference profile to the current time value in the live roast
                        # TODO: create method to find the closest value to a given value in a list
                    # compare it's temperature value to the current temperature in the live roast
                        # TODO: create a method to take to values and calculate the difference between them
                    # calculate correction factor based on the temperature differential
                        # is the temp differenc between live and ref is larger than x, try to correct
                            # how big is x? make is so this can be set dynamically
                        # this is probably some lookup table, so use the method to find a close value to a given value for it
                    # send correction factor to arduino
                        # TODO: create arduino interface
                    # append time and temperature to a list that will be used to later store the profile of the roast
                    # check if the current time is greater or equal than the biggest time value in the reference profile
                        # if yes, set a variable that is used to check if the roast is finished to true
                        # if no, repeat unitl it is
            # TODO: if no:
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
