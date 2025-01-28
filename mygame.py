
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


player = Player("./boych.png",200,100,200,300)


# surface = pygame.image.load('./boych.png')
# surface=pygame.transform.scale(surface,(100,100))
# rect =surface.get_rect(center=(200,200))

# surface2 = pygame.image.load('./boychdva.png')
# rect2=surface.get_rect(center=(300,300))
# red = 0

# blue = 255

# green = 
x = 0
y = 0
speed =3


isRunning = True

while isRunning:

    screen.fill(GREEN)
    # pygame.draw.rect(screen,RED,(x,y,200,100))
    # pygame.draw.circle(screen,BLUE,(x,y), 40)


    # screen.blit(surface,rect)
    # screen.blit(surface2,rect2)

    player.draw(screen)

    if x >= WIDTH:
        x=-200
    

    # rect.center=(x,y)
    


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        speed=8
    else: speed = 3
    if keys[pygame.K_a]:
        x -= speed
    elif keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_w]:
        y-=speed
    elif keys[pygame.K_s]:
        y+=speed
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
