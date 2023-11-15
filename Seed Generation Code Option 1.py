import random 
def generate_random_seed(seed = None):
    if seed is None: #Generates a random seed if one isn't provided
        seed = random.randint(0, 10000)
        print(f"Generating random seed. Seed code: {seed}")
    else:
        print(f"Generating entered seed:{seed}")
    random.seed(seed) #sets the seed

random_number = random.random() #change this later

user_seed = input("Input a seed or leave black to use a random seed:  ")
result = generate_random_seed(int(user_seed) if user_seed else None)
print(f"A random number has been generated: {result}")