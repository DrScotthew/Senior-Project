import random 

def random_seed():
    return random.randit(1000,9999) #Code will create a seed between these to numbers

def main(): 
    user_input = input("Do you want to input a seed? (y/n): ").lower()

    if user_input == 'y':
        seed = input("Put the seed value as an integer here: ")
        try: 
            seed = int(seed)
            random.seed(seed)
            print(f"The seed {seed} has been added to the game.")
        except ValueError: 
            print(f"The seed that has been entered is invalid. The seed for this game will be randomly generated")
            seed = random_seed(seed)
            random.seed(seed)
            print(f"The seed {seed} will be used.")
    else: 
        seed = random_seed()
        random.seed(seed)
        print(f"The seed {seed} will be used.")

    