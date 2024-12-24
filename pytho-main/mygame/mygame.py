
from classed.enemy import Enemy

from classed.player import Player

import pygame
from random import randint as rd


WIDTH = 800   
HEIGHT = 800

FPS = 30

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Моя перва игра кхехе")

clock = pygame.time.Clock()

# red = 0

# blue = 255

# green = 
x = 0


isRunning = True

while isRunning:

    screen.fill(GREEN)
    pygame.draw.rect(screen,RED,(x,0,200,100))
    pygame.draw.circle(screen,BLUE,(x,200), 40)
    x+=1

    if x >= WIDTH:
        x=-200
    
    keys = pygame.key.ger_pressed()

    if keys[pygame.K_LEFT]:
        x -= 3
    elif keys[pygame.K_d]:
        x += 3
    # blue -=1
    # if blue == 0:
    #     blue =255

    # red +=1
    # if red == 255:
    #     red =0




    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

pygame.quit











# ляляляляял я чёта ээ голова моя чёт пустая



# player1 = Player("Фордик", "какойтоguyизфнфмода", 100, 100, 50, 10)
# player1.print_infoP()

# # player1.say("блин...*cry*")


# enemy1 = Enemy("Матр4сс","тожегайсфнфмода", 100, 10)
# enemy1.info()
# player1.fight(enemy1)
# # enemy1.info()


  


# ⁣yes     yes  yes yes yes
# yesyes  yes  yes     yes
# yes yes yes  yes     yes
# yes  yesyes  yes     yes
# yes     yes  yes yes yes
