from Objects import *
import turtle
import random
import os
import time


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
        directions = [
            ("north", "south", (0, 50)),
            ("south", "north", (0, -50)),
            ("east", "west", (50, 0)),
            ("west", "east", (-50, 0)),
        ]
        i = 1
        room_amount = 0
        room_max = 7
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
        self.player_model.pencolor('black')

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
        if direction == "north":
            self.player_model.setheading(270)
            self.player_model.forward(25)
            self.player_model.setheading(180)
            self.player_model.forward(10)
            self.player_model.pendown()
            self.player_model.backward(20)
            self.player_model.penup()

        if direction == "south":
            self.player_model.setheading(90)
            self.player_model.forward(25)
            self.player_model.setheading(180)
            self.player_model.forward(10)
            self.player_model.pendown()
            self.player_model.backward(20)
            self.player_model.penup()

        if direction == "east":
            self.player_model.setheading(180)
            self.player_model.forward(25)
            self.player_model.setheading(90)
            self.player_model.forward(10)
            self.player_model.pendown()
            self.player_model.backward(20)
            self.player_model.penup()

        if direction == "west":
            self.player_model.setheading(0)
            self.player_model.forward(25)
            self.player_model.setheading(90)
            self.player_model.forward(10)
            self.player_model.pendown()
            self.player_model.backward(20)
            self.player_model.penup()

        self.player_model.pencolor("black")
        self.player_model.pensize(1)
        return

    # not used currently
    def insert_item(self):

        rand_num2 = random.randint(0, 100)

        # Need to change this to include different items and not just weapons
        if 90 > rand_num2 > 20:
            rand_item = Weapon()
            rand_item.type = "good"
            rand_item.damage = random.randint(15, 25)
            good_items = [
                "a Shiny Sword",
                "a Swiss Army Knife",
                "a Super Charged Tazer",
                "LOTR Mace",
            ]
            rand_name_num = random.randint(0, len(good_items) - 1)
            rand_name = good_items[rand_name_num]
            rand_item.name = rand_name
            rand_item.durability = 12

        if rand_num2 <= 20:
            rand_item = Weapon()
            rand_item.type = "bad"
            rand_item.damage = random.randint(5, 12)
            bad_items = [
                "a Nasty Knife",
                "a Flare Gun",
                "The Pointiest of Sticks",
                "a Shabby Sickle",
                "Bear Spray",
            ]
            rand_name_num = random.randint(0, len(bad_items) - 1)
            rand_name = bad_items[rand_name_num]
            rand_item.name = rand_name
            rand_item.durability = 6

        if rand_num2 >= 90:
            rand_item = Weapon()
            rand_item.type = "great"
            rand_item.damage = random.randint(45, 60)
            great_items = [
                "Cheese Slicing Katana",
                "Bazooka",
                "Dead Man's Dagger",
                "Carnivorous Cleaver",
                "Legolas' Bow",
            ]
            rand_name_num = random.randint(0, len(great_items) - 1)
            rand_name = great_items[rand_name_num]
            rand_item.name = rand_name
            rand_item.durability = 16

        return rand_item

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

    def new_floor(self):
        self.roomDict = {}
        self.numRooms = 0
        self.player_model.clear()

        self.current_room = Room()
        self.current_room.id = 0
        self.current_room.type = "easy"
        self.current_room.has_enemy = False
        self.current_room.has_item = False
        self.current_room.position = (0, 0)

        self.draw_square(self.current_room.position)

        self.came_from = Room()
        self.roomDict[self.current_room.id] = self.current_room
        self.numRooms += 1
        # self.create_game()
        self.create_random_map()
        return

    def game_setup(self):
        self.current_room = Room()
        self.current_room.id = 0
        self.current_room.type = "easy"
        self.current_room.has_enemy = False
        self.current_room.has_item = False
        self.current_room.position = (0, 0)

        self.draw_square(self.current_room.position)

        self.came_from = Room()
        self.roomDict[self.current_room.id] = self.current_room
        self.numRooms += 1
        # self.create_game()
        self.create_random_map()
        # self.med_game()
        self.player = Player()
        os.system("clear")
        print(
            "\n\nYou find yourself in a room and you have nothing but your trusty compass."
        )
        time.sleep(4)
        print(
            "\nYou see an old weary man sitting by himself in the corner of the room. You decide to approach him."
        )
        time.sleep(4)
        print(
            '\n\nOld Man: "Hello there young one, seems you have found yourself in this accursed dungeon as well!\nWell I am fed up with this place! Spent too much time down here... \nMaybe you will find more luck than I have. Here, take what little I have and see what you can do.\nGood Luck."\n'
        )
        time.sleep(6)
        print("You recieved 10 gold, and a rusty sword!")
        # self.game(start_room, player, came_from)

    def combat(self):
        # combat system
        print(
            "You decide to fight the enemy in front of you, choose which weapon you would like to use to attack!"
        )
        item_names = ""
        i = 0
        for x in self.player.items:
            i += 1
            if i < (len(self.player.items)):
                item_names += (
                    "("
                    + str(i)
                    + ") "
                    + x.name
                    + "       Durability: "
                    + str(x.durability)
                    + "       Power: "
                    + str(x.damage)
                    + "\n"
                )
            if i == len(self.player.items):
                item_names += (
                    "("
                    + str(i)
                    + ") "
                    + x.name
                    + "       Durability: "
                    + str(x.durability)
                    + "       Power: "
                    + str(x.damage)
                )

        weapon = input("your items are:\n" + item_names + "\n")
        # while weapon
        os.system("clear")
        chosenWeapon = self.player.items[int(weapon) - 1]
        enemyDamage = self.current_room.enemy.damage

        while self.current_room.has_enemy is True:
            if self.current_room.enemy.health <= 0:
                self.current_room.has_enemy = False
                print("You have defeated the enemy!\n")
                print("The enemy dropped " + str(self.current_room.enemy.gold) + " gold!")
                self.player.gold += self.current_room.enemy.gold
                break
            if self.player.health <= 0:
                print(
                    "After a valiant effort, you have been slain. It is a sad day for you indeed"
                )
                return 0
            else:
                print(
                    "Enemy Health: "
                    + str(self.current_room.enemy.health)
                    + "    Your Health: "
                    + str(self.player.health)
                    + "\n\n"
                )
                choice = input("  (1) Attack\n  (2) Flee\n  (3) Switch Weapon\n")
                os.system("clear")
                if choice == "1":
                    weaponDamage = chosenWeapon.damage
                    self.current_room.enemy.health -= weaponDamage
                    self.player.health -= enemyDamage
                    chosenWeapon.durability -= 1.5
                    print("You deal " + str(weaponDamage) + " damage\n")
                    print(
                        "The enemy strikes you and deals "
                        + str(enemyDamage)
                        + " damage\n"
                    )
                    if (chosenWeapon.durability <= 0) and (
                        self.current_room.enemy.health <= 0
                    ):
                        print("Your weapon broke!\n")
                        self.player.items.remove(chosenWeapon)
                        continue
                    elif chosenWeapon.durability <= 0:
                        print("Your weapon broke! Choose new weapon. \n")
                        self.player.items.remove(chosenWeapon)
                        choice = "3"
                if choice == "2":
                    break
                if choice == "3":
                    item_names = ""
                    i = 0
                    for x in self.player.items:
                        i += 1
                        if i < (len(self.player.items)):
                            item_names += "(" + str(i) + ") " + x.name + "\n"
                        if i == len(self.player.items):
                            item_names += "(" + str(i) + ") " + x.name
                    weapon = input("your items are:\n" + item_names + "\n")
                    os.system("clear")
                    chosenWeapon = self.player.items[int(weapon) - 1]
                    weaponDamage = chosenWeapon.damage
        return 1

    # Need to implement
    def inventory(self):
        item_names = ''
        i = 0
        for x in self.player.items:
            i += 1
            if i < (len(self.player.items)):
                item_names += '(' + str(i) + ') ' + x.name + '       Durability: ' + str(x.durability) + '       Power: ' + str(x.damage) + '\n'
            if i == len(self.player.items):
                item_names += '(' + str(i) + ') ' + x.name + '       Durability: ' + str(x.durability) + '       Power: ' + str(x.damage)

        print('your items are:\n' + item_names + '\n')
        print("Gold: " + str(self.player.gold) + "\n")
        input('\n\n\n press any key to continue...\n')
        return

    def npc_shop(self):
        print("Welcome to my shop!\nFeel free to browse my selection and if you have something nice ill buy it off ya too!\n")
        while True:
            choice = input("(1) Buy\n(2) Sell\n(3) Leave\n")
            os.system('clear')
            if choice == '1':
                item_names = ""
                i = 0
                for x in self.current_room.npc.inventory:
                    i += 1
                    if i < (len(self.current_room.npc.inventory)):
                        item_names += '(' + str(i) + ') ' + x.name + '     Price: ' + str(x.price) + '\n       Durability: ' + str(x.durability) + '       Power: ' + str(x.damage) + '\n\n'
                    if i == len(self.current_room.npc.inventory):
                        item_names += '(' + str(i) + ') ' + x.name + '     Price: ' + str(x.price) + '\n       Durability: ' + str(x.durability) + '       Power: ' + str(x.damage)
                print("Your Gold: " + str(self.player.gold) + "\n\n")
                buy = input("Here's what I've got for ya today:\n" + item_names + '\n\n(' + str(i+1) + ') ' + "Nevermind\n")
                if int(buy) == i+1:
                    os.system('clear')
                    continue
                else:
                    if self.player.gold < self.current_room.npc.inventory[int(buy)-1].price:
                        os.system('clear')
                        print("You don't have enough money for that!")
                        time.sleep(2)
                        os.system('clear')
                        continue
                    else:
                        self.player.items.append(self.current_room.npc.inventory[int(buy)-1])
                        self.player.gold -= self.current_room.npc.inventory[int(buy)-1].price
                        os.system('clear')
                        print("You obtained " + self.current_room.npc.inventory[int(buy)-1].name + "!\n")
                        time.sleep(2)
                        del self.current_room.npc.inventory[int(buy)-1]
                        os.system('clear')
                        continue
            if choice == '2':
                player_items = ''
                j = 0
                for y in self.player.items:
                    j += 1
                    if j < (len(self.player.items)):
                        player_items += '(' + str(j) + ') ' + y.name + '       Durability: ' + str(y.durability) + '       Power: ' + str(y.damage) + '\n'
                    if j == len(self.player.items):
                        player_items += '(' + str(j) + ') ' + y.name + '       Durability: ' + str(y.durability) + '       Power: ' + str(y.damage)

                sell = input("Which Item would you like to sell?\n" + player_items + '\n\n(' + str(j+1) + ') ' + "Nevermind\n")
                if int(sell) == j+1:
                    os.system('clear')
                    continue
                else:
                    self.player.gold += self.player.items[int(sell)-1].price
                    del self.player.items[int(sell)-1]
                    os.system('clear')
                    print("You now have " + str(self.player.gold) + " gold!")
                    time.sleep(2)
                    os.system('clear')
                    continue
            if choice == '3':
                return
