from colourtext import colours

def generate_map_array(my_level):
    my_map_file = "./maps/map_" + my_level + ".map"
    dungeon_map_array = []
    with open(my_map_file) as map:
        for row in map:
            row_list = list(row)
            dungeon_map_array.append(row_list)
    return dungeon_map_array

def print_map(my_level,x,y,player_char):
    map_array=generate_map_array(my_level)
    lx = x
    ly = y
    i = 0    
    print()
    for row in map_array:
        i += 1   
        if i == ly:
            row = list(row)          
            row[lx] = player_char                                  
        row = "".join(row)
        print(f"{row}", end='')   
    print("\n")
# 