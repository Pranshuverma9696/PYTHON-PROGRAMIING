from turtle import *
import math

# Set up the screen
bgcolor("black")
speed(0)
color("red")
pensize(2)

def heart(n):
    
    x = 15 * math.sin(n) ** 3
    y = 12 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y


for i in range(1, 18): 
    penup()
    for j in range(100):  
        x, y = heart(j / 15)
        goto(x * i, y * i) 
        pendown()

hideturtle()
done()