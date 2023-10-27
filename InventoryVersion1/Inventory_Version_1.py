class Item: 
    def __init__(self, name, description): 
        self.name = name 
        self.description = description 
        
class Inventory: 
    def __int__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)
        
    def list_items(self): 
        for i, item in enumerate(self.items, start=1):
            print(f"{i},{item.name}: {item.description}")
            
def main1():
    player_inventory = Inventory()
    
    while True: 
        print("\nInventory Menu:")
        print("1. Weapons List")
        print("2. Armor List")
        print("3. Ammo List")
        print("4. Health Items List")
        print("5. Currently Equipped List")
        print("6. Money")
        print("7. Add Items")
        print("8. Remove Items")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1": 
           if not player_inventory.items: 
               print("You have no weapons.")
        else:
            print("Weapons in your inventory:")
            player_inventory.list_items()
        if choice == "2":
            if not player_inventory.items:
                print("You have no armor.")
            else: 
                print("Armor in your inventory:")
                player_inventory.list_items()
        if choice == "3": 
            if not player_inventory.items:
                print("You have no ammo.")
            else: 
                print("Ammo in your inventory:")
                player_inventory.list_items()
        if choice == "4":
            if not player_inventory.items: 
                print("You have no health items.")
            else: 
                print("Health Items in your inventory:")
                player_inventory.list_items()
        if choice == "5":
            if not player_inventory.items:
                print("You have nothing equipped.")
            else:
                print("Items Equipped:")
                player_inventory.list_items()
        if choice == "6":
            if not player_inventory.items:
                print("You have no money.")
            else:
                print("Money Available:")
                player_inventory.list_items()
        if choice == "7":
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            item = Item(name, description)
            player_inventory.add_item(item)
            print(f"{name} has been added to your inventory.")
        if choice == "8":
            if not player_inventory.items: 
                print("Your inventory is empty.")
            else: 
                print("Items in your inventory: ")
                player_inventory.list_items()
                item_index = int(input("Enter the number of the item you wish to remove: ")) - 1
                if 0 <= item_index < len(player_inventory.items):
                    removed_item = player_inventory.items[item_index]
                    player_inventory.remove_item(removed_item)
                    print(f"{removed_item.name} has been removed from your inventory.")
                else:
                    print("The number you have entered is invalid.")
        if choice == "9":
            print("Leaving Inventory.")
            break
        else:
            print("The number you have chosen is invalid. Please try again.")
if __name__ == "__main__":
    main()
  
        
