from cgitb import lookup
from http.server import ThreadingHTTPServer
import os
import string
from InventoryVersion1 import Inventory_Version_1 #import inventory management inventory_version_1.py
import colorama
#Colorama is a way to highlight text color in the output console
from colorama import just_fix_windows_console
#'Fixes' windows and forces colored text to work
from colorama import init
from colorama import Fore   #ability for color change settings for objects...see 'settings'
import json

def display_title_screen():
    os.system("clear" if os.name == "posix" else "cls")  # Clear the screen

    title = """
_______  _______          _________          _______           _______ 
(  ____ )(  ___  )|\     /|\__   __/|\     /|(  ____ )|\     /|(  ____ \\
| (    )|| (   ) || )   ( |   ) (   | )   ( || (    )|| )   ( || (    \/
| (____)|| |   | || |   | |   | |   | |   | || (____)|| |   | || (_____ 
|     __)| |   | |( (   ) )   | |   ( (   ) )|     __)| |   | |(_____  )
| (\ (   | |   | | \ \_/ /    | |    \ \_/ / | (\ (   | |   | |      ) |
| ) \ \__| (___) |  \   /  ___) (___  \   /  | ) \ \__| (___) |/\____) |
|/   \__/(_______)   \_/   \_______/   \_/   |/   \__/(_______)\_______)
"""
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
    color_selection = """ Please choose a color for highlighted items.  (*Note: The default highlight color is Yellow).
    
    1. Blue
    2. Yellow
    3. Purple
    4. Red
    5. Green

    Enter 'exit' to go back to the main menu.
    """

    print(color_selection)

class Dagger:
    color_choice_weapons = Fore.YELLOW      #default object color set to YELLOW
    name = color_choice_weapons + 'small dagger'
    
smalldagger = Dagger()


def settings_screen():
     #uses ASCI codes to change colors...
     display_settings_screen()
     #for color_choice in ("Fore.BLUE", "Fore.YELLOW", "Fore.MAGENTA", "Fore.RED", "Fore.GREEN"):
     #color_choice = [Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.RED, Fore.GREEN]
     #color_list = [Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.RED, Fore.GREEN]
     for color_choice in [Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.RED, Fore.GREEN]:
         while True:
            choice = input("Make your choice: ")

            if choice == '1':
                #color = open("save.txt", 'w').write('0')
                #color_choice=data['highlight_color']
                data.update({'highlight_color': Fore.BLUE})
                print(Fore.BLUE + 'Highlight color changed to Blue')
                setattr(Dagger, 'name', Fore.BLUE + 'small dagger')    #changes object color for smalldagger in demo...i dont even know why this works but it does and it took me 8 hours
                print(Fore.RESET)   #resets color of text in console back to white...object color is set, however

            elif choice == '2':
                data.update({'highlight_color': Fore.YELLOW})
                print(Fore.YELLOW + 'Highlight color changed to Yellow')
                setattr(Dagger, 'name', Fore.YELLOW + 'small dagger')
                print(Fore.RESET)

            elif choice == '3':
                data.update({'highlight_color': Fore.MAGENTA})
                print(Fore.MAGENTA + 'Highlight color changed to Purple')
                setattr(Dagger, 'name', Fore.MAGENTA + 'small dagger')
                print(Fore.RESET)

            elif choice == '4':
                data.update({'highlight_color': Fore.RED})
                print(Fore.RED + 'Highlight color changed to Red')
                setattr(Dagger, 'name', Fore.RED + 'small dagger')
                print(Fore.RESET)
           
            elif choice == '5':
                data.update({'highlight_color': Fore.GREEN})
                print(Fore.GREEN + 'Highlight color changed to Green')
                setattr(Dagger, 'name', Fore.GREEN + 'small dagger')
                print(Fore.RESET)

            elif choice == 'go back':
                main()

            else:
                print("Invalid input.  Please choose a highlight color from the list.")
     
color_choice = [Fore.BLUE, Fore.YELLOW, Fore.MAGENTA , Fore.RED, Fore.GREEN]

data = {
    'checkpoint': 0,
    'complete inventory': Inventory_Version_1.Inventory,
    'weapons': Inventory_Version_1.InventoryWeapons,
    'armor': Inventory_Version_1.InventoryArmor,
    'ammo': Inventory_Version_1.InventoryAmmo,
    'health items': Inventory_Version_1.InventoryHealthItems,
    'currently equipped': Inventory_Version_1.InventoryCurrentlyEquipped,
    'money': Inventory_Version_1.InventoryMoney,
    'highlight_color': Fore.YELLOW
    }

