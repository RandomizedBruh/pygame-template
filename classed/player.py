import pygame


class Player:

    hp=100
    image=""
    surface=None
    rect=None
    width = 100
    height=100
    x=0
    y=0
    speed=8
    

    def __init__(self,image,width=100 ,height=100,x=0,y=0,speed=8):
        print("создаём игрока")
        self.x=x
        self.y=y
        self.image=image
        self.width = width
        self.height = height
        self.surface=pygame.image.load(image)
        self.surface=pygame.transform.scale(self.surface,(self.width, self.height))
        self.rect = self.surface.get_rect(center=(self.x,self.y))
        self.speed = speed


    def draw(self,screen: pygame.Surface):
        width=screen.get_width()
        height=screen.get_height()

        if(self.x< -self.width):
            self.x=width + 50
        elif(self.x >= width + 50):
            self.x = -50
        if (self.y < -50):
            self.y=height +50
        elif(self.y>height+50):
            self.y=-50


        self.rect.center=(self.x,self.y)
        screen.blit(self.surface,self.rect)
        self.showHp(screen)

    def move(self):


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            self.speed=8
        else: self.speed = 3
        if keys[pygame.K_a]:
            self.x -= self.speed
        elif keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -=self.speed
        elif keys[pygame.K_s]:
            self.y +=self.speed  

    def showHp(self,screen:pygame.Surface):
         pygame.draw.rect(screen,(255,0,0), (0,0,self.width,10))  
         pygame.draw.rect(screen,(0,255,0), (0,0,self.width * self.hp / 100,10))  