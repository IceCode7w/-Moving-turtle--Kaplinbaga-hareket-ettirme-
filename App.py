#karakteri import turle ile importluyoruz 
import turtle

#ekran ve arka plan kodlari
wn = turtle.Screen()
wn.bgcolor('blue')

#kaplunbaga
tr = turtle.Turtle()
tr.color("red")
tr.penup()

speed=1

#hareketi tanimlama kodlari
def up():
    if tr.heading() != 270:
     tr.setheading(90)

def down():
     if tr.heading() != 90:
         tr.setheading(270)
 
def left():
   if tr.heading() != 0:
       tr.setheading(180)

def right():
    if tr.heading() != 180:
        tr.setheading(0)
       
#harket kodlari

wn.listen()
wn.onkey(up, 'Up')
wn.onkey(down, 'Down')
wn.onkey(left, 'Left')
wn.onkey(right, 'Right')

#uygulamayi kapatmadan hareketliligi saglayan komut
while True:
    tr.forward(speed)

