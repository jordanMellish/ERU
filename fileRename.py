"""File renaming script for Environmental Reconnaissance Unit"""

import os


def main():
    valid_input = False
    while not valid_input:
        print(""" Menu: 
            1) Change file details
            2) Commit filename changes
            3) Exit
            """)
        menu_selection = input(">>> ")
        if menu_selection == "1":
            new_filename = set_filename_details()
            print()
        elif menu_selection == "2":
            print("Committing changes menu....")
            file_source = get_file_source()
            starting_file_number = get_starting_number()
            commit_filename_changes(new_filename, file_source, starting_file_number)
        elif menu_selection == "3":
            exit()
        else:
            print("Incorrect selection entered, please enter either 1, 2 or 3")


def set_filename_details():
    # Get the location of the drone recon flight
    print("Please enter the location of the flight using the CamelCaps format i.e. BlackRiver not blackriver")
    location = input(">>> ")

    # Get the date of the drone recon flight w/ error checking
    print("please enter the date of the flight in this formate DDMMYY. i.e. 240719 = 24th July 2019")
    valid_date_input = False
    while not valid_date_input:
        date = input(">>> ")
        if not date.isdigit() or date.__len__() < 6:
            print("invalid input, please try again without any letters or symbols.")
        else:
            valid_date_input = True
            print("")

    # Get the drone used while flying the drone.
    print(""" Select Drone:
        1) MAIR - Mavic Air
        2) M210 - Matrice 210
        3) MMI2 - Mavic Mini 2
        4) SPRO - Swell Pro Splash Drone
        """)
    valid_drone_selection = False
    while not valid_drone_selection:
        drone_selection = input(">>> ")
        if drone_selection == "1":
            drone = "MAIR"
            valid_drone_selection = True
        if drone_selection == "2":
            drone = "M210"
            valid_drone_selection = True
        if drone_selection == "3":
            drone = "MMI2"
            valid_drone_selection = True
        if drone_selection == "4":
            drone = "SPRO"
            valid_drone_selection = True

    # Get the camera used while flying the drone.
    print(""" Select Camera:
    1) XT2 - Thermal camera for Matrice 210
    2) Z30 - Zoom camera for Matrice 210
    3) X5S - 5.7K camera for Matrice 210
    4) MSP - Multi Spectral Camera
    5) STK - Stock for Mavic Air, Mini 2 & Splash Drone
    """)
    valid_camera_selection = False
    while not valid_camera_selection:
        camera_selection = input(">>> ")
        if camera_selection == "1":
            camera = "XT2"
            valid_camera_selection = True
        elif camera_selection == "2":
            camera = "Z30"
            valid_camera_selection = True
        elif camera_selection == "3":
            camera = "X5S"
            valid_camera_selection = True
        elif camera_selection == "4":
            camera = "MSP"
            valid_camera_selection = True
        elif camera_selection == "5":
            camera = "STK"
            valid_camera_selection = True
        else:
            print("invalid input, enter either 1 , 2 , 3 , 4 or 5 ")

    # Return the filename to the function to be used for renaming the files.
    return "{}_{}_{}_{}_".format(location, date, drone, camera)


def commit_filename_changes(new_filename, file_source, starting_file_number):
    for file in os.listdir(file_source):
        source = file_source + file
        file_extension = "." + file.split('.')[-1]
        destination = new_filename + "{:03d}".format(starting_file_number) + file_extension
        destination = file_source + destination
        os.rename(source, destination)
        starting_file_number += 1


def has_numbers(string):
    return any(char.isdigit() for char in string)


def get_file_source():
    print("""Please enter file directory where the files that need sorting are located. 
            Also, please ensure that none of the folder names contain spaces. 
        """)
    file_source = input(">>>")
    formatted_source = file_source.replace(" ", "") + r"/"
    return formatted_source


def get_starting_number():
    print("""Enter the starting number for your files i.e. 1 will be represented as 001 in the file name""")
    starting_file_number = int(input(">>>"))
    return starting_file_number


main()
