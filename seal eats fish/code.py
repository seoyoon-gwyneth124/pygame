import pgzrun
import random

WIDTH = 700
HEIGHT = 500

timer = 7
points = 0
gameover = False

seal = Actor('seal')
fish = Actor('fish')
seal.x = random.randint(0, 700)
seal.y = random.randint(0,500)

def move():
    fish.x = random.randint(0,700)
    fish.y = random.randint(0,500)
    
move()

def draw():
    if not gameover:
        screen.clear()
        screen.fill((79, 255, 252))
        seal.draw()
        fish.draw()
        screen.draw.text(str(timer), topleft = (0,0), color = "black", fontsize = 50)
        screen.draw.text('point:'+ str(points),topright = (700,0), color = 'black', fontsize = 45)
    else:
        quit()
def update():
    global points,gameover,timer
    if seal.colliderect(fish):
        if timer > 0:
            points = points + 1
            move()
            timer=7
        else:
            gameover = True
    if keyboard.right:
        seal.x = seal.x+3
    if keyboard.left:
        seal.x = seal.x-3
    if keyboard.up:
        seal.y = seal.y-3
    if keyboard.down:
        seal.y = seal.y+3
        

def countdown():
    global timer
    if timer > 0:
        timer = timer - 1
    else:
        timer = 0

clock.schedule_interval(countdown, 1.0)
