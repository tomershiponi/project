from classes.game import *
from classes.magic import *
import random
from classes.inventory import *

# Person = self, hp, mp, atk, df, magic

# creating class of spells

fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")

heal = Spell("Heal", 10, 100, "white")

# creating items
potion = Item("Potion", "potion", "Heals 50 HP", 50, 1)
hipotion = Item("Hi-potion", "potion", "Heals 100 HP", 100, 1)
superpotion = Item("Super-potion", "potion", "Heals 200 HP", 200, 1)

elixer = Item("Elixer", "elixer", "Fully restores HP/MP", 99999, 1)

grande = Item("Grande", "attack", "damage enemy hp by 300 dmg", 300, 1)
spalls = [fire, thunder, blizzard, heal]
items = [potion, hipotion, superpotion, elixer, grande]
# creating players
player = Person("Player", 700, 65, 80, 34, spalls, items)
enemy = Person("Enemy", 1200, 65, 45, 25, spalls, items)

run = True
print(Bcolors.FAIL + Bcolors.BOLO + "bottle began!" + Bcolors.ENDC)
c = ["d", "c ", "a"]

# starting battle
while run:
    player.player_stats()
    enemy.player_stats()
    # player attack: the player chose how to attack
    print("====================")
    choice = player.choose_action()
    # chose attack
    if choice == 0:
        dmg = player.generatre_damage()
        enemy.take_dmg(dmg)
        print(f"Player attack Enemy with {Bcolors.WARNING}{Bcolors.BOLO}{dmg}{Bcolors.ENDC}"
              f" DMG points Enemy HP is {Bcolors.WARNING}{Bcolors.BOLO}{enemy.get_hp()}{Bcolors.ENDC}")
        player.mp += 5
        if player.mp > player.max_mp:
            player.mp = player.max_mp
    # chose spell
    if choice == 1:
        chose = player.choose_magic()

        # checking if the player have enough "mp" to preform the move
        if player.get_mp() < chose.cost:
            print(Bcolors.FAIL + "\nYou do nat have MP for this move\n " + Bcolors.ENDC)
            continue
        # reduce the player mp by spell cost
        player.reduce_mp(chose.cost)
        if chose.type == "white":
            player.hp += heal.dmg
            print("player healed")
            if player.hp > player.max_hp:
                player.hp = player.max_hp
        else:
            m_dmg = chose.generatre_spall_dmg()
            enemy.take_dmg(m_dmg)
            print(
                f"Player attack Enemy with {chose.name} and cause {Bcolors.WARNING}{Bcolors.BOLO}{m_dmg}{Bcolors.ENDC} "
                f"DMG points. Enemy HP is {Bcolors.WARNING}{Bcolors.BOLO}{enemy.get_hp()}{Bcolors.ENDC}")
    # player choose item
    if choice == 2:
        choice = player.chose_itam()
        if choice.amount == 0:
            # checking if item in inventory
            print(f"{Bcolors.FAIL}{Bcolors.BOLO}"
                  f"You do not have this item in your inventory. \ntry something else{Bcolors.ENDC} ")
            continue
        player.use_item(choice, enemy)

    # checking if the enemy is dead
    if enemy.get_hp() == 0:
        print(Bcolors.OKGREEN + Bcolors.BOLO + "You win!!" + Bcolors.ENDC)
        break

    # enemy attack
    print("====================")
    print(Bcolors.FAIL + Bcolors.BOLO + "an enemy attack!" + Bcolors.ENDC)

    if enemy.hp < 200:
        if enemy.mp > 10:
            choice = 1

    else:
        choice = random.randrange(0, 2)
    # chose attack
    if choice == 0:
        dmg = enemy.generatre_damage()
        player.take_dmg(dmg)
        print(f"Enemy attack Player with {Bcolors.WARNING}{Bcolors.BOLO}{dmg}{Bcolors.ENDC}"
              f" DMG points Player HP is {Bcolors.WARNING}{Bcolors.BOLO}{player.get_hp()}{Bcolors.ENDC}")
        enemy.mp += 5
        if enemy.mp > enemy.max_mp:
            enemy.mp = enemy.max_mp
    # chose spell
    if choice == 1:
        if enemy.hp < 200:
            chose = 3
        else:
            chose = random.randrange(len(enemy.magic))
        chose = enemy.magic[chose]
    # checking if the player have enough "mp" to preform the move
        if enemy.get_mp() < chose.cost:
            print(Bcolors.FAIL + "\nYou do nat have MP for this move\n " + Bcolors.ENDC)
            dmg = enemy.generatre_damage()
            player.take_dmg(dmg)
            print(f"Enemy attack Player with {Bcolors.WARNING}{Bcolors.BOLO}{dmg}{Bcolors.ENDC}"
                f" DMG points Player HP is {Bcolors.WARNING}{Bcolors.BOLO}{player.get_hp()}{Bcolors.ENDC}")
        else:
            # reduce the player mp by spell cost
            enemy.reduce_mp(chose.cost)
        if chose.type == "white":
            enemy.hp += heal.dmg
            print("Enemy healed")
            if enemy.hp > enemy.max_hp:
                enemy.hp = enemy.max_hp
        else:
            m_dmg = chose.generatre_spall_dmg()
            player.take_dmg(m_dmg)
            print(
                f"Enemy attack player with {chose.name} and cause {Bcolors.WARNING}{Bcolors.BOLO}{m_dmg}{Bcolors.ENDC} "
                f"DMG points Player HP is {Bcolors.WARNING}{Bcolors.BOLO}{player.get_hp()}{Bcolors.ENDC}")

    # checking if the player is dead
    if player.get_hp() == 0:
        print(Bcolors.FAIL + Bcolors.BOLO + "You loss!!" + Bcolors.ENDC)
        run = False
