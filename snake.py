import turtle
import time
import random



# setting up the screen
width = 600
height = 600

window = turtle.Screen()
window.title("Snake")
window.bgcolor('black')
window.setup(width,height)
window.tracer(0) # turns off the screen updates


# snake head
head = turtle.Turtle()
head.penup() # stops the drawing (turtle were made for drawing lines when the turtles moved)
head.speed(0)
head.shape('square')
head.color('red')
head.goto(0,0) # middle of screen
head.direction = 'right'

body = [] #stores the body objects of the snakes (which is just other turtle objects)

# food
food = turtle.Turtle()
food.penup() # stops the drawing (turtle were made for drawing lines when the turtles moved)
food.speed(0)
food.shape('square')
food.color('green')
food.goto(random.randrange(0, 290, 20), random.randrange(0, 290, 20)) 


# functions / methods
def move():
    if head.direction == 'up':
        head.sety(head.ycor() + 20)
    if head.direction == 'down':
        head.sety(head.ycor() - 20)
    if head.direction == 'right':
        head.setx(head.xcor() + 20)
    if head.direction == 'left':
        head.setx(head.xcor() - 20)    

# directions
def go_up():
    head.direction = 'up'

def go_down():
    head.direction = 'down'

def go_right():
    head.direction = 'right'

def go_left():
    head.direction = 'left'

window.listen()
window.onkeypress(go_up, 'w')
window.onkeypress(go_down, 's')
window.onkeypress(go_right, 'd')
window.onkeypress(go_left, 'a')

# game loop
while True:
    
    window.update()

    if head.distance(food) < 20:
        food.goto(random.randrange(0, 290, 20), random.randrange(0, 290, 20)) 

        #adds a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.penup() 
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('darkred')
        body.append(new_segment)
        
    for i in range(len(body)-1, 0, -1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)
    
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)

    move()

    time.sleep(0.1)

#window.mainloop()