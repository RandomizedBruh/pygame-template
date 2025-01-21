import pygame


class Player:


    image=""
    surface=None
    rect=None
    width = 100
    height=100
    x=0
    y=0
    

    def __init__(self,image,width=100 ,height=100,x=0,y=0):
        print("создаём игрока")
        self.x=x
        self.y=y
        self.image=image
        self.width = width
        self.height = height
        self.surface=pygame.image.load(image)
        self.surface=pygame.transform.scale(self.surface,(self.width, self.height))
        self.rect = self.surface.get_rect(center=(self.x,self.y))


    def draw(self,screen: pygame.Surface):
        self.rect.center=(self.x,self.y)
        screen.blit(self.surface,self.rect)