def main():
    #automatically goes to title screen from main() function
    main_menu()

    choice = input()
    if choice == 'exit game':
        print("Saving the game...")
    checkpoints = [start, startpath, startpath_object, startpath_continue, crossroads, crossroads_left, crossroads_left1, crossroads_left2, crossroads_left3]

def load_game():
    #data = {
    #'checkpoint': 0,
    #'complete inventory': Inventory_Version_1.Inventory,
    #'weapons': Inventory_Version_1.InventoryWeapons,
    #'armor': Inventory_Version_1.InventoryArmor,
    #'ammo': Inventory_Version_1.InventoryAmmo,
    #'health items': Inventory_Version_1.InventoryHealthItems,
    #'currently equipped': Inventory_Version_1.InventoryCurrentlyEquipped,
    #'money': Inventory_Version_1.InventoryMoney,
    #'highlight_color': Fore.YELLOW
    #}
    #this allows for the player to load their game from a save file
    checkpoints = [start, startpath, startpath_object, startpath_continue, crossroads, crossroads_left, crossroads_left1, crossroads_left2, crossroads_left3]
    #checkpoints are defined as places in the story or 'timeline' for the player to access...
    #this allows for the game to always know where the player is in the story
    color = [Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.RED, Fore.GREEN]
    

    try:
        with open('save.txt') as save_file:
            data = json.load(save_file)     #gets data from save file...
            Inventory_Version_1.Inventory = data.get("inventory")   #checks what items player had in save file
            Inventory_Version_1.InventoryWeapons = data.get("weapons")
            Inventory_Version_1.InventoryArmor = data.get("armor")
            Inventory_Version_1.InventoryAmmo = data.get("ammo")
            Inventory_Version_1.InventoryHealthItems = data.get("health items")
            Inventory_Version_1.InventoryCurrentlyEquipped = data.get("currently equipped")
            Inventory_Version_1.InventoryMoney = data.get("money")
            Dagger.color_choice_weapons = data.get("highlight_color")
            saved_checkpoint = data.get("checkpoint")   #checks where player was when they exited the game last
            checkpoints[saved_checkpoint]()     #puts player back at same 'checkpoint' they were in last
    except:
        start()

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
            load_game()

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

        if choice == 'random': #for demo playthrough
            #Will generate a random seed for the world the player will be in...however, this is currently for the demo
            print("Generating random seed...")
            print("Loading...")
            Inventory_Version_1.Inventory.clear
            start()
            
        elif choice == 'exit':
            main_menu()
            
        else:
            print("Generating world based on seed given...")
            print("Loading...")


def start():
    print("""       You are standing in the middle of the woods at night.  There is a full moon overhead casting a faint glow on the ground in front of you.  There are trees surrounding you in every direction and span far into the night.  However, there seems to be traces of a path to your right.  It doesn't look to have been walked on in a long time.""")
    #checkpoints = [start, startpath, startpath_object, startpath_continue, crossroads, crossroads_left, crossroads_left1, crossroads_left2, crossroads_left3]
    while True:     #Loop continuously
        choice = input()   #Get the input
        if choice in ("go on path", "go along path"):    #Correct responses...
            startpath()       #...break the loop
        elif choice == 'exit game':
            data.update({'checkpoint': 0})
            with open('save.txt', 'w') as save_file:
                json.dump(data,save_file)
            print("Saving the game...")
        elif choice == 'inventory':
            Inventory_Version_1.main1()     #Will access Inventory_Version_1 to show inventory options
        else:
            print('I do not understand that statement.')    #error control

def startpath():
    print("""       You walk along the path, careful to not trip on any rocks or limbs along the way.  You don't get very far before seeing an object lying on the ground, shining from the moonlight filtering through the trees.  You can't make out exactly what it is, though.""")

    while True:
        choice = input()
        if choice in ("pick up object", "pick up the object", "look at object", "look at the object"):
            startpath_object()
        elif choice == 'exit game':
            data.update({'checkpoint': 1})
            with open('save.txt', 'w') as save_file:
                json.dump(data,save_file)
            print("Saving the game...")
        elif choice == 'inventory':
            Inventory_Version_1.main1()
        else:
            print('I do not understand that statement.') 

