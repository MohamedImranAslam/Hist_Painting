# import colorgram
# colors = colorgram.extract('hist spot painting.jpg',30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as turtle_module
import random
screen = turtle_module.Screen()
turtle_module.colormode(255)
buddy = turtle_module.Turtle()
buddy.speed("fastest")
buddy.penup()
color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
buddy.setheading(225)
buddy.forward(250)
buddy.setheading(0)

num_of_dots = 100
for dot_count in range(1,num_of_dots + 1):
    buddy.dot(20,random.choice(color_list))
    buddy.forward(50)
    if dot_count % 10 == 0:
        buddy.setheading(90)
        buddy.forward(50)
        buddy.setheading(180)
        buddy.forward(500)
        buddy.setheading(0)

screen.exitonclick()