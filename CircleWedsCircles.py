
import turtle
wn = turtle.Screen()
turtle.title("Make Your Circle With Me")
wn.bgcolor('black')
s = turtle.Turtle()
s.speed('fastest')
s.color('white')
rotate = int(100)

def circles(t, size):
    for i in range(10):
        t.circle(size)
        size = size-3

def dc(t, size, repeat):
    for i in range(repeat):
        circles(t, size)
        t.right(360/repeat)

dc(s, 200, 10)

t1 = turtle.Turtle()
t1.speed(0)
t1.color('white')
rotate = int(90)

def circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size-10

def dc(t, size, repeat):
    for i in range(repeat):
        circles(t, size)
        t.right(360/repeat)

dc(t1, 120, 10)

t3 = turtle.Turtle()
t3.speed('fastest')
t3.color('white')
rotate = int(100)

def circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size-19

def dc(t, size, repeat):
    for i in range(repeat):
        circles(t, size)
        t.right(360/repeat)

dc(t3, 80, 10)

t4 = turtle.Turtle()
t4.speed('fastest')
t4.color('white')
rotate = int(100)

def circles(t, size):
    for i in range(10):
        t.circle(size)
        size = size-20

def dc(t, size, repeat):
    for i in range(repeat):
        circles(t, size)
        t.right(360/repeat)

dc(t4, 40, 10)

turtle.done()
