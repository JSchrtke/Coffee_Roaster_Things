import ReferenceProfile
import LiveProfile


def main_menu(live_prof, ref_prof, temp_probe):
    """
    * live_prof: variable to store the live roast profile
    * ref_prof: variable to store the reference
    * temp_probe: an instance of a Phidget 1051 temperature sensor object

    This is the main roaster menu. User choices are:
    * 1: load reference profile: calls method that loads an existing profile
    * 2: start roast: calls method that starts the roast process
    * 3: exit program: raises SystemExit exception; this needs to be handled!
    """
    # define a variable that controls the menu loop
    is_menu_loop_running = True
    # create while loop that runs the menu
    while is_menu_loop_running is True:
        # show options to the user
        print("===== MAIN MENU =====")
        print("[1] Load reference profile")
        print("[2] Start roast")
        print("[3] Exit program")

        # get the user choice
        user_menu_choice = -1
        try:
            user_menu_choice = int(input(""))
        except ValueError:
            print("Invalid Input!")
            continue
        except EOFError:
            print("Oh no you dont!")
            continue

        # do the thing the user chose
        if user_menu_choice == 1:
            # set the variable for the reference profile to an instance of the RoastProfile class
            ref_prof = ReferenceProfile.ReferenceProfile()
            # get path to ref profile from user
            while True:
                try:
                    path_to_reference = input("Enter path to reference profile:\n")
                    break
                except EOFError:
                    print("Invalid input!")
                    continue
            # call import_profile method
            ref_prof.import_profile(path_to_reference)
        elif user_menu_choice == 2:
            # set the variable for the live roast to an instance of the RoastProfile class
            live_prof = LiveProfile.LiveProfile(temp_probe)
            # call start_roast() method from RoastProfile
            live_prof.do_roast(ref_prof)
        elif user_menu_choice == 3:
            raise SystemExit
        else:
            print("Invalid input!")
            continue
