import pygame
import GridGame
class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, building=True):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = GridGame.load_image('tower.png', -1)
        self.rect.topleft = (x,y)
        self.building = building
    def update(self):
        if (building):
            pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        
    def build(self):
        building = False
        pos = pygame.mouse.get_pos()
         
        