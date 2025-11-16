import keyboard
import turtle

turtle.pendown()
turtle.pencolor('red')

#клавиши управления
keyboard.add_hotkey('w', lambda:turtle.forward(10))
keyboard.add_hotkey('s', lambda:turtle.back(10))
keyboard.add_hotkey('a', lambda:turtle.left(90))
keyboard.add_hotkey('d', lambda:turtle.right(90))

#Аналог на стрелках
keyboard.add_hotkey('up', lambda:turtle.forward(10))
keyboard.add_hotkey('down', lambda:turtle.back(10))
keyboard.add_hotkey('left', lambda:turtle.left(90))
keyboard.add_hotkey('right', lambda:turtle.right(90))

turtle.exitonclick()
turtle.penup()