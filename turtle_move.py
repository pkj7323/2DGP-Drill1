import turtle


def move_up():
    turtle.setheading(90) # 방향 바꾸기
    turtle.forward(50)  # 이동
    turtle.stamp()  # 스탬프 찍기
def move_down():
    turtle.setheading(-90)  # 방향 바꾸기
    turtle.forward(50)  # 이동
    turtle.stamp()  # 스탬프 찍기
def move_left():
    turtle.setheading(180)  # 방향 바꾸기
    turtle.forward(50)  # 이동
    turtle.stamp()  # 스탬프 찍기
def move_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()
def restart():
    turtle.reset()

turtle.shape('turtle')
turtle.listen()
turtle.onkey(move_up,'w')
turtle.onkey(move_down,'s')
turtle.onkey(move_left,'a')
turtle.onkey(move_right,'d')
turtle.onkey(restart,'Escape')


turtle.exitonclick()
