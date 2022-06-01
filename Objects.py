import random


class Npc:
    def __init__(self):
        self.inventory = []

    def create_inventory(self):
        melee_weapons = ["Rapier", "Broadsword", "shortsword"]
        ranged_weapons = ["Bow", "Crossbow", "Longbow"]
        magic_weapons = ["Wand", "Fire Staff", "Ice Staff"]

        increment = 0
        while increment < 3:
            rand_num = random.randint(0, 2)
            new_weapon = Weapon()
            new_weapon.damage = 12
            new_weapon.durability = 32
            new_weapon.price = 15
            if increment == 0:
                new_weapon.type = "Melee"
                new_weapon.name = melee_weapons[rand_num]
                self.inventory.append(new_weapon)
                increment += 1
                continue
            elif increment == 1:
                new_weapon.type = "Ranged"
                new_weapon.name = ranged_weapons[rand_num]
                self.inventory.append(new_weapon)
                increment += 1
                continue
            else:
                new_weapon.type = "Magic"
                new_weapon.name = magic_weapons[rand_num]
                self.inventory.append(new_weapon)
                increment += 1
                continue
            


class Enemy:

    def __init__(self):
        self.health = 50
        self.damage = 0
        self.gold = random.randint(1,5)


class Player:
    def __init__(self):
        start_weapon = Weapon()
        start_weapon.name = "rusty sword"
        start_weapon.durability = 25
        start_weapon.damage = 8
        start_weapon.type = "melee"
        self.items = []
        self.items.append(start_weapon)
        self.health = 100
        self.experience = 0
        self.level = 0
        self.inventory_space = 3
        self.gold = 10

    def level_up(self):
        self.experience = 0
        self.level += 1
    # def get_experience(self):


class Weapon:

    def __init__(self):
        self.type = str
        self.durability = 0
        self.name = str
        self.damage = 0
        self.price = 0


class Item:

    def __init__(self):
        self.name = str
        self.type = str
        self.price = 0


class Room:

    def __init__(self):
        self.id = 0
        self.neighbor = {}
        self.type = str
        self.npc = None
        self.has_item = False
        self.enemy = Enemy()
        self.has_enemy = False
        self.position = (0, 0)

    def addNeighbor(self, direction, id):
        self.neighbor[direction] = id

    def takenNeighbors(self):
        neighbors = list(self.neighbor.keys())
        return neighbors
