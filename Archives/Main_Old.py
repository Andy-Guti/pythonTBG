
import random
import turtle
import os
from Objects import *
import time


class Main:
    def __init__(self):
        self.roomDict = {}
        self.numRooms = 0
        self.player_model = turtle.Turtle()

    def create_map(self):
        window = turtle.Screen()
        sprite = self.player_model
        sprite.penup()
        sprite.speed(0)
        #start room
        sprite.setheading(90)
        sprite.forward(25)
        self.draw_square(sprite)

        #east rooms
        sprite.setheading(0)
        sprite.forward(50)
        self.draw_square(sprite)
        sprite.setheading(0)
        sprite.forward(50)
        self.draw_square(sprite)

        #west Rooms
        sprite.setpos(0,25)
        sprite.setheading(180)
        sprite.forward(50)
        self.draw_square(sprite)
        sprite.setheading(180)
        sprite.forward(50)
        self.draw_square(sprite)

        #south Rooms
        sprite.setpos(0,-25)
        sprite.setheading(270)
        self.draw_square(sprite)
        sprite.setheading(270)
        sprite.forward(50)
        self.draw_square(sprite)

        #north Rooms
        sprite.setpos(0,25)
        sprite.setheading(90)
        sprite.forward(50)
        self.draw_square(sprite)
        sprite.setheading(90)
        sprite.forward(50)
        self.draw_square(sprite)

        #north-west Room
        sprite.setpos(-50,75)
        self.draw_square(sprite)

        #north-east Room
        sprite.setpos(50,75)
        self.draw_square(sprite)

        #south-east Room
        sprite.setpos(50,-25)
        self.draw_square(sprite)

        #south-west Room
        sprite.setpos(-50,-25)
        self.draw_square(sprite)

        #set player back to center
        sprite.setpos(0,0)
        sprite.setheading(90)
        sprite.speed(5)


    def draw_square(self, sprite):
        sprite.pendown()
        sprite.setheading(0)
        sprite.forward(25)
        sprite.setheading(270)
        sprite.forward(50)
        sprite.setheading(180)
        sprite.forward(50)
        sprite.setheading(90)
        sprite.forward(50)
        sprite.setheading(0)
        sprite.forward(25)
        sprite.setheading(90)
        sprite.penup()



    def create_game(self, start_room):
        key_list = list(self.roomDict.keys())
        val_list = list(self.roomDict.values())
        directions1 = ['north', 'east']
        directions2 = ['south', 'west']
        i = 1
        for x in directions1:
            start_room.addNeighbor(x, i)
            room1 = Room()
            room1.id = i
            rand_num1 = random.randint(0, 100)
            rand_num2 = random.randint(0, 100)
            rand_num3 = random.randint(0, 100)
            if rand_num1 > 33:
                room1.type = 'easy'
            if rand_num1 <= 33:
                room1.type = 'hard'
                room1.has_enemy = True
                room1.enemy.damage = random.randint(15, 30)
            if rand_num3 > 33:
                room1.has_item = True
                if 90 > rand_num2 > 20:
                    rand_item = Item()
                    rand_item.type = 'good'
                    room1.item = rand_item
                    good_items = ['a Shiney Sword', ' a Swiss Army Knife', ' a Super Charged Tazer']
                    rand_name_num = random.randint(0, len(good_items) - 1)
                    rand_name = good_items[rand_name_num]
                    room1.item.name = rand_name

                if rand_num2 <= 20:
                    rand_item = Item()
                    rand_item.type = 'bad'
                    room1.item = rand_item
                    bad_items = [' a Nasty Knife', ' a Flare Gun', 'The Pointiest of Sticks', 'a Shabby Sickle']
                    rand_name_num = random.randint(0, len(bad_items) - 1)
                    rand_name = bad_items[rand_name_num]
                    room1.item.name = rand_name

                if rand_num2 >= 90:
                    rand_item = Item()
                    rand_item.type = 'great'
                    room1.item = rand_item
                    great_items = ['Cheese Slicing Katana', 'Bazooka', "Dead Man's Dagger", 'Carnivorous Cleaver']
                    rand_name_num = random.randint(0, len(great_items) - 1)
                    rand_name = great_items[rand_name_num]
                    room1.item.name = rand_name

            self.roomDict[i] = room1
            index = directions1.index(x)
            room1.addNeighbor(directions2[index], key_list[val_list.index(start_room)])
            self.numRooms += 1
            i += 1

        for y in directions2:
            start_room.addNeighbor(y, i)
            room1 = Room()
            room1.id = i
            rand_num1 = random.randint(0, 100)
            rand_num2 = random.randint(0, 100)
            rand_num3 = random.randint(0, 100)
            if rand_num1 > 33:
                room1.type = 'easy'
            if rand_num1 <= 33:
                room1.type = 'hard'
                room1.has_enemy = True
                room1.enemy.damage = random.randint(15, 30)
            if rand_num3 > 33:
                room1.has_item = True
                if 90 > rand_num2 > 20:
                    rand_item = Item()
                    rand_item.type = 'good'
                    room1.item = rand_item
                    good_items = ['a Shiny Sword', 'a Swiss Army Knife', 'a Super Charged Tazer']
                    rand_name_num = random.randint(0, len(good_items)-1)
                    rand_name = good_items[rand_name_num]
                    room1.item.name = rand_name

                if rand_num2 <= 20:
                    rand_item = Item()
                    rand_item.type = 'bad'
                    room1.item = rand_item
                    bad_items = ['a Nasty Knife', 'a Flare Gun', 'The Pointiest of Sticks', 'a Shabby Sickle']
                    rand_name_num = random.randint(0, len(bad_items)-1)
                    rand_name = bad_items[rand_name_num]
                    room1.item.name = rand_name

                if rand_num2 >= 90:
                    rand_item = Item()
                    rand_item.type = 'great'
                    room1.item = rand_item
                    great_items = ['Cheese Slicing Katana', 'Bazooka', "Dead Man's Dagger", 'Carnivorous Cleaver']
                    rand_name_num = random.randint(0, len(great_items)-1)
                    rand_name = great_items[rand_name_num]
                    room1.item.name = rand_name

            self.roomDict[i] = room1
            index = directions2.index(y)
            room1.addNeighbor(directions1[index], key_list[val_list.index(start_room)])
            self.numRooms += 1
            i += 1

    def med_game(self, start_room):
        for direction, id in start_room.neighbor.items():

                if direction == "north":
                    placeHolder = self.roomDict[id]

                    newids = self.numRooms + 1
                    placeHolder.addNeighbor("north", newids)
                    #create new room
                    placeHolder2 = Room()
                    placeHolder2.id = newids
                    self.roomDict[newids] = placeHolder2
                    #end create new room
                    placeHolder2.addNeighbor("south",id)
                    self.numRooms += 1
                    self.roomDict[newids] = placeHolder2


                    newids = self.numRooms + 1
                    placeHolder.addNeighbor("west",newids)
                    #create new room
                    placeHolder2 = Room()
                    placeHolder2.id = newids
                    self.roomDict[newids] = placeHolder2
                    #end create new room
                    placeHolder2.addNeighbor("east",id)
                    placeHolder3 = self.roomDict[start_room.neighbor["west"]]
                    placeHolder3.addNeighbor("north",newids)
                    placeHolder2.addNeighbor("south",placeHolder3.id)
                    self.numRooms += 1

                    newids = self.numRooms + 1
                    placeHolder.addNeighbor("east",newids)
                    #create new room
                    placeHolder2 = Room()
                    placeHolder2.id = newids
                    self.roomDict[newids] = placeHolder2
                    #end create new room
                    placeHolder2.addNeighbor("west",id)
                    placeHolder3 = self.roomDict[start_room.neighbor["east"]]
                    placeHolder3.addNeighbor("north",newids)
                    placeHolder2.addNeighbor("south",placeHolder3.id)
                    self.numRooms += 1

                if direction == "south":
                    placeHolder = self.roomDict[id]

                    newids = self.numRooms + 1
                    placeHolder.addNeighbor("south",newids)
                    #create new room
                    placeHolder2 = Room()
                    placeHolder2.id = newids
                    self.roomDict[newids] = placeHolder2
                    rand_num1 = random.randint(0, 100)
                    rand_num2 = random.randint(0, 100)
                    rand_num3 = random.randint(0, 100)
                    if rand_num1 > 33:
                        placeHolder2.type = 'easy'
                    if rand_num1 <= 33:
                        placeHolder2.type = 'hard'
                        placeHolder2.has_enemy = True
                        placeHolder2.enemy.damage = random.randint(15, 30)
                    if rand_num3 > 33:
                        placeHolder2.has_item = True
                        if 90 > rand_num2 > 20:
                            rand_item = Item()
                            rand_item.type = 'good'
                            placeHolder2.item = rand_item
                            good_items = ['a Shiny Sword', 'a Swiss Army Knife', 'a Super Charged Tazer','LOTR Mace']
                            rand_name_num = random.randint(0, len(good_items)-1)
                            rand_name = good_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 <= 20:
                            rand_item = Item()
                            rand_item.type = 'bad'
                            placeHolder2.item = rand_item
                            bad_items = ['a Nasty Knife', 'a Flare Gun', 'The Pointiest of Sticks', 'a Shabby Sickle','Bear Spray']
                            rand_name_num = random.randint(0, len(bad_items)-1)
                            rand_name = bad_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 >= 90:
                            rand_item = Item()
                            rand_item.type = 'great'
                            placeHolder2.item = rand_item
                            great_items = ['Cheese Slicing Katana', 'Bazooka', "Dead Man's Dagger", 'Carnivorous Cleaver',"Legolas' Bow"]
                            rand_name_num = random.randint(0, len(great_items)-1)
                            rand_name = great_items[rand_name_num]
                            placeHolder2.item.name = rand_name
                    #end create new room
                    placeHolder2.addNeighbor("north",id)
                    self.numRooms += 1


                    newids = self.numRooms + 1
                    placeHolder.addNeighbor("west",newids)
                    #create new room
                    placeHolder2 = Room()
                    placeHolder2.id = newids
                    self.roomDict[newids] = placeHolder2
                    rand_num1 = random.randint(0, 100)
                    rand_num2 = random.randint(0, 100)
                    rand_num3 = random.randint(0, 100)
                    if rand_num1 > 33:
                        placeHolder2.type = 'easy'
                    if rand_num1 <= 33:
                        placeHolder2.type = 'hard'
                        placeHolder2.has_enemy = True
                        placeHolder2.enemy.damage = random.randint(15, 30)
                    if rand_num3 > 33:
                        placeHolder2.has_item = True
                        if 90 > rand_num2 > 20:
                            rand_item = Item()
                            rand_item.type = 'good'
                            placeHolder2.item = rand_item
                            good_items = ['a Shiny Sword', 'a Swiss Army Knife', 'a Super Charged Tazer','LOTR Mace']
                            rand_name_num = random.randint(0, len(good_items)-1)
                            rand_name = good_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 <= 20:
                            rand_item = Item()
                            rand_item.type = 'bad'
                            placeHolder2.item = rand_item
                            bad_items = ['a Nasty Knife', 'a Flare Gun', 'The Pointiest of Sticks', 'a Shabby Sickle','Bear Spray']
                            rand_name_num = random.randint(0, len(bad_items)-1)
                            rand_name = bad_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 >= 90:
                            rand_item = Item()
                            rand_item.type = 'great'
                            placeHolder2.item = rand_item
                            great_items = ['Cheese Slicing Katana', 'Bazooka', "Dead Man's Dagger", 'Carnivorous Cleaver',"Legolas' Bow"]
                            rand_name_num = random.randint(0, len(great_items)-1)
                            rand_name = great_items[rand_name_num]
                            placeHolder2.item.name = rand_name
                    #end create new room
                    placeHolder2.addNeighbor("east",id)
                    placeHolder3 = self.roomDict[start_room.neighbor["west"]]
                    placeHolder3.addNeighbor("south",newids)
                    placeHolder2.addNeighbor("north",placeHolder3.id)
                    self.numRooms += 1

                    newids = self.numRooms + 1
                    placeHolder.addNeighbor("east",newids)
                    #create new room
                    placeHolder2 = Room()
                    placeHolder2.id = newids
                    self.roomDict[newids] = placeHolder2
                    rand_num1 = random.randint(0, 100)
                    rand_num2 = random.randint(0, 100)
                    rand_num3 = random.randint(0, 100)
                    if rand_num1 > 33:
                        placeHolder2.type = 'easy'
                    if rand_num1 <= 33:
                        placeHolder2.type = 'hard'
                        placeHolder2.has_enemy = True
                        placeHolder2.enemy.damage = random.randint(15, 30)
                    if rand_num3 > 33:
                        placeHolder2.has_item = True
                        if 90 > rand_num2 > 20:
                            rand_item = Item()
                            rand_item.type = 'good'
                            placeHolder2.item = rand_item
                            good_items = ['a Shiny Sword', 'a Swiss Army Knife', 'a Super Charged Tazer','LOTR Mace']
                            rand_name_num = random.randint(0, len(good_items)-1)
                            rand_name = good_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 <= 20:
                            rand_item = Item()
                            rand_item.type = 'bad'
                            placeHolder2.item = rand_item
                            bad_items = ['a Nasty Knife', 'a Flare Gun', 'The Pointiest of Sticks', 'a Shabby Sickle','Bear Spray']
                            rand_name_num = random.randint(0, len(bad_items)-1)
                            rand_name = bad_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 >= 90:
                            rand_item = Item()
                            rand_item.type = 'great'
                            placeHolder2.item = rand_item
                            great_items = ['Cheese Slicing Katana', 'Bazooka', "Dead Man's Dagger", 'Carnivorous Cleaver',"Legolas' Bow"]
                            rand_name_num = random.randint(0, len(great_items)-1)
                            rand_name = great_items[rand_name_num]
                            placeHolder2.item.name = rand_name
                    #end create new room
                    placeHolder2.addNeighbor("west",id)
                    placeHolder3 = self.roomDict[start_room.neighbor["east"]]
                    placeHolder3.addNeighbor("south",newids)
                    placeHolder2.addNeighbor("north",placeHolder3.id)
                    self.numRooms += 1

                if direction == "east":
                    placeHolder = self.roomDict[id]

                    newids = self.numRooms + 1
                    placeHolder.addNeighbor("east",newids)
                    #create new room
                    placeHolder2 = Room()
                    placeHolder2.id = newids
                    self.roomDict[newids] = placeHolder2
                    rand_num1 = random.randint(0, 100)
                    rand_num2 = random.randint(0, 100)
                    rand_num3 = random.randint(0, 100)
                    if rand_num1 > 33:
                        placeHolder2.type = 'easy'
                    if rand_num1 <= 33:
                        placeHolder2.type = 'hard'
                        placeHolder2.has_enemy = True
                        placeHolder2.enemy.damage = random.randint(15, 30)
                    if rand_num3 > 33:
                        placeHolder2.has_item = True
                        if 90 > rand_num2 > 20:
                            rand_item = Item()
                            rand_item.type = 'good'
                            placeHolder2.item = rand_item
                            good_items = ['a Shiny Sword', 'a Swiss Army Knife', 'a Super Charged Tazer','LOTR Mace']
                            rand_name_num = random.randint(0, len(good_items)-1)
                            rand_name = good_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 <= 20:
                            rand_item = Item()
                            rand_item.type = 'bad'
                            placeHolder2.item = rand_item
                            bad_items = ['a Nasty Knife', 'a Flare Gun', 'The Pointiest of Sticks', 'a Shabby Sickle','Bear Spray']
                            rand_name_num = random.randint(0, len(bad_items)-1)
                            rand_name = bad_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 >= 90:
                            rand_item = Item()
                            rand_item.type = 'great'
                            placeHolder2.item = rand_item
                            great_items = ['Cheese Slicing Katana', 'Bazooka', "Dead Man's Dagger", 'Carnivorous Cleaver',"Legolas' Bow"]
                            rand_name_num = random.randint(0, len(great_items)-1)
                            rand_name = great_items[rand_name_num]
                            placeHolder2.item.name = rand_name
                    #end create new room
                    placeHolder2.addNeighbor("west",id)
                    self.numRooms += 1


                    newids = self.numRooms + 1
                    placeHolder.addNeighbor("north",newids)
                    #create new room
                    placeHolder2 = Room()
                    placeHolder2.id = newids
                    self.roomDict[newids] = placeHolder2
                    rand_num1 = random.randint(0, 100)
                    rand_num2 = random.randint(0, 100)
                    rand_num3 = random.randint(0, 100)
                    if rand_num1 > 33:
                        placeHolder2.type = 'easy'
                    if rand_num1 <= 33:
                        placeHolder2.type = 'hard'
                        placeHolder2.has_enemy = True
                        placeHolder2.enemy.damage = random.randint(15, 30)
                    if rand_num3 > 33:
                        placeHolder2.has_item = True
                        if 90 > rand_num2 > 20:
                            rand_item = Item()
                            rand_item.type = 'good'
                            placeHolder2.item = rand_item
                            good_items = ['a Shiny Sword', 'a Swiss Army Knife', 'a Super Charged Tazer','LOTR Mace']
                            rand_name_num = random.randint(0, len(good_items)-1)
                            rand_name = good_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 <= 20:
                            rand_item = Item()
                            rand_item.type = 'bad'
                            placeHolder2.item = rand_item
                            bad_items = ['a Nasty Knife', 'a Flare Gun', 'The Pointiest of Sticks', 'a Shabby Sickle','Bear Spray']
                            rand_name_num = random.randint(0, len(bad_items)-1)
                            rand_name = bad_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 >= 90:
                            rand_item = Item()
                            rand_item.type = 'great'
                            placeHolder2.item = rand_item
                            great_items = ['Cheese Slicing Katana', 'Bazooka', "Dead Man's Dagger", 'Carnivorous Cleaver',"Legolas' Bow"]
                            rand_name_num = random.randint(0, len(great_items)-1)
                            rand_name = great_items[rand_name_num]
                            placeHolder2.item.name = rand_name
                    #end create new room
                    placeHolder2.addNeighbor("south",id)
                    placeHolder3 = self.roomDict[start_room.neighbor["north"]]
                    placeHolder3.addNeighbor("east",newids)
                    placeHolder2.addNeighbor("west",placeHolder3.id)
                    self.numRooms += 1

                    newids = self.numRooms + 1
                    placeHolder.addNeighbor("south",newids)
                    #create new room
                    placeHolder2 = Room()
                    placeHolder2.id = newids
                    self.roomDict[newids] = placeHolder2
                    rand_num1 = random.randint(0, 100)
                    rand_num2 = random.randint(0, 100)
                    rand_num3 = random.randint(0, 100)
                    if rand_num1 > 33:
                        placeHolder2.type = 'easy'
                    if rand_num1 <= 33:
                        placeHolder2.type = 'hard'
                        placeHolder2.has_enemy = True
                        placeHolder2.enemy.damage = random.randint(15, 30)
                    if rand_num3 > 33:
                        placeHolder2.has_item = True
                        if 90 > rand_num2 > 20:
                            rand_item = Item()
                            rand_item.type = 'good'
                            placeHolder2.item = rand_item
                            good_items = ['a Shiny Sword', 'a Swiss Army Knife', 'a Super Charged Tazer','LOTR Mace']
                            rand_name_num = random.randint(0, len(good_items)-1)
                            rand_name = good_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 <= 20:
                            rand_item = Item()
                            rand_item.type = 'bad'
                            placeHolder2.item = rand_item
                            bad_items = ['a Nasty Knife', 'a Flare Gun', 'The Pointiest of Sticks', 'a Shabby Sickle','Bear Spray']
                            rand_name_num = random.randint(0, len(bad_items)-1)
                            rand_name = bad_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 >= 90:
                            rand_item = Item()
                            rand_item.type = 'great'
                            placeHolder2.item = rand_item
                            great_items = ['Cheese Slicing Katana', 'Bazooka', "Dead Man's Dagger", 'Carnivorous Cleaver',"Legolas' Bow"]
                            rand_name_num = random.randint(0, len(great_items)-1)
                            rand_name = great_items[rand_name_num]
                            placeHolder2.item.name = rand_name
                    #end create new room
                    placeHolder2.addNeighbor("north",id)
                    placeHolder3 = self.roomDict[start_room.neighbor["south"]]
                    placeHolder3.addNeighbor("east",newids)
                    placeHolder2.addNeighbor("west",placeHolder3.id)
                    self.numRooms += 1

                if direction == "west":
                    placeHolder = self.roomDict[id]

                    newids = self.numRooms + 1
                    placeHolder.addNeighbor("west",newids)
                    #create new room
                    placeHolder2 = Room()
                    placeHolder2.id = newids
                    self.roomDict[newids] = placeHolder2
                    rand_num1 = random.randint(0, 100)
                    rand_num2 = random.randint(0, 100)
                    rand_num3 = random.randint(0, 100)
                    if rand_num1 > 33:
                        placeHolder2.type = 'easy'
                    if rand_num1 <= 33:
                        placeHolder2.type = 'hard'
                        placeHolder2.has_enemy = True
                        placeHolder2.enemy.damage = random.randint(15, 30)
                    if rand_num3 > 33:
                        placeHolder2.has_item = True
                        if 90 > rand_num2 > 20:
                            rand_item = Item()
                            rand_item.type = 'good'
                            placeHolder2.item = rand_item
                            good_items = ['a Shiny Sword', 'a Swiss Army Knife', 'a Super Charged Tazer','LOTR Mace']
                            rand_name_num = random.randint(0, len(good_items)-1)
                            rand_name = good_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 <= 20:
                            rand_item = Item()
                            rand_item.type = 'bad'
                            placeHolder2.item = rand_item
                            bad_items = ['a Nasty Knife', 'a Flare Gun', 'The Pointiest of Sticks', 'a Shabby Sickle','Bear Spray']
                            rand_name_num = random.randint(0, len(bad_items)-1)
                            rand_name = bad_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 >= 90:
                            rand_item = Item()
                            rand_item.type = 'great'
                            placeHolder2.item = rand_item
                            great_items = ['Cheese Slicing Katana', 'Bazooka', "Dead Man's Dagger", 'Carnivorous Cleaver',"Legolas' Bow"]
                            rand_name_num = random.randint(0, len(great_items)-1)
                            rand_name = great_items[rand_name_num]
                            placeHolder2.item.name = rand_name
                    #end create new room
                    placeHolder2.addNeighbor("east",id)
                    self.numRooms += 1


                    newids = self.numRooms + 1
                    placeHolder.addNeighbor("north",newids)
                    #create new room
                    placeHolder2 = Room()
                    placeHolder2.id = newids
                    self.roomDict[newids] = placeHolder2
                    rand_num1 = random.randint(0, 100)
                    rand_num2 = random.randint(0, 100)
                    rand_num3 = random.randint(0, 100)
                    if rand_num1 > 33:
                        placeHolder2.type = 'easy'
                    if rand_num1 <= 33:
                        placeHolder2.type = 'hard'
                        placeHolder2.has_enemy = True
                        placeHolder2.enemy.damage = random.randint(15, 30)
                    if rand_num3 > 33:
                        placeHolder2.has_item = True
                        if 90 > rand_num2 > 20:
                            rand_item = Item()
                            rand_item.type = 'good'
                            placeHolder2.item = rand_item
                            good_items = ['a Shiny Sword', 'a Swiss Army Knife', 'a Super Charged Tazer','LOTR Mace']
                            rand_name_num = random.randint(0, len(good_items)-1)
                            rand_name = good_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 <= 20:
                            rand_item = Item()
                            rand_item.type = 'bad'
                            placeHolder2.item = rand_item
                            bad_items = ['a Nasty Knife', 'a Flare Gun', 'The Pointiest of Sticks', 'a Shabby Sickle','Bear Spray']
                            rand_name_num = random.randint(0, len(bad_items)-1)
                            rand_name = bad_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 >= 90:
                            rand_item = Item()
                            rand_item.type = 'great'
                            placeHolder2.item = rand_item
                            great_items = ['Cheese Slicing Katana', 'Bazooka', "Dead Man's Dagger", 'Carnivorous Cleaver',"Legolas' Bow"]
                            rand_name_num = random.randint(0, len(great_items)-1)
                            rand_name = great_items[rand_name_num]
                            placeHolder2.item.name = rand_name
                    #end create new room
                    placeHolder2.addNeighbor("south",id)
                    placeHolder3 = self.roomDict[start_room.neighbor["north"]]
                    placeHolder3.addNeighbor("west",newids)
                    placeHolder2.addNeighbor("east",placeHolder3.id)
                    self.numRooms += 1

                    newids = self.numRooms + 1
                    placeHolder.addNeighbor("south",newids)
                    #create new room
                    placeHolder2 = Room()
                    placeHolder2.id = newids
                    self.roomDict[newids] = placeHolder2
                    rand_num1 = random.randint(0, 100)
                    rand_num2 = random.randint(0, 100)
                    rand_num3 = random.randint(0, 100)
                    if rand_num1 > 33:
                        placeHolder2.type = 'easy'
                    if rand_num1 <= 33:
                        placeHolder2.type = 'hard'
                        placeHolder2.has_enemy = True
                        placeHolder2.enemy.damage = random.randint(15, 30)
                    if rand_num3 > 33:
                        placeHolder2.has_item = True
                        if 90 > rand_num2 > 20:
                            rand_item = Item()
                            rand_item.type = 'good'
                            placeHolder2.item = rand_item
                            good_items = ['a Shiny Sword', 'a Swiss Army Knife', 'a Super Charged Tazer','LOTR Mace']
                            rand_name_num = random.randint(0, len(good_items)-1)
                            rand_name = good_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 <= 20:
                            rand_item = Item()
                            rand_item.type = 'bad'
                            placeHolder2.item = rand_item
                            bad_items = ['a Nasty Knife', 'a Flare Gun', 'The Pointiest of Sticks', 'a Shabby Sickle','Bear Spray']
                            rand_name_num = random.randint(0, len(bad_items)-1)
                            rand_name = bad_items[rand_name_num]
                            placeHolder2.item.name = rand_name

                        if rand_num2 >= 90:
                            rand_item = Item()
                            rand_item.type = 'great'
                            placeHolder2.item = rand_item
                            great_items = ['Cheese Slicing Katana', 'Bazooka', "Dead Man's Dagger", 'Carnivorous Cleaver',"Legolas' Bow"]
                            rand_name_num = random.randint(0, len(great_items)-1)
                            rand_name = great_items[rand_name_num]
                            placeHolder2.item.name = rand_name
                    #end create new room
                    placeHolder2.addNeighbor("north",id)
                    placeHolder3 = self.roomDict[start_room.neighbor["south"]]
                    placeHolder3.addNeighbor("west",newids)
                    placeHolder2.addNeighbor("east",placeHolder3.id)
                    self.numRooms += 1



        return


    def game_setup(self):
        start_room = Room()
        start_room.id = 0
        start_room.type = "easy"
        start_room.has_enemy = False
        start_room.has_item = False
        came_from = Room()
        self.roomDict[start_room.id] = start_room
        self.numRooms += 1
        self.create_game(start_room)
        self.med_game(start_room)
        player = Player()
        os.system('clear')
        print("\n\nYou find yourself in a room and you have nothing but your trusty compass.")
        self.game(start_room, player, came_from)


    def combat(self, current_room, player, came_room):
        # combat system
        print('You decide to fight the enemy in front of you, choose which weapon you would like to use to attack!')
        item_names = ''
        i = 0
        for x in player.items:
            i += 1
            if i < (len(player.items)):
                item_names += '(' + str(i) + ') ' + x.name + '\n'
            if i == len(player.items):
                item_names += '(' + str(i) + ') ' + x.name

        weapon = input('your items are:\n' + item_names + '\n')
        #while weapon 
        os.system('clear')
        chosenWeapon = player.items[int(weapon) - 1]
        enemyDamage = current_room.enemy.damage

        while current_room.has_enemy is True:
            if current_room.enemy.health <= 0:
                current_room.has_enemy = False
                print('You have defeated the enemy!')
                break
            if player.health <= 0:
                print('After a valiant effort, you have been slain. It is a sad day for you indeed')
                break
            else:
                print("Enemy Health: "+str(current_room.enemy.health)+'    Your Health: '+str(player.health)+'\n\n')
                choice = input('(1) Attack\n(2) Flee\n(3) Switch Weapon\n')
                os.system('clear')
                if choice == '1':
                    if chosenWeapon.type == 'good':
                        rand_damage = random.randint(15, 25)
                        chosenWeapon.damage = rand_damage
                    if chosenWeapon.type == 'bad':
                        rand_damage = random.randint(5, 12)
                        chosenWeapon.damage = rand_damage
                    if chosenWeapon.type == 'great':
                        rand_damage = random.randint(45, 60)
                        chosenWeapon.damage = rand_damage
                    weaponDamage = chosenWeapon.damage
                    current_room.enemy.health -= weaponDamage
                    player.health -= enemyDamage
                    print("You deal " + str(weaponDamage) + ' damage\n')
                    print("The enemy strikes you and deals " + str(enemyDamage) + " damage\n")
                if choice == '2':
                    break
                if choice == '3':
                    item_names = ''
                    i = 0
                    for x in player.items:
                        i += 1
                        if i < (len(player.items)):
                            item_names += '(' + str(i) + ') ' + x.name + '\n'
                        if i == len(player.items):
                            item_names += '(' + str(i) + ') ' + x.name
                    weapon = input('your items are:\n' + item_names + '\n')
                    os.system('clear')
                    chosenWeapon = player.items[int(weapon) - 1]
                    weaponDamage = chosenWeapon.damage
        return


    def game(self, start_room, player, came_from):
        
        # basis of game

        if player.health < 100:
            if player.health > 75:
                diff = 100 - player.health
                player.health += diff
            else:
                player.health += 25

        current_room = start_room
        i = 0
        doors = ''
        if not current_room.has_item:
            has_item = 'There are no items in this room.\n'
        if current_room.has_item:
            has_item = 'You see an item in the corner of the room!\n'
        for x in current_room.neighbor:
            i += 1
            if i < len(current_room.neighbor):
                doors += x + ', '
            if i == (len(current_room.neighbor) - 1):
                doors += 'and '
            if i == len(current_room.neighbor):
                doors += x
        print(has_item + 'There is a door to the ' + doors + '.\n')
        number = 0


        # enemy encounter
        if current_room.has_enemy:
            print('There is an enemy in this room!\n What do you choose to do?')
            choice = input('(1) Flee the room the way you came\n(2) Stand and Fight\n')
            os.system('clear')
            if choice == '1':
                next_room = came_from
                came_from = current_room
                for keys, values in came_from.neighbor.items():
                    if values == next_room.id:
                        if keys == "north":
                            self.player_model.setheading(90)
                            self.player_model.forward(50)
                        elif keys == "south":
                            self.player_model.setheading(270)
                            self.player_model.forward(50)
                        elif keys == "west":
                            self.player_model.setheading(180)
                            self.player_model.forward(50)
                        else:
                            self.player_model.setheading(0)
                            self.player_model.forward(50)
                self.game(next_room, player, came_from)
            if choice == '2':
                self.combat(current_room, player, came_from)
                self.game(current_room, player, came_from)
            else:
                print(choice + 'is not an acceptable input')
                self.game(current_room, player, came_from)

        # what do you want to do
        if current_room.has_item:
            number = input("Do you... \n\n (1) Pick up the Item \n (2) Go through a door \n\n(type in a number)\n")
            os.system('clear')
        if number == '1':
            player.items.append(current_room.item)
            current_room.has_item = False
            print('You have picked up an item! (type (i) at any time to view your items)\n\n')
        if not current_room.has_item or number == '2':
            where_to_go = input("Which door do you decide to enter?\n(type in a direction i.e. north)\n")
            os.system('clear')
            directions1 = ['north', 'east']
            directions2 = ['south', 'west']
            if where_to_go == 'i':
                item_names = ''
                i = 0
                for x in player.items:
                    i += 1
                    if i < (len(player.items)):
                        item_names += '(' + str(i) + ') ' + x.name + '\n'
                    if i == len(player.items):
                        item_names += '(' + str(i) + ') ' + x.name

                print('your items are:\n' + item_names + '\n')
                self.game(current_room, player, came_from)
            # might not be needed
            elif (where_to_go in directions1) or (where_to_go in directions2):
                if where_to_go in directions1:
                    index = directions1.index(where_to_go)
                    coming_from = directions2[index]
                else:
                    index = directions2.index(where_to_go)
                    coming_from = directions1[index]

                came_from = current_room
                next_room = self.roomDict[self.roomDict[current_room.id].neighbor[where_to_go]]
                if where_to_go == "north":
                    self.player_model.setheading(90)
                    self.player_model.forward(50)
                elif where_to_go == "south":
                    self.player_model.setheading(270)
                    self.player_model.forward(50)
                elif where_to_go == "west":
                    self.player_model.setheading(180)
                    self.player_model.forward(50)
                else:
                    self.player_model.setheading(0)
                    self.player_model.forward(50)
                self.game(next_room, player, came_from)
            else:
                print("Invalid input")
                time.sleep(1)
                self.game(current_room, player, came_from)






if __name__ == '__main__':
    startGame = Main()
    startGame.create_map()
    startGame.game_setup()


# TO DO:
# implement experience
# implement larger map size
# implement what to do after defeating an enemy
#   1. Reset health after defeating enemy?
#   2. Reset health after getting level up? (possibly add potions)
#   3. Increase max health after level up and combine 1 and 2? (kinda like pokemon)
#   4. Slow incremental health while you aren't being attacked.
#   5. Make Rooms into a tree


#FeedBack:
# anounce what item you get when you pick it up
# possibly add multipliers based on level or something
# enemies drop something
# enemies
