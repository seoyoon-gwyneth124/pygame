import pgzrun
import random
gameover = False

WIDTH = 700
HEIGHT = 700

a = Actor("dog")
d = Actor("dog2")

def move():
    a.x = random.randint(0, 700)
    a.y = random.randint(0, 700)
    d.x = random.randint(0, 700)
    d.y = random.randint(0, 700)
    
move()

def draw():
    if not gameover: 
        screen.clear()
        screen.fill((252, 252, 227))
        a.draw()
        d.draw()
        screen.draw.text("score:"+ str(x), topleft = (0,0), color = ("black"))
    else:
        screen.fill("purple")
        screen.draw.text("gameover", center = (350,350), color = ("black"))
x = 0

def on_mouse_down(pos):
    global x
    global gameover
    if a.collidepoint(pos):
        x = x - 1
        move()
    elif d.collidepoint(pos):
        x = x + 2
        move()
    else:
        gameover = True
        
