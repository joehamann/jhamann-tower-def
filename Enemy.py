import pygame
import GridGame
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = GridGame.load_image('battlecruiser2.png', -1)
        self.rect.topleft = (x,y)
        
        