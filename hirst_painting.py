import colorgram,random
from turtle import Turtle,Screen,colormode

def draw_one_line():
    timmy.color(random.choice(my_list))
    timmy.dot(size=20)
    timmy.penup()
    timmy.forward(50)

def back_to_first_position(size):
    timmy.left(90)
    timmy.penup()
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(size*50)
    timmy.setheading(0)

# take each color in a tuple and put them all in a list 
#put full path of image
colors = colorgram.extract('/home/user/pyhon_course/python_intermediate/hirst_painting/image.jpg', 30)
my_list=[]
for color in colors:
    Red=color.rgb.r
    green=color.rgb.g
    blue=color.rgb.b
    new_color=(Red,green,blue)
    my_list.append(new_color)

#objects
colormode(255)
timmy=Turtle()

#start position
timmy.hideturtle()
timmy.setheading(225)
timmy.penup()
timmy.forward(250)
timmy.setheading(0)

size=int(input("size of square: "))

#Draw square size*size
for x in range(size):
    for _ in range(size):
        draw_one_line()
    back_to_first_position(size)

#screen object
my_screen=Screen()
my_screen.exitonclick()    
