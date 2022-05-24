import pygame

class Enemy:

    def __init__(self):
        self.health = 50
        self.damage = 0

class Player:

    def __init__(self):
        self.items = []
        self.health = 100
        self.experience = 0
        self.level = 0
        self.inventory_space = 3

    def level_up(self):
        self.experience = 0
        self.level += 1
    
    #def get_experience(self):
        
class Weapon:
    
    def __init__(self):
        self.type = str
        self.durability = 0
        self.name = str
        self.damage = 0

class Item:

    def __init__(self):
        self.name = str
        self.type = str


class Room:

    def __init__(self):
        self.id = 0
        self.neighbor = {}
        self.type = str
        self.items = []
        self.has_item = False
        self.enemy = Enemy()
        self.has_enemy = False
        self.position = (0,0)


    def addNeighbor(self, direction, id):
        self.neighbor[direction] = id

    def takenNeighbors(self):
        neighbors = list(self.neighbor.keys())
        return neighbors
