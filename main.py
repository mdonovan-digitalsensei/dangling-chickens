import os
from random import seed
from random import randint
import readchar
import csv
import player
import monster
import inventory

clear = lambda: os.system('clear')  #on Linux System


class Player_role:
    def __init__(self, name, health, attack):
        pass

class Kill_list:
    def __init__(self):
        self.my_list = []

    def add_kill(self, monster):
        self.my_list.append(monster)

    def return_list(self):
        return self.my_list

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
    my_list = []
    with open(my_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            my_list.append(class_type(*row))
    return my_list


def serialise_list(my_file):
    my_list = []
    with open(my_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:            
            my_list.append(row)
    return my_list


role = [["cadet", 5, 3, 0], ["recruit", 10, 2, 0]]

weaponlist = serialise_list("weapons.csv")
itemslist = serialise_list("items.csv")
monsterlist = serialise_objects(monster.Monster, "monsters.csv")

new_game = Game()
new_game.setup()
seed(1)
mindex = 0
rindex = 0

player_inv = inventory.Inventory()
kill_list = Kill_list()

print("Input your heroes name: ")
player_name = input("name: ")

nobody = player.Player(player_name, *role[rindex])
nobody.change_weapon(0,weaponlist)


while True:
    pwpn = nobody.return_weapon_name()
    pdmg = nobody.return_weapon_dmg()
    
    print(f"there are {len(monsterlist) - mindex} monsters left in list")

    if mindex >= len(monsterlist):
        print("No monsters left")
        print("You Killed: ")
        for kills in kill_list.return_list():
            print(kills)        
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
    action = readchar.readchar()

    if action == "q":
        print("End Game")
        break
    elif action == "i":
        clear()
        print("*** Inventory ***")
        for item in player_inv.list_items():
            print(f"You have {item[1]} {itemslist[item[0]][1]}")
        print("*** Inventory ***")
        print("---------------------")

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
            if monsterlist[mindex].return_alive() == False:
                print(f"The {monsterlist[mindex].return_name()} has died")
                kill_list.add_kill(monsterlist[mindex].return_name())
                mindex += 1
        else:
            print(
                f"The {monsterlist[mindex].return_name()} has damaged you! You have taken {monsterlist[mindex].return_dmg()}"
            )
            nobody.take_damage(monsterlist[mindex].return_dmg())
            print(f"You have {nobody.return_health()} health remaining")
            if nobody.return_health() <= 0:
                print(f"You have died")
                print("You Killed: ")
                for kills in kill_list.return_list():
                    print(kills)
                break
        print("---------------------")
        new_game.increment_turn()
    else:
        clear()
        print("Unkown Action")
