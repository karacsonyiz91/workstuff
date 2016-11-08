import csv
import collections
from collections import OrderedDict


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = [
    'gold coin',
    'dagger',
    'gold coin',
    'gold coin',
    'ruby',
    'dragon meat']

def options():

    opt1 = "I : inventory"
    opt2 = "P : sort your inventory"
    opt3 = "L : adding loot"
    opt4 = "S : save inventory"
    opt5 = "X : exit"

    print(opt1)
    print(opt2)
    print(opt3)
    print(opt4)
    print(opt5)

def display_inventory(action):
    for j, i in inventory.items():
        print(i, " ", j)
    Items(inventory)
    print()

def print_table(inventory):
    sorting = input(str("Growing or Decreasing? (G/D): "))
    sorting = sorting[0].upper()
    if sorting == "D":
        orderSorted(inventory)
    elif sorting == "G":
        orderReversed(inventory)
    else:
        print("\nWrong command,returning to main menu...")

def add_to_inventory(inventory, addedItems):
    for j in dragonLoot:
        if j in inventory:
            inventory[j] = int(inventory[j]) + 1
        else:
            inventory.update({j: 1})                

def ShowSavedItems(inventory):
    Items = 0
    for i in inventory.values():
        if Items == 0:
            Items = i
        else:
            Items = int(Items)
            i = int(i)
            Items = Items + i
    print("Total items: ", Items)


def orderSorted(inv):
    keyLength = 0
    valueLength = 0
    inv_1 = OrderedDict(sorted(inv.items(), key=lambda t: t[1], reverse=True))
    for k1, v1 in inv_1.items():
        if valueLength < len(str(v1)):
            valueLength = len(str(v1))
        if keyLength < len(str(k1)):
            keyLength = len(str(k1))
    keyLength = int(keyLength)
    dashes = keyLength * 2 + valueLength * 2 + 10
    print(" " * 10, "Your inventory")
    print(" " * 10, "amount" + " " * keyLength + "items")
    print("-" * dashes)
    for k1, v1 in inv_1.items():
        a_v_len = (int(len(str(v1))))
        a_k_len = (int(len(str(k1))))
        frontspaces = (valueLength - a_v_len)
        spaces = (keyLength - a_k_len)
        print(" " * 10, " " * frontspaces, v1, " " * 5, " " * spaces, k1)
    print("-" * dashes)


def orderReversed(inv):
    keyLength = 0
    valueLength = 0
    inv_2 = OrderedDict(sorted(inv.items(), key=lambda t: t[1]))
    for k2, v2 in inv_2.items():
        if valueLength < len(str(v2)):
            valueLength = len(str(v2))
        if keyLength < len(str(k2)):
            keyLength = len(str(k2))
    keyLength = int(keyLength)
    dashes = keyLength * 2 + valueLength * 2 + 10
    print(" " * 10, "Your inventory")
    print(" " * 10, "amount" + " " * keyLength + "items")
    print("-" * dashes)
    for k2, v2 in inv_2.items():
        a_v_len = (int(len(str(v2))))
        a_k_len = (int(len(str(k2))))
        frontspaces = (valueLength - a_v_len)
        spaces = (keyLength - a_k_len)
        print(" " * 10, " " * frontspaces, v2, " " * 5, " " * spaces, k2)
    print("-" * dashes)


def export_inventory(inventory, filename):
    file = open(filename, "w")
    writer = csv.writer(open(filename, 'w'))
    writer.writerows(inventory.items())
    file.close()
    print("Your inventory has been saved.")
        
while True:
    action = (input("\nWhat do you want to do? (O:options) : "))
    action = action[0].upper()
    if action == "O":
        options()
    elif action == "P":
        print_table(inventory)
    elif action == "L":
        add_to_inventory(inventory, dragonLoot)
        print("Loot has been added to your stash.")
    elif action == "S":
        export_inventory(inventory, 'export_inventory.csv')
        ShowSavedItems(inventory)
    elif action == "I":
        print("This is your inventory:\n ")
        display_inventory(action)
    elif action == "X":
        quit()