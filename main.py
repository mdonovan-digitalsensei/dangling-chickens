class Player:
  def __init__(self,name,role,health,attack):
    self.name = name
    self.role = role
    self.plevel = 0
    self.health = health
    self.attack = attack
  def return_name(self):
    return self.name
  def return_role(self):
    return self.role
  def return_level(self):
    return self.plevel
  def return_health(self):
    return self.health
  def return_attack(self):
    return self.attack
    
class player_role:
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

role = [["cadet",5,1],["recruit",10,2]]


new_game = Game()
new_game.setup()

print("Input your heroes name: ")
player_name = input("name: ")

nobody = Player(player_name,role[0][0],role[0][1],role[0][2])

while True:
  print(f"{nobody.return_name()} you are a {nobody.return_role()}")
  print(f"Current Health: {nobody.return_health()}")
  print(f"Current Attack: {nobody.return_attack()}")
  print(f"Current Game Turn {new_game.return_turn()} you are on level {new_game.return_level()}")
  print("Type q to quit any other to continue")
  end_game = input()

  if end_game == "q":
    print("End Game")
    break
  else:
    new_game.increment_turn()    
