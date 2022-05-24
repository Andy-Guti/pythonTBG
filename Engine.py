from Objects import * 
import turtle
import random
import os


class Game:

    def __init__(self):
        self.roomDict = {}
        self.numRooms = 0
        self.player_model = turtle.Turtle()
        self.current_room = Room()
        self.came_from = Room()
        self.player = Player()
        self.floor = 0    

    def create_random_map(self):
        directions = [('north', 'south', (0,50)), ('south', 'north', (0,-50)), ('east', 'west', (50,0)), ('west', 'east', (-50,0))]
        i = 1
        room_amount = 0
        while room_amount < 20:
            reset = False
            game_key_list = list(self.roomDict.keys())
            game_val_list = list(self.roomDict.values())

            rand_num = random.randint(0,3)
            direct = directions[rand_num]

            rand_num2 = random.randint(0, self.numRooms-1)
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
            
            if reset == True:
                continue
            

            temp_room.addNeighbor(direct[0], i)

            new_room = Room()
            new_room.id = i
            new_room.type, new_room.has_enemy, new_room.has_item, new_room.enemy.damage, new_room.item = self.room_setup()

            

            new_room.position = (new_x, new_y)
            self.draw_square(new_room.position)
            self.draw_door(direct[0], new_room.position)

            self.roomDict[i] = new_room
            new_room.addNeighbor(direct[1], temp_room.id)
            self.numRooms += 1
            i += 1
            room_amount += 1

        
        return

    def draw_square(self, position):
        self.player_model.penup()
        self.player_model.speed(100)

        self.player_model.setpos(position)
        self.player_model.setheading(90)

        self.player_model.forward(25)
        self.player_model.pendown()
        self.player_model.setheading(180)
        self.player_model.forward(25)
        self.player_model.setheading(270)
        self.player_model.forward(50)
        self.player_model.setheading(0)
        self.player_model.forward(50)
        self.player_model.setheading(90)
        self.player_model.forward(50)
        self.player_model.setheading(180)
        self.player_model.forward(25)

        self.player_model.penup()

        return

    def draw_door(self, direction, position):
        self.player_model.setpos(position)
        self.player_model.pencolor("green")
        self.player_model.pensize(3)
        if direction == 'north':
            self.player_model.setheading(270)
            self.player_model.forward(25)
            self.player_model.setheading(180)
            self.player_model.forward(10)
            self.player_model.pendown()
            self.player_model.backward(20)
            self.player_model.penup()

        if direction == 'south':
            self.player_model.setheading(90)
            self.player_model.forward(25)
            self.player_model.setheading(180)
            self.player_model.forward(10)
            self.player_model.pendown()
            self.player_model.backward(20)
            self.player_model.penup()

        if direction == 'east':
            self.player_model.setheading(180)
            self.player_model.forward(25)
            self.player_model.setheading(90)
            self.player_model.forward(10)
            self.player_model.pendown()
            self.player_model.backward(20)
            self.player_model.penup()

        if direction == 'west':
            self.player_model.setheading(0)
            self.player_model.forward(25)
            self.player_model.setheading(90)
            self.player_model.forward(10)
            self.player_model.pendown()
            self.player_model.backward(20)
            self.player_model.penup()
        
        self.player_model.pencolor('black')
        self.player_model.pensize(1)
        return

    def insert_item(self):

        rand_num2 = random.randint(0, 100)

        # Need to change this to include different items and not just weapons
        if 90 > rand_num2 > 20:
            rand_item = Weapon()
            rand_item.type = 'good'
            rand_item.damage = random.randint(15, 25)
            good_items = ['a Shiny Sword', 'a Swiss Army Knife', 'a Super Charged Tazer','LOTR Mace']
            rand_name_num = random.randint(0, len(good_items) - 1)
            rand_name = good_items[rand_name_num]
            rand_item.name = rand_name
            rand_item.durability = 12

        if rand_num2 <= 20:
            rand_item = Weapon()
            rand_item.type = 'bad'
            rand_item.damage = random.randint(5, 12)
            bad_items = ['a Nasty Knife', 'a Flare Gun', 'The Pointiest of Sticks', 'a Shabby Sickle','Bear Spray']
            rand_name_num = random.randint(0, len(bad_items) - 1)
            rand_name = bad_items[rand_name_num]
            rand_item.name = rand_name
            rand_item.durability = 6

        if rand_num2 >= 90:
            rand_item = Weapon()
            rand_item.type = 'great'
            rand_item.damage = random.randint(45, 60)
            great_items = ['Cheese Slicing Katana', 'Bazooka', "Dead Man's Dagger", 'Carnivorous Cleaver',"Legolas' Bow"]
            rand_name_num = random.randint(0, len(great_items) - 1)
            rand_name = great_items[rand_name_num]
            rand_item.name = rand_name
            rand_item.durability = 16

        return rand_item
            
    def room_setup(self):
        rand_num1 = random.randint(0,100)
        rand_num2 = random.randint(0,100)

        room_type = ''
        has_enemy = False
        has_item = False
        enemy_damage = 0
        item = Weapon()

        if rand_num1 > 33:
            room_type = 'easy'
        if rand_num1 <= 33:
            room_type = 'hard'
            has_enemy = True
            enemy_damage = random.randint(15,30)
        if rand_num2 > 10:
            has_item = True
            item = self.insert_item()

        return (room_type, has_enemy, has_item, enemy_damage, item)
    
    def game_setup(self):
        self.current_room = Room()
        self.current_room.id = 0
        self.current_room.type = "easy"
        self.current_room.has_enemy = False
        self.current_room.has_item = False
        self.current_room.position = (0,0)

        self.draw_square(self.current_room.position)

        self.came_from = Room()
        self.roomDict[self.current_room.id] = self.current_room
        self.numRooms += 1
        #self.create_game()
        self.create_random_map()
        #self.med_game()
        self.player = Player()
        os.system('clear')
        print("\n\nYou find yourself in a room and you have nothing but your trusty compass.")
        #self.game(start_room, player, came_from)
            
    def combat(self):
        # combat system
        print('You decide to fight the enemy in front of you, choose which weapon you would like to use to attack!')
        item_names = ''
        i = 0
        for x in self.player.items:
            i += 1
            if i < (len(self.player.items)):
                item_names += '(' + str(i) + ') ' + x.name + '       Durability: ' + str(x.durability) + '       Power: ' + str(x.damage) + '\n'
            if i == len(self.player.items):
                item_names += '(' + str(i) + ') ' + x.name + '       Durability: ' + str(x.durability) + '       Power: ' + str(x.damage) 

        weapon = input('your items are:\n' + item_names + '\n')
        #while weapon 
        os.system('clear')
        chosenWeapon = self.player.items[int(weapon) - 1]
        enemyDamage = self.current_room.enemy.damage

        while self.current_room.has_enemy is True:
            if self.current_room.enemy.health <= 0:
                self.current_room.has_enemy = False
                print('You have defeated the enemy!')
                break
            if self.player.health <= 0:
                print('After a valiant effort, you have been slain. It is a sad day for you indeed')
                return 0
            else:
                print("Enemy Health: "+str(self.current_room.enemy.health)+'    Your Health: '+str(self.player.health)+'\n\n')
                choice = input('  (1) Attack\n  (2) Flee\n  (3) Switch Weapon\n')
                os.system('clear')
                if choice == '1':
                    weaponDamage = chosenWeapon.damage
                    self.current_room.enemy.health -= weaponDamage
                    self.player.health -= enemyDamage
                    chosenWeapon.durability -= 2
                    print("You deal " + str(weaponDamage) + ' damage\n')
                    print("The enemy strikes you and deals " + str(enemyDamage) + " damage\n")
                    if ((chosenWeapon.durability <=0) and (self.current_room.enemy.health<=0)):
                        continue
                    elif (chosenWeapon.durability<=0):
                        print("Your weapon broke! Choose new weapon. \n")
                        self.player.items.remove(chosenWeapon)
                        choice = '3'
                if choice == '2':
                    break
                if choice == '3':
                    item_names = ''
                    i = 0
                    for x in self.player.items:
                        i += 1
                        if i < (len(self.player.items)):
                            item_names += '(' + str(i) + ') ' + x.name + '\n'
                        if i == len(self.player.items):
                            item_names += '(' + str(i) + ') ' + x.name
                    weapon = input('your items are:\n' + item_names + '\n')
                    os.system('clear')
                    chosenWeapon = self.player.items[int(weapon) - 1]
                    weaponDamage = chosenWeapon.damage
        return 1

    def inventory(self):
        return

    


    """
    def create_game(self):
        key_list = list(self.roomDict.keys())
        val_list = list(self.roomDict.values())
        directions1 = ['north', 'east']
        directions2 = ['south', 'west']
        i = 1
        for x in directions1:
            self.current_room.addNeighbor(x, i)
            room1 = Room()
            room1.id = i

            room1.type, room1.has_enemy, room1.has_item, room1.enemy.damage, room1.item = self.room_setup()

            if x == 'north':
                room1.position = (0,50)
            if x == 'east':
                room1.position = (50,0)
            
            #self.create_square(room1.position)
            
            self.roomDict[i] = room1
            index = directions1.index(x)
            room1.addNeighbor(directions2[index], key_list[val_list.index(self.current_room)])
            self.numRooms += 1
            i += 1

        for y in directions2:
            self.current_room.addNeighbor(y, i)
            room1 = Room()
            room1.id = i

            room1.type, room1.has_enemy, room1.has_item, room1.enemy.damage, room1.item = self.room_setup()

            if y == 'south':
                room1.position = (0,-50)
            if y == 'west':
                room1.position = (-50,0)

            #self.create_square(room1.position)

            self.roomDict[i] = room1
            index = directions2.index(y)
            room1.addNeighbor(directions1[index], key_list[val_list.index(self.current_room)])
            self.numRooms += 1
            i += 1

    def med_game(self):
        for direction, id in self.current_room.neighbor.items():

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
                    placeHolder3 = self.roomDict[self.current_room.neighbor["west"]]
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
                    placeHolder3 = self.roomDict[self.current_room.neighbor["east"]]
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
                        placeHolder2.item = self.insert_item()
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
                        placeHolder2.item = self.insert_item()
                    #end create new room
                    placeHolder2.addNeighbor("east",id)
                    placeHolder3 = self.roomDict[self.current_room.neighbor["west"]]
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
                        placeHolder2.item = self.insert_item()
                    #end create new room
                    placeHolder2.addNeighbor("west",id)
                    placeHolder3 = self.roomDict[self.current_room.neighbor["east"]]
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
                        placeHolder2.item = self.insert_item()
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
                        placeHolder2.item = self.insert_item()
                    #end create new room
                    placeHolder2.addNeighbor("south",id)
                    placeHolder3 = self.roomDict[self.current_room.neighbor["north"]]
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
                        placeHolder2.item = self.insert_item()
                    #end create new room
                    placeHolder2.addNeighbor("north",id)
                    placeHolder3 = self.roomDict[self.current_room.neighbor["south"]]
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
                        placeHolder2.item = self.insert_item()
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
                        placeHolder2.item = self.insert_item()
                    #end create new room
                    placeHolder2.addNeighbor("south",id)
                    placeHolder3 = self.roomDict[self.current_room.neighbor["north"]]
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
                        placeHolder2.item = self.insert_item()
                    #end create new room
                    placeHolder2.addNeighbor("north",id)
                    placeHolder3 = self.roomDict[self.current_room.neighbor["south"]]
                    placeHolder3.addNeighbor("west",newids)
                    placeHolder2.addNeighbor("east",placeHolder3.id)
                    self.numRooms += 1



        return

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

    def create_map(self):
        window = turtle.Screen()
        sprite = self.player_model
        sprite.penup()
        sprite.speed(100)
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
    """
 



  