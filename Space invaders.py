# Space invaders
import turtle
import os
import math
import random
from playsound import playsound



# Her setter jeg opp skjermen
Hv = turtle.Screen() # Hv = Hoved skjerm
Hv.bgcolor("black")

Hv.title("Space invaders")
Hv.bgpic("invaders1.jpg")


#register formene
Hv.register_shape("spiller.gif")
Hv.register_shape("saucer3a.gif")

# Tegne en grense
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Setter poeng til 0

score = 0

#Tegner scoren
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: {}" .format(score) 
score_pen.clear()
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Lager turtle spilleren
spiller = turtle.Turtle()
spiller.shape("spiller.gif")
spiller.penup()
spiller.speed(0)
spiller.setposition(0, -250)
spiller.setheading(90)
spiller.fart = 0



# Velger hvor mange finder det skal være
nummer_av_fiender = 5


# Lag en tom liste med fiender
fiender = []


# Legger til fiender i lista
for i in range(nummer_av_fiender):
    # Lager fiender
    fiender.append(turtle.Turtle())



for fiende in fiender:
    fiende.color("red")
    fiende.shape("saucer3a.gif")
    fiende.penup()
    fiende.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    fiende.setposition(x, y)

fiendefart = 2


# Spillern sitt våpen
skudd = turtle.Turtle()
skudd.color("yellow")
skudd.shape("circle")
skudd.penup()
skudd.speed(0)
skudd.setheading(90)
skudd.shapesize(0.5, 0.5)
skudd.hideturtle()

skuddfart = 20

# Definer hvilket stadiet våpen er i
# Ready - klar til å skyte
# Fire - våpenet skyter
skuddtilstand = "ready"




# Bevegelse venstre og høyre
def beveg_venstre():
    spiller.fart = -15
    

def beveg_høyre():
    spiller.fart = 15
    

def beveg_spiller():
    x = spiller.xcor()
    x += spiller.fart
    if x < -280:
        x = -280
    if x > 280:
        x = 280
        
    spiller.setx(x)
    

def skyt_skudd():
    # Sett våpenstadiet til global viss det må endres
    global skuddtilstand
    if skuddtilstand == "ready":
        
        #Lager skyte effekten 
       
        playsound('shoot.wav',False)
        
        skuddtilstand = "fire"
        

        # beveger våpenet/skuddet rett over spillern
        x = spiller.xcor()
        y = spiller.ycor() +10
        skudd.setposition(x ,y)
        skudd.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
    

    

# Tastatur knapper
Hv.listen()
Hv.onkeypress(beveg_venstre, "Left")
Hv.onkeypress(beveg_høyre, "Right")
Hv.onkeypress(skyt_skudd, "space")



 

# Hoved spill løkke
while True:
    
    beveg_spiller()
    
    for fiende in fiender:
        # Beveg fienden
        x = fiende.xcor()
        x += fiendefart
        fiende.setx(x)

        # Beveg fienden tilbake og ned
        if fiende.xcor() > 280:
                y = fiende.ycor()
                y -= 40
                fiendefart *= -1
                fiende.sety(y)
                

        if fiende.xcor() < -280:
                y = fiende.ycor()
                y -= 40
                fiendefart *= -1
                fiende.sety(y)
        # Tester om fienden og skuddet koliderer
        if isCollision(skudd, fiende):
            playsound('killed.wav',False)
            # Restarter skuddet
            skudd.hideturtle()
            skuddtilstand = "ready"
            skudd.setposition(0, -400)
            # Restarter fienden
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            fiende.setposition(x, y)
            # Oppdatere scoren
            score += 10
            scorestring = "Score: {}" .format(score)
            score_pen.clear() # Fjerner den gamle scoren
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            

        if isCollision(spiller, fiende):
            spiller.hideturtle()
            fiende.hideturtle()
            print ("Game Over")
            break

    

    # Beveg våpenet
    if skuddtilstand == "fire":
        y = skudd.ycor()
        y += skuddfart
        skudd.sety(y)

    # Tester om skuddet har flyttet seg til toppen
    if skudd.ycor() > 300:
        skudd.hideturtle()
        skuddtilstand = "ready"

