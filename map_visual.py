import turtle

class Visuals:

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



