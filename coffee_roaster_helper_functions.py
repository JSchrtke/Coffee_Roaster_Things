from RoastProfile import *


def main_menu(live_prof, ref_prof):
    """
    * live_prof: variable to store the live roast profile
    * ref_prof: variable to store the reference

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

        # do the thing the user chose
        if user_menu_choice == 1:
            # set the variable for the reference profile to an instance of the RoastProfile class
            ref_prof = RoastProfile()
            # call load_reference method; should be member of RoastProfile
            ref_prof.load_reference(1)
        elif user_menu_choice == 2:
            # set the variable for the live roast to an instance of the RoastProfile class
            live_prof = RoastProfile()
            # call start_roast() method from RoastProfile
            live_prof.start_roast(ref_prof)
        elif user_menu_choice == 3:
            raise SystemExit
        else:
            print("Invalid input!")
            continue
