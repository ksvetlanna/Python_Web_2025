# Фрактальное дерево
import turtle as t

def tree(length):
    if length < 10:
        return
    t.forward(length)
    t.left(30)
    tree(length *0.7)
    t.right(60)
    tree(length * 0.7)
    t.left(30)
    t.backward(length)

t.left(90)
tree(100)
t.mainloop()