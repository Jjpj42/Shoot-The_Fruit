import pgzrun
import random

WIDTH = 800
HEIGHT = 400

apple = Actor("apple")
orange= Actor("orange")
pineapple = Actor("pineapple")
def draw():
    
    screen.fill((100,200,200))
    apple.draw()
    orange.draw()
    pineapple.draw()
    
def place_apple():
    apple.x = random.randint(40,600)
    apple.y=random.randint(40,400)

def place_orange():
    orange.x = random.randint(40,600)
    orange.y=random.randint(40,400)

def place_pineapple():
    pineapple.x = random.randint(40,600)
    pineapple.y=random.randint(40,400)
    
def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good Shot!")
        place_apple()
    elif orange.collidepoint(pos):
        print("Good Shot!")
        place_orange()
    elif pineapple.collidepoint(pos):
        print("Good Shot!")
        place_pineapple()
    else:
        print("You Missed")
    


place_apple()
place_orange()
place_pineapple()
pgzrun.go()

