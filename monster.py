class Monster:
    my_name = str
    my_health = int
    my_attack = int
    my_dmg = int
    my_index = int
    my_loot = int

    def __init__(self, index, name, health, attack, dmg, loot):
        self.my_name = name
        self.my_health = int(health)
        self.my_attack = int(attack)
        self.my_dmg = int(dmg)
        self.my_index = int(index)
        self.my_loot = int(loot)
        self.my_max_health = int(health)
        self.my_alive = True

    def return_name(self):
        return self.my_name

    def return_health(self):
        return self.my_health

    def return_attack(self):
        return self.my_attack

    def return_dmg(self):
        return self.my_dmg

    def return_index(self):
        return self.my_index

    def return_loot(self):
        return self.my_loot
    
    def return_alive(self):
        return self.my_alive

    def take_damage(self, dmg):
        self.my_health -= dmg
        if self.my_health <= 0:
            self.my_alive = False

    def heal_damage(self, heal):
        self.my_health += heal