def startpath_object():
    print("     You pick up the object and notice that it is a " + smalldagger.name)
    print("     \033[39m" + "The blade is slightly rusted, but otherwise seems to be in good condition.  The handle is tightly wrapped in what looks like some type of leather cloth.")
    global Inventory
    while True:
        choice = input()

        if choice in ("keep blade", "keep dagger", "keep knife", "take dagger", "take knife", "take blade"):
            print("     You take the " + "\033[33m" +  "small dagger" + "\033[39m" + " and hold it tightly in your hand.")  #ANSI codes implemented...change to yellow then back to white
            Inventory_Version_1.Inventory.append("Small Dagger")    #this adds the item to overall inventory list
            Inventory_Version_1.addToInventoryWeapons("Small Dagger")   #adds item to inventory under 'Weapons' list
            #this is currently hardcoded...to effectively be randomly generated, this will need to change so that there is a list of preconceived items associated with their respective types
            #e.g. if the player picked up a health item, one would need to code 'addToInventoryHealthItems'...would be better if program automatically assigned it
            #will work on this soon
            data.update({'complete inventory': Inventory_Version_1.Inventory})
            data.update({'weapons': Inventory_Version_1.InventoryWeapons})
            startpath_continue()
        elif choice in ("drop blade", "drop dagger", "drop knife", "leave dagger", "leave knife", "leave blade"):
            print("     You put the " + "\033[33m" +  "small dagger" + "\033[39m" + " back on the ground.")
            startpath_continue()
        elif choice in ("go down path", "continue", "go along path", "continue down path", "continue on path"):
            startpath_continue()
        elif choice == 'exit game':
            data.update({'checkpoint': 2})
            with open('save.txt', 'w') as save_file:
                json.dump(data,save_file)
            print("Saving the game...")
        elif choice == 'inventory':
            Inventory_Version_1.main1()
        else:
            print("I don't understand that statement.")

def startpath_continue():
     print("     You look around and see that the path still continues in front of you.  No other path is in sight and trees surround you.  The moonlight still filters through shining a faint light on the path ahead.")
     global Inventory
     while True:     
        choice = input() 
        if choice in ("go down path", "continue", "go along path", "continue down path", "continue on path"):   
            crossroads()
        elif choice == 'exit game':
            data.update({'checkpoint': 3})
            with open('save.txt', 'w') as save_file:
                json.dump(data,save_file)
            print("Saving the game...")
        elif choice == 'inventory':
            Inventory_Version_1.main1()
        else:
            print('I do not understand that statement.')

def crossroads():
    print("""       You continue to go along the path and eventually reach the center of a crossroads.  There are 3 paths in front of you: one to the left, one to the right, and one that seems to continue from the path you are on currently.  The middle section of the crossroads is a wide circle with a trash can sitting in the center.  There is a lamp post lighting the center of the crossroads.""")
    
    while True:
        choice = input()

        if choice in ("go to trashcan", "go to trash can"):
            print("""       You are now standing right in front of the trash can.""")
        elif choice in ("look inside trashcan", "look inside trash can", "look inside the trashcan", "look inside the trash can", "look inside the trashcan"):
            print("     You look inside the trash can and see there is a single " + "\033[33m" +  "piece of paper" + "\033[39m" + "  at the bottom")
        elif choice in ("get paper", "get the paper", "get piece of paper", "get the piece of paper", "pick up paper", "pick up the paper", "pick up the piece of paper", "pick up piece of paper"):
            print("     You pick up the " + "\033[33m" +  "piece of paper" + "\033[39m" + " and are able to read it from the light above." + 
                  """It reads: 
                        Welcome to (INSERT GAME NAME HERE)!  In this game, you will find there are many paths to go on.  There is no right or wrong way to play this game.  While one path might lead to something incredible, 
                        another could lead to your demise.  Be cautious.  There are several others in this world, but not all will be friendly.  Be prepared for anything.""")
        elif choice in ("go on left path", "go down left path"):
            crossroads_left()   #demo 1 playthrough...code others in phase 2
        elif choice in ("go on right path", "go down right path"):
            crossroads_right()
        elif choice in ("go forward", "go down same path", "go on same path", "continue on same path", "continue down same path"):
            crossroads_forward()
        elif choice == 'exit game':
            data.update({'checkpoint': 4})
            with open('save.txt', 'w') as save_file:
                json.dump(data,save_file)
            print("Saving the game...")
        elif choice == 'inventory':
            Inventory_Version_1.main1()
        else:
            print("I don't understand that statement.")

