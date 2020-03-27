import os
from random import seed
from random import randint
import csv
import player
import monster
import inventory

clear = lambda: os.system('clear')  #on Linux System

class Player_role:
    def __init__(self, name, health, attack):
        pass


class Game:
    def __init__(self):
        self.turn = int
        self.glevel = int
        pass

    def setup(self):
        self.turn = 0
        self.glevel = 0

    def increment_turn(self):
        self.turn = self.turn + 1

    def return_turn(self):
        return self.turn

    def return_level(self):
        return self.glevel

def serialise_objects(class_type, my_file):    
    my_list=[]
    with open(my_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)
            my_list.append(class_type(*row))
    return my_list

def serialise_list(my_file):    
    my_list=[]
    with open(my_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)
            my_list.append(row)
    return my_list

role = [["cadet", 5, 3, 0], ["recruit", 10, 2, 0]]
weaponlist = serialise_list("weapons.csv")
itemslist = serialise_list("items.csv")

monsterlist = serialise_objects(monster.Monster,"monsters.csv")

new_game = Game()
new_game.setup()
seed(1)
mindex = 0
rindex = 0

player_inv = inventory.Inventory()
player_inv.add_item(0, 1)

player_inv.add_item(0, 1)

player_inv.add_item(0, 1)

print("Input your heroes name: ")
player_name = input("name: ")

nobody = player.Player(player_name, role[rindex][0], role[rindex][1], role[rindex][2],
                role[rindex][3])

while True:
    pwpn = weaponlist[nobody.return_weapon()][1]
    pdmg = weaponlist[nobody.return_weapon()][2]

    print(f"there are {len(monsterlist) - mindex} monsters left in list")

    if mindex >= len(monsterlist):
        print("No monsters left")
        break

    print(f"{nobody.return_name()} you are a {nobody.return_role()}")
    print(f"Current Health: {nobody.return_health()}")
    print(f"Current Attack: {nobody.return_attack()}")
    print(f"Current Weapon: {pwpn}")
    print(
        f"Current Game Turn {new_game.return_turn()} you are on level {new_game.return_level()}"
    )

    print(f"You are facing a {monsterlist[mindex].return_name()}")

    print("Type q to quit any other to continue")
    print("Type q to quit")
    print("Type a to attack")
    print("Type i to view inventory")
    action = input()

    if action == "q":
        print("End Game")
        break
    elif action == "i":
        print("*** Inventory ***")
        for item in player_inv.show_items():
            itemName = itemslist[item[0]][1]
            itemNumber = item[1]
            print(f"You have {itemNumber} {itemName}")
        print("*** Inventory ***")

    elif action == "a":
        clear()
        attackroll = nobody.attack()
        print(f"You perform an attack scoring a {attackroll}")
        monsterattackroll = randint(0, 6) + monsterlist[mindex].return_attack()
        print(
            f"The {monsterlist[mindex].return_name()} gets an attack roll of {monsterattackroll}"
        )
        if attackroll > monsterattackroll:
            print(f"You have damanged the {monsterlist[mindex].return_name()}")
            monsterlist[mindex].take_damage(pdmg)
            if monsterlist[mindex].return_health() <= 0:
                print(f"The {monsterlist[mindex].return_name()} has died")
                mindex += 1
        else:
            print(
                f"The {monsterlist[mindex].return_name()} has damaged you! You have taken {monsterlist[mindex].return_dmg()}"
            )
            nobody.take_damage(monsterlist[mindex].return_dmg())
            print(f"You have {nobody.return_health()} health remaining")
            if nobody.return_health() <= 0:
                print(f"You have died")
                break
        new_game.increment_turn()
    else:
        clear()
        print("Unkown Action")
