import turtle as t
import random as rd
import time as ti

t.bgcolor('yellow')

catterpiller = t.Turtle()
catterpiller.shape('square')
catterpiller.speed(0)
catterpiller.penup()
catterpiller.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(100)

#text_turtle = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start',align = 'center',font = ('Arial',18,'bold'))
text_turtle.hideturtle()

def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_width()/2
    bottom_wall = -t.window_width()/2
    (x,y) = catterpiller.pos()
    outside = x<left_wall or x>right_wall or x>top_wall or x<bottom_wall
    return outside

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200, 200))
    leaf.showturtle()

def game_over():
    catterpiller.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER !' ,align = 'center',font = ('arial',30,'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/2) - 50
    y = (t.window_height()/2) - 100
    score_turtle.setposition(x,y)
    score_turtle.write(str(current_score),align='right',font=('arial',40,'bold'))

def start_game():
    global game_started
    #if game_started:
        #return
    game_started = True

    score = 0
    text_turtle.clear()

    catterpillar_speed = 2
    catterpillar_length = 3
    catterpiller.shapesize(1,catterpillar_length,1)
    catterpiller.showturtle()
    display_score(score)
    place_leaf()

    while True:
        catterpiller.forward(catterpillar_speed)
        if catterpiller.distance(leaf)<20:
            place_leaf()
            catterpillar_length = catterpillar_length + 1
            catterpiller.shapesize(1, catterpillar_length, 1)
            catterpillar_speed = catterpillar_speed +1
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            break



def move_up():
    if catterpiller.heading() == 0 or catterpiller.heading() == 180:
        catterpiller.setheading(90)
def move_down():
    if catterpiller.heading() == 0 or catterpiller.heading() == 180:
        catterpiller.setheading(270)
def move_left():
    if catterpiller.heading() == 90 or catterpiller.heading() == 270:
        catterpiller.setheading(180)
def move_right():
    if catterpiller.heading() == 90 or catterpiller.heading() == 270:
        catterpiller.setheading(0)

t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_down,'Down')
t.onkey(move_right,'Right')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()

