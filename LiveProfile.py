import time
import csv
import os
import RoastProfile
import ReferenceProfile
import ArduinoInterface
from get_closest_in_list import get_closest_in_list as get_index


class LiveProfile(RoastProfile.RoastProfile):
    def __init__(self, temp_probe=None):
        self.temperature_current = -1
        self.temperature_target = -1
        # create variable that holds the temperature sensor
        self._sensor = temp_probe
        if self._sensor:
            self.temperature_current = self._sensor.getTemperature()
        super().__init__()

    def export_profile(self, data):
        """Save profile to file"""

        # get path and name from user and create file path name to open
        while True:
            try:
                path = input("Enter the folder path:\n")
                name = input("Enter file name:\n")
            # in case the user is trying to be clever
            except EOFError:
                print("Oh no you dont!")
                continue
            file_path_name = os.path.join(path, name)
            break

        # open file at specified path
        while True:
            print("Saving profile...")
            try:
                # empty newline in the args is there to prevent extra /r
                with open(file_path_name, "w", newline="") as file:
                    # creating csv writer
                    _csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
                    _csv_writer.writerows(data)
                print("Saved!")
                break
            # Invalid path given by user
            except FileNotFoundError:
                path = os.path.abspath(os.path.expanduser("~/Desktop"))
                name = str(time.strftime("%Y%m%d%H%M%S", time.localtime())) + ".csv"
                file_path_name = os.path.join(path, name)
                print("Error! Invalid file path or name! Saving to desktop as " + name)
                continue

    def set_temp_current(self):
        """set self.temperature_current to temp"""
        self.temperature_current = self._sensor.getTemperature()

    def get_temp_current(self):
        """return self.temperature_current"""
        return self.temperature_current

    def set_temp_target(self, value):
        """set the target temperature roaster to passed value"""
        self.temperature_target = value

    def get_temp_target(self):
        """return the target temperature"""
        return self.temperature_target

    def compare_current_to_target_temp(self, reference_profile):
        """compare the current temp to target temp, return correction voltage"""
        ref = reference_profile
        # calculate the difference between current and target
        temp_target = self.get_temp_target()
        temp_current = self.get_temp_current()
        temp_diff_abs = abs(temp_target - temp_current)

        # check if the difference is to big
        # difference is too big
        if temp_diff_abs > 0.25:
            # get the voltage associated with the target temp and return it
            temp_target_index = get_index(temp_target, ref.temp_values)
            voltage = ref.get_val_at_index(temp_target_index, ref.voltage_values)
            return voltage
        # difference is small enough
        else:
            # do nothing
            pass

    def do_preheat(self, value):
        """preheat the roaster to passed value"""
        self.set_temp_target(value)
        self.set_temp_current()
        print("Preheating...")
        while True:
            if self.temperature_current < self.temperature_target:
                self.set_temp_current()
                print("Target temperature: " + str(self.temperature_target	)
                      + "\tCurrent temperature: " + str(self.temperature_current), end="\r")
                continue
            else:
                break
        while True:
            try:
                input("\nPreheating done! Press Enter to continue!\n")
                break
            except EOFError:
                print("No!")
                continue

    def do_roast(self, reference_profile=None):
        # TODO: both reference and manual mode need check if there is a reference profile; if there isn't you should load some default profile
        """start the roasting process"""
        # ask user which mode to run
        while True:
            try:
                mode = input("[R] Reference mode\n[M] Manual mode\n")
                mode = str(mode)
                break
            except EOFError:
                print("Invalid input!")
                continue

        # reference mode
        if mode == "R" or mode == "r":
            print("Starting roaster in reference mode...")
            # preheating
            # getting the first temperature value out of the reference profile
            self.set_temp_target(reference_profile.temp_values[0])
            self.do_preheat(self.temperature_target)

            # every second, do:
            is_roast_finished = False
            time_at_roast_start = time.time()
            while is_roast_finished is False:
                time_at_loop_start = time.time()

                # update the current temp
                self.set_temp_current()

                # get the index of the time closest to now from reference
                time_in_roast_now = time.time() - time_at_roast_start
                time_now_index = get_index(time_in_roast_now, reference_profile.time_values)
                # end roast
                if time_now_index == -1:
                    is_roast_finished = True
                    time_now_index = len(reference_profile.time_values) - 1

                # set the target temp to the temp in reference corresponding with now
                target_temp_index = time_now_index
                target_temp = reference_profile.get_val_at_index(target_temp_index,
                                                                 reference_profile.temp_values)
                self.set_temp_target(target_temp)

                # compare the target temp to the current temp and get the target voltage for roaster
                target_voltage = self.compare_current_to_target_temp(reference_profile)

                # set the heating voltage to voltage corresponding to target temp
                ArduinoInterface.ArduinoInterface.set_heating_voltage(target_voltage)

                # get time, temp and voltage and append it to the data list
                temp = self.get_temp_current()
                voltage = ArduinoInterface.ArduinoInterface.get_heating_voltage()
                data_tuple = time_in_roast_now, temp, voltage
                self.roast_data.append(data_tuple)

                # print the relevant data
                print("Current time: " + str(round(time_in_roast_now, 1)) + "s"
                      + "\tCurrent temperature: " + str(temp) + "°C"
                      + "\tTarget temperature: " + str(target_temp) + "°C"
                      + "\tCurrent voltage: " + str(voltage) + "V"
                      + "\t Target Voltage: " + str(target_voltage) + "V",
                      end="\r")

                # making the loop sleep for a second
                time_at_loop_end = time.time()
                time.sleep(1 - (time_at_loop_end - time_at_loop_start))

        # manual mode
        elif mode == "M" or mode == "m":
            print("Starting roaster in manual mode...")
            # preheating
            # get preheat value from user
            while True:
                try:
                    temp_target = input("Enter value to preheat to (°C):\n")
                    temp_target = float(temp_target)
                    self.set_temp_target(temp_target)
                    break
                except EOFError:
                    print("Invalid input")
                    continue
            self.do_preheat(self.temperature_target)

        # invalid user input for mode
        else:
            print("Invalid input! " + mode + " is not a valid mode!")

        # roast done, save data
        print("\n\nRoast finished!\n")
        self.export_profile(self.roast_data)
