
def init():
    print("お知らせ：The game will be paused when you are in the inventory.")
    input("(Press enter to continue)")
    print(20 * "\n")
    print("Avaliable Inventory commands: \n get item <item> \n drop <item> \n show inventory \n exit inventory \n show items"); input("(Press enter to continue)")
    print(20 * "\n")


def inventory():
    items = ["food","water","rope","torch","sack","wood","iron","steel","ginger","garlic","fish","stone","wool"]

    inventory = {}
    userDesire = 1
    while userDesire == 1:
        action = input("what would you like to do?: ").strip().lower()
        actionSplit = action.split(" ", 1)
        if len(actionSplit) < 2:
            print("error: invalid input. please enter an action, followed by an item (if applicable). for example: <action> <item name>")
            continue
        userAction, item = actionSplit

        if userAction == "exit" and item == "inventory":
            print("exiting inventory")
            userDesire = 0

        elif userAction == "show" and item == "inventory":
            print(20 * "\n")
            if inventory:
                print("Your inventory contains the following items:")
                for i, (item_name, quantity) in enumerate(inventory.items(), 1):
                    print(f"{i}. {item_name} (Quantity: {quantity})")
            else:
                print("Your inventory is empty.")

        elif userAction == "get" and item in items:
            print(20 * "\n")
            if item in inventory:
                inventory[item] += 1
            else:
                inventory[item] = 1
            print(f"{item} x1 has been added to your inventory.")
        
        elif userAction == "drop" and item in inventory:
            print(20 * "\n")
            if inventory[item] > 1:
                inventory[item] -= 1
                print(f"you have dropped one {item} from your inventory.")
            else:
                del inventory[item]
                print(f"{item} has been removed from your inventory.")

        elif userAction == "show" and item == "items":
            print(20 * "\n")
            for item in items:
                print(f"{item}")
        
        elif userAction in ["get", "drop"]:
            print(20 * "\n")
            print(f"{item} is not a valid item or is not in your inbentory.")
        else:
            print("Invalid command. Please use \"get <item>\", \"drop <item>\", \"show items\", \"show inventory\", or \"exit inventory\".")

init()
inventory()


## del