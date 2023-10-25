from http.server import ThreadingHTTPServer
import os
import colorama
#Colorama is a way to highlight text color in the output console
from colorama import just_fix_windows_console
just_fix_windows_console()
#'Fixes' windows and forces colored text to work

def display_title_screen():
    os.system("clear" if os.name == "posix" else "cls")  # Clear the screen

    title = """ 
   ____              _ _   _       _        ____        _
  / ___|  __ _ _ __ (_) | | |_   _| |      / ___|  __ _| | _____
  \___ \ / _` | '_ \| | | | | | | | |     | |  _ / _` | |/ / _ \\
   ___) | (_| | | | | | | | |_| | | |___  | |_| | (_| |   <  __/
  |____/ \__,_|_| |_|_|_|  \__,_| |_____|  \____|\__,_|_|\_\___|
    """ #change this later!!!!!!
    menu = """
    1. Start New Game
    2. Load Saved Game
    3. Settings
    4. Exit Game
    """

    print(title)
    print(menu)

def display_new_game_screen():
    #asks player if they want to enter a custom seed or use a pregenerated random seed for their new game
    os.system("clear" if os.name == "posix" else "cls")  # Clear the screen

    seed_selection = """
    Enter a custom seed.  Alternatively, type 'random' for a random seed.  Enter 'exit' to go back to the main menu.
    """

    print(seed_selection)

def display_settings_screen():
    #displays all available color choices player can choose from before starting their game
    color_choice = """ Please choose a color for highlighted items.  (*Note: The default highlight color is Yellow).
    
    1. Blue
    2. Yellow
    3. Purple
    4. Red
    5. Green

    Enter 'exit' to go back to the main menu.
    """

    print(color_choice)



def main():
    #automatically goes to title screen from main() function
    main_menu()
    
def main_menu():
    #the title screen
    display_title_screen()

    while True:
        choice = input("Make Your Choice (1/2/3/4): ")
        
        if choice == '1':
            # Allows player to either a) enter a custom seed or b) use a pregenerated random seed in order to create the world and start the game
            new_game_screen()
            
        elif choice == '2':
            # Loads last saved game
            print("Loading a saved game...")
            
        elif choice == '3':
            # Allows player to change different settings (includes: highlight color)
            settings_screen()
            
        elif choice == '4':
            # Exits the game
            print("Exiting the game...")
            
        else:
            # Error control...
            print("Invalid choice. Please select a valid option (1/2/3/4).")

def new_game_screen():
    display_new_game_screen()

    while True:
        choice = input()

        if choice == 'random':
            #Will generate a random seed for the world the player will be in
            print("Generating random seed...")
            print("Loading...")
            display_random_seed_screen_start()
            
        elif choice == 'exit':
            main_menu()
            
        else:
            print("Generating world based on seed given...")
            print("Loading...")

def display_random_seed_screen_start():
    print("""You are standing in the middle of the woods at night.  There is a full moon overhead casting a faint glow on the ground in front of you.
      There are trees surrounding you in every direction and span far into the night.  However, there seems to be traces of a path to your right.  It doesn't look to have been walked on in a long time.""")

    while True:
        choice = input()

        if choice == 'go to the right' or 'go to right' or 'go on path' or 'go along path':
            display_random_seed_screen_path_start() #displays next set of options...these are set as different def values to help follow where exactly user is...will help for 'path timeline' user story later

        elif choice == 'go to path':
            print("It's here!")

        else:
            print("I don't understand that statement.")  #Will need revisions later for 'user error control system' user story...

def display_random_seed_screen_path_start():
    print("""You walk along the path, careful to not trip on any rocks or limbs along the way.  You eventually reach the center of a crossroads.  There are 3 paths in front of you: one to the left, one to the right, and one that seems to continue from the path you are on currently.
    The middle section of the crossroads is a wide circle with a trash can sitting in the center.  There is a lamp post lighting the center of the crossroads.""")

    while True:
        choice = input()

        if choice == 'go to trashcan' or 'go to trash can':
            print("""You are now standing right in front of the trash can.""")

        elif choice == 'look inside trashcan' or 'look inside trash can' or 'look inside the trashcan' or 'look inside the trash can' or 'look inside the trashcan':
            print("""You look inside the trash can and see there is a single piece of paper at the bottom""")

        elif choice == 'get paper' or 'get the paper' or 'get piece of paper' or 'get the piece of paper' or 'pick up paper' or 'pick up the paper' or 'pick up the piece of paper' or 'pick up piece of paper':
            print("""You pick up the piece of paper and are able to read it from the light above.  It reads: 
            Welcome to (INSERT GAME NAME HERE)!  In this game, you will find there are many paths to go on.  There is no right or wrong way to play this game.  While one path might lead to something incredible, another could lead to your demise.
            Be cautious.  There are several others in this world, but not all will be friendly.  Be prepared for anything.
            """)

        elif choice == 'go on left path' or 'go down left path':
            display_random_seed_screen_crossroads_left()

        elif choice == 'go on right path' or 'go down right path':
            display_random_seed_screen_crossroads_right()

        else:
            print("I don't understand that statement.")

def settings_screen():
    #uses ASCI codes to change colors...
     display_settings_screen()
     while True:
        choice = input("Make your choice: ")

        if choice == '1':
            print("Highlight color changed to " + "\033[34m" + "Blue")

        elif choice == '2':
            print("Highlight color changed to " + "\033[33m" + "Yellow")

        elif choice == '3':
            print("Highlight color changed to " + "\033[35m" + "Purple")

        elif choice == '4':
            print("Highlight color changed to " + "\033[31m" + "Red")
            #The '\033[31m' ANSI statement changes the text after it to red
            #general 'red' color printing code: print('\033[31m' + 'some red text')

        elif choice == '5':
            print("Highlight color changed to " + "\033[32m" + "Green")

        else:
            print("Invalid input.  Please choose a highlight color from the list.")

if __name__ == "__main__":
    main()


#Inventory Control