import turtle
import keyboard

turtle.shape("turtle")

#wsad 이동
def move(key):
    if key.name == 'w':
        turtle.setheading(90)
        turtle.forward(50)
       
    elif key.name == 's':
        turtle.setheading(270)
        turtle.forward(50)
       
    elif key.name == 'a':
        turtle.setheading(180)
        turtle.forward(50)
       
    elif key.name == 'd':
        turtle.setheading(0)
        turtle.forward(50)

#esc 리셋
    elif key.name == 'esc':
        turtle.reset()


keyboard.on_press(move)
turtle.mainloop()
turtle.listen()
