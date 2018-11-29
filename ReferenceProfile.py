import csv
import RoastProfile


class ReferenceProfile(RoastProfile.RoastProfile):
    def __init__(self):
        # time storage list for later comparison
        self.time_values = []
        # temp storage list for later comparison
        self.temp_values = []
        # voltage value storage
        self.voltage_values = []
        super().__init__()

    def import_profile(self, path_):
        """Load roast profile data from specified path"""
        path = path_
        while True:
            try:
                # Opening the specified file
                # convert given path to string
                file_path = str(path)
                print("Loading " + file_path)
                # open the file at given filepath
                with open(file_path, "r") as file:
                    # creating the csv reader
                    csv_reader = csv.reader(file)
                    self.roast_data = list(csv_reader)

                # splitting the roast data up into the correspoding lists
                for data_tuple in self.roast_data:
                    # converting the data into floats
                    time_val = data_tuple[0]
                    time_val = float(time_val)
                    temp_val = data_tuple[1]
                    temp_val = float(temp_val)
                    voltage_val = data_tuple[2]
                    voltage_val = float(voltage_val)
                    # appending the values to the respective lists
                    self.time_values.append(time_val)
                    self.temp_values.append(temp_val)
                    self.voltage_values.append(voltage_val)

                # sanity check on if the two seperate data lists are still the same length
                if len(self.time_values) != len(self.temp_values):
                    raise ValueError
                break
            except FileNotFoundError:
                print("Invalid file path! Using default profile")
                path = "test.csv"
                continue

    def get_val_at_index(self, index, value_list):
        """Get the value from passed list at passed index"""
        return value_list[index]
