from random import randint


class Player:
    my_name = str
    my_role = str
    my_plevel = int
    my_health = int
    my_attack = int
    my_weapon = int
    my_gold = int
    my_weapon_dmg = int
    my_weapon_name = str
    my_weapon_idx = int
    is_engaged = False

    def __init__(self, name, role, health, attack, weapon, x, y):
        self.my_name = name
        self.my_role = role
        self.my_plevel = 0
        self.my_health = int(health)
        self.my_attack = int(attack)
        self.my_weapon = int(weapon)
        self.my_gold = 0
        self.my_weapon_dmg = 0
        self.my_weapon_name = str 
        self.my_max_health = int(health)
        self.my_icon = "@"
        self.y = x
        self.x = y

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

    def return_weapon_idx(self):
        return self.my_weapon_idx
    
    def return_weapon_name(self):
        return self.my_weapon_name

    def return_weapon_dmg(self):
        return self.my_weapon_dmg

    def return_my_max_health(self):
        return self.my_max_health

    def return_x(self):
        return self.x

    def return_y(self):
        return self.y

    def return_char(self):
        return self.my_icon

    def attack(self):
        return randint(0, 6) + self.my_attack

    def take_damage(self, dmg):
        self.my_health -= dmg

    def heal_damage(self, heal):
        self.my_health += heal
        if self.my_health > self.my_max_health:
            self.my_health = self.my_max_health


    def change_weapon(self, index, li):
        self.my_weapon_idx = index
        self.my_weapon_name = li[self.return_weapon_idx()][1]
        self.my_weapon_dmg = int(li[self.return_weapon_idx()][2])

    def move(self,x,y,entities,map_array):
        test_x = self.x + x
        test_y = self.y + y
        for entity in entities:
            if entity[0] == test_x and entity[1] == test_y:
                return entity[3]       
        if map_array[test_y - 1][test_x] == "x":
            return True

        self.x += x
        self.y += y
          