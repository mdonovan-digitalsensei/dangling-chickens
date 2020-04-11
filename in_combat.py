
def in_combat(px,py,entity_list):
    for row in entity_list:
        if row[0] in (px - 1, px, px + 1) and row[1] in (py - 1, py, py + 1):
            return True, row[3]

    return False, None 

