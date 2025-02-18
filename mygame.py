
from classed.enemy import Enemy

from classed.player import Player
from classed.bullet import Bullet

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


font =pygame.font.Font(None, 36)


player = Player("./boych.png",200,100,200,HEIGHT-100)
micros = Enemy("./microp.png",50,50,200,300)
enemy2 = Enemy("./microp.png",x=100, y =50)




listEnemy = []
enemyGroup = pygame.sprite.Group(listEnemy)
def spawnEnemyes():
    x = rd(0,WIDTH)
    y=rd(0,200)
    enemy = Enemy("./microp.png",x=x, y=y,speed =rd(1,3))
    enemyGroup.add(enemy)
    listEnemy.append(enemy)
    
for i in range(0,10):
    spawnEnemyes()

bulletList =[]


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

kills =0

isRunning = True

while isRunning:

    screen.fill(BLUE)

    text=font.render(f"убийств {kills}", 1,BLACK)
    screen.blit(text,(400,100))




    # pygame.draw.rect(screen,RED,(x,y,200,100))
    # pygame.draw.circle(screen,BLUE,(x,y), 40)
    for enemy in listEnemy:
        enemy.draw(screen)
        enemy.follow(player)


    # screen.blit(surface,rect)
    # screen.blit(surface2,rect2)

    player.draw(screen)
    micros.draw(screen)
    enemy2.draw(screen)

    micros.follow(player)
    # enemy2.follow(player,2)
    
    player.move()
    # rect.center=(x,y)
    


    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LSHIFT]:
    #     speed=8
    # else: speed = 3
    # if keys[pygame.K_a]:
    #     player.x -= speed
    # elif keys[pygame.K_d]:
    #     player.x += speed
    # if keys[pygame.K_w]:
    #     player.y -=speed
    # elif keys[pygame.K_s]:
    #     player.y +=speed
    # blue -=1
    # if blue == 0:
    #     blue =255

    # red +=1
    # if red == 255:
    #     red =0
    keys =pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bullet =Bullet("./пуля.png", 20, 10, player.x,player.y)
        bulletList.append(bullet)

    collideWithPlayer=pygame.sprite.spritecollideany(player,enemyGroup)
    if collideWithPlayer:
        print("KABOOM")
        player.hp -=3
        if player.hp<=0:
            print("дэд")
            isRunning =False






    for bullet in bulletList:
        bullet.draw(screen)
        bullet.move()
        if bullet.x > WIDTH or bullet.x <0 or bullet.y > HEIGHT or bullet.x < 0:
            bulletList.remove(bullet)
            #проверка столкновения пуль с противником
        collideSprite = pygame.sprite.spritecollideany(bullet,enemyGroup)
        if collideSprite:
            print("SHOWDOWNBS", collideSprite)
            bulletList.remove(bullet)
            enemyGroup.remove(collideSprite)
            listEnemy.remove(collideSprite)


#          .......
#       
# 
# 
# 
#  ______
# |SanS  |
#  ___________________________ 
# | er er er er er            |
# |                           |
# |chevo????                  |
# |                           |
# | yes                 yes   |
# |___________________________|


    spawnChance=rd(0,100)
    if spawnChance <= 10:
        spawnEnemyes()


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
