
import random
import turtle
import os
from Objects import *
import time
from Archives.Engine_Old import *


def main():

    game = Game()

    game.game_setup()

    game.player_model.setpos(0,0)
    game.player_model.speed(5)
    game.player_model.pencolor('red')
    game.player_model.pendown()
    #game.create_map()

    while True:
        # For NPC
        skip = False
        
        # PlaceHolder for regenerating health. Potentially replace with potions or something
        if game.player.health < 100:
            if game.player.health > 75:
                diff = 100 - game.player.health
                game.player.health += diff
            else:
                game.player.health += 25

        
        doors_str = ''
        avail_doors = []
        for x in game.current_room.neighbor:
            avail_doors.append(x)
            
            '''
            i += 1
            if i < len(game.current_room.neighbor):
                doors_str += x + ', '
            if i == (len(game.current_room.neighbor) - 1):
                doors_str += 'and '
            if i == len(game.current_room.neighbor):
                doors_str += x
            '''
        #print(has_item + 'There is a door to the ' + doors + '.\n')
        #print('There is a door to the ' + doors_str + '.\n')
        number = 0
        i = 0
        avail_doors.sort()
        for door in avail_doors:
            i += 1
            doors_str += '(' + str(i) + ')' + door + '\n'
        


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

        if game.current_room.npc != None:
            print("You see a person with a shop setup in this room!\n")
            choice = input("(1) Continue on into a different room\n(2) Approach the Shop\n")
            os.system('clear')
            if choice == '1':
                skip = True
                pass
            if choice == '2':
                game.npc_shop()
                continue
            elif not skip:
                print(choice + ' is not an acceptable input')
                continue
        
        # NEXT FLOOR
        if game.current_room.ladder is True:
            print("You find a ladder leading down to the next floor.\nThere seems to be a drop so you can't make it back up after you drop down...\nWhat do you chose?")
            drop_down = input('(1) Take the Plunge!\n(2) Stay on this floor for now\n')
            if drop_down == '1':
                game.new_floor()
                game.player_model.setpos(0, 0)
                game.player_model.speed(5)
                game.player_model.pencolor('red')
                game.player_model.pendown()
                game.floor += 1
            if drop_down == '2':
                os.system('clear')
                pass


        if not game.current_room.has_item or number == '2':
            print("Which door do you decide to enter?\n")
            where_to_go = input(doors_str)
            os.system('clear')
            directions1 = ['north', 'n', 'east', 'e']
            directions2 = ['south', 's', 'west', 'w']
            if where_to_go == 'i':
                game.inventory()
            try:
                direction = avail_doors[int(where_to_go)-1]
            except:
                print("Not a valid input!")
                time.sleep(1)
                os.system('clear')
                continue
                
            if direction in directions1 or direction in directions2:
                if direction not in game.current_room.neighbor.keys():
                    print("no room in that direction\n")
                    continue
                came_from = game.current_room
                next_room = game.roomDict[game.roomDict[game.current_room.id].neighbor[direction]]
                if direction == "north":
                    game.player_model.setheading(90)
                    game.player_model.forward(50)
                elif direction == "south":
                    game.player_model.setheading(270)
                    game.player_model.forward(50)
                elif direction == "west":
                    game.player_model.setheading(180)
                    game.player_model.forward(50)
                else:
                    game.player_model.setheading(0)
                    game.player_model.forward(50)
                game.current_room = next_room
                game.came_from = came_from
                continue
            else:
                print("Invalid input")
                time.sleep(1)
                continue

    print('Game Over :(')
    return


if __name__ == '__main__':
    startGame = main()
    
    # startGame.create_map()
    # startGame.game_setup()

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
 