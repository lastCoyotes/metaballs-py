import turtle
from random import randint
import numpy as np
import time
import math

# global variables

# screen
winWidth = 640
winHeight = 480
res = 40

# fidelity
cols = int(winWidth / res) + 1
rows = int(winHeight / res) + 1
field = np.random.random((rows, cols))

# FPS variables
tick2Frame = 0
tick2FPS = 20000000 # real raw FPS
tick2t0 = time.time()

# customizable FPS
def tick(fps = 60):
    global tick2Frame, tick2FPS, tick2t0
    n = tick2FPS / fps
    tick2Frame += n

    while n>0: n -= 1
    if time.time() - tick2t0 > 1:
        tick2t0 = time.time()
        tick2FPS = tick2Frame
        tick2Frame = 0

# binary tables
edgeTable = np.array([
    0x0, 0x9, 0x3, 0xA,
    0x6, 0xF, 0x5, 0xC,
    0xC, 0x5, 0xF, 0x6,
    0xA, 0x3, 0x9, 0x0
])

lineTable = np.array([
    [-1, -1, -1, -1],
    [3, 0, -1, -1, -1, -1],
    [0, 1, -1, -1, -1, -1],
    [1, 3, -1, -1, -1, -1],
    [1, 2, -1, -1, -1, -1],
    [1, 2, 3, 0, -1, -1],
    [0, 2, -1, -1, -1, -1],
    [2, 3, -1, -1, -1, -1],
    [2, 3, -1, -1, -1, -1],
    [0, 2, -1, -1, -1, -1],
    [0, 1, 2, 3, -1, -1],
    [1, 2, -1, -1, -1, -1],
    [1, 3, -1, -1, -1, -1],
    [0, 1, -1, -1, -1, -1],
    [3, 0, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1]
])

print("Columns | " + str(cols))
print("Rows    | " + str(rows))

# give random ints to field[][]
for x in range (rows):
    for y in range (cols):
        field[x][y] = randint(0, 1)

# turtle boilerplate
def setwindowsize(x=winWidth, y=winHeight):
    turtle.setup(x, y)
    turtle.setworldcoordinates(0,0,x,y)
   
def drawpixel(x, y, color, pixelsize = 1):
    turtle.tracer(0,0)
    turtle.colormode(255)
    turtle.penup()
    turtle.setpos(x*pixelsize, y*pixelsize)
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(pixelsize)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def showimage():
    turtle.hideturtle()
    turtle.update()

class circle:
    instances = []

    def __init__(self, flag, name, position, radius):
        self.name = name
        self.flag = flag
        self.position = position
        self.radius = radius
        self.instances.append(self)

    # visualize circle for debug
    def drawCircle(self, flag):
        if self.flag == True:
            turtle.tracer(0, 0)
            turtle.colormode(255)
            turtle.setpos(self.position[0]*1, self.position[1]*1)
            turtle.color('black')
            turtle.pendown()
            turtle.circle(self.radius)
            turtle.penup()
    
# metaball sum formula
# WIP check if this is the proper way to iterate through all circle instances and calling their values
def metaballSummation():
    sum = 0.0
    
    # for all circles.
    # add each to sum
    # formula: SUM (r_i)^2 / ((x - x_i)^2 + (y - y_i)^2)
    for i in range (circle.instances):
        sum += math.pow(circle.radius, 2) / ((math.pow(circle.position[0], 2 ) + math.pow( circle.position[1], 2)))
    
    return sum

# moving grid of dots out of main
def renderGrid():

    #establish grid
    for i in range (cols):
        for j in range (rows):
            if field[j][i] == 1:
                drawpixel(i*res, j*res, "blue", 1)
            else:
                drawpixel(i*res, j*res, "red", 1)

def renderEdge(a, b, c, d):
    # a = top left, b = top right, c = bottom left, d = bottom right
    # for points being either 0 or 1
    # a * 8 + b * 4 + c * 2 + d (*1 is redundant)
    case = a*8+b*4+c*2+d

    
    #linear interpolation implemented in next installment
    
    

if __name__ == '__main__':
    setwindowsize()
    
    # to console
    for row in field:
        print(row)
    
    renderGrid()

    # test draw circle
    d = circle(True, "d", [80, 150], 150.0)
    d.drawCircle(True)

    showimage()

    # test FPS code
    # while True:
    #     tick(1) # 1 FPS
    #     print(time.time())



    # wait
    input()