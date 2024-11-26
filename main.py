import turtle
import random
import time

delay=0.1
sc=0
hs=0
bodies=[]

#creatind screen for game
s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("Light blue")
s.setup(width=600,height=600)


#creating head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("Black")
head.fillcolor("Red")
head.penup()
head.ht()
head.goto(0,0)
head.direction="stop"
head.st()

#creating foood for snake
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("Black")
food.fillcolor("Green")
food.penup()
food.ht()#for hiding turtle
food.goto(150,200)
food.st()#for showing turtle



#creating an score borad
sb=turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-250,250)
sb.write("Score:0   |   Higest Score:0 ")#print msg for first time


#creating functions moving  in all directions 
def moveUp():
    if head.direction!="down":
        head.direction="up"

def moveDown():
    if head.direction!="up":
        head.direction="down"

def moveLeft():
    if head.direction!="right":
        head.direction="left"

def moveRight():
    if head.direction!="left":
        head.direction="right"   

def moveStop():
    head.direction="stop"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)           

#event handling
s.listen()
s.onkey(moveUp,"Up")
s.onkey(moveDown,"Down")
s.onkey(moveLeft,"Left")
s.onkey(moveRight,"Right")
s.onkey(moveStop,"space")

#mainloop,       #moving snake continiously
while True:
    s.update() #to update screen
    #check collision with border
    if head.xcor()>290:
        head.setx(-290)

    if head.xcor()<-290:
        head.setx(290)
    
    if head.ycor()>290:
        head.sety(-290)
    
    if head.ycor()<-290:
        head.sety(290)
    
    #check collision with food
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #increase snake size
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)  #append new body in list


        sc=sc+100  #increase score
        delay=delay-0.0001

        if sc>hs:
            hs=sc #update high score
        sb.clear()

        sb.write("Score:{}  |  Higest Score:{}" .format(sc,hs))
    #move snake bodeies
    for i in range(len(bodies)-1,0,-1):
        x=bodies[i-1].xcor()
        y=bodies[i-1].ycor()
        bodies[i].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()
#check collision wiht snake body
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()
            sc=0
            delay=0.1
            sb.clear()
            sb.write("Score:{}   | Higest Score:{}".format(sc,hs))
    time.sleep(delay)

s.mainloop()
# time.sleep(115)  
