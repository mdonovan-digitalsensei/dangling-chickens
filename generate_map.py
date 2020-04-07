from colourtext import colours


class Dungeon_map:
    def generate_map_array(self,my_level):
        my_map_file = "./maps/map_" + my_level + ".map"
        self.map_array = []
        with open(my_map_file) as map:
            for row in map:
                row_list = list(row)
                self.map_array.append(row_list)
        return self.map_array

    def print_map(self,x,y,player_char,entity_list):        
        lx = x
        ly = y
        i = 0    
        print()
        for row in self.map_array:
            i += 1   
            if i == ly:
                row = list(row)          
                row[lx] = player_char                                  
            row = "".join(row)
            print(f"{row}", end='')   
        print("\n")
# 