import curses
import random
from Objects import *
import time
class Game:

    def __init__(self):
        self.roomDict = {}
        self.numRooms = 0
        self.current_room = Room()
        self.came_from = Room()
        self.player = Player()
        self.floor = 0
        self.center_x = 0
        self.center_y = 0
        self.map_center_x = 0
        self.map_center_y = 0
        self.main_screen = None
        self.map_window = None
        self.status_window = None
        self.options_window = None
        self.main_window = None
        self.current_window = str
        self.current_option = 0
        self.selected_option = -1
        self.options_max = 0
    
    def game_setup(self):
        blank_dict = {}
        self.current_window = "options_window"
        self.roomDict = blank_dict
        self.current_room = Room()
        self.current_room.id = 0
        self.current_room.type = "easy"
        self.current_room.has_enemy = False
        self.current_room.has_item = False
        self.current_room.position = (self.map_center_x, self.map_center_y)
        
        #self.draw_square(stdscr, 6, 4, self.current_room.position[0], self.current_room.position[1])

        self.came_from = Room()
        self.roomDict[self.current_room.id] = self.current_room
        self.numRooms += 1
        # self.create_game()
        self.create_random_map()
        # self.med_game()
    def print_str(self, stdscr, str, y=0, x=0):
        stdscr.addstr(y+2,x+2,str)
        return
    #not currently used/should be updated for new map_window
    def update_pos(self):
        old_center_x, old_center_y = self.roomDict[0].position
        self.roomDict[0].position = (self.map_center_x, self.map_center_y)
        for room in self.roomDict.values():
            diff_x = old_center_x - room.position[0]
            new_x = self.roomDict[0].position[0] - diff_x
            diff_y = old_center_y - room.position[1]
            new_y = self.roomDict[0].position[1] - diff_y
            
            room.position = (new_x,new_y)

        return

    def draw_map(self,stdscr):
        try:
            for room in self.roomDict.values():
                self.draw_square(stdscr,6,4,room.position[0],room.position[1])
        except:
            return False

        return True

    def room_setup(self, modifier):
        rand_num1 = random.randint(0, 100)
        rand_num2 = random.randint(0, 100)

        room_type = ""
        has_enemy = False
        #has_item = False
        enemy_damage = 0
        #item = Weapon()

        if rand_num1 > 33:
            room_type = "easy"
        if rand_num1 <= 33:
            room_type = "hard"
            has_enemy = True
            enemy_damage = random.randint(8, 20) + modifier
        """
        if rand_num2 > 10:
            has_item = True
            item = self.insert_item()
        """

        #return (room_type, has_enemy, has_item, enemy_damage, item)
        return (room_type, has_enemy, enemy_damage)
    
    def create_random_map(self):
        directions = [
            ("north", "south", (0, -3)),
            ("south", "north", (0, 3)),
            ("east", "west", (6, 0)),
            ("west", "east", (-6, 0)),
        ]
        i = 1
        room_amount = 0
        room_max = 10
        npc_int = random.randint(round((room_max/6)-2), round(room_max/6))
        down_shaft_int = random.randint(round((room_max/2)-2), round(room_max/2))
        floor_modifier = self.floor * 1.275

        while room_amount < room_max:
            reset = False
            # game_key_list = list(self.roomDict.keys())
            game_val_list = list(self.roomDict.values())

            rand_num = random.randint(0, 3)
            direct = directions[rand_num]

            rand_num2 = random.randint(0, self.numRooms - 1)
            temp_room = game_val_list[rand_num2]

            if len(temp_room.takenNeighbors()) == 4:
                continue
            elif direct[0] in temp_room.takenNeighbors():
                continue

            temp_x, temp_y = temp_room.position
            new_x, new_y = direct[2]
            new_x = temp_x + new_x
            new_y = temp_y + new_y

            for room in game_val_list:
                if room.position == (new_x, new_y):
                    reset = True
                    break

            if reset:
                continue

            temp_room.addNeighbor(direct[0], i)

            new_room = Room()
            new_room.id = i
            (
                new_room.type,
                new_room.has_enemy,
                #new_room.has_item,
                new_room.enemy.damage,
                #new_room.item,
            ) = self.room_setup(floor_modifier)
            new_room.enemy.health += floor_modifier
            
            if self.floor % 3 == 0:
                if npc_int == room_amount:
                    if not new_room.has_enemy:
                        new_npc = Npc()
                        new_npc.create_inventory()
                        new_room.npc = new_npc
                    else:
                        npc_int += 1
            if room_amount == down_shaft_int:
                if new_room.npc is None:
                    new_room.ladder = True
                else:
                    down_shaft_int += 1
            new_room.position = (new_x, new_y)
            #self.draw_square(stdscr,6,4,new_x,new_y)
            #stdscr.addstr(new_y, new_x, "X")
            #self.draw_door(direct[0], new_room.position)

            self.roomDict[i] = new_room
            new_room.addNeighbor(direct[1], temp_room.id)
            #stdscr.refresh()
            self.numRooms += 1
            i += 1
            room_amount += 1
        return

    def draw_square(self, stdscr,box_width, box_height, center_x, center_y):
        
        for i in range(box_width):
                stdscr.addstr(center_y-int(box_height//2), center_x-int(box_width//2)+i, "#")
                stdscr.addstr(center_y+int(box_height//2)-1, center_x-int(box_width//2)+i, "#")
        for j in range(box_height):
            stdscr.addstr(center_y-int(box_height//2)+j,center_x-int(box_width//2),"#")
            stdscr.addstr(center_y-int(box_height//2)+j,center_x+int(box_width//2),"#")
        return

    def new_floor(self):
        self.roomDict = {}
        self.numRooms = 0
        self.current_window = "options_window"
        self.current_room = Room()
        self.current_room.id = 0
        self.current_room.type = "easy"
        self.current_room.has_enemy = False
        self.current_room.has_item = False
        self.current_room.position = (self.map_center_x, self.map_center_y)

        #self.draw_square(self.current_room.position)

        self.came_from = Room()
        self.roomDict[self.current_room.id] = self.current_room
        self.numRooms += 1
        # self.create_game()
        self.create_random_map()
        return
    # needs some tuning
    def combat(self):
        # combat system
        k=0
        self.current_option = 0
        self.selected_option = -1
        self.print_str(self.main_window, "You decide to fight the enemy in front of you!")
        

        while self.current_room.has_enemy is True:
            self.clear_scr()
            self.refresh_scr()
            self.window_boarders()
            self.map_window.addstr(self.current_room.position[1],self.current_room.position[0], "X", curses.A_BLINK)

            if k == curses.KEY_DOWN:
                self.current_option += 1
            if k == curses.KEY_UP:
                self.current_option -= 1
            if k == curses.KEY_LEFT:
                self.current_window = "options_window"
                self.current_option = 0
            if k == curses.KEY_RIGHT:
                self.current_window = "status_window"
                self.current_option = 0
            if k == 10:
                if self.current_window == "status_window":
                    self.player.equiped_weapon = self.player.items[selected_inventory[self.current_option]]
                else:
                    self.selected_option = self.current_option
                    self.current_option = 0
            k=0
            selected_inventory = self.inventory()
            
            chosenWeapon = self.player.equiped_weapon
            enemyDamage = self.current_room.enemy.damage

            if self.current_room.enemy.health <= 0:
                self.current_room.has_enemy = False
                self.print_str(self.main_window,"You have defeated the enemy!")
                self.print_str(self.main_window,"The enemy dropped " + str(self.current_room.enemy.gold) + " gold!", 1)
                self.main_window.refresh()
                curses.napms(3000)
                self.player.gold += self.current_room.enemy.gold
                break
            if self.player.health <= 0:
                self.print_str(self.main_window,"After a valiant effort, you have been slain. It is a sad day for you indeed")
                self.main_window.refresh()
                return 0
            else:
                self.print_str(self.main_window, "Enemy Health: " + str(self.current_room.enemy.health))
                self.options(self.options_window, ["Attack","Flee"], "options_window")

                if self.selected_option < 0:
                    k = self.main_screen.getch()
                    continue

                if self.selected_option == 0:
                    weaponDamage = round(chosenWeapon.damage)
                    self.current_room.enemy.health = round(self.current_room.enemy.health - weaponDamage)
                    self.player.health -= round(enemyDamage)
                    chosenWeapon.durability -= 1.5
                    self.print_str(self.main_window, "You deal " + str(weaponDamage) + " damage")
                    self.print_str(self.main_window, "The enemy strikes you and deals " + str(round(enemyDamage)) + " damage", 1)
                    self.refresh_scr()
                    curses.napms(2000)
                    if (chosenWeapon.durability <= 0) and (
                        self.current_room.enemy.health <= 0
                    ):
                        self.print_str(self.main_window, "Your weapon broke!", 2)
                        self.player.items.remove(chosenWeapon)
                        curses.napms(2000)
                        continue
                    elif chosenWeapon.durability <= 0:
                        self.print_str(self.main_window, "Your weapon broke! Choose new weapon. ", 2)
                        del self.player.items[chosenWeapon.name]
                    self.selected_option = -1
                    continue
                if self.selected_option == 1:
                    break
        return 1

    def inventory(self):
        height, width = self.status_window.getmaxyx()
        gold = "Gold: " + str(self.player.gold)
        health = "Health: " + str(self.player.health)
        item_names = []
        for item in self.player.items.keys():
            item_names.append(item)

        self.status_window.addstr(2,width-(len(gold)+3),gold)
        self.status_window.addstr(2,2,health)
        self.print_str(self.status_window, "Inventory",4)
        self.options(self.status_window,item_names,"status_window",6)

        return item_names
    #needs some tuning
    def npc_shop(self):
        
        option_int = 0
        k=0
        buy = False

        while(k != ord('q')):

            self.clear_scr()
            self.window_boarders()
            self.refresh_scr()
            
            self.map_window.addstr(self.current_room.position[1],self.current_room.position[0], "X", curses.A_BLINK)

            if k == curses.KEY_DOWN and self.current_option != self.options_max -1:
                self.current_option += 1
            if k == curses.KEY_UP and self.current_option != 0:
                self.current_option -= 1
            if k == curses.KEY_LEFT:
                self.current_window = "options_window"
                self.current_option = 0
            if k == curses.KEY_RIGHT:
                self.current_window = "status_window"
                self.current_option = 0
            if k == 10:
                if self.current_window == "status_window":
                    self.player.equiped_weapon = self.player.items[selected_inventory[self.current_option]]
                else:
                    self.selected_option = self.current_option
                    self.current_option = 0
            k=0
            selected_inventory = self.inventory()
           
            if option_int == 0:
                self.clear_scr()
                self.print_str(self.main_window, "Welcome to my shop!")
                self.print_str(self.main_window, "Feel free to browse my selection and if you have something nice ill buy it off ya too!", 1)
                self.window_boarders()
                self.refresh_scr()
                self.options(self.options_window, ["Buy", "Sell", "Leave"], "options_window")
                self.options_max = 3
                if self.selected_option < 0:
                    k = self.main_screen.getch()
                    continue
                if self.selected_option == 0:
                    self.selected_option = -1
                    option_int = 1
                    continue
                if self.selected_option == 1:
                    self.selected_option = -1
                    option_int = 2
                    # needs implementation
                    continue
                if self.selected_option == 2:
                    self.selected_option = -1
                    return

            # Buy Mechanics
            if option_int == 1:
                
                item_options = []
                self.print_str(self.main_window, "Here's what I've got for ya today:")
                for x in self.current_room.npc.inventory:
                    
                    price_str = "Price: " + str(x.price)
                    dura_str = "Durability: " + str(x.durability)
                    pow_str = "Power: " + str(x.damage)
                    item_options.append(x.name + "     " + price_str + "     " + dura_str + "     " + pow_str)
                    
                item_options.append("Nevermind")
                self.options_max = len(item_options)
                self.current_window = "main_window"
                self.options(self.main_window, item_options, "main_window")

                if self.selected_option < 0:
                    k = self.main_screen.getch()
                    continue
                elif self.selected_option == len(item_options)-1:
                    self.selected_option = -1
                    option_int = 0
                    self.current_window = "options_window"
                    continue
                else:
                    
                    if self.current_room.npc.inventory[self.selected_option].price > self.player.gold:
                        self.main_window.clear()
                        self.print_str(self.main_window, "You don't have enough money for that!")
                        self.main_window.box()
                        self.main_window.refresh()
                        curses.napms(2000)
                        self.selected_option = -1
                        continue
                    else:
                        self.player.items[self.current_room.npc.inventory[self.selected_option].name] = self.current_room.npc.inventory[self.selected_option]
                        self.player.gold -= self.current_room.npc.inventory[self.selected_option].price
                        self.main_window.clear()
                        self.print_str(self.main_window,"You obtained " + self.current_room.npc.inventory[self.selected_option].name)
                        self.main_window.box()
                        self.main_window.refresh()
                        del self.current_room.npc.inventory[self.selected_option]
                        curses.napms(2000)
                        self.selected_option = -1
                        continue
            if option_int == 2:
                #selling mechanics
                inventory_item_options = []
                inventory_item_names = []
                for key, val in self.player.items.items():
                    inventory_item_names.append(key)
                    price_str = "Price: " + str(val.price)
                    dura_str = "Durability: " + str(val.durability)
                    pow_str = "Power: " + str(val.damage)
                    inventory_item_options.append(key + "     " + price_str + "     " + dura_str + "     " + pow_str)
                    
                inventory_item_options.append("Nevermind")
                self.options_max = len(inventory_item_options)
                self.current_window = "main_window"
                self.options(self.main_window, inventory_item_options, "main_window")

                if self.selected_option < 0:
                    k = self.main_screen.getch()
                    continue
                elif self.selected_option == len(inventory_item_options)-1:
                    self.selected_option = -1
                    option_int = 0
                    self.current_window = "options_window"
                    continue
                else:
                    self.player.gold += self.player.items[inventory_item_names[self.selected_option]].price
                    self.current_room.npc.inventory.append(self.player.items[inventory_item_names[self.selected_option]])
                    del self.player.items[inventory_item_names[self.selected_option]]
                    self.main_window.clear()
                    self.print_str(self.main_window,"You Sold " + inventory_item_names[self.selected_option])
                    self.main_window.box()
                    self.main_window.refresh()
                    curses.napms(2000)
                    self.selected_option = -1
                    continue

                
    
    def clear_scr(self):
        self.map_window.clear()
        self.status_window.clear()
        self.options_window.clear()
        self.main_window.clear()
        self.main_screen.clear()
        return

    def refresh_scr(self):
        self.main_screen.refresh()
        self.map_window.refresh()
        self.status_window.refresh()
        self.options_window.refresh()
        self.main_window.refresh()
        return

    def window_boarders(self):
        #height, width = stdscr.getmaxyx()
        #center_x = int(width//2.3)
        #center_y = int(height//2.3)

        #map_height, map_width = self.map_window.getmaxyx()
        #map_center_x = int(map_width//2)
        #map_center_y = int(map_height//2)
        #self.map_center_x = map_center_x
        #self.map_center_y = map_center_y

        #self.update_pos()

        
        
        #self.draw_square(stdscr, box_width, box_height, center_x, center_y)
        self.draw_map(self.map_window)
        #map_window.border()
        self.map_window.box()
        self.status_window.box()
        self.options_window.box()
        self.main_window.box()
        # Refresh the screen
        
        
        return

    def options(self, stdscr, options, which_window, y=0, x=0):

        
        for i, option in enumerate(options):
            first = "[ ]"
            if which_window == "status_window":
                if self.player.equiped_weapon != None:
                    if option == self.player.equiped_weapon.name:
                        first = "[Equiped]"
                        stdscr.addstr(y+i+2, x+2, first)
                    else:
                        stdscr.addstr(y+i+2, x+2, first )
                else:
                    stdscr.addstr(y+i+2, x+2, first )
            else:
                stdscr.addstr(y+i+2, x+2, first)
            if which_window == self.current_window:
                if i == self.current_option:
                    stdscr.addstr(y+i+2, x+len(first)+2, option, curses.color_pair(3) | curses.A_BLINK)
                else:
                    stdscr.addstr(y+i+2, x+len(first)+2, option)
            else:
                stdscr.addstr(y+i+2, x+len(first)+2, option)
        self.refresh_scr()
        return

    def Main(self, stdscr):
        k = 0
        cursor_x = 0
        cursor_y = 0
        temp_options= ["Flee the room the way you came", "Stand and Fight"]
        # Box size
        box_width = 6
        box_height = 4
        self.main_screen = stdscr
        height, width = self.main_screen.getmaxyx()
        seperation_x = int(width//1.4)
        seperation_y = int(height//1.6)
        
        # Clear and refresh the screen for a blank canvas
        self.main_screen.clear()
        self.main_screen.refresh()

        # Map window setup
        self.map_window = curses.newwin(height-seperation_y, width-seperation_x, 0, seperation_x)
        map_height, map_width = self.map_window.getmaxyx()
        map_center_x = int(map_width//2)
        map_center_y = int(map_height//2)
        self.map_center_x = map_center_x
        self.map_center_y = map_center_y

        #Status window
        self.status_window = curses.newwin(height-(height-seperation_y), width-seperation_x,height-seperation_y, seperation_x)

        #Options window
        self.options_window = curses.newwin(int(0.4*height), seperation_x, height-int(0.4*height), 0)

        #Main window
        self.main_window = curses.newwin((height-int(0.4*height)), seperation_x, 0, 0)

        # Start colors in curses
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
        
        self.game_setup()
        
        # Loop where k is the last character pressed
        while (k != ord('q')):
            
            # Initialization
            
                
            
            # moving curses
            self.clear_scr()
            if k == curses.KEY_DOWN:
                self.current_option += 1
            elif k == curses.KEY_UP:
                self.current_option -= 1
            elif k == 10:
                self.new_floor()
            
            self.window_boarders()
            #self.print_str(self.options_window,"Hello")
            self.options(self.options_window,temp_options, "options_window")
            self.map_window.addstr(self.current_room.position[1],self.current_room.position[0], "X")
            self.refresh_scr()
            
            # Wait for next input
            k = self.main_screen.getch()

    def main_1(self):
        curses.wrapper(self.Main)

if __name__ == "__main__":
    test = Game()
    test.main_1()