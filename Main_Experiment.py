
import random
import turtle
import os
from Objects import *
import time
from Engine import *


def main():

    game = Game()

    game.game_setup()

    game.player_model.setpos(0,0)
    game.player_model.speed(5)
    game.player_model.pencolor('red')
    game.player_model.pendown()
    #game.create_map()

    while True:
        # basis of game

        # PlaceHolder for regenerating health. Potentially replace with potions or something
        if game.player.health < 100:
            if game.player.health > 75:
                diff = 100 - game.player.health
                game.player.health += diff
            else:
                game.player.health += 25

        i = 0
        doors = ''
        if not game.current_room.has_item:
            has_item = 'There are no items in this room.\n'
        if game.current_room.has_item:
            has_item = 'You see an item in the corner of the room!\n'
        for x in game.current_room.neighbor:
            i += 1
            if i < len(game.current_room.neighbor):
                doors += x + ', '
            if i == (len(game.current_room.neighbor) - 1):
                doors += 'and '
            if i == len(game.current_room.neighbor):
                doors += x
        print(has_item + 'There is a door to the ' + doors + '.\n')
        number = 0


        # enemy encounter
        if game.current_room.has_enemy:
            print('There is an enemy in this room!\n What do you choose to do?')
            choice = input('(1) Flee the room the way you came\n(2) Stand and Fight\n')
            os.system('clear')
            if choice == '1':
                next_room = game.came_from
                came_from = game.current_room
                for keys, values in came_from.neighbor.items():
                    if values == next_room.id:
                        if keys == "north":
                            game.player_model.setheading(90)
                            game.player_model.forward(50)
                        elif keys == "south":
                            game.player_model.setheading(270)
                            game.player_model.forward(50)
                        elif keys == "west":
                            game.player_model.setheading(180)
                            game.player_model.forward(50)
                        else:
                            game.player_model.setheading(0)
                            game.player_model.forward(50)
                game.current_room = next_room
                game.came_from = came_from
                continue
                #self.game(next_room, player, came_from)
            if choice == '2':
                success = game.combat()
                if (success == 0):
                    break
                continue
                #self.game(current_room, player, came_from)
            else:
                print(choice + ' is not an acceptable input')
                continue
                #self.game(current_room, player, came_from)

        # what do you want to do
        if game.current_room.has_item:
            number = input("Do you... \n\n (1) Pick up the Item \n (2) Go through a door \n\n(type in a number)\n")
            os.system('clear')
        if number == '1':
            print("You found " + game.current_room.item.name + '       Durability: ' + str(game.current_room.item.durability) + '       Power: ' + str(game.current_room.item.damage) + '\n')
            if (len(game.player.items) >= game.player.inventory_space):
                print("You have no more space in your backpack! Drop an item? \n")
                drop_item = input("(1) Drop Item \n(2) Leave item in room \n")
                if drop_item == '1':
                    item_names = ''
                    i = 0
                    for x in game.player.items:
                        i += 1
                        if i < (len(game.player.items)):
                            item_names += '(' + str(i) + ') ' + x.name + '       Durability: ' + str(x.durability) + '       Power: ' + str(x.damage) + '\n'
                        if i == len(game.player.items):
                            item_names += '(' + str(i) + ') ' + x.name + '       Durability: ' + str(x.durability) + '       Power: ' + str(x.damage)
                    item_dropped_index = input('Which weapon do you drop?\n' + item_names + '\n')
                    os.system('clear')
                    item_dropped = game.player.items[int(item_dropped_index) - 1]
                    print(item_dropped.name)
                    game.player.items.append(game.current_room.item)
                    game.player.items.remove(item_dropped)
                    game.current_room.item = item_dropped
                else:
                    continue
            else:
                game.current_room.has_item = False       
                game.player.items.append(game.current_room.item)
        if not game.current_room.has_item or number == '2':
            where_to_go = input("Which door do you decide to enter?\n(type in a direction i.e. north)\n")
            os.system('clear')
            directions1 = ['north', 'east']
            directions2 = ['south', 'west']
            if where_to_go == 'i':
                item_names = ''
                i = 0
                for x in game.player.items:
                    i += 1
                    if i < (len(game.player.items)):
                        item_names += '(' + str(i) + ') ' + x.name + '       Durability: ' + str(x.durability) + '       Power: ' + str(x.damage) + '\n'
                    if i == len(game.player.items):
                        item_names += '(' + str(i) + ') ' + x.name + '       Durability: ' + str(x.durability) + '       Power: ' + str(x.damage)

                print('your items are:\n' + item_names + '\n')
                continue
                #self.game(current_room, player, came_from)
            # might not be needed
            if where_to_go in directions1 or where_to_go in directions2:
                if where_to_go not in game.current_room.neighbor.keys():
                    print("no room in that direction\n")
                    continue
                
            if (where_to_go in directions1) or (where_to_go in directions2):
                if where_to_go in directions1:
                    index = directions1.index(where_to_go)
                    coming_from = directions2[index]
                else:
                    index = directions2.index(where_to_go)
                    coming_from = directions1[index]

                came_from = game.current_room
                next_room = game.roomDict[game.roomDict[game.current_room.id].neighbor[where_to_go]]
                if where_to_go == "north":
                    game.player_model.setheading(90)
                    game.player_model.forward(50)
                elif where_to_go == "south":
                    game.player_model.setheading(270)
                    game.player_model.forward(50)
                elif where_to_go == "west":
                    game.player_model.setheading(180)
                    game.player_model.forward(50)
                else:
                    game.player_model.setheading(0)
                    game.player_model.forward(50)
                game.current_room = next_room
                game.came_from = came_from
                continue
                #self.game(next_room, player, came_from)
            else:
                print("Invalid input")
                time.sleep(1)
                continue
                #self.game(current_room, player, came_from)

    print('Game Over :(')
    return






if __name__ == '__main__':
    startGame = main()
    #startGame.create_map()
    #startGame.game_setup()



# TO DO:
# implement experience
# implement larger map size DONE
# implement what to do after defeating an enemy
#   1. Reset health after defeating enemy?
#   2. Reset health after getting level up? (possibly add potions)
#   3. Increase max health after level up and combine 1 and 2? (kinda like pokemon)
#   4. Slow incremental health while you aren't being attacked.
#   5. Make Rooms into a tree  DONEISH
# Either make weapons have durability and have a seperate weapons "pocket" OR 
#       Less weapons available but they dont lose durability. They lose viability
#       the lower into the dungeon you get by being to weak to defeat the harder enemies.
#   Posibility to either buy/find better weapons, or upgrade your existing weapon to keep using it.

#FeedBack:
# anounce what item you get when you pick it up  DONE
# possibly add multipliers based on level or something 
# enemies drop something
# enemies
# skills
# npc's that will help you (merchants and companions) 
# different classes of player (mage, soldier)
# randomized skills that are offered per level up
# perks for different weapon classes (ranged vs melee vs magic)
# different weapons work well against others (rock paper scissor situation)
