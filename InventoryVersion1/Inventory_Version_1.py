#Inventory Management System (for demo)
#Full game will include lists of possible items that may appear in game when randomly generating seeds

from asyncio.windows_events import NULL

Inventory=[]
InventoryWeapons=[]
InventoryArmor=[]
InventoryAmmo=[]
InventoryHealthItems=[]
InventoryCurrentlyEquipped=[]
InventoryMoney=[]

def addToInventory(item):
    Inventory.append(item)

def addToInventoryWeapons(item):
    InventoryWeapons.append(item)

def showCompleteInventory():
    for i in Inventory:
        print(i)

def showWeapons():
    for i in InventoryWeapons:
        print(i)

def showArmor():
    for i in InventoryArmor:
        print(i)

def showAmmo():
    for i in InventoryAmmo:
        print(i)

def showHealthItems():
    for i in InventoryHealthItems:
        print(i)

def showCurrentlyEquipped():
    for i in InventoryCurrentlyEquipped:
        print(i)

def showMoney():
    for i in InventoryMoney:
        print(i)
            
def main1():
    
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
        print("9. Show All Inventory")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1": 
            if not InventoryWeapons:
                print("You have no weapons.")
                break
            else:
                print("Weapons in your inventory:")
                showWeapons()
                break
        elif choice == "2":
            if not InventoryArmor:
                print("You have no armor.")
                break
            else: 
                print("Armor in your inventory:")
                showArmor()
                break
        elif choice == "3": 
            if not InventoryAmmo:
                print("You have no ammo.")
                break
            else: 
                print("Ammo in your inventory:")
                showAmmo()
                break
        elif choice == "4":
            if not InventoryHealthItems: 
                print("You have no health items.")
                break
            else: 
                print("Health Items in your inventory:")
                showHealthItems()
                break
        elif choice == "5":
            if not InventoryCurrentlyEquipped:
                print("You have nothing equipped.")
                break
            else:
                print("Items Equipped:")
                showCurrentlyEquipped()
                break
        elif choice == "6":
            if not InventoryMoney:
                print("You have no money.")
                break
            else:
                print("Money Available:")
                showMoney()
                break
        elif choice == "7":
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            item = Item(name, description)
            Inventory.add_item(item)
            print(f"{name} has been added to your inventory.")
            break
        elif choice == "8":
            if not Inventory.items: 
                print("Your inventory is empty.")
                break
            else: 
                print("Items in your inventory: ")
                Inventory.list_items()
                item_index = int(input("Enter the number of the item you wish to remove: ")) - 1
                if 0 <= item_index < len(Inventory.items):
                    removed_item = Inventory.items[item_index]
                    Inventory.remove_item(removed_item)
                    print(f"{removed_item.name} has been removed from your inventory.")
                    break
                else:
                    print("The number you have entered is invalid.")
                    break
        elif choice == "9":
            if not Inventory: 
                print("You have no items.")
                break
            else:
                print("All items in your inventory:")
                showCompleteInventory()
                break
        elif choice == "0":
            print("Leaving Inventory.")
            break
        else:
            print("The number you have chosen is invalid. Please try again.")
  
        
