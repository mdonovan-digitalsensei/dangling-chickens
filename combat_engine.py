# the combat system for the game. 


def ce_attack_roll(player, monster):
    player_attack_roll = player.attack()
    monster_attack_roll = monster.attack()
    if player_attack_roll > monster_attack_roll:
        return 



print(f"You perform an attack scoring a {attackroll}")

monsterattackroll = randint(0, 6) + combat_with_monster.return_attack()


print(f"The {combat_with_monster.return_name()} gets an attack roll of {monsterattackroll}")

if attackroll > monsterattackroll:
    print(f"You have damanged the {combat_with_monster.return_name()}")
    combat_with_monster.take_damage(pdmg)
    if combat_with_monster.return_alive() == False:
        print(f"The {combat_with_monster.return_name()} has died")
        if combat_with_monster.loot_drop():
            temp_list = combat_with_monster.loot_drop()
            player_inv.add_item(*temp_list)
            kill_list.add_kill(combat_with_monster.return_name())
            entities.remove(combat_with_monster)
                    
        else:
            print(f"The {combat_with_monster.return_name()} has damaged you! You have taken {combat_with_monster.return_dmg()}")
            nobody.take_damage(combat_with_monster.return_dmg())
            print(f"You have {nobody.return_health()} health remaining")
            if nobody.return_health() <= 0:
                print(f"You have died")
                print("You Killed: ")
                for kills in kill_list.return_list():
                    print(kills)
        break