# 3. ülesanne
# Aare 5.12.24

nimi = "Imre" #sõne, string, str
vanus = 20 # int, integer, täisarv
keskmine_hinne = 6.5 #komaarv, float
# plussiga saan stringid kokku
print(nimi+", "+str(vanus)+" aastat vana ja keskmine hinne on "+str(keskmine_hinne))
# komaga saan mitu asja printida
print(nimi,",",vanus,"aastat vana ja keskmine hinne on",keskmine_hinne)
# lause vormindamine lünkadega
print(f"{nimi}, {vanus} aastat vana ja keskmine hinne on {keskmine_hinne}")


"""
Ülesanne 3.7: Python Turtle kolmnurk
Loo muutuja kylje_pikkus, mis määrab kujundi külje pikkuse (täisarv)
Loo muutuja nurk, mis määrab kujundi nurga (täisarv)
Loo muutuja kujundi_varv, mis määrab kujundi joonevärvi (string)
Kasutades Turtle’i, joonista kõrvuti 3 värvilist kolmnurka, mis kasutab loodud muutujaid
Iga kolmnurk on järgmisest 1,5 korda eemal
Testi: muuda külje pikkust ning kolmnurgad on kenasti teineteisest eemal
"""

# 3.7 kolmnurk
import turtle
kylje_pikkus = 100
nurk = 120
varv = "blue"
varv2 = "red"
varv3 = "green"

turtle.speed(5)
turtle.color(varv)
turtle.pensize(1)
turtle.penup()
turtle.pendown()
turtle.forward(kylje_pikkus) 
turtle.left(nurk) 
turtle.forward(kylje_pikkus)
turtle.left(nurk) 
turtle.forward(kylje_pikkus)
turtle.left(nurk)

turtle.penup()
turtle.goto(kylje_pikkus*1.5,0)
turtle.pendown()

turtle.speed(5)
turtle.color(varv2)
turtle.pensize(5)
turtle.penup()
turtle.pendown()
turtle.forward(kylje_pikkus) 
turtle.left(nurk) 
turtle.forward(kylje_pikkus)
turtle.left(nurk) 
turtle.forward(kylje_pikkus)
turtle.left(nurk)

turtle.penup()
turtle.goto(kylje_pikkus*3,0)
turtle.pendown()

turtle.speed(5)
turtle.color(varv3)
turtle.pensize(10)
turtle.penup()
turtle.pendown()
turtle.forward(kylje_pikkus) 
turtle.left(nurk) 
turtle.forward(kylje_pikkus)
turtle.left(nurk) 
turtle.forward(kylje_pikkus)
turtle.left(nurk)


turtle.done()
