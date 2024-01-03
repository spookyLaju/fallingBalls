import turtle
import random 


#create the environment of the game 
root = turtle.Screen()
root.title('falling balls')
root.bgcolor('black')
root.setup(width=500, height=500)
root.tracer(0)

random_y = random.randint(-500, 500)





#create the container for the balls 

container  = turtle.Turtle()
container.speed (0)
container.shape('square')
container.color('green')
container.penup()
container.goto(0,-100 )

#create  the falling balls 

balls = turtle.Turtle()
balls.speed(0)
balls.shape('circle')
balls.color('red')
balls.penup()
balls.goto(random_y,300)
balls.dy = -0.1


# functions 

def conatainerMoveLeft():
    x = container.xcor()
    x -=150
    container.setx(x)
def containerMoveRight():
     x = container.xcor()
     x +=150
     container.setx(x)  

#keyboard binding 
root.listen()
root.onkeypress(containerMoveRight,'d')
root.onkeypress(conatainerMoveLeft, 'a')      







#to loop the window 
while True:
    root.update()
    #movement loop for the ball 
    balls.sety(balls.ycor() + balls.dy)   

    #loop the movement of the ball 
    if balls.ycor() <= - 490:
        balls.goto(random_y,240)

        










   

    
   
    
