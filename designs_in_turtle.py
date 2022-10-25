# Using loops to draw Designs
import turtle
from 

# Defining the screen
wn = turtle.Screen()
wn.title('This is turtle trial')
wn.bgcolor('green')
wn.setup(width=300, height=500)

# drawing a square shape
for x in range(4):
    turtle.forward(100)
    turtle.right(90)

# drawing an octagon
for oct in range(8):
    turtle.forward(100)
    turtle.right(45)


# Main loop
while True:
    wn.update()
