class Kill_list:
    def __init__(self):
        self.my_list = []

    def add_kill(self, monster):
        self.my_list.append(monster)

    def return_list(self):
        return self.my_list