from random import seed
from random import randint

class Player:
    my_name = str
    my_role = str
    my_plevel = int
    my_health = int
    my_attack = int
    my_weapon = int
    my_gold = int

    def __init__(self, name, role, health, attack, weapon):
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
        return randint(0, 6) + self.my_attack

    def take_damage(self, dmg):
        self.my_health -= dmg

    def heal_damage(self, heal):
        self.my_health += heal