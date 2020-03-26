import os
from random import seed
from random import randint

clear = lambda: os.system('clear') #on Linux System

class Player:
  my_name = str
  my_role = str
  my_plevel = int
  my_health = int
  my_attack = int
  my_weapon = int
  my_gold = int

  def __init__(self,name,role,health,attack,weapon):
    self.my_name = name
    self.my_role = role
    self.my_plevel = 0
    self.my_health = health
    self.my_attack = attack
    self.my_weapon = weapon
    self.my_gold = 0
    
  def return_name(self):
    return self.my_name
  def return_role(self):
    return self.my_role
  def return_level(self):
    return self.my_plevel
  def return_health(self):
    return self.my_health
  def return_attack(self):
    return self.my_attack
  def return_weapon(self):
    return self.my_weapon
  def attack(self):
    return randint(0,6) + self.my_attack
  def take_damage(self,dmg):
    self.my_health -= dmg
  def heal_damage(self,heal):
    self.my_health += heal
  
class Monster:
  my_name = str
  my_health = int
  my_attack = int
  my_dmg = int
  
  def __init__(self,name,health,attack,dmg):
    self.my_name=name
    self.my_health=health
    self.my_attack=attack
    self.my_dmg=dmg
  def return_name(self):
    return self.my_name
  def return_health(self):
    return self.my_health
  def return_attack(self):
    return self.my_attack
  def return_dmg(self):
    return self.my_dmg
  def take_damage(self,dmg):
    self.my_health -= dmg
  def heal_damage(self,heal):
    self.my_health += heal
  
class Player_role:
  def __init__(self,name,health,attack):
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

class Inventory:
  my_items = []
  def __init__(self):
    pass
  def add_item(self,index,number):
    i = 0
    if self.my_items:
      for item in self.my_items:
        if item[0]==index:
          self.my_items[i][1] += number
        else:
          self.my_items.append([index,number])
    else:
      self.my_items.append([index,number])
    
  def remove_item(self,index,number):
    i = 0
    for item in self.my_items:
      if item[0]==index:
        self.my_items[i][1] -= number
        if self.my_items[i][1] <= 0:
          del self.my_items[i]
          break

  def show_items(self):
    return self.my_items

role = [["cadet",5,3,0],["recruit",10,2,0]]
monsterlist = [Monster("goblin",2,1,1),Monster("imp",3,2,1)]
weaponlist = [[0,"knife",1],[1,"blunt short sword",2]]
itemslist = [[0,"Health Potion"],[1,"Nothing"]]

new_game = Game()
new_game.setup()
seed(1)
mindex = 0
rindex = 0

player_inv = Inventory()
player_inv.add_item(0,1)

player_inv.add_item(0,1)

player_inv.add_item(0,1)



print("Input your heroes name: ")
player_name = input("name: ")

nobody = Player(player_name,role[rindex][0],role[rindex][1],role[rindex][2],role[rindex][3])

while True:
  pwpn = weaponlist[nobody.return_weapon()][1]
  pdmg = weaponlist[nobody.return_weapon()][2]
  
  print(f"{nobody.return_name()} you are a {nobody.return_role()}")
  print(f"Current Health: {nobody.return_health()}")
  print(f"Current Attack: {nobody.return_attack()}")
  print(f"Current Weapon: {pwpn}")
  print(f"Current Game Turn {new_game.return_turn()} you are on level {new_game.return_level()}")

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
    monsterattackroll=randint(0,6) + monsterlist[mindex].return_attack()
    print(f"The {monsterlist[mindex].return_name()} gets an attack roll of {monsterattackroll}")
    if attackroll > monsterattackroll:
      print(f"You have damanged the {monsterlist[mindex].return_name()}")
      monsterlist[mindex].take_damage(pdmg)
      if monsterlist[mindex].return_health() <= 0:
        print(f"The {monsterlist[mindex].return_name()} has died")
        mindex += 1
    else:
      print(f"The {monsterlist[mindex].return_name()} has damaged you! You have taken {monsterlist[mindex].return_dmg()}")
      nobody.take_damage(monsterlist[mindex].return_dmg())
      print(f"You have {nobody.return_health()} health remaining")
      if nobody.return_health() <= 0:
        print(f"You have died")
        break
    new_game.increment_turn()    
  else:
    clear()
    print("Unkown Action")
    