def crossroads_left():
    print("""       You go down the path to your left, leaving the crossroads behind you.  Eventually, the light from the crossroads becomes faint.  The path in front of you is almost invisible from the pitch black darkness all around.  Suddenly, a growling sound can be heard from in front of you, though you cannot see what is making the sound.""")
       
    while True:
        choice = input()

        if choice in ("keep going forward", "go forward", "continue forward", "keep going"):
            crossroads_left1()
        elif choice in ("turn around", "turn back"):
            print("     You are turned around with the growling still menacingly continuing behind you.")
        elif choice in ("go back to crossroads", "go to crossroads", "return to crossroads"):
            print("""       You turn around and go back to the crossroads that you can barely make out in the dark from walking so far from it.  The growling continues behind you, but it eventually becomes faint.  Soon you are back at the crossroads.""")
            crossroads()
        elif choice in ("fight", "attack", "kill"):
            print("     What do you want to fight with?")
            #add option to user for accessing inventory to attack...
            #print("Items in your inventory: ")
            #player_inventory.list_items()
        elif choice == 'exit game':
            data.update({'checkpoint': 5})
            with open('save.txt', 'w') as save_file:
                json.dump(data,save_file)
            print("Saving the game...")
        elif choice == 'inventory':
            Inventory_Version_1.main1()
        else:
            print("I don't understand that statement.")

def crossroads_left1():
    print("""       You slowly move forward towards the growling which has gotten significantly louder and more menacing now.  After a few steps, you can start to make out what seems to be a wolf-like creature in the dark.  Glowing yellow eyes are faint, but seem to be staring right into your soul.  The creature's growling starts to hurt your ears as it increases in volume.""")

    while True:
        choice = input()

        if choice in ("keep going forward", "go forward", "continue forward", "keep going"):
            crossroads_left2()
        elif choice in ("turn around", "turn back"):
            print("     You are turned around with the growling still menacingly continuing behind you.")
        elif choice in ("go back to crossroads", "go to crossroads", "return to crossroads"):
            print("""       You turn around and go back to the crossroads that you can barely make out in the dark from walking so far from it.  The growling continues behind you, but it eventually becomes faint.  Soon you are back at the crossroads.""")
            crossroads()
        elif choice in ("fight", "attack", "kill"):
            print("     What do you want to fight with?")
            #add option to user for accessing inventory to attack...
            #print("Items in your inventory: ")
            #player_inventory.list_items()
        elif choice == 'exit game':
            data.update({'checkpoint': 6})
            with open('save.txt', 'w') as save_file:
                json.dump(data,save_file)
            print("Saving the game...")
        elif choice == 'inventory':
            Inventory_Version_1.main1()
        else:
            print("I don't understand that statement.")

def crossroads_left2():
    print("""       You continue to move forward towards the creature still growling.  You only get three steps further before the creature suddenly lunges forward at you.  Fangs sink down into your right arm as the creature bites down hard.  Seeing it clearly, you now know it is a large black wolf.  The pain causes you to scream out in pain.  Blood is now all over your arm and falling to the forest floor.  The wolf continues to hold his grip on your arm and shows no signs of letting go.""")

    while True:
        choice = input()

        if choice in ("attack", "fight", "attack the wolf", "fight the wolf"):
            crossroads_left3()
        elif choice in ("run away", "run", "leave"):
            print("You try to get away from the wolf, but it is futile.  It continues to bite down even harder than before.  More blood continues to pool around its mouth")
        elif choice == 'exit game':
            data.update({'checkpoint': 7})
            with open('save.txt', 'w') as save_file:
                json.dump(data,save_file)
            print("Saving the game...")
        elif choice == 'inventory':
            Inventory_Version_1.main1()
        else:
            print("I don't understand that statement.")

def crossroads_left3():
    print("What do you want to attack the wolf with?")

    while True:
        choice = input()

        #incorporate inventory management and options...list any available weapons

def objects():
    weapons = [small_dagger]

    for weapons in objects():
        color_choice = color_choice
    

if __name__ == "__main__":
    main()

checkpoints = [start, startpath, startpath_object, startpath_continue, crossroads, crossroads_left, crossroads_left1, crossroads_left2, crossroads_left3]

def load_game():
    try:
        saved_checkpoint = int(open("save.txt").read())
        checkpoints[saved_checkpoint]()
    except FileNotFoundError:
        start()