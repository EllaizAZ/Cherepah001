import keyboard
import turtle

#цвет черепахи
color_choice = input("Выберите цвет (синий, красный, желтый или зеленый ")

if color_choice == "красный":
    turtle.color("red")
elif color_choice == "зеленый":
    turtle.color("green")
elif color_choice == "синий":
    turtle.color("blue")
elif color_choice == "желтый":
    turtle.color("yellow")
else:
    turtle.color("black")
turtle.pendown()

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

#Выбор цвета во время рисования
keyboard.add_hotkey('g', lambda: turtle.color("green"))
keyboard.add_hotkey('b', lambda: turtle.color("blue"))
keyboard.add_hotkey('y', lambda: turtle.color("yellow"))
keyboard.add_hotkey('r', lambda: turtle.color("red"))
keyboard.add_hotkey('q', lambda: turtle.color("black"))

turtle.exitonclick()
turtle.penup()