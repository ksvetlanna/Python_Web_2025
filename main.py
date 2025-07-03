# Черепашья графика

'''import turtle as t
# скорость рисования при выводе на экран
t.speed(0)

N = 6     #количество запусков

t.penup() #подняли перо
t.goto(100,200) # координаты
t.pendown() #опустили перо

for _ in range(N):
    # длинна шага
    t.forward(100)
# пишем в градусах на сколько поворачивать вправо
    t.right(360//N) # поворот
# экран по умолчанию 800*600
t.mainloop()'''
#--------------------------------------------------------------------------------------
'''import turtle as t
t.speed(0)
N=8
for _ in range(N):
    t.circle(50) #круг
    t.right(360//N)

t.mainloop()'''
#--------------------------------------------------------------------------------------

import turtle as t
t.speed(0)
N=8
colors = ['red','purple','blue','green','orange','yellow']

t.bgcolor('black') #цвет фона
angle = 360 // len(colors)-1 #угол для узора

for x in range(200):
    t.pencolor(colors[x % len(colors)]) # цвет свой у каждого шага
    t.width(x // 100 + 1) # Толщина линий 1 до 100 а дальше толщина 2
    t.forward(x)
    t.left(angle)


def square(side):
    for _ in range(4):
        t.forward(side)
        t.right(90)

# цветок
'''def flower():
    for _ in range(36):
        t.circle(50)
        t.right(10)

flower()'''

'''for _ in range(N):
    for _ in range(4):
        t.forward(100) # квадрат в цикле со сдвигом
        t.right(90)
    t.right(360//5)'''
t.mainloop()
#--------------------------------------------------------------------------------------
