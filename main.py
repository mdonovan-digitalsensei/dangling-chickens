import os
from random import seed
from random import randint
import readchar
import csv
import player
import monster
import inventory
from killlist import Kill_list
from generate_map import Dungeon_map
from entities import Entity_List
from in_combat import in_combat

clear = lambda: os.system('clear')  #on Linux System

FLOOR_LEVELS = ("00","01","02","03","04","05")

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

def create_dungeon_floor_monster_list(monsters, entity):
    my_list = []
    temp_list=monsters.split(" ")
    monster_list=[]
    for m in temp_list:
        monster_list.append(m.split(","))
    
    for i in range(len(monster_list)):                    
        with open("data/monsters.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:                    
                if row[0][0] == monster_list[i][0]:
                    my_list.append(monster.Monster(*row))
                    my_list[-1].set_x(monster_list[i][1])
                    my_list[-1].set_y(monster_list[i][2])
                    entity.add(my_list[-1].return_x(),my_list[-1].return_y(),my_list[-1].return_mchar(),my_list[-1])
    return my_list

def bio():
    print(f"{nobody.return_name()} you are a {nobody.return_role()}")
    print(f"You are on level {dungeon_floor_level} in the {dungeon_floor_list[dungeon_floor_level][1]}")
    print(dungeon_floor_list[dungeon_floor_level][2])
    print(f"Current Health: {nobody.return_health()}")
    print(f"Current Attack: {nobody.return_attack()}")
    print(f"Current Weapon: {pwpn}")
    print(
        f"Current Game Turn {new_game.return_turn()} you are on level {new_game.return_level()}"
    )

dungeon_map=Dungeon_map()
dungeon_floor_level = 1


entities = Entity_List()



role = [["cadet", 5, 3, 0], ["recruit", 10, 2, 0]]

weaponlist = serialise_list("data/weapons.csv")
itemslist = serialise_list("data/items.csv")
#monsterlist = serialise_objects(monster.Monster, "monsters.csv")
dungeon_floor_list = serialise_list("data/dungeonlevel.csv")


new_game = Game()
new_game.setup()
seed(1)
rindex = 0
dungeon_floor_cleared = False


player_inv = inventory.Inventory()
kill_list = Kill_list()

print("Input your heroes name: ")
player_name = input("name: ")

nobody = player.Player(player_name, *role[rindex], 2, 8)
nobody.change_weapon(0,weaponlist)

player_inv.add_item(0,1)

new_floor_load = True
use_stairs_up = False


while True:
    pwpn = nobody.return_weapon_name()
    pdmg = nobody.return_weapon_dmg()
   
    # this used to change the level when we were using the end of the monster list to generate things, most of this is probably unecessary now

    if new_floor_load == True:
        dungeon_map.generate_map_array(FLOOR_LEVELS[dungeon_floor_level])
        create_dungeon_floor_monster_list(dungeon_floor_list[dungeon_floor_level][3],entities)
        new_floor_load = False

    if use_stairs_up == True:
        if dungeon_floor_level < (len(dungeon_floor_list) - 1):
            dungeon_floor_level += 1
            new_floor_load = True
            print(dungeon_floor_list[dungeon_floor_level][3])                
                        
        elif dungeon_floor_level == (len(dungeon_floor_list) - 1):            
            print("All cleared")
            print("No monsters left")
            print("You Killed: ")
            for kills in kill_list.return_list():
                print(kills)        
            break              
        
    is_in_combat, combat_with_monster = in_combat(nobody.return_x(), nobody.return_y(), entities.return_list())
        
    # if is_in_combat == True we should lock the player in place and present a diffrent interface

    if is_in_combat == True:
        
        bio()
        print("------------------------------------")
        print("Stuck in combat")
        print(f"In combat with {combat_with_monster.return_name()}")
        print("Type q to quit")
        print("Type a to attack")
        for item in player_inv.list_items():
            if item[0] == 0:
                print ("Type h to heal")
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
        
        elif action == "h":
            nobody.heal_damage(5)
            player_inv.remove_item(0,1)
            print(f"You have healed, current health {nobody.return_health()} of {nobody.return_my_max_health()}")        

        elif action == "a":
            clear()

            # need to create a way better combat engine

            attackroll = nobody.attack()
            print(f"You perform an attack scoring a {attackroll}")
            monsterattackroll = randint(0, 6) + combat_with_monster.return_attack()
            print(
                f"The {combat_with_monster.return_name()} gets an attack roll of {monsterattackroll}"
            )
            if attackroll > monsterattackroll:
                print(f"You have damanged the {combat_with_monster.return_name()}")
                combat_with_monster.take_damage(pdmg)
                if combat_with_monster.return_alive() == False:
                    print(f"The {combat_with_monster.return_name()} has died")
                    if combat_with_monster.loot_drop():
                        temp_list = combat_with_monster.loot_drop()
                        player_inv.add_item(*temp_list)
                    kill_list.add_kill(combat_with_monster.return_name())
                    entities.remove(combat_with_monster)
                    
            else:
                print(
                    f"The {combat_with_monster.return_name()} has damaged you! You have taken {combat_with_monster.return_dmg()}"
                )
                nobody.take_damage(combat_with_monster.return_dmg())
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
        bio()        
        print("------------------------------------")
        dungeon_map.print_map(nobody.return_x(),nobody.return_y(), nobody.return_char(),entities.return_list())
        print("------------------------------------")
        print("Type q to quit")        
        for item in player_inv.list_items():
            if item[0] == 0:
                print ("Type h to heal")
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
        
        elif action == "h":
            nobody.heal_damage(5)
            player_inv.remove_item(0,1)
            print(f"You have healed, current health {nobody.return_health()} of {nobody.return_my_max_health()}")        

        elif action == "A":
            clear()
            dy = -1
            dx = 0
            nobody.move(dx,dy,entities.return_list(),dungeon_map.return_map_array())
            
        elif action == "B":
            clear()
            dy = 1
            dx = 0
            nobody.move(dx,dy,entities.return_list(),dungeon_map.return_map_array())
            
        elif action == "C":
            clear()
            dy = 0
            dx = 1
            nobody.move(dx,dy,entities.return_list(),dungeon_map.return_map_array())
            
        elif action == "D":
            clear()
            dy = 0
            dx = -1
            nobody.move(dx,dy,entities.return_list(),dungeon_map.return_map_array())        
            
        else:
            clear()
            print(f"{action} Unkown Action")
