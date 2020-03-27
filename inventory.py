class Inventory:
    my_items = []

    def __init__(self):
        pass

    def add_item(self, index, number):
        i = 0
        if self.my_items:
            for item in self.my_items:
                if item[0] == index:
                    self.my_items[i][1] += number
                else:
                    self.my_items.append([index, number])
        else:
            self.my_items.append([index, number])

    def remove_item(self, index, number):
        i = 0
        for item in self.my_items:
            if item[0] == index:
                self.my_items[i][1] -= number
                if self.my_items[i][1] <= 0:
                    del self.my_items[i]
                    break

    def show_items(self):
        return self.my_items