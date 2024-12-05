# 01. ülesanne
# Aare-Aigar 05.12.24


# See impordib kilpkonna mooduli
import turtle

# kolmnurk
turtle.speed(5) # reguleeri 1-9
turtle.penup()
turtle.goto(-500,200)
turtle.pendown()
turtle.forward(200) #fd, pikslistes
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)

# süda
turtle.penup()
turtle.goto(-200,200)
turtle.pendown()
turtle.left(120)
turtle.fd(100)
turtle.circle(50,180)
turtle.right(90)
turtle.circle(50,180)
turtle.fd(100)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()


# lõpetab kilpkonna, et ei jooksesks kokku
turtle.done()