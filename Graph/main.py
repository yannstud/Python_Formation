import turtle

turtle.getscreen()
# Personnalisation
turtle.title("Stock AMAZON")
turtle.speed(10)
turtle.color("black", "black")

# initialisation echelle
zoom = 0.2
echelle_x = 20
echelle_y = 10
n_affichage = 40

#Afficher l'axe x
s = turtle.screensize()
turtle.up()
turtle.setpos(-s[0], 0)
turtle.down()
turtle.setpos(2 * s[0], 0)

#Afficher l'axe y
turtle.up()
turtle.setpos(-s[0], -s[0])
turtle.down()
turtle.setpos(-s[0], 2 * s[0])

# Position du curseur
offset_x = -s[0]
turtle.up()
turtle.setpos(offset_x,0)
turtle.down()

turtle.color("red", "black")


with open("AMZN.csv", "r", encoding="utf-8") as f:
    data = f.readlines()
    final_data = []
    for i, l in enumerate(data):
        if i != 0:
            final_data.append(float(l.split(',')[1]))

for i, v in enumerate(final_data):
    x = zoom * i * echelle_x + offset_x
    y = zoom * v * echelle_y
    if i == 0:
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
    else:
        turtle.goto(x, y)
    #Afficher valeurs
    if i % n_affichage == 0:
        turtle.color("green", "black")
        turtle.write(int(v), font=("Verdana", 12, "bold"))
        turtle.dot(5)
        turtle.color("red", "black")

turtle.done()