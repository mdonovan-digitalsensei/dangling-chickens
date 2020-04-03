import os
from random import seed
from random import randint
import readchar
import csv
import player
import monster
import inventory
from killlist import Kill_list

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

def create_dungeon_floor_monster_list(monsters):
    my_list = []
    for i in monsters:        
        if i != ' ':            
            with open("monsters.csv") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:                    
                    if row[0][0] == i:
                        my_list.append(monster.Monster(*row))
    return my_list

def print_map(my_level,x,y,player_char):
    my_map_file = "./maps/map_" + my_level + ".map"
    lx = x
    ly = y
    i = 0    
    print()
    with open(my_map_file) as map:  
        for row in map:            
            i += 1   
            if i == ly:
                row = list(row)          
                row[lx] = player_char                  
                row = "".join(row)
            print(f"{row}", end='')               

role = [["cadet", 5, 3, 0], ["recruit", 10, 2, 0]]

weaponlist = serialise_list("weapons.csv")
itemslist = serialise_list("items.csv")
#monsterlist = serialise_objects(monster.Monster, "monsters.csv")
dungeon_floor_list = serialise_list("dungeonlevel.csv")
dungeon_floor_level = 0

new_game = Game()
new_game.setup()
seed(1)
mindex = 0
rindex = 0
dungeon_floor_cleared = True
dungeon_floor_monsters = []

player_inv = inventory.Inventory()
kill_list = Kill_list()

print("Input your heroes name: ")
player_name = input("name: ")

nobody = player.Player(player_name, *role[rindex], 2, 8)
nobody.change_weapon(0,weaponlist)

player_inv.add_item(0,1)

while True:
    pwpn = nobody.return_weapon_name()
    pdmg = nobody.return_weapon_dmg()

    print(f"there are {len(dungeon_floor_monsters) - mindex} monsters left in list on floor")
    
    if mindex >= len(dungeon_floor_monsters):       
        if dungeon_floor_level < (len(dungeon_floor_list) - 1):
            dungeon_floor_level += 1
            dungeon_floor_monsters = []
            dungeon_floor_monsters = create_dungeon_floor_monster_list(list(dungeon_floor_list[dungeon_floor_level][3]))    
            mindex=0
        elif dungeon_floor_level == (len(dungeon_floor_list) - 1):            
            print("All cleared")
            print("No monsters left")
            print("You Killed: ")
            for kills in kill_list.return_list():
                print(kills)        
            break          
            
    print(f"{nobody.return_name()} you are a {nobody.return_role()}")
    print(f"You are on level {dungeon_floor_level} in the {dungeon_floor_list[dungeon_floor_level][1]}")
    print(dungeon_floor_list[dungeon_floor_level][2])
    print(f"Current Health: {nobody.return_health()}")
    print(f"Current Attack: {nobody.return_attack()}")
    print(f"Current Weapon: {pwpn}")
    print(
        f"Current Game Turn {new_game.return_turn()} you are on level {new_game.return_level()}"
    )

    print_map("01",nobody.return_x(),nobody.return_y(), nobody.return_char())

    print(f"You are facing a {dungeon_floor_monsters[mindex].return_name()}")

    print("Type q to quit any other to continue")
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

    elif action == "A":
        clear()
        dy = -1
        dx = 0
        nobody.move(dx,dy)
        print("UP")
        
    elif action == "B":
        clear()
        dy = 1
        dx = 0
        nobody.move(dx,dy)
        print("DOWN")
        
    elif action == "C":
        clear()
        dy = 0
        dx = 1
        nobody.move(dx,dy)
        print("RIGHT")
        
    elif action == "D":
        clear()
        dy = 0
        dx = -1
        nobody.move(dx,dy)
        print("LEFT")
        

    elif action == "a":
        clear()
        attackroll = nobody.attack()
        print(f"You perform an attack scoring a {attackroll}")
        monsterattackroll = randint(0, 6) + dungeon_floor_monsters[mindex].return_attack()
        print(
            f"The {dungeon_floor_monsters[mindex].return_name()} gets an attack roll of {monsterattackroll}"
        )
        if attackroll > monsterattackroll:
            print(f"You have damanged the {dungeon_floor_monsters[mindex].return_name()}")
            dungeon_floor_monsters[mindex].take_damage(pdmg)
            if dungeon_floor_monsters[mindex].return_alive() == False:
                print(f"The {dungeon_floor_monsters[mindex].return_name()} has died")
                if dungeon_floor_monsters[mindex].loot_drop():
                    temp_list = dungeon_floor_monsters[mindex].loot_drop()
                    player_inv.add_item(*temp_list)
                kill_list.add_kill(dungeon_floor_monsters[mindex].return_name())
                mindex += 1
        else:
            print(
                f"The {dungeon_floor_monsters[mindex].return_name()} has damaged you! You have taken {dungeon_floor_monsters[mindex].return_dmg()}"
            )
            nobody.take_damage(dungeon_floor_monsters[mindex].return_dmg())
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
        print(f"{action} Unkown Action")
