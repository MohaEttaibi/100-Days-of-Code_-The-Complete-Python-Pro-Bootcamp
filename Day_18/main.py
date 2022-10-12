import random
import turtle as t

# pip install heroes

# timmy_the_turtle = Turtle()
tim = t.Turtle()
t.colormode(255)
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("black")
# timmy_the_turtle.pencolor(0.2, 0.8, 0.55)

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Draw a Triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon.
# num_sides = 5
# colours =["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color

# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed(0)
# for _ in range(200):
#     # tim.color(random.choice(colours))
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         tim.speed(0)
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
# draw_spirograph(5)

# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim.penup()
tim.speed(0)
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
