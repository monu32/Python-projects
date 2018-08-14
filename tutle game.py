import turtle,random
from turtle import *

title("TURTLE RACE")
bgcolor("black")
goto(-150,-200)
speed(20)
for i in range(1,16):
    pencolor("white")
    write(i)
    for j in range(0,15):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(300)
    left(90)
    forward(20)
    right(90)

red_turtle=Turtle()
red_turtle.color("red")
red_turtle.shape("turtle")
red_turtle.penup()
red_turtle.goto(-130,-230)
red_turtle.pendown()
red_turtle.right(270)

yellow_turtle=Turtle()
yellow_turtle.color("yellow")
yellow_turtle.shape("turtle")
yellow_turtle.penup()
yellow_turtle.goto(-80,-230)
yellow_turtle.pendown()
yellow_turtle.right(270)

green_turtle=Turtle()
green_turtle.color("green")
green_turtle.shape("turtle")
green_turtle.penup()
green_turtle.goto(-40,-230)
green_turtle.pendown()
green_turtle.right(270)

blue_turtle=Turtle()
blue_turtle.color("blue")
blue_turtle.shape("turtle")
blue_turtle.penup()
blue_turtle.goto(0,-230)
blue_turtle.pendown()
blue_turtle.right(270)

white_turtle=Turtle()
white_turtle.color("white")
white_turtle.shape("turtle")
white_turtle.penup()
white_turtle.goto(40,-230)
white_turtle.pendown()
white_turtle.right(270)    

orange_turtle=Turtle()
orange_turtle.color("orange")
orange_turtle.shape("turtle")
orange_turtle.penup()
orange_turtle.goto(80,-230)
orange_turtle.pendown()
orange_turtle.right(270)    

pink_turtle=Turtle()
pink_turtle.color("pink")
pink_turtle.shape("turtle")
pink_turtle.penup()
pink_turtle.goto(120,-230)
pink_turtle.pendown()
pink_turtle.right(270)

for_check_winner=[0]*7
    
while True:
    red_turtle.penup()
    store=random.randint(1,10)
    for_check_winner[0]+=store
    red_turtle.forward(store)
    if for_check_winner[0]>=300:
        break
    
    yellow_turtle.penup()
    store=random.randint(1,10)
    for_check_winner[1]+=store
    yellow_turtle.forward(store)
    if for_check_winner[1]>=300:
        break

    green_turtle.penup()
    store=random.randint(1,10)
    for_check_winner[2]+=store
    green_turtle.forward(store)
    if for_check_winner[2]>=300:
        break 

      
    blue_turtle.penup()
    store=random.randint(1,10)
    for_check_winner[3]+=store
    blue_turtle.forward(store)
    if for_check_winner[3]>=300:
        break
    
    white_turtle.penup()
    store=random.randint(1,10)
    for_check_winner[4]+=store
    white_turtle.forward(store)
    if for_check_winner[4]>=300:
        break
     
    orange_turtle.penup()
    store=random.randint(1,10)
    for_check_winner[5]+=store
    orange_turtle.forward(store)
    if for_check_winner[5]>=300:
        break
    
    pink_turtle.penup()
    store=random.randint(1,10)
    for_check_winner[6]+=store
    pink_turtle.forward(store)
    if for_check_winner[6]>=300:
        break  

index=-1
for i in range(0,len(for_check_winner)):
    if for_check_winner[i]>=300:
        index=i

goto(-150,150)
if index==0:
    write("Red Turtle is Won",font=("Arial",20,"normal"))
elif index==1:
    write("Yellow Turtle is Won",font=("Arial",20,"normal"))
elif index==2:
    write("Green Turtle is Won",font=("Arial",20,"normal"))
elif index==3:
    write("Blue Turtle is Won",font=("Arial",20,"normal"))
elif index==4:
    write("White Turtle is Won",font=("Arial",20,"normal"))
elif index==5:
    write("Orange Turtle is Won",font=("Arial",20,"normal"))
else:
    write("Pink Turtle is Won",font=("Arial",20,"normal"))
