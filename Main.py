from Objects import *
import time
from Engine import *


def Main(stdscr):

    game = Game()

    selected_inventory = []
    k = 0
    game.main_screen = stdscr
    height, width = game.main_screen.getmaxyx()
    seperation_x = int(width//1.4)
    seperation_y = int(height//1.6)
    
    curses.curs_set(0)
    # Clear and refresh the screen for a blank canvas
    game.main_screen.clear()
    game.main_screen.refresh()

    # Map window setup
    game.map_window = curses.newwin(height-seperation_y-2, width-seperation_x-2, 1, seperation_x+1)
    game.map_border_window = curses.newwin(height-seperation_y, width-seperation_x, 0, seperation_x)
    game.map_border_window.box()
    game.map_border_window.refresh()

    map_height, map_width = game.map_window.getmaxyx()
    map_center_x = int(map_width//2)
    map_center_y = int(map_height//2)
    game.map_center_x = map_center_x
    game.map_center_y = map_center_y

    #Status window
    game.status_window = curses.newwin(height-(height-seperation_y)-2, width-seperation_x-2,height-seperation_y+1, seperation_x+1)
    game.status_border_window = curses.newwin(height-(height-seperation_y), width-seperation_x,height-seperation_y, seperation_x)
    game.status_border_window.box()
    game.status_border_window.refresh()

    #Options window
    game.options_window = curses.newwin(int(0.4*height)-2, seperation_x-2, height-int(0.4*height)+1,1)
    game.options_border_window = curses.newwin(int(0.4*height), seperation_x, height-int(0.4*height), 0)
    game.options_border_window.box()
    game.options_border_window.refresh()

    #Main window
    game.main_window = curses.newwin((height-int(0.4*height))-2, seperation_x-2, 1, 1)
    game.main_border_window = curses.newwin((height-int(0.4*height)), seperation_x, 0, 0)
    game.main_border_window.box()
    game.main_border_window.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    game.game_setup()
    
    game.window_boarders()
    game.map_window.addstr(game.current_room.position[1],game.current_room.position[0], "X")
    game.print_str(game.main_window,"You find yourself in a room and you have nothing but your trusty compass.")
    game.refresh_scr()
    
    curses.napms(1000)
    game.print_str(game.main_window, "You see an old weary man sitting by himself in the corner of the room. You decide to approach him.",2)
    game.refresh_scr()
    
    curses.napms(1000)
    game.print_str(game.main_window, 'Old Man: "Hello there young one, seems you have found yourself in this accursed dungeon as well!'  , 4)
    game.print_str(game.main_window, 'Well I am fed up with this place! Spent too much time down here...', 5)
    game.print_str(game.main_window, 'Maybe you will find more luck than I have. Here, take what little I have and see what you can do.', 6)
    game.print_str(game.main_window, 'Good Luck."', 7)
    game.refresh_scr()
    curses.napms(1000)
    game.print_str(game.main_window, "Press any key to start...", game.main_window.getmaxyx()[0]-4)
    game.refresh_scr()
    x = game.main_screen.getch()
    skip = False
    game.clear_scr()
    
    while (k != ord('q')):
        # For NPC
         
        curses.napms(16)
        game.clear_scr()
        game.refresh_scr()
        game.window_boarders()
        game.map_window.addstr(game.current_room.position[1],game.current_room.position[0], "X", curses.A_BLINK)

        if k == curses.KEY_DOWN and game.current_option != game.options_max -1:
            game.current_option += 1
        if k == curses.KEY_UP and game.current_option != 0:
            game.current_option -= 1
        if k == curses.KEY_LEFT:
            game.current_window = "options_window"
            game.current_option = 0
        if k == curses.KEY_RIGHT:
            game.current_window = "status_window"
            game.current_option = 0
            game.options_max = len(game.player.items.keys())
        if k == 10:
            if game.current_window == "status_window":
                game.player.equiped_weapon = game.player.items[selected_inventory[game.current_option]]
            else:
                game.selected_option = game.current_option
                game.current_option = 0
        k=0
        selected_inventory = game.inventory()
        

        
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
            
        number = 0
        i = 0
        avail_doors.sort()
        for door in avail_doors:
            i += 1
            doors_str += '(' + str(i) + ')' + door + '\n'
        


        # enemy encounter
        if game.current_room.has_enemy:
            game.print_str(game.main_window, 'There is an enemy in this room!')
            game.print_str(game.main_window, 'What do you choose to do?',1)
            enemy_room_options = ["Flee the room the way you came", "Stand and Fight"]
            game.options(game.options_window, enemy_room_options, "options_window")
            if game.current_window != "status_window":
                game.options_max = len(enemy_room_options)
            game.refresh_scr()
            if game.selected_option < 0:
                k = game.main_screen.getch()
                continue
            if game.selected_option == 0:
                next_room = game.came_from
                came_from = game.current_room
                game.current_room = next_room
                game.came_from = came_from
                game.update_pos()
                game.selected_option = -1
                continue
                #self.game(next_room, player, came_from)
            if game.selected_option == 1:
                if game.player.equiped_weapon == None:
                    game.selected_option = -1
                    game.main_window.clear()
                    game.print_str(game.main_window, "Please equip a weapon")
                    game.main_window.refresh()
                    curses.napms(2000)
                    continue
                success = game.combat()
                if (success == 0):
                    break
                game.selected_option = -1
                continue
                #self.game(current_room, player, came_from)
                #self.game(current_room, player, came_from)

        if (game.current_room.npc != None) and skip == False:
            game.print_str(game.main_window,"You see a person with a shop setup in this room!")
            npc_room_options = ["Continue on into a different room", "Approach the Shop"]
            game.options(game.options_window, npc_room_options, "options_window")
            if game.current_window != "status_window":
                game.options_max = len(npc_room_options)
            game.refresh_scr()
            if game.selected_option < 0:
                k = game.main_screen.getch()
                continue
            if game.selected_option == 0:
                game.selected_option = -1
                game.main_window.clear()
                game.options_window.clear()
                game.main_window.refresh()
                game.options_window.refresh()
                skip = True
                continue
            if game.selected_option == 1:
                game.selected_option = -1
                game.npc_shop()
                skip = True
                game.main_window.clear()
                game.options_window.clear()
                game.main_window.refresh()
                game.options_window.refresh()
                continue
        
        # NEXT FLOOR
        if (game.current_room.ladder is True) and skip == False:
            game.print_str(game.main_window, "You find a ladder leading down to the next floor.")
            game.print_str(game.main_window, "There seems to be a drop so you can't make it back up after you drop down...", 1)
            game.print_str(game.main_window, "What do you chose?", 2)
            drop_down_options = ["Stay on this floor for now", "Take the Plunge!"]
            game.options(game.options_window, drop_down_options, "options_window")
            if game.current_window != "status_window":
                game.options_max = len(drop_down_options)
            game.refresh_scr()
            if game.selected_option < 0:
                k = game.main_screen.getch()
                continue
            if game.selected_option == 1:
                game.selected_option = -1
                game.new_floor()
                game.floor += 1
                continue
            if game.selected_option == 0:
                game.selected_option = -1
                skip = True
                continue



        if not game.current_room.has_item or number == '2':
            avail_doors = []
            for x in game.current_room.neighbor:
                avail_doors.append(x)
            
            avail_doors.sort()
            game.print_str(game.main_window,"Which door do you decide to enter?")
            game.options(game.options_window, avail_doors, "options_window")
            if game.current_window != "status_window":
                game.options_max = len(avail_doors)
            directions1 = ['north', 'n', 'east', 'e']
            directions2 = ['south', 's', 'west', 'w']
            game.refresh_scr()
            if game.selected_option < 0:
                k = game.main_screen.getch()
                continue
            
            try:
                direction = avail_doors[game.selected_option]
            except:
                print("Not a valid input!")
                time.sleep(1)
                continue
                
            if direction in directions1 or direction in directions2:
                if direction not in game.current_room.neighbor.keys():
                    game.print_str(game.main_screen,"no room in that direction")
                    game.selected_option = -1
                    continue
                
                came_from = game.current_room
                next_room = game.roomDict[game.roomDict[game.current_room.id].neighbor[direction]]

                game.current_room = next_room
                game.came_from = came_from
                game.update_pos()
                game.selected_option = -1
                skip = False
                continue
            else:
                print("Invalid input")
                time.sleep(1)
                continue
        

    print('Game Over :(')
    return


def main():
    curses.wrapper(Main)

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